# PDF Source Files

## Purpose
Store your source PDF blueprint files here for easy access and conversion.

## Usage

### 1. Add Your PDFs
```bash
# Copy PDFs to this folder
cp ~/Downloads/electrical_plans.pdf .
cp ~/Documents/blueprints/*.pdf .
```

### 2. Convert to Images
```bash
# Convert a single PDF
python ../scripts/convert_pdf.py electrical_plans.pdf

# Convert all PDFs in this folder
python ../scripts/convert_pdf.py --batch .
```

### 3. Review & Process
Images will be saved to `data_holding/` for review.

## File Organization

### Recommended naming:
```
pdfs/
├── project_name_electrical.pdf
├── project_name_mechanical.pdf
├── project_name_plumbing.pdf
└── building_a_floor_plans.pdf
```

### Tips:
- Use descriptive names
- Include project name
- Include plan type (electrical, mechanical, etc.)
- Keep originals as backup

## Conversion Examples

### Convert entire PDF:
```bash
python ../scripts/convert_pdf.py electrical_plans.pdf
```

### Convert specific pages:
```bash
# Pages 3-7 only
python ../scripts/convert_pdf.py electrical_plans.pdf --pages 3-7

# Single page
python ../scripts/convert_pdf.py electrical_plans.pdf --pages 5
```

### High resolution:
```bash
python ../scripts/convert_pdf.py electrical_plans.pdf --dpi 600
```

### Batch convert all:
```bash
python ../scripts/convert_pdf.py --batch .
```

## Next Steps

1. **Convert PDFs** → Images go to `data_holding/`
2. **Review images** → Select relevant pages
3. **Move to data_raw/** → Copy selected pages
4. **Label & train** → Process with AI

See **PDF_WORKFLOW.md** for complete instructions.

---

**Note**: This folder is gitignored - your PDFs won't be committed to the repository.
