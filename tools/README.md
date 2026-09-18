# Publication tooling

## `check_publication_invariants.py`

Enforces the two invariants of this publication surface:

1. **Self-containment.** Every repository-relative path cited by a published
   file resolves inside this repository. A reader never needs a document that
   is not here.
2. **Publication scope.** The public surface carries no reference to
   development work prior to v0.9.0 — no decision-record identifiers, no
   pre-v0.9.0 specification or release-candidate identifiers, no internal
   registry, research, or release-evidence paths.

It also checks that every published JSON and JSON-LD file is well-formed.

Run it directly:

```bash
python3 tools/check_publication_invariants.py
```

It exits non-zero and names every violation with file and line. CI runs it on
every push and pull request via `.github/workflows/publication-invariants.yml`.
