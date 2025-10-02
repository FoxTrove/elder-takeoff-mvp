#!/bin/bash

# AI Takeoff MVP - Setup Script
# This script automates the environment setup process

echo "=================================================="
echo "AI TAKEOFF MVP - AUTOMATED SETUP"
echo "=================================================="

# Check if conda is available
if command -v conda &> /dev/null; then
    echo ""
    echo "✅ Conda detected"
    echo ""
    echo "Creating conda environment 'takeoff_mvp' with Python 3.10..."
    conda create -n takeoff_mvp python=3.10 -y
    
    echo ""
    echo "To activate the environment, run:"
    echo "  conda activate takeoff_mvp"
    echo ""
    echo "Then install dependencies with:"
    echo "  pip install -r requirements.txt"
    
elif command -v python3.10 &> /dev/null; then
    echo ""
    echo "✅ Python 3.10 detected"
    echo ""
    echo "Creating virtual environment 'takeoff_mvp'..."
    python3.10 -m venv takeoff_mvp
    
    echo ""
    echo "To activate the environment, run:"
    echo "  source takeoff_mvp/bin/activate"
    echo ""
    echo "Then install dependencies with:"
    echo "  pip install -r requirements.txt"
    
else
    echo ""
    echo "❌ Neither conda nor Python 3.10 found"
    echo ""
    echo "Please install one of the following:"
    echo "  - Miniconda: https://docs.conda.io/en/latest/miniconda.html"
    echo "  - Python 3.10: https://www.python.org/downloads/"
    echo ""
    exit 1
fi

echo ""
echo "=================================================="
echo "NEXT STEPS:"
echo "=================================================="
echo ""
echo "1. Activate the virtual environment (see command above)"
echo "2. Install dependencies:"
echo "     pip install -r requirements.txt"
echo ""
echo "3. Install LabelImg for data labeling:"
echo "     pip install labelImg"
echo ""
echo "4. Read the documentation:"
echo "     - README.md: Project overview and setup"
echo "     - LABELING_GUIDE.md: How to label blueprint images"
echo ""
echo "5. Start labeling your data:"
echo "     labelImg"
echo ""
echo "6. Train your model:"
echo "     jupyter notebook notebooks/train_mvp.ipynb"
echo ""
echo "7. Run inference:"
echo "     jupyter notebook notebooks/test_mvp.ipynb"
echo ""
echo "=================================================="
echo "For help, see README.md or visit:"
echo "https://docs.ultralytics.com/"
echo "=================================================="
