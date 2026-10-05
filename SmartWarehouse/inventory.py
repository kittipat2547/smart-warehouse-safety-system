from datetime import datetime
from pathlib import Path
import time

import cv2

from config import EVENT_DIR
from database.db import insert_event


class EventLogger:
    def __init__(self):
        self.event_dir = Path(EVENT_DIR)
        self.event_dir.mkdir(parents=True, exist_ok=True)
        self._last_events = {}

    def _is_duplicate_event(self, event_type, center):
        if center is None:
            return False

        now = time.time()
        key = (event_type, int(center[0] // 50), int(center[1] // 50))
        last = self._last_events.get(key)

        if last is not None:
            last_time, last_center = last
            if (now - last_time) < 5:
                if (
                    abs(center[0] - last_center[0]) <= 50
                    and abs(center[1] - last_center[1]) <= 50
                ):
                    return True

        self._last_events[key] = (now, center)
        return False

    def log_event(self, event_type, confidence, frame, center=None):
        if center is not None and self._is_duplicate_event(event_type, center):
            return False

        timestamp = datetime.now()
        filename = timestamp.strftime("%Y%m%d_%H%M%S_%f") + ".jpg"
        image_path = self.event_dir / filename

        cv2.imwrite(str(image_path), frame)

        insert_event(
            timestamp=timestamp.isoformat(timespec="seconds"),
            event_type=event_type,
            confidence=confidence,
            image_path=str(image_path),
            camera="CAM-01",
        )

        print(
            f"[EVENT] {event_type} | "
            f"confidence={confidence:.2f} | "
            f"{image_path}"
        )
        return True
