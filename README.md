# 🏭 Smart Warehouse Safety & Inventory Management System

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-purple?style=for-the-badge&logo=opencv" />
  <img src="https://img.shields.io/badge/YOLOv8-Object%20Detection-cyan?style=for-the-badge" />
  <img src="https://img.shields.io/badge/MySQL-Database-orange?style=for-the-badge&logo=mysql" />
  <img src="https://img.shields.io/badge/IoT-Sensors-green?style=for-the-badge" />
</p>

<p align="center">
  <b>Smart Warehouse Safety & Inventory Management System</b>
  <br>
  Computer Vision + IoT + Database
</p>

---

## 📌 About The Project

ระบบบริหารจัดการและตรวจจับความปลอดภัยในคลังสินค้าอัจฉริยะ
โดยประยุกต์ใช้ **Computer Vision, Artificial Intelligence และ IoT**

ระบบถูกออกแบบเพื่อช่วยตรวจสอบความปลอดภัยของบุคลากร
ตรวจจับวัตถุภายในคลังสินค้า และจัดเก็บข้อมูลเข้าสู่ฐานข้อมูล
เพื่อสนับสนุนการบริหารจัดการคลังสินค้าแบบอัตโนมัติ

### 🎯 Main Objectives

- ตรวจจับบุคคลและวัตถุแบบ Real-Time
- ตรวจสอบพื้นที่อันตรายภายในคลังสินค้า
- ตรวจสอบอุปกรณ์ความปลอดภัยของพนักงาน
- นับจำนวนสินค้า
- ติดตามข้อมูล Inventory
- รับข้อมูลจาก IoT Sensors
- บันทึกเหตุการณ์เข้าสู่ Database
- แจ้งเตือนเมื่อพบเหตุการณ์ผิดปกติ

---

# 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │     CCTV / Camera   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Computer Vision     │
                    │ OpenCV + YOLO       │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
        Person Detection   Object Detection   Safety Detection
              │                │                │
              └────────────────┼────────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Event Processing  │
                    └──────────┬──────────┘
                               │
             ┌─────────────────┼─────────────────┐
             │                                   │
             ▼                                   ▼
      ┌──────────────┐                    ┌──────────────┐
      │ IoT Sensors  │                    │    MySQL     │
      └──────┬───────┘                    │   Database   │
             │                            └──────┬───────┘
             └────────────────┬──────────────────┘
                              │
                              ▼
                    ┌─────────────────────┐
                    │ Dashboard / Alert   │
                    └─────────────────────┘
