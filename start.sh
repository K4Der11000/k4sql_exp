#!/bin/bash
echo "Starting SQLi Scanner by kader11000..."
sleep 1
if [ -d "venv" ]; then
    source venv/bin/activate
    echo "Virtual environment activated."
fi
python app.py