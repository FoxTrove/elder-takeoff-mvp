# 📄 PDF to Image Workflow Guide

## Overview

This guide explains how to convert your PDF blueprints to images and select which pages to process.

## 🔄 The Workflow

```
Your PDFs → Convert to Images → Holding Area → Review → Select → Process
```

### Step-by-Step:

1. **Convert PDF** → All pages extracted to `data_holding/`
2. **Review images** → Look at all pages in Finder/Preview
3. **Select relevant pages** → Copy only the pages you want to `data_raw/`
4. **Gather marked-up drawings** → If Elder provided them (highly valuable!)
5. **Label & Train** → Process selected images with AI using marked-up drawings as reference

---

## 📦 Setup (One-Time)

### Install Required Dependencies

```bash
# Activate environment
source activate.sh

# Install PDF converter packages
pip install pdf2image pillow

# Install poppler (required for PDF conversion on Mac)
brew install poppler
```

**Note**: If you don't have Homebrew, install it first:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

---

## 🚀 Using the PDF Converter

### Basic Usage

```bash
# Convert entire PDF to holding area
python scripts/convert_pdf.py your_blueprint.pdf
```

**Output:**
- All pages saved to `data_holding/`
- Named: `your_blueprint_page_001.png`, `your_blueprint_page_002.png`, etc.

### Convert Specific Pages

```bash
# Convert pages 3-7 only
python scripts/convert_pdf.py blueprint.pdf --pages 3-7

# Convert single page
python scripts/convert_pdf.py blueprint.pdf --pages 5
```

### Batch Convert Multiple PDFs

```bash
# Convert all PDFs in a folder
python scripts/convert_pdf.py --batch pdfs/
```

### High Resolution Output

```bash
# For detailed blueprints, use higher DPI
python scripts/convert_pdf.py blueprint.pdf --dpi 600
```

### Custom Output Directory

```bash
# Save to different location
python scripts/convert_pdf.py blueprint.pdf --output my_review_folder/
```

---

## 📋 Complete Example Workflow

### 1. Place Your PDFs

```bash
# Create a folder for your PDFs (optional)
mkdir pdfs
cp ~/Downloads/*.pdf pdfs/
```

### 2. Convert PDF to Images

```bash
# Convert a single PDF
python scripts/convert_pdf.py pdfs/electrical_plans.pdf
```

**Output:**
```
======================================================================
PDF TO IMAGE CONVERTER
======================================================================

📄 Input PDF: electrical_plans.pdf
📁 Output directory: data_holding
🎨 Resolution: 300 DPI
📐 Format: PNG
📋 Pages: All

🔄 Converting PDF to images...
✅ Extracted 5 page(s)
   💾 Saved: electrical_plans_page_001.png
   💾 Saved: electrical_plans_page_002.png
   💾 Saved: electrical_plans_page_003.png
   💾 Saved: electrical_plans_page_004.png
   💾 Saved: electrical_plans_page_005.png

======================================================================
✅ CONVERSION COMPLETE
======================================================================

📊 Summary:
   • Pages converted: 5
   • Files saved: 5
   • Location: /path/to/data_holding

📋 Next Steps:
   1. Review images in: data_holding/
   2. Select pages you want to process
   3. Move selected images to: data_raw/
   4. Start labeling with: labelImg
```

### 3. Review Images in Holding Area

```bash
# Open holding area in Finder
open data_holding/
```

**Or use Preview:**
```bash
# Open all images in Preview
open data_holding/*.png
```

### 4. Select Pages to Process

**Review each image and identify:**
- ✅ Pages with outlets/doors/objects you want to count
- ❌ Title pages, cover sheets, text-only pages

### 5. Move Selected Images to Processing Folder

**Option A: Move specific files**
```bash
# Move only pages 3 and 4 (the electrical floor plans)
cp data_holding/electrical_plans_page_003.png data_raw/
cp data_holding/electrical_plans_page_004.png data_raw/
```

**Option B: Move all at once**
```bash
# Move all pages (if all are relevant)
cp data_holding/electrical_plans_page_*.png data_raw/
```

**Option C: Rename while moving**
```bash
# Give them descriptive names
cp data_holding/electrical_plans_page_003.png data_raw/floor1_electrical.png
cp data_holding/electrical_plans_page_004.png data_raw/floor2_electrical.png
```

### 6. Start Labeling

```bash
# Launch LabelImg
labelImg
```

---

## 📁 Directory Structure

```
takeoff-handler/
├── pdfs/                    # (Optional) Store your source PDFs
│   └── electrical_plans.pdf
│
├── data_holding/            # Holding area for review
│   ├── electrical_plans_page_001.png  (Title page - skip)
│   ├── electrical_plans_page_002.png  (Site plan - skip)
│   ├── electrical_plans_page_003.png  (Floor 1 - KEEP)
│   ├── electrical_plans_page_004.png  (Floor 2 - KEEP)
│   └── electrical_plans_page_005.png  (Details - skip)
│
├── data_raw/                # Selected pages for processing
│   ├── floor1_electrical.png
│   └── floor2_electrical.png
│
└── data_labeled/            # After labeling
    ├── images/
    │   ├── floor1_electrical.png
    │   └── floor2_electrical.png
    └── labels/
        ├── floor1_electrical.txt
        └── floor2_electrical.txt
```

---

## 💡 Tips & Best Practices

### Page Selection
- **Include**: Pages with objects you want to count
- **Skip**: Title pages, text-only pages, irrelevant details
- **When in doubt**: Convert it and review - you can always delete later

### Naming Conventions
Use descriptive names when moving to `data_raw/`:
```bash
# Good names
floor1_electrical.png
floor2_electrical.png
building_a_outlets.png

# Less helpful
page_003.png
image_1.png
```

### Resolution (DPI)
- **300 DPI**: Good for most blueprints (default)
- **600 DPI**: For very detailed plans or small text
- **150 DPI**: For quick previews (faster processing)

### Batch Processing
If you have many PDFs:
```bash
# Convert all PDFs in a folder
python scripts/convert_pdf.py --batch pdfs/

# Then review all images at once
open data_holding/
```

---

## 🔧 Troubleshooting

### "pdf2image not found"
```bash
pip install pdf2image pillow
```

### "poppler not found" (Mac)
```bash
brew install poppler
```

### "poppler not found" (Linux)
```bash
sudo apt-get install poppler-utils
```

### Images are blurry
Increase DPI:
```bash
python scripts/convert_pdf.py blueprint.pdf --dpi 600
```

### PDF is password protected
Unlock the PDF first using Preview or Adobe Acrobat, then convert.

### Conversion is slow
- Lower DPI: `--dpi 150`
- Convert specific pages only: `--pages 3-5`

---

## 📊 Quick Reference

| Task | Command |
|------|---------|
| Convert entire PDF | `python scripts/convert_pdf.py file.pdf` |
| Convert specific pages | `python scripts/convert_pdf.py file.pdf --pages 3-7` |
| Batch convert | `python scripts/convert_pdf.py --batch pdfs/` |
| High resolution | `python scripts/convert_pdf.py file.pdf --dpi 600` |
| View holding area | `open data_holding/` |
| Move to processing | `cp data_holding/*.png data_raw/` |
| Start labeling | `labelImg` |

---

## 🎯 Complete Workflow Summary

```bash
# 1. Convert PDF
python scripts/convert_pdf.py blueprint.pdf

# 2. Review images
open data_holding/

# 3. Select and move relevant pages
cp data_holding/blueprint_page_003.png data_raw/floor1.png
cp data_holding/blueprint_page_004.png data_raw/floor2.png

# 4. Start labeling
labelImg

# 5. Train model
jupyter notebook notebooks/train_mvp.ipynb

# 6. Run inference on new blueprints
jupyter notebook notebooks/test_mvp.ipynb
```

---

## ✅ Next Steps

After converting and selecting your pages:
1. **Label the images** with LabelImg (see LABELING_GUIDE.md)
2. **Train the model** (see QUICKSTART.md)
3. **Run inference** on new blueprints

**You're ready to convert your PDFs!** 🚀
