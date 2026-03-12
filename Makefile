PYTHONPATH ?= src

.PHONY: run test lint format typecheck check

run:
	PYTHONPATH=$(PYTHONPATH) python -m chatgtp

test:
	PYTHONPATH=$(PYTHONPATH) python -m unittest discover -s tests -p 'test_*.py'

lint:
	PYTHONPATH=$(PYTHONPATH) python -m ruff check src tests

format:
	PYTHONPATH=$(PYTHONPATH) python -m black src tests

typecheck:
	PYTHONPATH=$(PYTHONPATH) python -m mypy src

check: lint typecheck test
