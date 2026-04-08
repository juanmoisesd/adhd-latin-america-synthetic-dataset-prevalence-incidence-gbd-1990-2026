.PHONY: all setup test run clean

all: setup test run

setup:
	pip install -r requirements.txt

test:
	pytest tests/

run:
	bash run.sh

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
