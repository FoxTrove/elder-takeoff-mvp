# 🚀 Quick Start Guide - AI Takeoff MVP

Get up and running in 5 steps!

## Step 1: Setup Environment (5 minutes)

### Option A: Using Conda (Recommended)
```bash
conda create -n takeoff_mvp python=3.10 -y
conda activate takeoff_mvp
pip install -r requirements.txt
```

### Option B: Using venv
```bash
python3.10 -m venv takeoff_mvp
source takeoff_mvp/bin/activate  # Mac/Linux
pip install -r requirements.txt
```

### Option C: Automated Setup
```bash
./setup.sh
```

## Step 2: Install LabelImg (2 minutes)
```bash
pip install labelImg
```

## Step 3: Label Your Data (30-60 minutes)

1. **Add blueprint images** to `data_raw/` folder
   - Need at least 5 images (10-20 recommended)
   - PNG or JPEG format

2. **Launch LabelImg**:
   ```bash
   labelImg
   ```

3. **Configure LabelImg**:
   - Click "Open Dir" → Select `data_raw`
   - Click "Change Save Dir" → Select `data_labeled/labels`
   - Click "PascalVOC" button to switch to "YOLO"

4. **Label objects**:
   - Press `W` to create bounding box
   - Draw box around object (e.g., outlet, door)
   - Type class name (use same name consistently!)
   - Press `Ctrl+S` to save
   - Press `D` for next image

5. **Copy labeled images**:
   ```bash
   cp data_raw/*.png data_labeled/images/
   # or manually copy the images you labeled
   ```

6. **Update dataset.yaml**:
   - Edit `data_labeled/dataset.yaml`
   - Change class name from "outlet" to your object type

📖 **Need help?** See [LABELING_GUIDE.md](LABELING_GUIDE.md) for detailed instructions.

## Step 4: Train the Model (10-20 minutes)

### Option A: Jupyter Notebook (Recommended for beginners)
```bash
jupyter notebook notebooks/train_mvp.ipynb
```
Then run all cells (Cell → Run All)

### Option B: Command Line
```bash
python scripts/train.py --epochs 20 --batch 8 --device cpu
```

**Training time**: ~10-20 minutes on CPU, ~2-5 minutes on GPU

## Step 5: Run Inference (2 minutes)

### Option A: Jupyter Notebook
```bash
jupyter notebook notebooks/test_mvp.ipynb
```
Update the `test_image_path` variable, then run all cells.

### Option B: Command Line

**Single image**:
```bash
python scripts/inference.py --image data_raw/test_blueprint.png
```

**Batch processing**:
```bash
python scripts/inference.py --directory data_raw/ --output-csv results.csv
```

## 🎯 Expected Output

```
==================================================
🎯 TAKEOFF RESULTS
==================================================

📊 Total Objects Detected: 12

📋 Breakdown by Type:
   • outlet: 12

==================================================
```

Plus an annotated image showing bounding boxes around detected objects!

## 📁 Project Structure

```
takeoff-handler/
├── data_raw/              # Your blueprint images
├── data_labeled/
│   ├── images/           # Labeled images
│   ├── labels/           # YOLO .txt files
│   └── dataset.yaml      # Dataset config
├── models/               # Trained models
│   └── best.pt          # Your trained model
├── notebooks/
│   ├── train_mvp.ipynb  # Training notebook
│   └── test_mvp.ipynb   # Inference notebook
├── scripts/
│   ├── train.py         # CLI training
│   └── inference.py     # CLI inference
└── requirements.txt     # Dependencies
```

## ⚙️ Common Commands

### Training
```bash
# Basic training
python scripts/train.py

# Custom parameters
python scripts/train.py --epochs 50 --batch 16 --device cuda

# With GPU
python scripts/train.py --device cuda
```

### Inference
```bash
# Single image
python scripts/inference.py --image path/to/image.png

# Directory with CSV output
python scripts/inference.py --directory data_raw/ --output-csv results.csv

# Adjust confidence threshold
python scripts/inference.py --image test.png --conf 0.35

# JSON output with details
python scripts/inference.py --directory data_raw/ --output-json results.json
```

### Data Labeling
```bash
# Launch LabelImg
labelImg

# Or with specific directory
labelImg data_raw/ data_labeled/labels/
```

## 🔧 Troubleshooting

### "No module named 'ultralytics'"
```bash
# Make sure environment is activated
conda activate takeoff_mvp
# Then reinstall
pip install -r requirements.txt
```

### "Model not found"
- Run training first: `jupyter notebook notebooks/train_mvp.ipynb`
- Check that `models/best.pt` exists

### "No images found"
- Verify images are in `data_labeled/images/`
- Check file extensions (.png, .jpg, .jpeg)

### Low accuracy / No detections
- Add more training data (50-100+ images recommended)
- Train for more epochs: `--epochs 50`
- Lower confidence threshold: `--conf 0.15`
- Check that labels are correct in `data_labeled/labels/`

### Out of memory during training
- Reduce batch size: `--batch 4`
- Use smaller image size: `--imgsz 416`

## 📚 Next Steps

1. **Improve accuracy**: Add more labeled training data
2. **Add more classes**: Label doors, windows, fixtures, etc.
3. **Optimize**: Try larger models (yolov8s, yolov8m)
4. **Deploy**: Create a web interface or API
5. **Integrate**: Connect to your estimation software

## 📖 Full Documentation

- **[README.md](README.md)**: Complete project documentation
- **[LABELING_GUIDE.md](LABELING_GUIDE.md)**: Detailed labeling instructions
- **[YOLOv8 Docs](https://docs.ultralytics.com/)**: Official YOLOv8 documentation

## 💡 Tips

- Start with **one object type** (e.g., outlets only)
- Use **consistent naming** for classes
- Label **all instances** in each image
- **Review labels** before training
- Keep **backup copies** of your labeled data

## 🎉 Success Checklist

- [ ] Environment created and activated
- [ ] Dependencies installed
- [ ] LabelImg installed
- [ ] 5-10 images labeled
- [ ] Images copied to `data_labeled/images/`
- [ ] Labels exist in `data_labeled/labels/`
- [ ] `dataset.yaml` updated with correct class name
- [ ] Training completed successfully
- [ ] Model saved to `models/best.pt`
- [ ] Inference runs and produces count
- [ ] Annotated images generated

---

**Need help?** Check the full [README.md](README.md) or open an issue!
