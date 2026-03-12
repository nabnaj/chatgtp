# chatgtp

This repository is organized as a **three-stage Python workflow** so newcomers can onboard incrementally.

## Workflow overview (3 stages)

### Stage 1 — Foundation ✅
Goal: establish a runnable Python project skeleton and development conventions.

- Project packaging via `pyproject.toml`
- Source layout under `src/chatgtp/`
- CLI entrypoint for sanity checks

### Stage 2 — Core implementation 🚧 (started)
Goal: add the actual application modules and domain logic.

Current simple example:

- `src/chatgtp/core.py` includes a tiny domain model (`MessageRequest`) and logic (`build_response`)
- CLI calls the Stage 2 logic to show how modules connect
- Unit tests in `tests/test_core.py` validate normal and fallback behavior

### Stage 3 — Hardening and delivery
Goal: make the project production-ready.

- Add lint/format/type-check automation
- Add CI workflow for tests and quality gates
- Add release/versioning and deployment docs

## Current repository structure

- `pyproject.toml`: Python project metadata and packaging config
- `src/chatgtp/__init__.py`: package marker + version
- `src/chatgtp/__main__.py`: CLI entrypoint invoking Stage 2 demo flow
- `src/chatgtp/core.py`: Stage 2 sample domain model and logic
- `tests/test_core.py`: Stage 2 unit tests
- `README.md`: onboarding and staged workflow
- `.gitkeep`: placeholder from initial scaffold

## Run the demo and tests

```bash
PYTHONPATH=src python -m chatgtp
PYTHONPATH=src python -m unittest discover -s tests -p 'test_*.py'
```
