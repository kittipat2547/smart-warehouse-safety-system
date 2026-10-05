# Smart Warehouse Safety & Inventory Management System

ระบบบริหารจัดการและตรวจจับความปลอดภัยในคลังสินค้าอัจฉริยะ
ด้วย Computer Vision และ IoT

## ระบบ
CCTV/Webcam -> OpenCV -> YOLO -> Safety Analysis -> SQLite -> Dashboard
                                               -> ESP32 Alarm

## ส่วนประกอบ
- Person Detection
- Helmet / Vest Detection (ใช้ custom YOLO model)
- Forklift Detection
- Danger Zone Detection
- Event Logging
- SQLite Database
- Inventory Management
- Streamlit Dashboard
- ESP32 Buzzer / Warning Light
- Webcam / RTSP Camera

## ติดตั้ง
แนะนำ Python 3.12 หรือ 3.13

```powershell
cd SmartWarehouse
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

ถ้า Activate ไม่ได้:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## ทดสอบกล้อง
```powershell
python scripts/test_camera.py
```

## ทดสอบ YOLO
```powershell
python scripts/test_yolo.py
```

## รันระบบหลัก
```powershell
python main.py
```

## Dashboard
```powershell
streamlit run dashboard/app.py
```

## Training
วาง dataset ตามโครงสร้างใน dataset/README_DATASET.md แล้วรัน:
```powershell
yolo detect train data=dataset/data.yaml model=yolo11n.pt epochs=100 imgsz=640
```

จากนั้นนำ:
`runs/detect/warehouse_ppe/weights/best.pt`
ไปไว้ที่:
`models/best.pt`

## หมายเหตุสำคัญ
yolo11n.pt ที่ดาวน์โหลดจาก Ultralytics ไม่ได้ตรวจ Helmet/Vest โดยตรง
ต้องใช้ custom dataset และ train model สำหรับงานนี้

อย่าเดา RTSP URL ของกล้อง Yoosee เพราะแต่ละรุ่นต่างกัน
ให้ตั้งค่า RTSP หลังจาก webcam pipeline ทำงานแล้ว
