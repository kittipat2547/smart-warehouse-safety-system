import cv2
from ultralytics import YOLO

model = YOLO("yolo11n.pt")
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("ไม่สามารถเปิดกล้องได้")
    raise SystemExit

print("YOLO Person Detection")
print("กด Q เพื่อออก")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    results = model.predict(
        source=frame,
        classes=[0],
        conf=0.5,
        verbose=False
    )

    annotated = results[0].plot()

    cv2.imshow("Smart Warehouse - Person Detection", annotated)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
