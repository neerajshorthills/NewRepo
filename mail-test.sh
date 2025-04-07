#!/bin/bash
set -e

# Extend PATH to include Python 3.13 binaries
export PATH=$PATH:/Library/Frameworks/Python.framework/Versions/3.13/bin

# Upgrade pip and install required packages
python3.13 -m pip install --upgrade pip
pip3 install pytest pytest-html

# Run pytest and generate the HTML report
pytest --html=report.html
