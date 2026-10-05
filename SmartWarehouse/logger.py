import cv2

from config import CAMERA_SOURCE, MODEL_PATH
from database.db import init_database, prune_old_events
from detector import WarehouseDetector
from logger import EventLogger


def main():
    print("=" * 60)
    print("SMART WAREHOUSE")
    print("Safety & Inventory Management System")
    print("=" * 60)

    init_database()
    prune_old_events()

    detector = WarehouseDetector(str(MODEL_PATH))
    logger = EventLogger()

    cap = cv2.VideoCapture(CAMERA_SOURCE)

    if not cap.isOpened():
        print("ERROR: ไม่สามารถเปิดกล้องได้")
        return

    print("เปิดกล้องสำเร็จ")
    print("กด Q เพื่อออก")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("ERROR: อ่านภาพจากกล้องไม่ได้")
            break

        result = detector.process(frame)
        annotated = result["frame"]
        cv2.imshow("Smart Warehouse", annotated)

        for event in result["events"]:
            logger.log_event(
                event_type=event["event_type"],
                confidence=event["confidence"],
                frame=annotated,
                center=event.get("center"),
            )

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
