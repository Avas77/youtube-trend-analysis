#!/bin/bash

# Go to your project directory
cd "$(dirname "$0")"

# Run your scripts
python3 youtube_data_ingestion.py
python3 data-cleaning-transform.py

# Optional: log the time of execution
echo "Pipeline ran at $(date)" >> pipeline_log.txt
