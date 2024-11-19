#!/bin/bash
python csv_scraper.py \
    --job-id 1 \
    --csv-url "https://www.uvek-gis.admin.ch/BFE/ogd/104/ogd104_stromproduktion_swissgrid.csv" \
    --output-path "./stromproduktion_swissgrid.csv" \
    --kp_auth_token test123 --kp_host localhost --kp_port 8000 --kp_scheme http \
    --log-level INFO
