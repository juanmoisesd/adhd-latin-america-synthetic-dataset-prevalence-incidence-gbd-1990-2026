#!/bin/bash
set -e

echo "🚀 Starting ADHD Latin America Research Pipeline"

# Setup environment
pip install -r requirements.txt

# Run integrity tests
pytest tests/test_integrity.py

# Run simulation
python3 orchestrator.py

# Generate smoke test report
python3 smoke_test_v13.py

echo "✅ Pipeline complete. Results in results/"
