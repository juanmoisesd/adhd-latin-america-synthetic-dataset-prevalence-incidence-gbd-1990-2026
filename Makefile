.PHONY: all setup test run clean

all: setup test run

setup:
	pip install -r requirements.txt

test:
	pytest tests/
	python3 smoke_test_v13.py

run:
	python3 orchestrator.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf results/paper_draft_v13_NHB.txt
