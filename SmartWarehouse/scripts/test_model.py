#!/usr/bin/env python3
"""
Quick test to verify YOLO model works
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))


def test_model():
    """ทดสอบว่า model load ได้และ predict ได้"""
    print("\n" + "="*60)
    print("Testing YOLO Model")
    print("="*60)
    
    model_path = Path(__file__).parent.parent / "models" / "best.pt"
    
    if not model_path.exists():
        print(f"✗ Model not found: {model_path}")
        print("Run setup first: python scripts/setup.py")
        return False
    
    try:
        from ultralytics import YOLO
        import cv2
        import numpy as np
        
        print(f"Loading model: {model_path}")
        model = YOLO(str(model_path))
        print("✓ Model loaded successfully")
        
        # Create a test image
        print("\nCreating test image...")
        test_image = np.zeros((640, 640, 3), dtype=np.uint8)
        test_image = cv2.rectangle(test_image, (100, 100), (300, 300), (255, 255, 255), -1)
        
        print("Running inference...")
        results = model.predict(test_image, verbose=False)
        print(f"✓ Inference completed")
        
        print(f"  - Detections: {len(results[0].boxes)} objects")
        print(f"  - Classes: {results[0].names}")
        
        return True
        
    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = test_model()
    print("\n" + "="*60)
    if success:
        print("✓ Model test passed!")
        sys.exit(0)
    else:
        print("✗ Model test failed!")
        sys.exit(1)
