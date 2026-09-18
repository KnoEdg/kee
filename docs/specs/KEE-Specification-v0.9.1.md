# KEE Specification v0.9.1

Status: Published Normative Baseline  
Version: 0.9.1  
Date: 2026-09-17  
SemVer classification: PATCH  
Supersedes as current version identifier: KEE v0.9.0  
Authorizing release policy: ADR-0074  
Published public API: `normative-api/v0.9.1.json`

---

## 0. Status and release rule

KEE v0.9.1 is a **Semantic Versioning PATCH release** under ADR-0074.

It corrects public-facing explanation and stale current-state documentation after publication of v0.9.0. It does not change the KEE normative contract.

An implementation conforming to KEE v0.9.0 conforms to KEE v0.9.1 **without implementation change**.

v0.9.1 adds:

- zero new normative requirements;
- zero new KEE-owned semantic terms;
- zero profile promotions or demotions;
- zero new Capability Levels;
- zero changes to the seventeen Section 7.1 non-collapse rules;
- zero conformance-behaviour changes; and
- zero governed-data migration requirements.

## 1. Public explanation correction

The repository front door now introduces KEE in plain language before presenting the formal architectural definition.

The correction makes explicit that:

1. **Time is a first-class cross-cutting concern.** A claim may have distinct valid, observation, assertion, recording, publication, review, invalidation, deprecation, supersession and archival times. Relevant temporal roles must not be silently collapsed into one generic timestamp.
2. **Non-collapse means preserving important distinctions.** Related concepts are not automatically identical.
3. Public-facing uses of terms such as *epistemic*, *provenance*, *temporal qualification*, *authority*, *evidence*, *confidence*, *profile* and *interoperability* should be defined before relying on them.
4. KEE's ownership boundary remains unchanged: prior art owns foundational semantics; specialized profiles own domain and artifact-specific behaviour; the KEE family contract owns published cross-profile rules; KEE framework governance owns the standing of KEE's own normative instruments.

These statements clarify already-published v0.9.0 semantics. They do not add a new normative obligation.

## 2. Normative content carried unchanged from v0.9.0

Except for version metadata and the documentation corrections described above, every normative obligation of `KEE-Specification-v0.9.0.md` is carried unchanged into v0.9.1.

In particular, v0.9.1 preserves unchanged:

- Prior Art First;
- the KnoEdg + Eidos responsibility boundaries;
- source and consumer neutrality;
- all seventeen non-collapse rules;
- temporal qualification as a cross-cutting dimension;
- governance, authority/delegation, evidence/confidence, contradiction/promotion, retrieval, archival and historical-query rules;
- the five conformance dimensions;
- profile statuses;
- terminology and Capability Levels;
- compatibility and migration obligations; and
- the v0.9.0 rule that no settled shared-contract count is published.

## 3. Compatibility

No implementation change is required.

New conformance declarations SHOULD identify `0.9.1` as the current baseline.

Existing declarations naming v0.9.0 or earlier remain historical facts and MUST NOT be silently rewritten merely to update a version label.

No governed-data migration is required.

## 4. Historical provenance

Published v0.9.0 and every earlier published baseline remain immutable historical normative provenance.

v0.9.1 does not rewrite v0.9.0. It supersedes only the current-version identifier and records the documentation correction as a new PATCH release.

## 5. Change discipline

Published v0.9.1 is immutable.

Future corrections or compatible/incompatible changes follow ADR-0074 and the normal governed pipeline:

`Observation -> Evidence / Research Question -> Research Brief -> ADR -> PATCH / MINOR / MAJOR release -> Profile or Implementation`
