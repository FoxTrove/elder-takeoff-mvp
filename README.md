# AI Takeoff MVP - Construction Blueprint Object Detection

## Project Overview
This is a Minimum Viable Product (MVP) for an AI-powered construction takeoff solution. The initial goal is to train a YOLOv8 model to accurately detect and count a single, distinct element (e.g., electrical outlets or doors) on construction blueprint images.

## Tech Stack
- **Model**: YOLOv8 (Ultralytics)
- **Framework**: PyTorch
- **Python Version**: 3.10
- **Labeling Tool**: LabelImg

## Directory Structure
```
/takeoff_mvp
    /data_raw        - Source blueprint files (PNG/JPEG)
    /data_labeled    - YOLO format training data
        /images      - Labeled images
        /labels      - YOLO .txt annotation files
    /models          - Trained model files (.pt)
    /notebooks       - Jupyter notebooks for development
    /scripts         - Production training/inference scripts
    requirements.txt - Python dependencies
```

## Setup Instructions

### 1. Create Virtual Environment

**Using Conda (Recommended):**
```bash
conda create -n takeoff_mvp python=3.10 -y
conda activate takeoff_mvp
```

**Using venv (Alternative):**
```bash
python3.10 -m venv takeoff_mvp
source takeoff_mvp/bin/activate  # On Mac/Linux
# takeoff_mvp\Scripts\activate  # On Windows
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Verify Installation
```bash
python -c "from ultralytics import YOLO; print('YOLOv8 installed successfully!')"
```

## Data Labeling Setup

### Install LabelImg
```bash
pip install labelImg
```

### Launch LabelImg
```bash
labelImg
```

### Labeling Instructions
1. **Open Dir**: Select the `data_raw` folder containing your blueprint images
2. **Change Save Dir**: Select `data_labeled/labels` for output
3. **Set Format**: Click "PascalVOC" button to switch to "YOLO" format
4. **Create Box**: Press 'W' or click "Create RectBox"
5. **Label**: Draw bounding boxes around target objects (e.g., outlets, doors)
6. **Save**: Press 'Ctrl+S' or click "Save"
7. **Next Image**: Press 'D'

**Important**: 
- Use consistent class names (e.g., "outlet", "door")
- Save annotations in YOLO format (.txt files)
- Copy labeled images to `data_labeled/images`

## Running the MVP

### 1. Prepare Training Data
- Place at least 5-10 blueprint images in `data_raw/`
- Label them using LabelImg
- Ensure images are in `data_labeled/images/`
- Ensure labels are in `data_labeled/labels/`

### 2. Train the Model
Open and run the training notebook:
```bash
jupyter notebook notebooks/train_mvp.ipynb
```

This will:
- Load a pre-trained YOLOv8n (nano) model
- Train on your labeled data (20 epochs)
- Save the trained model to `models/best.pt`

### 3. Run Inference
Open and run the testing notebook:
```bash
jupyter notebook notebooks/test_mvp.ipynb
```

This will:
- Load your trained model
- Run detection on a test image
- Display the image with bounding boxes
- **Output the total count** of detected objects

## Expected Output
The inference script will print:
```
Detected Objects: 12 outlets
```

And display the blueprint image with bounding boxes drawn around each detected object.

## Next Steps
- Collect more training data (50-100+ images recommended)
- Add more object classes (doors, windows, fixtures, etc.)
- Fine-tune hyperparameters for better accuracy
- Deploy model for production use

## Troubleshooting

### CUDA/GPU Issues
If you have an NVIDIA GPU and want to use it:
```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

### LabelImg Not Opening
Try installing with:
```bash
pip install labelImg PyQt5
```

### Import Errors
Ensure your virtual environment is activated:
```bash
conda activate takeoff_mvp  # or source takeoff_mvp/bin/activate
```

## Support
For issues or questions, refer to:
- [YOLOv8 Documentation](https://docs.ultralytics.com/)
- [LabelImg GitHub](https://github.com/heartexlabs/labelImg)
