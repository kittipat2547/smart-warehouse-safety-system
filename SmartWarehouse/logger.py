from datetime import datetime
from pathlib import Path
import cv2

from config import EVENT_DIR
from database.db import insert_event


class EventLogger:
    def __init__(self):
        Path(EVENT_DIR).mkdir(parents=True, exist_ok=True)

    def log_event(self, event_type, confidence, frame):
        timestamp = datetime.now()
        filename = timestamp.strftime("%Y%m%d_%H%M%S_%f") + ".jpg"
        image_path = Path(EVENT_DIR) / filename

        cv2.imwrite(str(image_path), frame)

        insert_event(
            timestamp=timestamp.isoformat(timespec="seconds"),
            event_type=event_type,
            confidence=confidence,
            image_path=str(image_path),
            camera="CAM-01"
        )

        print(
            f"[EVENT] {event_type} | "
            f"confidence={confidence:.2f} | "
            f"{image_path}"
        )
