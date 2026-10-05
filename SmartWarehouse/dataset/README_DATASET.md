# Dataset

โครงสร้าง:

dataset/
├── images/
│   ├── train/
│   └── val/
└── labels/
    ├── train/
    └── val/

YOLO label format:
class_id x_center y_center width height

Class:
0 person
1 helmet
2 vest
3 forklift

ควรใช้ภาพหลายมุม หลายระยะ และหลายสภาพแสง
แบ่ง train/val อย่างเหมาะสม
