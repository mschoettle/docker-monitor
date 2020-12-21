#!/bin/bash
SCRIPT_DIR=`dirname $0`

# activate virtual environment
source "$SCRIPT_DIR/.venv/bin/activate"

python monitor.py
