#!/usr/bin/env python3
"""
Environment Test Script
Verifies all dependencies are correctly installed
"""

import sys

def test_imports():
    """Test all critical imports"""
    print("="*70)
    print("TESTING ENVIRONMENT SETUP")
    print("="*70)
    
    tests_passed = 0
    tests_failed = 0
    
    # Test 1: Ultralytics/YOLOv8
    print("\n1. Testing Ultralytics (YOLOv8)...")
    try:
        from ultralytics import YOLO
        print("   ✅ Ultralytics imported successfully")
        tests_passed += 1
    except Exception as e:
        print(f"   ❌ Failed: {e}")
        tests_failed += 1
    
    # Test 2: PyTorch
    print("\n2. Testing PyTorch...")
    try:
        import torch
        print(f"   ✅ PyTorch {torch.__version__} imported successfully")
        print(f"   Device available: {torch.device('cuda' if torch.cuda.is_available() else 'cpu')}")
        tests_passed += 1
    except Exception as e:
        print(f"   ❌ Failed: {e}")
        tests_failed += 1
    
    # Test 3: OpenCV
    print("\n3. Testing OpenCV...")
    try:
        import cv2
        print(f"   ✅ OpenCV {cv2.__version__} imported successfully")
        tests_passed += 1
    except Exception as e:
        print(f"   ❌ Failed: {e}")
        tests_failed += 1
    
    # Test 4: Pillow
    print("\n4. Testing Pillow...")
    try:
        from PIL import Image
        print(f"   ✅ Pillow imported successfully")
        tests_passed += 1
    except Exception as e:
        print(f"   ❌ Failed: {e}")
        tests_failed += 1
    
    # Test 5: Jupyter
    print("\n5. Testing Jupyter...")
    try:
        import jupyter
        print(f"   ✅ Jupyter imported successfully")
        tests_passed += 1
    except Exception as e:
        print(f"   ❌ Failed: {e}")
        tests_failed += 1
    
    # Test 6: NumPy
    print("\n6. Testing NumPy...")
    try:
        import numpy as np
        print(f"   ✅ NumPy {np.__version__} imported successfully")
        tests_passed += 1
    except Exception as e:
        print(f"   ❌ Failed: {e}")
        tests_failed += 1
    
    # Test 7: Matplotlib
    print("\n7. Testing Matplotlib...")
    try:
        import matplotlib
        print(f"   ✅ Matplotlib {matplotlib.__version__} imported successfully")
        tests_passed += 1
    except Exception as e:
        print(f"   ❌ Failed: {e}")
        tests_failed += 1
    
    # Test 8: YAML
    print("\n8. Testing PyYAML...")
    try:
        import yaml
        print(f"   ✅ PyYAML imported successfully")
        tests_passed += 1
    except Exception as e:
        print(f"   ❌ Failed: {e}")
        tests_failed += 1
    
    # Summary
    print("\n" + "="*70)
    print("TEST SUMMARY")
    print("="*70)
    print(f"✅ Passed: {tests_passed}")
    print(f"❌ Failed: {tests_failed}")
    print(f"Total: {tests_passed + tests_failed}")
    
    if tests_failed == 0:
        print("\n🎉 All tests passed! Environment is ready to use.")
        return True
    else:
        print(f"\n⚠️  {tests_failed} test(s) failed. Please check the errors above.")
        return False

def test_yolo_model():
    """Test YOLOv8 model loading"""
    print("\n" + "="*70)
    print("TESTING YOLO MODEL LOADING")
    print("="*70)
    
    try:
        from ultralytics import YOLO
        print("\nLoading YOLOv8n model (this will download ~6MB on first run)...")
        model = YOLO('yolov8n.pt')
        print("✅ YOLOv8n model loaded successfully!")
        print(f"   Model type: {type(model)}")
        print(f"   Model classes: {len(model.names)} classes")
        return True
    except Exception as e:
        print(f"❌ Failed to load model: {e}")
        return False

if __name__ == "__main__":
    print("\n🔧 AI Takeoff MVP - Environment Test\n")
    
    # Run import tests
    imports_ok = test_imports()
    
    # Run YOLO model test
    if imports_ok:
        model_ok = test_yolo_model()
        
        if model_ok:
            print("\n" + "="*70)
            print("🎉 ENVIRONMENT SETUP COMPLETE!")
            print("="*70)
            print("\nNext steps:")
            print("1. Place blueprint images in data_raw/")
            print("2. Run: ./takeoff_mvp/bin/labelImg")
            print("3. Label your images")
            print("4. Run: ./takeoff_mvp/bin/jupyter notebook notebooks/train_mvp.ipynb")
            print("\nFor detailed instructions, see QUICKSTART.md")
            print("="*70)
            sys.exit(0)
        else:
            sys.exit(1)
    else:
        sys.exit(1)
