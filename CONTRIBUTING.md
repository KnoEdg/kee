# Contributing to KEE

KEE is a specification-first project. Its normative artifacts — the specification, the SHACL shape graphs, the SKOS concept schemes, the JSON Schemas, the JSON-LD context, and the profiles — change through a governed process, not through ordinary pull-request review alone. This page says what you can do directly, what goes through that process, and where to ask.

## Where to ask and report

- **Questions and bug reports:** open an issue at https://github.com/KnoEdg/kee/issues. There is a template for a bug report and one for a question.
- **Security concerns:** see `SECURITY.md`.
- **Conduct concerns:** see `CODE_OF_CONDUCT.md`.

## The governed change workflow

Substantive changes follow this sequence:

```text
Observation -> Evidence / Research Question -> Research Brief -> Decision Record -> SemVer Release -> Profile or Implementation
```

- **Research briefs** are prior-art-first and domain-neutral: they map existing standards, frameworks, and production precedent before considering any KEE-specific concept, and must not assume KEE's own terms while doing so.
- **Decision records** are append-only. An accepted decision is never rewritten; a later decision supersedes it explicitly.
- **The published specification** is frozen against substantive in-place edits. A semantic or architectural change requires the appropriate PATCH, MINOR, or MAJOR release, not a direct edit.
- A narrow editorial fix that changes no meaning may go directly to a working specification draft.

The research briefs, the decision records, and the governance document that defines this process are kept in the project's working repository, which is not public; the public repository publishes what the process produces. A proposal does not need access to them to be considered. It needs the observation, the evidence, and the prior art, stated in the issue.

## What changes for outside contributors

Everything above applies to any contributor, not only the founding team. What changes once contributors aren't the founding author:

- **Decision rights stay with the maintainer.** Acceptance of a decision record, promotion of a profile, and designation of a release remain the primary maintainer's call. A pull request proposes; it does not by itself decide.
- **Prior art review is not optional and not assumed.** A proposal that does not first check the current specification's Prior Art First rule (Section 4.1), its references (Section 23), and the open items it records (Section 24) will be asked to do that before substantive review continues.
- **New KEE-owned vocabulary needs a demonstrated residual gap**, not a preference. See the admission test in the current specification (Section 4.2) before proposing a new term, primitive, or profile.

## Smaller contributions

Bug reports, documentation fixes that don't change normative meaning, test coverage, corrections to examples and fixtures, and tooling improvements don't need the full research-brief pipeline — open a pull request directly. If a maintainer determines a contribution does have normative effect, expect to be routed into the governed workflow above rather than merged as-is.

The public repository is a publication surface. Its specification, shape graphs, concept schemes, schemas, context, vocabulary, examples, and fixtures are published from the working repository, so a fix accepted against one of them is applied at the source and republished rather than merged in place. The pull request is still the contribution; expect the maintainer to say which path it takes.

## Pull requests

- Commit messages follow Conventional Commits: `type(scope)?: subject`, with `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `build`, `ci` as types.
- No commit, file, pull-request title, or description names a software tool as an author or carries a co-author trailer, a "generated with" line, or a session link for one. CI rejects a pull request or push that does.
- Branch names describe the work (`fix/<subject>`, `docs/<subject>`), not a tool or a session.
- Continuous integration runs the test suite on one Python and dependency set for a pull request, and skips the lint and wheel checks when every changed path is documentation; the full Python-by-dependency matrix runs on `main` and on a pull request labelled `full-matrix`.

## Licensing your contribution

By submitting a contribution, you agree it is licensed under the same terms as the file(s) you changed — Apache License 2.0 for everything except `reference/`, which is AGPLv3 (see `LICENSE`, `reference/LICENSE`, and `NOTICE`).

**Contributions to `reference/` specifically** additionally require signing a Contributor License Agreement (CLA) before merge, so that the project can continue to offer a separate commercial license for that component without your contribution being excluded from it. The CLA mechanism and final text are not yet in place — this is tracked as an open item, and will be finalized, with legal review, before `reference/` accepts outside contributions at scale. Until then, contributions to `reference/` from outside the founding team may be held rather than merged.

## Code of conduct

See `CODE_OF_CONDUCT.md`.
