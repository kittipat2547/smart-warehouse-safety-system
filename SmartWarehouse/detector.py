import time

import cv2
import numpy as np
from ultralytics import YOLO

from config import (
    CONFIDENCE_THRESHOLD,
    DANGER_ZONE,
    EVENT_DEDUP_WINDOW,
    FORKLIFT_CLASS,
    HELMET_CLASS,
    PPE_X_TOLERANCE,
    PPE_Y_TOLERANCE,
    PERSON_CLASS,
    SAME_EVENT_DISTANCE_THRESHOLD,
    VEST_CLASS,
)


class WarehouseDetector:
    def __init__(self, model_path: str):
        print(f"Loading model: {model_path}")
        self.model = YOLO(model_path)
        self._last_events = {}

    @staticmethod
    def center(box):
        x1, y1, x2, y2 = box
        return ((x1 + x2) / 2, (y1 + y2) / 2)

    @staticmethod
    def point_in_polygon(point, polygon):
        x, y = point
        inside = False
        j = len(polygon) - 1

        for i in range(len(polygon)):
            xi, yi = polygon[i]
            xj, yj = polygon[j]

            intersect = (
                ((yi > y) != (yj > y))
                and
                (x < (xj - xi) * (y - yi) / ((yj - yi) or 1e-9) + xi)
            )

            if intersect:
                inside = not inside

            j = i

        return inside

    def _is_duplicate_event(self, event_type, center):
        if center is None:
            return False

        now = time.time()
        bucket = (
            event_type,
            int(center[0] // SAME_EVENT_DISTANCE_THRESHOLD),
            int(center[1] // SAME_EVENT_DISTANCE_THRESHOLD),
        )

        last = self._last_events.get(bucket)
        if last is not None:
            last_time, last_center = last
            if (now - last_time) < EVENT_DEDUP_WINDOW:
                if (
                    abs(center[0] - last_center[0]) <= SAME_EVENT_DISTANCE_THRESHOLD
                    and abs(center[1] - last_center[1]) <= SAME_EVENT_DISTANCE_THRESHOLD
                ):
                    return True

        self._last_events[bucket] = (now, center)

        for key, (timestamp, _) in list(self._last_events.items()):
            if now - timestamp > EVENT_DEDUP_WINDOW * 2:
                del self._last_events[key]

        return False

    def process(self, frame):
        result = self.model.predict(
            source=frame,
            conf=CONFIDENCE_THRESHOLD,
            verbose=False,
        )[0]

        annotated = frame.copy()

        pts = np.array(DANGER_ZONE, dtype="int32")
        cv2.polylines(
            annotated,
            [pts],
            isClosed=True,
            color=(0, 0, 255),
            thickness=2,
        )

        persons, helmets, vests, forklifts = [], [], [], []

        for box in result.boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())

            item = {
                "box": (x1, y1, x2, y2),
                "center": self.center((x1, y1, x2, y2)),
                "confidence": conf,
            }

            if cls == PERSON_CLASS:
                persons.append(item)
            elif cls == HELMET_CLASS:
                helmets.append(item)
            elif cls == VEST_CLASS:
                vests.append(item)
            elif cls == FORKLIFT_CLASS:
                forklifts.append(item)

        events = []

        for person in persons:
            px, py = person["center"]

            if self.point_in_polygon((px, py), DANGER_ZONE):
                if not self._is_duplicate_event("DANGER_ZONE", person["center"]):
                    events.append({
                        "event_type": "DANGER_ZONE",
                        "confidence": person["confidence"],
                        "center": person["center"],
                    })

            helmet_ok = self.has_ppe_near_person(person, helmets)
            vest_ok = self.has_ppe_near_person(person, vests)

            if not helmet_ok and not self._is_duplicate_event("NO_HELMET", person["center"]):
                events.append({
                    "event_type": "NO_HELMET",
                    "confidence": person["confidence"],
                    "center": person["center"],
                })

            if not vest_ok and not self._is_duplicate_event("NO_VEST", person["center"]):
                events.append({
                    "event_type": "NO_VEST",
                    "confidence": person["confidence"],
                    "center": person["center"],
                })

        for item in persons:
            self.draw_box(annotated, item["box"], "Person", (0, 255, 0))

        for item in helmets:
            self.draw_box(annotated, item["box"], "Helmet", (255, 255, 0))

        for item in vests:
            self.draw_box(annotated, item["box"], "Vest", (255, 0, 255))

        for item in forklifts:
            self.draw_box(annotated, item["box"], "Forklift", (0, 165, 255))

        return {
            "frame": annotated,
            "events": events,
            "counts": {
                "person": len(persons),
                "helmet": len(helmets),
                "vest": len(vests),
                "forklift": len(forklifts),
            },
        }

    def has_ppe_near_person(self, person, ppe_items):
        px, py = person["center"]

        for ppe in ppe_items:
            x, y = ppe["center"]

            if (
                abs(px - x) <= PPE_X_TOLERANCE
                and abs(py - y) <= PPE_Y_TOLERANCE
                and y < py
            ):
                return True

        return False

    @staticmethod
    def draw_box(frame, box, label, color):
        x1, y1, x2, y2 = box

        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

        cv2.putText(
            frame,
            label,
            (x1, max(y1 - 10, 20)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            color,
            2,
        )
