"""
Production Training Script for AI Takeoff MVP

This script provides a command-line interface for training the YOLOv8 model.
Use this for automated training pipelines or production environments.

Usage:
    python scripts/train.py --epochs 20 --batch 8 --device cpu
"""

import argparse
from pathlib import Path
from ultralytics import YOLO
import yaml


def train_model(
    data_yaml: str = 'data_labeled/dataset.yaml',
    epochs: int = 20,
    batch: int = 8,
    imgsz: int = 640,
    device: str = 'cpu',
    name: str = 'takeoff_mvp',
    patience: int = 5
):
    """
    Train YOLOv8 model for construction takeoff.
    
    Args:
        data_yaml: Path to dataset YAML configuration
        epochs: Number of training epochs
        batch: Batch size
        imgsz: Image size for training
        device: Device to use ('cpu', 'cuda', or device number)
        name: Experiment name
        patience: Early stopping patience
    """
    print("="*70)
    print("AI TAKEOFF MVP - TRAINING SCRIPT")
    print("="*70)
    
    # Verify data configuration exists
    data_path = Path(data_yaml)
    if not data_path.exists():
        raise FileNotFoundError(f"Dataset configuration not found: {data_path}")
    
    # Load and display dataset info
    with open(data_path, 'r') as f:
        config = yaml.safe_load(f)
    
    print(f"\n📋 Dataset Configuration:")
    print(f"   Path: {data_path.absolute()}")
    print(f"   Classes: {config.get('names', {})}")
    
    # Check for training images
    images_dir = data_path.parent / config.get('train', 'images')
    if images_dir.exists():
        image_files = list(images_dir.glob('*.png')) + list(images_dir.glob('*.jpg'))
        print(f"   Training images: {len(image_files)}")
        
        if len(image_files) < 5:
            print("\n⚠️  WARNING: Less than 5 training images found.")
            print("   Consider adding more data for better results.")
    
    # Load pre-trained model
    print(f"\n🔄 Loading YOLOv8n model...")
    model = YOLO('yolov8n.pt')
    
    # Training parameters
    print(f"\n⚙️  Training Parameters:")
    print(f"   Epochs: {epochs}")
    print(f"   Batch size: {batch}")
    print(f"   Image size: {imgsz}")
    print(f"   Device: {device}")
    print(f"   Patience: {patience}")
    
    # Start training
    print(f"\n🚀 Starting training...\n")
    
    results = model.train(
        data=str(data_path),
        epochs=epochs,
        imgsz=imgsz,
        batch=batch,
        name=name,
        patience=patience,
        save=True,
        plots=True,
        device=device,
        verbose=True
    )
    
    print("\n✅ Training completed!")
    
    # Save best model to models directory
    source_model = Path(f'runs/detect/{name}/weights/best.pt')
    target_model = Path('models/best.pt')
    
    if source_model.exists():
        target_model.parent.mkdir(parents=True, exist_ok=True)
        import shutil
        shutil.copy(source_model, target_model)
        print(f"\n💾 Best model saved to: {target_model.absolute()}")
        print(f"   Model size: {target_model.stat().st_size / (1024*1024):.2f} MB")
    
    # Display results location
    results_dir = Path(f'runs/detect/{name}')
    print(f"\n📊 Training results saved to: {results_dir.absolute()}")
    print(f"   - results.png: Training metrics")
    print(f"   - confusion_matrix.png: Model performance")
    print(f"   - weights/best.pt: Best model checkpoint")
    
    print("\n" + "="*70)
    print("Next step: Run inference with scripts/inference.py")
    print("="*70)
    
    return results


def main():
    parser = argparse.ArgumentParser(
        description='Train YOLOv8 model for construction takeoff'
    )
    
    parser.add_argument(
        '--data',
        type=str,
        default='data_labeled/dataset.yaml',
        help='Path to dataset YAML file'
    )
    
    parser.add_argument(
        '--epochs',
        type=int,
        default=20,
        help='Number of training epochs'
    )
    
    parser.add_argument(
        '--batch',
        type=int,
        default=8,
        help='Batch size'
    )
    
    parser.add_argument(
        '--imgsz',
        type=int,
        default=640,
        help='Image size for training'
    )
    
    parser.add_argument(
        '--device',
        type=str,
        default='cpu',
        help='Device to use (cpu, cuda, or device number)'
    )
    
    parser.add_argument(
        '--name',
        type=str,
        default='takeoff_mvp',
        help='Experiment name'
    )
    
    parser.add_argument(
        '--patience',
        type=int,
        default=5,
        help='Early stopping patience'
    )
    
    args = parser.parse_args()
    
    train_model(
        data_yaml=args.data,
        epochs=args.epochs,
        batch=args.batch,
        imgsz=args.imgsz,
        device=args.device,
        name=args.name,
        patience=args.patience
    )


if __name__ == '__main__':
    main()
