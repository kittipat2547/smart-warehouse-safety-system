#!/usr/bin/env python3
"""
System check script - verify all components before running
"""

import os
import sys
from pathlib import Path


def check_model():
    """ตรวจสอบว่ามี model file"""
    model_path = Path(__file__).parent.parent / "models" / "best.pt"
    
    if model_path.exists():
        size_mb = model_path.stat().st_size / (1024 * 1024)
        print(f"✓ Model found: {model_path} ({size_mb:.1f} MB)")
        return True
    else:
        print(f"✗ Model NOT found: {model_path}")
        print("  Run: python scripts/setup.py")
        return False


def check_database():
    """ตรวจสอบ database"""
    db_path = Path(__file__).parent.parent / "database" / "warehouse.db"
    
    if db_path.exists():
        print(f"✓ Database exists: {db_path}")
    else:
        print(f"ℹ Database will be created on first run: {db_path}")
    return True


def check_folders():
    """ตรวจสอบ folder structure"""
    base = Path(__file__).parent.parent
    folders = [
        base / "models",
        base / "database",
        base / "events",
        base / "logs",
    ]
    
    all_ok = True
    for folder in folders:
        if folder.exists():
            print(f"✓ {folder.name}/")
        else:
            print(f"✗ {folder.name}/ (missing)")
            all_ok = False
    
    return all_ok


def check_dependencies():
    """ตรวจสอบ Python packages"""
    packages = {
        'ultralytics': 'YOLO Detection',
        'cv2': 'OpenCV',
        'numpy': 'NumPy',
        'pandas': 'Pandas',
        'streamlit': 'Streamlit',
        'sqlite3': 'SQLite',
    }
    
    all_ok = True
    for package, name in packages.items():
        try:
            __import__(package)
            print(f"✓ {name}")
        except ImportError:
            print(f"✗ {name} (missing)")
            all_ok = False
    
    return all_ok


def check_camera():
    """ตรวจสอบกล้อง"""
    try:
        import cv2
        cap = cv2.VideoCapture(0)
        if cap.isOpened():
            ret, _ = cap.read()
            cap.release()
            if ret:
                print("✓ Camera is working")
                return True
            else:
                print("⚠ Camera found but cannot capture")
                return False
        else:
            print("⚠ Camera not available (optional)")
            return True
    except Exception as e:
        print(f"⚠ Camera check failed: {e}")
        return True


def main():
    print("\n" + "="*60)
    print("Smart Warehouse - System Check")
    print("="*60)
    
    print("\n📁 Folders:")
    folder_ok = check_folders()
    
    print("\n📦 Dependencies:")
    deps_ok = check_dependencies()
    
    print("\n🤖 Model:")
    model_ok = check_model()
    
    print("\n📷 Camera:")
    camera_ok = check_camera()
    
    print("\n" + "="*60)
    print("Summary:")
    print("="*60)
    
    status = {
        'Folders': folder_ok,
        'Dependencies': deps_ok,
        'Model': model_ok,
        'Camera': camera_ok,
    }
    
    for name, ok in status.items():
        symbol = "✓" if ok else "✗"
        print(f"{symbol} {name}")
    
    if model_ok and deps_ok:
        print("\n✓ System is ready to run!")
        print("\nRun with:")
        print("  python main.py              # Start detection")
        print("  streamlit run dashboard/app.py  # View dashboard")
        return 0
    else:
        print("\n✗ Please fix the issues above.")
        if not model_ok:
            print("  → Run: python scripts/setup.py")
        if not deps_ok:
            print("  → Run: pip install -r requirements.txt")
        return 1


if __name__ == "__main__":
    sys.exit(main())
