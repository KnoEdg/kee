# Changelog

All notable governed KEE releases are recorded here.

KEE follows Semantic Versioning 2.0.0 with a stricter pre-1.0 compatibility promise: a published `0.y.z` PATCH release must not hide an incompatible change.

This changelog is informative release guidance. Normative force remains in the published specification and in the Accepted / Normative profiles.

## [0.10.0] — 2026-09-19

Published specification: [`docs/specs/KEE-Specification-v0.10.0.md`](docs/specs/KEE-Specification-v0.10.0.md).
Published public API: [`normative-api/v0.10.0.json`](normative-api/v0.10.0.json).

Backward-compatible MINOR release: it carries exactly one conformance-behaviour change, disclosed below, and adds no new normative requirement, KEE-owned semantic term, profile promotion, or Capability Level.

### Changed

- **The Section 12.3 accountable-root constraint is enforced.** The reference shape now rejects a grantee that resolves to no accountable person or organization, rather than only warning about it. A grantee that conformed structurally under v0.9.2 does not conform under v0.10.0. This is the release's one conformance-behaviour change, and the reason it is MINOR rather than PATCH.
- The escalation is MINOR-compatible because the profile that owns this constraint, Authority and Delegation, is Draft / Non-Normative and excluded from the public normative API — the same ground the v0.9.0 release used for a comparable Promotion-shape change.
- Section 18.7 is restated. The base identifier and the artifact and confidence namespaces are independently verified to resolve to RDF; the generic lifecycle namespace and the Section 5 profile identifiers redirect to a human-readable page rather than content-negotiating to RDF, and this release says so rather than generalizing from the identifiers actually tested.
- The published term declarations now carry a version-specific identifier (`owl:versionIRI`) alongside the unversioned one, so a consumer can tell which release it received.

### Compatibility

- MINOR release: one disclosed incompatible conformance behaviour, confined to a Draft / Non-Normative profile outside the public normative API.
- An implementation claiming the Authority and Delegation profile and relying on the prior warning-level behaviour must resolve its delegation chains to an accountable person or organization before adopting v0.10.0. No stored data requires rewriting; what changes is whether a structural validation passes.
- No new KEE-owned semantic term, profile promotion or demotion, or new Capability Level.

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

[0.10.0]: https://github.com/KnoEdg/kee/blob/main/docs/specs/KEE-Specification-v0.10.0.md
[0.9.2]: https://github.com/KnoEdg/kee/blob/main/docs/specs/KEE-Specification-v0.9.2.md
