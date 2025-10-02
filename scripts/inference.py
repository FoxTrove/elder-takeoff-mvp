"""
Production Inference Script for AI Takeoff MVP

This script provides a command-line interface for running inference on blueprint images.
Use this for batch processing or production deployments.

Usage:
    python scripts/inference.py --image path/to/blueprint.png
    python scripts/inference.py --directory data_raw/ --output results.csv
"""

import argparse
from pathlib import Path
from ultralytics import YOLO
import cv2
import pandas as pd
import json


def run_inference(
    model_path: str,
    image_path: str = None,
    directory_path: str = None,
    conf: float = 0.25,
    iou: float = 0.45,
    save_images: bool = True,
    output_csv: str = None,
    output_json: str = None
):
    """
    Run inference on single image or directory of images.
    
    Args:
        model_path: Path to trained model (.pt file)
        image_path: Path to single image
        directory_path: Path to directory of images
        conf: Confidence threshold
        iou: IoU threshold for NMS
        save_images: Save annotated images
        output_csv: Path to save CSV results
        output_json: Path to save JSON results
    """
    print("="*70)
    print("AI TAKEOFF MVP - INFERENCE SCRIPT")
    print("="*70)
    
    # Load model
    model_path = Path(model_path)
    if not model_path.exists():
        raise FileNotFoundError(f"Model not found: {model_path}")
    
    print(f"\n🔄 Loading model from: {model_path}")
    model = YOLO(str(model_path))
    print(f"✅ Model loaded successfully")
    print(f"   Classes: {model.names}")
    
    # Collect images to process
    images_to_process = []
    
    if image_path:
        img_path = Path(image_path)
        if not img_path.exists():
            raise FileNotFoundError(f"Image not found: {img_path}")
        images_to_process.append(img_path)
    
    if directory_path:
        dir_path = Path(directory_path)
        if not dir_path.exists():
            raise FileNotFoundError(f"Directory not found: {dir_path}")
        
        images_to_process.extend(dir_path.glob('*.png'))
        images_to_process.extend(dir_path.glob('*.jpg'))
        images_to_process.extend(dir_path.glob('*.jpeg'))
    
    if not images_to_process:
        raise ValueError("No images to process. Specify --image or --directory")
    
    print(f"\n📁 Processing {len(images_to_process)} image(s)...")
    print(f"   Confidence threshold: {conf}")
    print(f"   IoU threshold: {iou}\n")
    
    # Process images
    all_results = []
    
    for img_path in images_to_process:
        print(f"🔍 Processing: {img_path.name}")
        
        # Run detection
        results = model(str(img_path), conf=conf, iou=iou, verbose=False)
        
        for result in results:
            boxes = result.boxes
            total_count = len(boxes)
            
            # Count by class
            class_counts = {}
            detections = []
            
            for box in boxes:
                class_id = int(box.cls[0])
                class_name = model.names[class_id]
                confidence = float(box.conf[0])
                
                # Update class counts
                class_counts[class_name] = class_counts.get(class_name, 0) + 1
                
                # Store detection details
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                detections.append({
                    'class': class_name,
                    'confidence': confidence,
                    'bbox': [float(x1), float(y1), float(x2), float(y2)]
                })
            
            # Print results
            print(f"   ✅ Detected {total_count} objects")
            for class_name, count in class_counts.items():
                print(f"      • {class_name}: {count}")
            
            # Store results
            result_data = {
                'filename': img_path.name,
                'total_count': total_count,
                **class_counts,
                'detections': detections
            }
            all_results.append(result_data)
            
            # Save annotated image
            if save_images:
                annotated_img = result.plot(conf=True, line_width=2)
                output_img_path = Path('models') / f'annotated_{img_path.name}'
                output_img_path.parent.mkdir(parents=True, exist_ok=True)
                cv2.imwrite(str(output_img_path), annotated_img)
                print(f"   💾 Saved annotated image: {output_img_path}")
            
            print()
    
    # Display summary
    print("="*70)
    print("📊 SUMMARY")
    print("="*70)
    
    total_objects = sum(r['total_count'] for r in all_results)
    print(f"\nTotal images processed: {len(all_results)}")
    print(f"Total objects detected: {total_objects}")
    
    # Aggregate class counts
    aggregate_counts = {}
    for result in all_results:
        for class_name in model.names.values():
            if class_name in result:
                aggregate_counts[class_name] = aggregate_counts.get(class_name, 0) + result[class_name]
    
    if aggregate_counts:
        print("\nBreakdown by class:")
        for class_name, count in aggregate_counts.items():
            print(f"   • {class_name}: {count}")
    
    # Save to CSV
    if output_csv or directory_path:
        csv_path = output_csv or 'models/takeoff_results.csv'
        
        # Prepare DataFrame (exclude detections list for CSV)
        df_data = [{k: v for k, v in r.items() if k != 'detections'} for r in all_results]
        df = pd.DataFrame(df_data).fillna(0)
        
        df.to_csv(csv_path, index=False)
        print(f"\n💾 Results saved to CSV: {csv_path}")
    
    # Save to JSON
    if output_json:
        with open(output_json, 'w') as f:
            json.dump(all_results, f, indent=2)
        print(f"💾 Detailed results saved to JSON: {output_json}")
    
    print("\n" + "="*70)
    
    return all_results


def main():
    parser = argparse.ArgumentParser(
        description='Run inference on construction blueprints'
    )
    
    parser.add_argument(
        '--model',
        type=str,
        default='models/best.pt',
        help='Path to trained model'
    )
    
    parser.add_argument(
        '--image',
        type=str,
        help='Path to single image'
    )
    
    parser.add_argument(
        '--directory',
        type=str,
        help='Path to directory of images'
    )
    
    parser.add_argument(
        '--conf',
        type=float,
        default=0.25,
        help='Confidence threshold (0.0-1.0)'
    )
    
    parser.add_argument(
        '--iou',
        type=float,
        default=0.45,
        help='IoU threshold for NMS'
    )
    
    parser.add_argument(
        '--no-save-images',
        action='store_true',
        help='Do not save annotated images'
    )
    
    parser.add_argument(
        '--output-csv',
        type=str,
        help='Path to save CSV results'
    )
    
    parser.add_argument(
        '--output-json',
        type=str,
        help='Path to save JSON results'
    )
    
    args = parser.parse_args()
    
    if not args.image and not args.directory:
        parser.error("Must specify either --image or --directory")
    
    run_inference(
        model_path=args.model,
        image_path=args.image,
        directory_path=args.directory,
        conf=args.conf,
        iou=args.iou,
        save_images=not args.no_save_images,
        output_csv=args.output_csv,
        output_json=args.output_json
    )


if __name__ == '__main__':
    main()
