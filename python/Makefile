PYTHON ?= python3

.DEFAULT_GOAL := run
.PHONY: run test test-unit test-approbation

test: test-unit test-approbation

test-unit:
	PYTHONPATH=.. $(PYTHON) -m unittest discover -s tests/unit -p "test_*.py" -v

test-approbation:
	PYTHONPATH=.. $(PYTHON) -m unittest discover -s tests/approbation -p "test_*.py" -v

run:
	PYTHONPATH=.. $(PYTHON) main.py

