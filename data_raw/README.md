# Raw Data Directory

## Purpose
Place your source blueprint images here before labeling.

## Supported Formats
- PNG
- JPEG/JPG
- TIFF

## Image Requirements
- **Resolution**: Higher is better (minimum 800x600 recommended)
- **Quality**: Clear, readable blueprints
- **Format**: Digital scans or photos of construction blueprints

## Workflow
1. Add blueprint images to this folder
2. Use LabelImg to annotate objects
3. Save annotations in YOLO format
4. Move labeled images to `data_labeled/images/`
5. Annotations will be saved to `data_labeled/labels/`

## Example Naming
- `blueprint_floor1_001.png`
- `electrical_plan_building_a.jpg`
- `floor_plan_level2.png`

Keep filenames descriptive and consistent for easier tracking.
