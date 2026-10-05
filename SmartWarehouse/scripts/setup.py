#!/usr/bin/env python3
"""
Setup script to download and prepare YOLO model for Smart Warehouse
"""

import os
import sys
from pathlib import Path
import urllib.request
import shutil


def create_directories():
    """สร้าง folder structure ที่ต้องการ"""
    base_dir = Path(__file__).parent.parent
    dirs = [
        base_dir / "models",
        base_dir / "database",
        base_dir / "events",
        base_dir / "logs",
    ]
    
    for d in dirs:
        d.mkdir(exist_ok=True, parents=True)
        print(f"✓ Created: {d}")


def download_model():
    """ดาวโหลด YOLO model"""
    print("\n" + "="*60)
    print("Downloading YOLO11n Model...")
    print("="*60)
    
    try:
        from ultralytics import YOLO
        
        print("Loading YOLO11n model (this may take a few minutes)...")
        model = YOLO('yolo11n.pt')
        
        print("✓ Model loaded successfully!")
        print(f"Model path: {model.model_name}")
        
        return True
    except Exception as e:
        print(f"✗ Error downloading model: {e}")
        print("\nTrying alternative download method...")
        return download_model_alternative()


def download_model_alternative():
    """ดาวโหลด model ด้วยวิธี alternative"""
    try:
        import urllib.request
        from pathlib import Path
        
        model_path = Path(__file__).parent.parent / "models" / "best.pt"
        url = "https://github.com/ultralytics/assets/releases/download/v8.2.0/yolo11n.pt"
        
        print(f"Downloading from: {url}")
        print(f"Saving to: {model_path}")
        
        urllib.request.urlretrieve(url, model_path)
        print(f"✓ Model downloaded to: {model_path}")
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        return False


def check_dependencies():
    """ตรวจสอบ dependencies"""
    print("\n" + "="*60)
    print("Checking Dependencies...")
    print("="*60)
    
    required = [
        'ultralytics',
        'opencv',
        'torch',
        'numpy',
        'pandas',
        'streamlit'
    ]
    
    missing = []
    for package in required:
        try:
            if package == 'opencv':
                import cv2
            elif package == 'torch':
                import torch
            else:
                __import__(package)
            print(f"✓ {package}")
        except ImportError:
            print(f"✗ {package} (missing)")
            missing.append(package)
    
    if missing:
        print(f"\n⚠ Missing packages: {', '.join(missing)}")
        print("Install with: pip install -r requirements.txt")
        return False
    
    return True


def test_camera():
    """ทดสอบกล้อง"""
    print("\n" + "="*60)
    print("Testing Camera...")
    print("="*60)
    
    try:
        import cv2
        cap = cv2.VideoCapture(0)
        
        if cap.isOpened():
            ret, frame = cap.read()
            cap.release()
            
            if ret:
                print(f"✓ Camera working! Resolution: {frame.shape[1]}x{frame.shape[0]}")
                return True
            else:
                print("✗ Camera found but cannot read frame")
                return False
        else:
            print("⚠ Camera not found (you can still test with image files)")
            return False
    except Exception as e:
        print(f"✗ Error: {e}")
        return False


def main():
    print("\n")
    print("█" * 60)
    print("█  Smart Warehouse Setup Script".ljust(59) + "█")
    print("█  Safety & Inventory Management System".ljust(59) + "█")
    print("█" * 60)
    
    # Step 1: Create directories
    create_directories()
    
    # Step 2: Check dependencies
    deps_ok = check_dependencies()
    
    # Step 3: Download model
    model_ok = download_model()
    
    # Step 4: Test camera
    camera_ok = test_camera()
    
    # Summary
    print("\n" + "="*60)
    print("Setup Summary")
    print("="*60)
    print(f"Directories:  {'✓ OK' if True else '✗ FAILED'}")
    print(f"Dependencies: {'✓ OK' if deps_ok else '⚠ MISSING'}")
    print(f"Model:        {'✓ OK' if model_ok else '✗ FAILED'}")
    print(f"Camera:       {'✓ OK' if camera_ok else '⚠ NOT AVAILABLE'}")
    
    if model_ok and deps_ok:
        print("\n✓ Setup complete! Ready to run.")
        print("\nNext steps:")
        print("  1. Run main program: python main.py")
        print("  2. Run dashboard:    streamlit run dashboard/app.py")
        return 0
    else:
        print("\n✗ Setup incomplete. Please fix the issues above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
