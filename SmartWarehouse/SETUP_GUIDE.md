# Smart Warehouse Setup Guide

## Quick Start

### 1. Install Dependencies
```powershell
cd SmartWarehouse
pip install -r requirements.txt
```

### 2. Setup Project (Download Model + Create Folders)
```powershell
python scripts/setup.py
```

This will:
- ✅ Create folder structure (models, database, events, logs)
- ✅ Download YOLO11n model automatically
- ✅ Check dependencies
- ✅ Test camera

### 3. Check System Before Running
```powershell
python scripts/check_system.py
```

Verifies:
- ✅ All folders exist
- ✅ All dependencies installed
- ✅ Model file present
- ✅ Camera working

### 4. Test Model
```powershell
python scripts/test_model.py
```

Tests:
- ✅ Model loads correctly
- ✅ Inference works

### 5. Run Main Detection System
```powershell
python main.py
```

- Opens camera
- Detects persons, helmets, vests, forklifts
- Logs events to database
- Press 'Q' to quit

### 6. View Dashboard (New Terminal)
```powershell
streamlit run dashboard/app.py
```

Access at: http://localhost:8501

---

## Folder Structure After Setup

```
SmartWarehouse/
├── models/
│   └── best.pt              ← YOLO model (downloaded by setup.py)
├── database/
│   └── warehouse.db         ← SQLite database (created on first run)
├── events/
│   └── *.jpg                ← Event images
├── logs/
│   └── *.log                ← System logs
├── config.py
├── main.py
├── detector.py
├── logger.py
├── inventory.py
├── scripts/
│   ├── setup.py             ← Setup script
│   ├── check_system.py      ← System check
│   ├── test_model.py        ← Model test
│   ├── test_camera.py       ← Camera test
│   ├── test_yolo.py         ← YOLO test
│   └── train_model.ps1      ← Model training
├── dashboard/
│   └── app.py               ← Streamlit dashboard
├── database/
│   └── db.py                ← Database functions
└── dataset/
    ├── data.yaml
    └── README_DATASET.md
```

---

## Troubleshooting

### Issue: Model not found
```powershell
# Run setup to download model
python scripts/setup.py
```

### Issue: Dependencies missing
```powershell
# Install all requirements
pip install -r requirements.txt
```

### Issue: Camera not working
```powershell
# Test camera
python scripts/test_camera.py

# Check if camera is being used by another application
```

### Issue: Dashboard not loading
```powershell
# Make sure you're in the SmartWarehouse directory
cd SmartWarehouse
streamlit run dashboard/app.py
```

---

## Configuration

Edit `config.py` to customize:

```python
# Camera settings
CAMERA_SOURCE = 0              # Webcam index or RTSP URL
CAMERA_WIDTH = 1280
CAMERA_HEIGHT = 720

# Detection settings
CONFIDENCE_THRESHOLD = 0.50    # Minimum confidence for detection
PPE_X_TOLERANCE = 120          # Helmet/vest distance tolerance (X)
PPE_Y_TOLERANCE = 180          # Helmet/vest distance tolerance (Y)

# Event deduplication
EVENT_DEDUP_WINDOW = 5         # Seconds to avoid duplicate events
SAME_EVENT_DISTANCE_THRESHOLD = 50  # Pixels

# Database
DB_RETENTION_DAYS = 30         # Keep events for 30 days
```

---

## For Training Custom Model

See `dataset/README_DATASET.md` for dataset preparation.

```powershell
# Train with your dataset
yolo detect train data=dataset/data.yaml model=yolo11n.pt epochs=100 imgsz=640 batch=8

# Copy trained model
copy runs\detect\train\weights\best.pt models\best.pt
```

---

## System Requirements

- Python 3.12 or 3.13
- 4GB+ RAM
- 5GB+ disk space (for model + events)
- Webcam or IP camera (RTSP)
- Windows 10/11 or Linux

---

## License

Smart Warehouse Safety & Inventory Management System
