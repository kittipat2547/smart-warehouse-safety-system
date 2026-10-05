from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "models" / "best.pt"
DATABASE_PATH = BASE_DIR / "database" / "warehouse.db"
EVENT_DIR = BASE_DIR / "events"

# 0 = webcam
# ถ้าใช้ RTSP ให้ใส่ URL ของกล้องจริง
CAMERA_SOURCE = 0

CONFIDENCE_THRESHOLD = 0.50

# ต้องตรงกับ data.yaml
PERSON_CLASS = 0
HELMET_CLASS = 1
VEST_CLASS = 2
FORKLIFT_CLASS = 3

PPE_X_TOLERANCE = 120
PPE_Y_TOLERANCE = 180

DANGER_ZONE = [
    (200, 150),
    (600, 150),
    (600, 450),
    (200, 450),
]

ESP32_URL = "http://192.168.1.50/alarm"
ESP32_TIMEOUT = 2
