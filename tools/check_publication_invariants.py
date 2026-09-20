#!/usr/bin/env python3
"""Enforce the two invariants of the KEE public publication surface.

This file is maintained in the KEE working repository and published verbatim to
the public repository by the publication script it is maintained beside. The forbidden-pattern list below is
the single definition of the publication scoping rule: the working repository's
own manifest test imports it from here rather than restating it. An earlier
hand-copy of this list had already fallen a pattern behind, so a source naming
an amendment passed the working-repository gate and failed public CI.

1. Self-containment — every repository-relative path the published files cite
   must resolve inside this repository.
2. Publication scope — the public surface carries no reference to development
   work prior to v0.9.0: no decision-record identifiers, no pre-v0.9.0
   specification or release-candidate identifiers, no internal registry,
   research, or release-evidence paths.

Exit status is non-zero when either invariant is violated.
"""

from __future__ import annotations

import glob
import json
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SKIP_DIRS = {".git", ".github", "node_modules", "__pycache__"}
TEXT_SUFFIXES = {".md", ".json", ".jsonld", ".ttl", ".txt", ".yml", ".yaml", ".py"}

# Top-level directories a cited path may start with.
CITABLE_ROOTS = (
    "docs", "shacl", "schemas", "vocab", "context", "normative-api",
    "sparql", "tests", "reference", "lineage", "conformance", "examples",
    "profiles", "tools", "experiments",
)

PATH_PATTERN = re.compile(
    r"(?:`|\(|\[|\"|\s)((?:%s)/[A-Za-z0-9/._*-]+)" % "|".join(CITABLE_ROOTS)
)

FORBIDDEN = [
    (re.compile(r"\bADR-\d{3,}\b"), "decision-record identifier"),
    (re.compile(r"\bKEE-v0\.[0-8]\b"), "pre-v0.9.0 artifact identifier"),
    (re.compile(r"\bv0\.[0-8]\.\d+\b"), "pre-v0.9.0 version identifier"),
    (re.compile(r"-rc\d+\b"), "release-candidate identifier"),
    (re.compile(r"\bRC\d+\b"), "release-candidate identifier"),
    (re.compile(r"\bKCHG-\d+\b"), "change-package identifier"),
    (re.compile(r"\bamendment-0\d\b"), "amendment identifier"),
    (re.compile(r"\bdocs/(?:release|adr|migration|research|planning)/"),
     "internal evidence path"),
]

# "ADR-style decision contract" is generic prior art (Nygard), not a KEE ADR.
ALLOWED_SUBSTRINGS = ("ADR-style",)


def iter_files():
    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in files:
            path = os.path.join(root, name)
            if os.path.splitext(name)[1] in TEXT_SUFFIXES:
                yield path


def read(path):
    try:
        with open(path, encoding="utf-8") as handle:
            return handle.read()
    except (UnicodeDecodeError, OSError):
        return None


def check_self_containment(path, text, failures):
    rel = os.path.relpath(path, REPO_ROOT)
    for cited in sorted(set(PATH_PATTERN.findall(text))):
        target = cited.rstrip(".,;:)]\"'")
        absolute = os.path.join(REPO_ROOT, target)
        if "*" in target:
            resolved = bool(glob.glob(absolute))
        else:
            resolved = os.path.exists(absolute)
        if not resolved:
            failures.append(f"{rel}: cites {target!r}, which does not exist in this repository")


def check_publication_scope(path, text, failures):
    rel = os.path.relpath(path, REPO_ROOT)
    for number, line in enumerate(text.splitlines(), start=1):
        if any(allowed in line for allowed in ALLOWED_SUBSTRINGS):
            continue
        for pattern, label in FORBIDDEN:
            match = pattern.search(line)
            if match:
                failures.append(
                    f"{rel}:{number}: {label} {match.group(0)!r} "
                    f"is development work prior to v0.9.0"
                )
                break


def check_json_wellformed(path, failures):
    if os.path.splitext(path)[1] not in {".json", ".jsonld"}:
        return
    rel = os.path.relpath(path, REPO_ROOT)
    try:
        with open(path, encoding="utf-8") as handle:
            json.load(handle)
    except (json.JSONDecodeError, OSError) as error:
        failures.append(f"{rel}: not well-formed JSON ({error})")


def main() -> int:
    failures: list[str] = []
    for path in sorted(iter_files()):
        if os.path.relpath(path, REPO_ROOT) == os.path.join("tools", "check_publication_invariants.py"):
            continue
        text = read(path)
        if text is None:
            continue
        check_self_containment(path, text, failures)
        check_publication_scope(path, text, failures)
        check_json_wellformed(path, failures)

    if failures:
        print("Publication invariants violated:\n", file=sys.stderr)
        for failure in failures:
            print(f"  {failure}", file=sys.stderr)
        print(f"\n{len(failures)} violation(s).", file=sys.stderr)
        return 1

    print("Publication invariants hold: self-contained, and scoped to v0.9.0 onward.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
