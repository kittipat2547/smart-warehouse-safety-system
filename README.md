#Smart Warehouse Safety & Inventory Management System

![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![YOLO](https://img.shields.io/badge/YOLOv8-00FFFF?style=for-the-badge&logo=ultralytics&logoColor=black)
![MySQL](https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white)
![IoT](https://img.shields.io/badge/IoT-Sensors-FF6F00?style=for-the-badge&logo=microgenistics&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)

An end-to-end automated warehouse management system integrating **Computer Vision (YOLO/OpenCV)** and **IoT Sensor Networks** for real-time stock counting, workplace safety hazard monitoring, and centralized data analytics.

---

## Demo & System Preview

> *Replace the links below with your actual demo GIF or screenshots in your repository.*

| Real-Time Object Detection & Inventory Counting | Safety Zone Violation Alert |
| :---: | :---: |
| ![Inventory Demo](https://raw.githubusercontent.com/placeholder/demo_inventory.gif) | ![Safety Demo](https://raw.githubusercontent.com/placeholder/demo_safety.gif) |

---

## Key Features

-  **Automated Stock Counting:** Utilizes YOLO object detection models to count, track, and locate inventory items in real time.
-  **Workplace Safety Hazard Monitoring:** Detects unauthorized personnel in restricted zones, missing PPE gear, or blocked safety aisles.
-  **IoT Sensor Integration:** Streams environmental metrics (temperature, humidity, motion) from ESP32/Arduino sensor nodes.
-  **High-Frequency Data Logging:** Stores structured tracking logs and sensor telemetry efficiently in a MySQL relational database.
-  **Centralized Dashboard:** Real-time visual monitoring dashboard for warehouse managers.

---

##  Tech Stack & Architecture

- **Programming Language:** Python 3.9+
- **Computer Vision & AI:** OpenCV, Ultralytics YOLOv8
- **Database & Storage:** MySQL Workbench
- **Hardware & IoT:** ESP32 / Arduino, DHT22, Ultrasonic Sensors
- **Version Control:** Git & GitHub

---

##  Repository Structure

```text
smart-warehouse-system/
├── assets/                  # Demo images, GIFs, and badges
├── config/                  # Database configuration and AI model parameters
├── src/
│   ├── vision/              # YOLO and OpenCV object detection scripts
│   ├── iot/                 # Serial/MQTT communication with IoT sensors
│   ├── database/            # MySQL connectors and query helpers
│   └── dashboard/           # UI visualization scripts
├── models/                  # Trained YOLO weights (.pt files)
├── requirements.txt         # Project dependencies
├── main.py                  # System execution entry point
└── README.md                # Project documentation
