# Release and versioning guide

This project follows a lightweight semantic versioning process.

## Versioning rules

- `MAJOR`: incompatible API changes
- `MINOR`: backward-compatible features
- `PATCH`: backward-compatible fixes

Current source version lives in `src/chatgtp/__init__.py`.

## Release checklist

1. Ensure CI is green.
2. Run local quality gates:
   - `make lint`
   - `make typecheck`
   - `make test`
3. Update `__version__` in `src/chatgtp/__init__.py`.
4. Update changelog/release notes (if maintained).
5. Create a tagged release in Git:
   - `git tag vX.Y.Z`
   - `git push origin vX.Y.Z`
