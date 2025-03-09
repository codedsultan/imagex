#!/bin/bash
set -e

echo "============================"
echo "Starting database migration..."
echo "============================"
bash migrate.sh

echo ""
echo "============================"
echo "Seeding data..."
echo "============================"
python seed_data.py

echo ""
echo "============================"
echo "All tasks completed successfully."
echo "============================"
