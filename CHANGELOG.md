# Changelog

All notable governed KEE releases are recorded here.

KEE follows Semantic Versioning 2.0.0 under ADR-0074. This changelog is informative release guidance; normative force remains in the specification, Accepted / Normative profiles, ADRs, and release records.

## [0.9.1] — 2026-09-17

Published specification: `docs/specs/KEE-Specification-v0.9.1.md`. Backward-compatible PATCH release under ADR-0074: an implementation conforming to v0.9.0 conforms to v0.9.1 without implementation change.

### Fixed

- Reworked the repository front door so the public explanation precedes the formal architectural definition.
- Made **time / temporal qualification** explicit near the top as a first-class cross-cutting concern rather than leaving it implicit in later architecture text.
- Defined public-facing terms including epistemic, provenance, temporal qualification, authority, responsibility/accountability, evidence, confidence, epistemic standing, profile, interoperability, and non-collapse.
- Defined **non-collapse** in plain language: related concepts are not automatically identical.
- Clarified what KEE owns and what prior art and specialized profiles own.
- Removed stale current-state wording that still described the v0.9.0 programme as merely proposed after v0.9.0 had already been published.

### Compatibility

- PATCH release.
- No new normative requirement.
- No profile promotion or demotion.
- No new KEE-owned semantic term.
- No new Capability Level.
- No change to the seventeen non-collapse rules.
- No incompatible conformance change.
- No governed-data migration.
- v0.9.0 remains immutable historical normative provenance.

## [0.9.0] — 2026-09-17

Published specification: `docs/specs/KEE-Specification-v0.9.0.md`. Publication record: `docs/release/KEE-v0.9.0-publication.md`. Backward-compatible MINOR release under ADR-0074: an implementation conforming to v0.8.2 conforms to v0.9.0 without change.

**This release publishes no shared-contract count.** ADR-0077 restates that figure as a band after the classification predicate failed blind replication, and ADR-0078 forbids narrowing it by drafting alone. The count is evidence for the role claim, appears in no published surface, and no conforming implementation depends on it.

### Added

- **ADR-0075 Accepted (2026-09-17)** — KEE v0.9 adopted as a governed application-profile family and interoperability framework, with the ownership boundary stated: prior art owns foundational semantics, profiles own domain behaviour, a shared cross-profile contract is demonstrated necessary, and no evidence demonstrates it must be KEE's. **The size of that contract is a band, not a figure** — ADR-0077 restated it after the classification predicate failed blind replication, and ADR-0078 forbids narrowing it by drafting alone. Acceptance publishes no specification, promotes no profile, graduates no KEEpack and mints no term; the published baseline remains v0.8.2.
- **ADR-0076 Accepted (2026-09-17)** — the independent-convergence experiment is authorized at **gate 1** (design and pre-registration) only. The run is gate 2 and remains undecided; the protocol must not be executed until then.
- ADR-0075's acceptance was conditioned on ADR-0076's, so that standing limitation SL-01's rule — the analytic (a) count must not by itself carry acceptance — was honoured rather than waived. Recorded in `docs/release/KEE-v0.9.0-adr-acceptance-record-01.md`.
- Proposed obligation-level prior-art lineage over the frozen 120-unit audit.
- Proposed plain-JSON profile declaration plus JSON Schema; the candidate does not claim an RDF/PROF serialization for unmapped application fields.
- Separate conformance-report JSON and semantic EARL/PROV/SHACL evidence graph, with immutable artifact binding and five separately reported KEE dimensions.
- Candidate stable `NC-01..NC-17` identifiers mapped explicitly to the published v0.8.2 Section 7.1 rules rather than retrofitted into the historical baseline.
- Stable handling records and positive/negative declaration examples for all 17 non-collapse rules, without treating declaration polarity as behavioral proof or minting universal trust/accountability terms.
- Experimental RO-Crate KEEpack profile contract, normative API manifests and a deterministic compatibility-diff review gate.
- Proposed ADR-0075 and permanent KEE-minus-KEE contributor test.
- Third-pass core-survival review preserved as historical evidence. It established zero irreducible KEE-specific semantic machinery but used that narrower result to zero the broader G1/G2 classes.
- Fourth-pass source reconciliation of the six H rows. All six were already resolved by governed v0.8.2 lineage controls; H remains zero.
- Fifth-pass contract-predicate review after the first independent adversarial review. It restored the original G1/G2/G3 definitions and produced frozen-120 counts A 11 / B 24 / C 52 / D 10 / E 2 / F 3 / G1 22 / G2 1 / G3 0 / H 0. **Superseded by the sixth pass; preserved as historical evidence.**
- Sixth-pass predicate-and-ownership review after a second independent adversarial review, which found the contested classes still had no predicate: three noun phrases, copied verbatim into the fifth pass under a key named `predicates`, with no necessary condition, no sufficient condition and no disconfirming observation. The sixth pass writes them, re-tests all 120 rows rather than only the 16 the second pass left residual, and separates the shared-contract question from the ownership question. Current frozen-120 counts A 11 / B 24 / C 46 / D 10 / E 2 / F 4 / G1 22 / G2 1 / G3 0 / H 0. Seventeen rows changed class; `PROM-001` returns to H because the fourth pass resolved only the scope-ordering half of a compound obligation.
- Five first-pass registry defects recorded in `lineage/v0.9-registry-corrections-01.json` as a superseding artifact, without editing the frozen base registry.
- Outcome-pinning assertions removed from the lineage tests. A re-review asserted equal to its own input is a fixture, not a review; it is now demonstrably possible to change a disposition, or reverse the ownership finding, and still pass CI.
- Three Section 15.5 status-aware tooling MUSTs — profile governance status, shape-or-shape-contract version, and normative effect for the evaluated claim — now reported in the candidate conformance evidence and enforced in `reference/v090.py` with negative cases.
- Research brief 0018 on independent-implementation convergence testing, opened because the sixth pass established that the programme's load-bearing claim is empirical and cannot be settled by another pass over frozen prose.
- Canonical v0.9 conformance fixture using the profile-specific Assertion lifecycle namespace and byte-bound SHA-256 identity shared by JSON, EARL/PROV evidence, and SHACL report.
- Expanded v0.8.2 public-API snapshot coverage for Capability Levels, declaration-status values, canonical lifecycle namespaces, status-aware tooling obligations, and the registered-legacy compatibility window.
- Promotion SHACL check and regression test rejecting cyclic scope ordering.

### Compatibility

- Expected MINOR-compatible candidate additions. No v0.8.2 public term, Accepted profile, non-collapse rule, lifecycle namespace, Capability Level, declaration-status value, registered-legacy compatibility promise, or conformance dimension is removed or weakened.
- Historical `governance/policy` remains the published dimension label; candidate tooling accepts both it and the machine-safe `governance-policy` spelling.
- `independent-interoperability-evidence` is a new profile-promotion requirement, not a retroactive obligation on existing v0.8.2 interoperability claims.
- Fifth- and sixth-pass reclassification changes the audit interpretation, not v0.8.2 semantics. G1/G2 identify **shared** cross-profile interoperability and framework-governance contracts with **KEE ownership not demonstrated**; G3 semantic novelty remains zero. The sixth pass withdrew the ownership assertion the fifth pass's class names carried, on the evidence of this repository's own Phase 5 decision record.
- The frozen 120 counts are explicitly scoped to the 2026-09-06 audit universe and do not claim to exhaust later Amendment 01/02 or ADR-0074 normative instruments.
- Nothing in this section is published normative KEE until maintainer governance accepts and integrates it.

## [0.8.2] - 2026-09-15

### Fixed

- Consolidated the already-effective KEE v0.8.1 + amendment-01 + amendment-02 contract under the single current version identifier `0.8.2`.
- Carried amendment-01 term-registry, migration-control, frozen-denominator/living-control, and vocabulary-declaration corrections into the current patch baseline.
- Carried amendment-02 Section 18.5 correction into the current patch baseline: behavioral coverage of the seventeen non-collapse rules is fifteen; rules 3 and 6 remain non-demonstrable for representational reasons.

### Changed

- Adopted Semantic Versioning 2.0.0 for governed KEE releases via ADR-0074.
- Defined KEE's public normative API for compatibility classification.
- Added a stricter pre-1.0 compatibility promise for published `0.y.z` baselines.
- Established `CHANGELOG.md` as release hygiene.

### Compatibility

- PATCH release.
- No new normative requirement.
- No profile promotion or demotion.
- No new KEE-owned semantic term.
- No incompatible conformance change.
- Implementations conforming to v0.8.1 + amendment-01 + amendment-02 conform to v0.8.2 without implementation change.

## [0.8.1] - 2026-09-08

### Fixed

- Restored 69 obligations dropped or weakened during the v0.8.0 publication consolidation.
- Integrated ADR-0049 source and consumer neutrality in full.
- Restored terminology, Capability Levels, dated references, and explicit dispositions for carried-forward v0.7.2 obligations.
- Repaired release controls so they could detect semantic loss rather than merely report success.

### Compatibility

- Corrective patch release relative to v0.8.0 data.
- Published amendments 01 and 02 on 2026-09-09 and 2026-09-10 respectively; both are now consolidated into v0.8.2 while retained as historical normative provenance.

## [0.8.0] - 2026-09-07

### Changed

- Published the post-audit standards-composed application-profile and interoperability architecture.
- Consolidated the RC1-RC11 sequence and KCHG-001..070.
- Shifted foundational semantics toward explicit prior-art composition and narrowed KEE-owned semantic surfaces.

### Historical note

- A 2026-09-08 adversarial audit found that the publication dropped 39 and weakened 30 frozen RFC 2119 obligations. v0.8.1 corrected that loss.

## [0.7.2] - historical baseline

### Historical note

- Previous published KEE baseline before the post-audit v0.8 architecture.
- ADR-0049 amendment remains preserved as historical normative provenance.
