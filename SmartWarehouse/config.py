from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "models" / "best.pt"
DATABASE_PATH = BASE_DIR / "database" / "warehouse.db"
EVENT_DIR = BASE_DIR / "events"

# ========== CAMERA SETTINGS ==========
# 0 = webcam
# ถ้าใช้ RTSP ให้ใส่ URL ของกล้องจริง เช่น "rtsp://192.168.1.100:554/stream"
CAMERA_SOURCE = 0
CAMERA_WIDTH = 1280
CAMERA_HEIGHT = 720
CAMERA_FPS = 30

# ========== DETECTION SETTINGS ==========
CONFIDENCE_THRESHOLD = 0.50

# ต้องตรงกับ data.yaml
PERSON_CLASS = 0
HELMET_CLASS = 1
VEST_CLASS = 2
FORKLIFT_CLASS = 3

# PPE Detection - ระยะที่ helmet/vest ต้องอยู่ใกล้คน (pixels)
PPE_X_TOLERANCE = 120
PPE_Y_TOLERANCE = 180

# ========== DANGER ZONE SETTINGS ==========
# กำหนดพื้นที่อันตรายเป็นพิกัด 4 มุม (ตามลำดับ: TL, TR, BR, BL)
DANGER_ZONE = [
    (200, 150),
    (600, 150),
    (600, 450),
    (200, 450),
]

# ========== EVENT DEDUPLICATION SETTINGS ==========
# เพื่อป้องกันการบันทึก event ซ้ำหลายครั้งเมื่อคนอยู่ในจุดเดียวกัน
EVENT_DEDUP_WINDOW = 5
SAME_EVENT_DISTANCE_THRESHOLD = 50

# ========== ESP32 SETTINGS ==========
ESP32_URL = "http://192.168.1.50/alarm"
ESP32_TIMEOUT = 2

# ========== DATABASE SETTINGS ==========
DB_RETENTION_DAYS = 30

# ========== LOGGING SETTINGS ==========
LOG_LEVEL = "INFO"
LOG_DIR = BASE_DIR / "logs"
MAX_LOG_SIZE = 10
BACKUP_LOG_COUNT = 5
