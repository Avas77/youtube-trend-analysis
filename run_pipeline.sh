#!/bin/bash

# Go to your project directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Run your scripts
python3 youtube_data_ingestion.py
python3 data_cleaning.py
python3 postgres_setup.py
python3 dashboard.py

# Optional: log the time of execution
echo "Pipeline ran at $(date)" >> pipeline_log.txt
