# Changelog

All notable governed KEE releases are recorded here.

KEE follows Semantic Versioning 2.0.0 with a stricter pre-1.0 compatibility promise: a published `0.y.z` PATCH release must not hide an incompatible change.

This changelog is informative release guidance. Normative force remains in the published specification and in the Accepted / Normative profiles.

## [0.9.2] — 2026-09-18

Published specification: [`docs/specs/KEE-Specification-v0.9.2.md`](docs/specs/KEE-Specification-v0.9.2.md).
Published public API: [`normative-api/v0.9.2.json`](normative-api/v0.9.2.json).

Backward-compatible PATCH release: an implementation conforming to v0.9.1 conforms to v0.9.2 without implementation change.

### Changed

- **The published baseline is now self-contained.** v0.9.0 and v0.9.1 were delta documents that stated their normative content by reference to an earlier baseline. v0.9.2 inlines the full contract, so determining the meaning of a KEE obligation requires no other document.
- Consolidated v0.9.0 and v0.9.1 under one current version identifier.
- The publication surface cites only artifacts published alongside it.

### Compatibility

- PATCH release.
- No new normative requirement.
- No profile promotion or demotion.
- No new KEE-owned semantic term.
- No new Capability Level.
- No change to the seventeen non-collapse rules.
- No incompatible conformance change.
- No governed-data migration.

## [0.9.1] — 2026-09-17

Backward-compatible PATCH release: an implementation conforming to v0.9.0 conforms to v0.9.1 without implementation change.

### Fixed

- Reworked the repository front door so the public explanation precedes the formal architectural definition.
- Made **time / temporal qualification** explicit near the top as a first-class cross-cutting concern rather than leaving it implicit in later architecture text.
- Defined public-facing terms including epistemic, provenance, temporal qualification, authority, responsibility/accountability, evidence, confidence, epistemic standing, profile, interoperability, and non-collapse.
- Defined **non-collapse** in plain language: related concepts are not automatically identical.
- Clarified what KEE owns and what prior art and specialized profiles own.
- Removed stale current-state wording that still described the v0.9.0 programme as merely proposed after v0.9.0 had already been published.

### Compatibility

- PATCH release. No new normative requirement, profile promotion, KEE-owned semantic term, Capability Level, non-collapse change, incompatible conformance change, or governed-data migration.

## [0.9.0] — 2026-09-17

Backward-compatible MINOR release. The first KEE release published under the current public-API and change-classification discipline.

**This release publishes no shared-contract count.** The figure is carried as a band after the classification predicate failed blind replication, and it must not be narrowed by drafting alone. The count is evidence for the role claim, appears in no published surface, and no conforming implementation depends on it.

### Added

- **KEE's role stated.** KEE v0.9 is a governed application-profile family and interoperability framework — a published, versioned, testable shared contract over prior art, and not a semantic foundation. Prior art owns foundational semantics; specialized profiles own domain and artifact-type behaviour; the KEE family contract owns the published cross-profile rules; KEE framework governance owns the standing of KEE's own normative instruments.
- **Stable non-collapse rule identifiers** `NC-01` through `NC-17`, mapped to the already-published non-collapse rules. The identifiers are new in v0.9.0; the rules are unchanged, and an artifact that does not use them is not thereby non-conforming.
- **Machine-safe conformance dimension tokens**, preserving the published human label `governance/policy`. Both spellings are accepted and the historical spelling is not deprecated.
- **Independent interoperability evidence** as a requirement for new profile promotion or graduation claims. Not retroactive. Reference self-roundtrip is insufficient.
- **Optional candidate surfaces**, none required for conformance: obligation lineage registry, JSON profile declaration and its schema, EARL / PROV / SHACL evidence graph, RO-Crate KEEpack packaging experiment (Experimental / Non-Normative), and public API diff.
- **Promotion shape: cyclic scope ordering.** The Promotion shape gained a constraint rejecting a `skos:broader` ordering in which the source and target scopes are mutually broader. This is a real conformance-behaviour change and is recorded as one; it is MINOR-compatible because the Promotion Profile is Draft / Non-Normative and excluded from the public normative API.

### Compatibility

- MINOR release. No new KEE-owned semantic term, no profile promotion, no new Capability Level, and no change to the seventeen non-collapse rules.

[0.9.2]: https://github.com/KnoEdg/kee/blob/main/docs/specs/KEE-Specification-v0.9.2.md
