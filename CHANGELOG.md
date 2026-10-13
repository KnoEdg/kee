# Changelog

All notable governed KEE releases are recorded here.

KEE follows Semantic Versioning 2.0.0 with a stricter pre-1.0 compatibility promise: a published `0.y.z` PATCH release must not hide an incompatible change.

This changelog is informative release guidance. Normative force remains in the published specification and in the Accepted / Normative profiles.

## [0.11.0] — 2026-10-12

Published specification: [`docs/specs/KEE-Specification-v0.11.0.md`](docs/specs/KEE-Specification-v0.11.0.md), with its informative annex [`docs/specs/KEE-Specification-v0.11.0-release-governance-annex.md`](docs/specs/KEE-Specification-v0.11.0-release-governance-annex.md).
Published public API: [`normative-api/v0.11.0.json`](normative-api/v0.11.0.json).

Backward-compatible MINOR release: it adds three controlled value sets and carries two conformance-behaviour changes, disclosed below, on different schedules, plus one reporting-only guard. No KEE-owned class or property is added, removed or renamed; no profile is promoted or demoted; no Capability Level changes; no governed-data migration is required.

### Added

- **Three controlled value sets.** The governance-record review-status scheme at `https://w3id.org/kee/lifecycle/governance-record#` ([`schemas/skos/governance-record-lifecycle.ttl`](schemas/skos/governance-record-lifecycle.ttl); Proposed, Accepted, Rejected, Withdrawn, Superseded; Section 9.2), the query-time-dimension scheme at `https://w3id.org/kee/vocab/query-time-dimension#` ([`schemas/skos/query-time-dimension.ttl`](schemas/skos/query-time-dimension.ttl); RecordedTime, ValidTime; Section 14.2) and the retrieval-eligibility scheme at `https://w3id.org/kee/vocab/retrieval-eligibility#` ([`schemas/skos/retrieval-eligibility.ttl`](schemas/skos/retrieval-eligibility.ttl); seven categories; Section 14.5), each with a JSON-LD prefix.
- A composed shape graph, [`shacl/governance-record-review-status-constraints.ttl`](shacl/governance-record-review-status-constraints.ttl), which the reference validator composes with the four owning profile shapes and not with Assertion Metadata.
- Section 15.8 names the conformance targets (producer, consumer, validator, profile claimant) each obligation falls on, from the section that states it, adding none. Section 21 defines the terms the text relied on without defining. Section 0.7 lists every KEE-owned namespace. Section 26 adds security and privacy considerations. Every top-level section is marked Normative or Informative.
- The informative annex carries the text that governs only the project's release process (formerly Sections 0.4, 18.3 to 18.6, 18.8 to 18.10, 20, 24 and 25), with a pointer left in each so that section numbering is unchanged from v0.10.0.
- [`docs/worked-example.md`](docs/worked-example.md), [`docs/vocabulary.md`](docs/vocabulary.md), [`docs/non-collapse-traceability.md`](docs/non-collapse-traceability.md), [`shacl/README.md`](shacl/README.md), `examples/`, `fixtures/`, and the community surface: `CITATION.cff`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, issue and pull request templates.

### Changed

- **Conformance-behaviour change 1 (Section 9.2).** The composed review-status shape checks, by `sh:in`, that `kee:lifecycleState` on the four governance-record classes is a concept of the scheme, and reports at `sh:Warning`. No conformance outcome changes for those classes at this release. **v0.11.0 is the last dual-read version for generic `https://w3id.org/kee/lifecycle#` values on those classes, and v0.12.0 is the first rejecting version**, in which the same shape reports at `sh:Violation`. No generic value maps to a scheme concept.
- **Conformance-behaviour change 2 (Sections 14.2, 14.5).** `kee:queryTimeDimension` and `kee:eligibilityCategory` are closed by `sh:in` over their schemes, and the membership check on a new-write record escalates from `sh:Warning` to `sh:Violation`. A point-in-time query record or retrieval result that wrote an identifier of its own in either slot conformed structurally under v0.10.0 and does not conform under v0.11.0: **v0.10.0 is the last version in which such a value conforms and v0.11.0 the first rejecting version.** A registered-legacy record (one declaring only `kee:profileConformance`) is reported at `sh:Warning` and retires with that carrier.
- Both changes are MINOR-compatible on the ground v0.9.0 and v0.10.0 used: every owning profile is Draft / Non-Normative and excluded from the public normative API. The public normative contract is unchanged.
- Section 16.4 states that `kee:lifecycleState` on an Assertion Metadata record is the managed unit's lifecycle, with `https://w3id.org/kee/lifecycle/assertion#` the default scheme for new writes, and that the review-status scheme is not a value set for that slot. This adds no rejecting constraint: [`shacl/lifecycle-status-constraints.ttl`](shacl/lifecycle-status-constraints.ttl) reports a generic or mixed-axis value on that slot at `sh:Warning`; no conformance outcome changes, and whether that profile will ever reject such a value is a separate decision not yet taken.
- Section 18.7 is restated from a live re-verification on 2026-10-12. The base identifier content-negotiates to the term declarations, the context or the repository page. The artifact and confidence namespaces, the profile lifecycle namespaces and the local-vocabulary namespaces each resolve to their published concept scheme by an unconditional redirect, served as `text/plain`, which a consumer must not read as evidence that they are not RDF. The three new namespaces and the version identifier return `404` until their registration merges.
- Shape-contract version moves to 0.11.0, declared by the public-API manifest alone; the `Shape-contract version` header comments the shape graphs carried are removed.
- `LICENSE` is the verbatim Apache-2.0 text; the trademark and conformance-claim policy is referenced from `NOTICE`.

### Compatibility

- MINOR release: two disclosed conformance-behaviour changes, each confined to Draft / Non-Normative profiles outside the public normative API, and one reporting-only guard inside it that rejects nothing.
- An implementation that conformed to v0.10.0 remains conforming without change unless it opts into a capability one of the three schemes serves, or claims one of the two Draft profiles whose classifier slots are now closed and wrote its own identifier there.
- Implementers of the four Draft profiles that adopt the review-status scheme get one release in which a generic review-status value is reported before it fails.
- The v0.10.0 and v0.9.2 specification and manifest files are retained on this surface.

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
