# KEE Profiles

Profiles adapt the KEE core specification to a specific artifact type, domain, or implementation context. Domain details remain outside the core wherever practical.

## Published v0.8 Baseline

The current published normative baseline is:

- `docs/specs/KEE-Specification-v0.9.0.md`.

v0.9.0 changes no profile status; the previous baseline `docs/specs/KEE-Specification-v0.8.2.md` is retained as historical provenance.

v0.8.2 is a SemVer PATCH consolidation of v0.8.1 + amendment-01 + amendment-02. It changes no profile status.

Historical normative provenance includes:

- `docs/specs/KEE-Specification-v0.8.1.md`;
- `docs/specs/KEE-Specification-v0.8.1-amendment-01.md`;
- `docs/specs/KEE-Specification-v0.8.1-amendment-02.md`;
- `docs/specs/KEE-Specification-v0.8.1-rc1.md`; and
- `docs/specs/KEE-Specification-v0.8.0-rc11.md`.

Earlier RC profile companions remain frozen evidence of the bounded decisions they introduced; publication does not rewrite them.

Applicable frozen companions include:

- `KEE-v0.8.0-rc3-lifecycle-status-overrides.md`;
- `KEE-v0.8.0-rc5-confidence-evidence-overrides.md`;
- `KEE-v0.8.0-rc6-authority-delegation-overrides.md`;
- `KEE-v0.8.0-rc7-contradiction-promotion-overrides.md`;
- `KEE-v0.8.0-rc8-temporal-history-retrieval-overrides.md`;
- `KEE-v0.8.0-rc9-profile-conformance-overrides.md`; and
- `KEE-v0.8.0-rc10-domain-profile-overrides.md`.

## Current Profile Status

1. Assertion Profile — Draft.
2. Assertion Metadata Profile — Accepted / Normative (ADR-0040).
3. Lifecycle Crosswalk Profile — Draft / Non-Normative.
4. Governance Transition Profile — Draft / Non-Normative.
5. Promotion Profile — Draft / Non-Normative.
6. Authority and Delegation Profile — Draft / Non-Normative.
7. Contradiction Records Profile — Draft / Non-Normative.
8. AI-Grounded Retrieval Profile — Draft / Non-Normative.
9. Artifact Identity and Granularity Profile — Draft / Non-Normative.
10. Historical and Bitemporal Querying Profile — Draft / Non-Normative.
11. Decision Profile — Draft.
12. Organizational Memory Profile — Draft.
13. Software Engineering Profile — Accepted / Normative (ADR-0032).
14. Scientific Claim Profile — Accepted / Normative (ADR-0035).

v0.8.2 promotes no Draft profile merely because it has executable shapes, fixtures, examples, or tests. Profile status is unchanged from v0.8.1.

## Cross-Profile Rules

Profiles MUST preserve Source and Consumer Neutrality. Producer or consumer type alone MUST NOT establish epistemic status.

Profiles MUST NOT collapse independent lifecycle, publication, review/currency, archival/disposition, epistemic/evidential, ranking, confidence, evidence-strength, replication, authority, scope/context, retrieval, or retained-history dimensions merely because implementations call them “status” or store them together.

The v0.8.2 conformance contract requires:

- new profile-conformance claims use `dcterms:conformsTo`;
- structural, profile-semantic, procedural, governance/policy, and interoperability conformance remain separate;
- Capability Levels are not aggregate conformance results;
- Draft structural PASS does not create normative effect; and
- normative effect requires both Accepted / Normative profile status and an actual conformance claim.

## Release Controls Affecting Profiles

v0.8.2 carries forward the v0.8.1 release evidence and both amendments without changing profile semantics.

The effective non-collapse behavioral coverage incorporated from amendment-02 is fifteen of the seventeen Section 7.1 rules. Rules 3 and 6 remain non-demonstrable because accountability and trust are not represented as distinct KEE surfaces at this baseline.

The relevant historical evidence remains under `docs/release/KEE-v0.8.1-*` and `docs/migration/KEE-v0.8.1-*`. The frozen RC11 set remains publication provenance for v0.8.0.

## Workflow

```text
Research Brief -> ADR -> SemVer Release -> Profile -> Release Evidence
```

Future profile semantics that change the published v0.8.2 contract require the appropriate governed PATCH, MINOR, or MAJOR release under ADR-0074 rather than an in-place semantic edit.
