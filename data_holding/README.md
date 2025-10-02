# Data Holding Area

## Purpose
This is a **temporary holding area** for reviewing PDF pages before processing.

## Workflow

### 1. Convert PDFs
```bash
python scripts/convert_pdf.py your_blueprint.pdf
```

All pages will be extracted here for review.

### 2. Review Images
```bash
# Open in Finder
open .

# Or open in Preview
open *.png
```

Look through all pages and identify which ones contain the objects you want to count.

### 3. Select Relevant Pages

**What to keep:**
- ✅ Electrical plans (if counting outlets)
- ✅ Floor plans (if counting doors/windows)
- ✅ HVAC plans (if counting fixtures)
- ✅ Any page with objects you want to detect

**What to skip:**
- ❌ Title pages
- ❌ Cover sheets
- ❌ Text-only pages
- ❌ Site plans (unless relevant)
- ❌ Detail sheets without target objects

### 4. Move Selected Images

Copy only the relevant pages to `data_raw/`:

```bash
# Move specific pages
cp blueprint_page_003.png ../data_raw/floor1_electrical.png
cp blueprint_page_004.png ../data_raw/floor2_electrical.png

# Or move all at once
cp *.png ../data_raw/
```

### 5. Clean Up (Optional)

After moving the images you want, you can delete the holding area:

```bash
# Delete all images in holding area
rm *.png

# Or keep them as backup
```

## Tips

- **Descriptive names**: Rename files when moving to `data_raw/` for easier tracking
- **Batch review**: Convert multiple PDFs, then review all at once
- **Keep originals**: Don't delete PDFs until you're sure the conversion worked
- **Quality check**: Zoom in on images to ensure text/symbols are readable

## Example Structure

```
data_holding/
├── electrical_plans_page_001.png  (Title - skip)
├── electrical_plans_page_002.png  (Site plan - skip)
├── electrical_plans_page_003.png  (Floor 1 - KEEP ✅)
├── electrical_plans_page_004.png  (Floor 2 - KEEP ✅)
└── electrical_plans_page_005.png  (Details - skip)

After review, move to data_raw/:
data_raw/
├── floor1_electrical.png  (from page 003)
└── floor2_electrical.png  (from page 004)
```

## Next Steps

After moving selected images to `data_raw/`:
1. Start labeling with `labelImg`
2. Follow the LABELING_GUIDE.md
3. Train your model

---

**This folder is temporary** - images here are for review only. The actual processing happens with images in `data_raw/`.
