#!/bin/bash

mkdir -p data reports
pip install -r requirements.txt || true
python3 logic/load_targets.py