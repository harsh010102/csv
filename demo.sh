#!/bin/bash
python csv_scraper.py \
    --job-id 1 \
    --csv-url "https://www.uvek-gis.admin.ch/BFE/ogd/104/ogd104_stromproduktion_swissgrid.csv" \
    --output-path "./stromproduktion_swissgrid.csv" \
    --log-level INFO
