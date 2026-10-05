# Activate virtual environment first
# .venv\Scripts\Activate.ps1

yolo detect train `
    data=dataset/data.yaml `
    model=yolo11n.pt `
    epochs=100 `
    imgsz=640 `
    batch=8 `
    project=runs `
    name=warehouse_ppe
