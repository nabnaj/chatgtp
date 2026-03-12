# chatgtp

This repository is currently a minimal scaffold with Git initialized and no application source code yet.

## Current structure

- `.git/`: Git metadata and history.
- `.gitkeep`: Placeholder file to keep the repository non-empty.

## What to know right now

1. There is no runtime code, build system, or dependency manifest yet.
2. The branch `work` currently contains only the initial "Initialize repository" commit.
3. The project is ready for first-commit setup (language/runtime choice, tooling, and baseline docs).

## Suggested next steps for newcomers

- Add a short architecture-and-goals section once implementation starts.
- Choose a stack and add core project files:
  - JavaScript/TypeScript: `package.json`, `tsconfig.json`, `src/`
  - Python: `pyproject.toml`, `src/`, `tests/`
  - Go: `go.mod`, `cmd/`, `internal/`
- Add developer experience basics early:
  - `README` usage instructions
  - lint/format config
  - test runner setup and CI workflow
  - `.env.example` for configuration conventions

## Learning path once code is added

1. Read entrypoints first (e.g., `src/main.*`, app bootstrap).
2. Follow request/data flow through core modules.
3. Review tests to learn expected behavior and edge cases.
4. Inspect tooling (`Makefile`, CI, linters) to match team standards.
