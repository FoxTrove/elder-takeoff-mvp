# 🚀 Quick Command Reference

## Setup (One-Time)

```bash
# Install PDF converter dependencies
pip install pdf2image pillow
brew install poppler
```

---

## 📄 PDF Conversion

### Basic Conversion
```bash
# Convert entire PDF
python scripts/convert_pdf.py blueprint.pdf
```

### Specific Pages
```bash
# Convert pages 3-7
python scripts/convert_pdf.py blueprint.pdf --pages 3-7

# Convert single page
python scripts/convert_pdf.py blueprint.pdf --pages 5
```

### Batch Convert
```bash
# Convert all PDFs in pdfs/ folder
python scripts/convert_pdf.py --batch pdfs/
```

### High Resolution
```bash
# For detailed blueprints
python scripts/convert_pdf.py blueprint.pdf --dpi 600
```

---

## 📁 File Management

### Review Converted Images
```bash
# Open holding area in Finder
open data_holding/

# View images in Preview
open data_holding/*.png
```

### Move Selected Images
```bash
# Move specific files
cp data_holding/blueprint_page_003.png data_raw/floor1.png

# Move all at once
cp data_holding/*.png data_raw/
```

---

## 🏷️ Data Labeling

### Start LabelImg
```bash
labelImg
```

### LabelImg Quick Keys
- `W` - Create bounding box
- `D` - Next image
- `A` - Previous image
- `Ctrl+S` - Save
- `Del` - Delete box

---

## 🤖 Training & Inference

### Train Model (Jupyter)
```bash
jupyter notebook notebooks/train_mvp.ipynb
```

### Train Model (CLI)
```bash
python scripts/train.py --epochs 20 --batch 8
```

### Run Inference (Jupyter)
```bash
jupyter notebook notebooks/test_mvp.ipynb
```

### Run Inference (CLI)
```bash
# Single image
python scripts/inference.py --image data_raw/test.png

# Batch with CSV output
python scripts/inference.py --directory data_raw/ --output-csv results.csv
```

---

## 🔧 Environment

### Activate
```bash
source activate.sh
```

### Deactivate
```bash
deactivate
```

### Test Setup
```bash
./takeoff_mvp/bin/python test_environment.py
```

---

## 📊 Complete Workflow

```bash
# 1. Convert PDF
python scripts/convert_pdf.py blueprint.pdf

# 2. Review images
open data_holding/

# 3. Move selected pages
cp data_holding/blueprint_page_003.png data_raw/floor1.png

# 4. Label images
labelImg

# 5. Train model
jupyter notebook notebooks/train_mvp.ipynb

# 6. Run inference
jupyter notebook notebooks/test_mvp.ipynb
```

---

## 📚 Documentation

| Guide | Purpose |
|-------|---------|
| `QUICKSTART.md` | 5-step quick start |
| `PDF_WORKFLOW.md` | PDF conversion guide |
| `LABELING_GUIDE.md` | Labeling instructions |
| `ENVIRONMENT_SETUP.md` | Environment details |
| `README.md` | Complete documentation |

---

## 🆘 Troubleshooting

### PDF Converter Issues
```bash
# Install dependencies
pip install pdf2image pillow
brew install poppler
```

### Environment Issues
```bash
# Reinstall dependencies
./takeoff_mvp/bin/pip install -r requirements.txt
```

### Test Everything
```bash
./takeoff_mvp/bin/python test_environment.py
```

---

**Keep this file handy for quick reference!** 📌
