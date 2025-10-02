#!/bin/bash

# Quick activation script for the takeoff_mvp environment
# Usage: source activate.sh

echo "🚀 Activating AI Takeoff MVP environment..."
source takeoff_mvp/bin/activate

echo ""
echo "✅ Environment activated!"
echo ""
echo "Available commands:"
echo "  jupyter notebook          - Start Jupyter"
echo "  labelImg                  - Start LabelImg for labeling"
echo "  python scripts/train.py   - Train model (CLI)"
echo "  python scripts/inference.py --help  - Run inference (CLI)"
echo ""
echo "Quick start:"
echo "  jupyter notebook notebooks/train_mvp.ipynb"
echo ""
