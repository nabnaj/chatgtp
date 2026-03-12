# chatgtp

This repository is organized as a **three-stage Python workflow** so newcomers can onboard incrementally.

## Workflow overview (3 stages)

### Stage 1 — Foundation ✅
Goal: establish a runnable Python project skeleton and development conventions.

- Project packaging via `pyproject.toml`
- Source layout under `src/chatgtp/`
- CLI entrypoint for sanity checks

### Stage 2 — Core implementation ✅
Goal: add the actual application modules and domain logic.

Current simple example:

- `src/chatgtp/core.py` includes a tiny domain model (`MessageRequest`) and logic (`build_response`)
- CLI calls the Stage 2 logic to show how modules connect
- Unit tests in `tests/test_core.py` validate normal and fallback behavior

### Stage 3 — Hardening and delivery ✅
Goal: make the project production-ready.

Implemented in this stage:

- Dev tooling config for lint/format/type-check in `pyproject.toml`
- Standard quality commands in `Makefile`
- CI workflow in `.github/workflows/ci.yml` running lint, type-check, and tests
- Release/versioning process in `RELEASE.md`

## Current repository structure

- `pyproject.toml`: Python project metadata + tooling config
- `src/chatgtp/__init__.py`: package marker + version
- `src/chatgtp/__main__.py`: CLI entrypoint invoking Stage 2 demo flow
- `src/chatgtp/core.py`: Stage 2 sample domain model and logic
- `tests/test_core.py`: unit tests
- `Makefile`: run/lint/format/type-check/test tasks
- `.github/workflows/ci.yml`: CI checks
- `RELEASE.md`: release checklist and versioning notes

## Run the demo and tests

```bash
make run
make test
```

## Run full quality checks

```bash
python -m pip install -e .[dev]
make check
```
