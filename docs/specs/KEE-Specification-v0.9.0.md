# KEE Specification v0.9.0

Status: Published Normative Baseline  
Version: 0.9.0  
Date: 2026-09-17  
SemVer classification: MINOR  
Supersedes as current version identifier: KEE v0.8.2  
Release candidate: `docs/specs/KEE-Specification-v0.9.0-rc1.md`, preserved unchanged as historical provenance  
Authorizing decisions: ADR-0074 (release policy), ADR-0075 (v0.9 role), as corrected by ADR-0077 and ADR-0078  
Published public API: `normative-api/v0.9.0.json`  
Change classification: `normative-api/v0.9.0-change-classifications.json`

---

## 0. Status and release rule

KEE v0.9.0 is the current published normative baseline. It supersedes v0.8.2 as the current version identifier; v0.8.2 and every earlier published baseline remain immutable historical normative provenance and are not rewritten by this release.

KEE v0.9.0 is a **Semantic Versioning MINOR release** under ADR-0074: a backward-compatible addition. An implementation conforming to KEE v0.8.2 remains conforming under v0.9.0 without implementation change.

v0.9.0 adds no new KEE-owned semantic term, promotes no profile to Accepted / Normative, adds no Capability Level, and changes no Section 7.1 non-collapse rule.

## 1. What v0.9.0 states about KEE's role

Per ADR-0075, KEE v0.9 is a **governed application-profile family and interoperability framework**: a published, versioned, testable shared contract over prior art, and **not a semantic foundation**.

The ownership boundary is:

1. **Prior art owns foundational semantics.** KEE does not restate, replace, or shadow what an established standard already defines.
2. **Specialized profiles own domain and artifact-type behaviour.**
3. **The KEE family contract owns the published cross-profile rules** that make independently designed profiles interpretable to one another.
4. **KEE framework governance owns the standing of KEE's own normative instruments** — the distinction between a decision being Accepted and its being integrated as a binding requirement.

**No genuinely KEE-specific semantic primitive is claimed.** The v0.9 audit of the frozen 120-observation registry returns **zero** for the class of obligations that would require a KEE-owned semantic surface not supplied by prior art and not dissolved by publishing the same surface under a neutral name. This result was re-derived independently by a party that had not seen the prior result.

## 2. What this specification deliberately does NOT state

**This specification states no count of shared-contract requirements, and no future release may introduce one without new evidence of the kind ADR-0078 requires.**

That omission is deliberate and is the point of this section rather than an oversight:

- Successive audits of the same frozen registry produced materially different counts under differently worded predicates.
- A blind replication of the classification predicate **failed**: two replicators, working from the predicate and twenty sampled obligations with every classification-bearing field withheld, agreed with the audit on 9/20 and 10/20 (Cohen's κ 0.233 and 0.288) and with each other on 12/20.
- A disagreement audit found roughly three quarters of the divergence to be **discrimination failure** — two parties applying the same named condition to the same quoted evidence and reaching different answers — rather than under-specification that better drafting could repair.
- ADR-0077 accordingly restates the figure as a **band**, and ADR-0078 forbids narrowing that band by drafting alone.

The count is **evidence for** the role claim in Section 1. It is not part of the normative contract, and nothing in `vocab/`, `shacl/`, `schemas/`, `context/` or this document depends on it. A consumer implements the published surfaces in Section 3; it never implements a number.

The zero in Section 1 is a different kind of claim and does not rest on the contested predicate: it is supported by executable demonstrations that reproduced the behaviour using zero KEE-owned terms, and by the concession that the surviving contract survives renaming its publishing body.

## 3. Compatible additions in this release

Each addition below is classified in `normative-api/v0.9.0-change-classifications.json` with a stated reason.

### 3.1 Stable non-collapse rule identifiers

Introduces `NC-01` through `NC-17` as stable identifiers mapped to the already-published Section 7.1 non-collapse rules.

These identifiers are **new in v0.9.0**. This specification does not claim they existed in v0.8.2, and a v0.8.2 artifact that does not use them is not thereby non-conforming.

The rules themselves are unchanged. Section 18.5 behavioural coverage remains **fifteen of seventeen**; NC-03 (authority/responsibility) and NC-06 (confidence/trust) remain representation-gap cases, because KEE represents authority and confidence but does not represent accountability and trust as distinct semantic surfaces. That obstacle is representational, not an epistemic judgment, and v0.9.0 does not close it.

### 3.2 Machine-safe conformance dimension tokens

Adds machine-safe aliases for the five conformance dimensions while **preserving the published v0.8.2 human label** `governance/policy`. Both spellings are accepted; the historical spelling is not deprecated by this release and historical declarations using it MUST NOT be rewritten.

### 3.3 Independent interoperability evidence as a promotion requirement

Adds `independent-interoperability-evidence` as a requirement for **new profile promotion or graduation claims**.

This is **not** a retroactive obligation on existing v0.8.2 conformance claims. Reference self-roundtrip remains insufficient as independent interoperability evidence: a producer and a consumer that share an implementation demonstrate that the implementation is self-consistent, not that the contract is interoperable.

### 3.4 Optional candidate surfaces

The following are added as optional, non-required surfaces. An implementation that ignores all of them remains conforming:

- obligation lineage registry;
- JSON profile declaration and its schema (`schemas/json-schema/v0.9-profile-declaration.schema.json`);
- EARL / PROV / SHACL evidence graph;
- RO-Crate KEEpack experiment — **Experimental / Non-Normative**;
- public API diff.

### 3.5 Promotion shape: cyclic scope ordering

`shacl/promotion-profile.ttl` gains a constraint rejecting a cyclic `skos:broader` ordering between `kee:sourceScope` and `kee:scope`.

**This is a real conformance-behaviour change and is recorded as one.** The v0.8.2 shape reports `conforms = true` for a mutated fixture making the two scopes mutually `skos:broader`; the v0.9 shape reports `conforms = false`. An unmutated control conforms under both.

It is classified MINOR-compatible because `docs/profiles/promotion-profile.md` is **Draft / Non-Normative**, which ADR-0074 §2 excludes from the public normative API. A reader who disagrees with that exclusion should read this as the one place where v0.9.0's MINOR classification depends on a governance-status judgment rather than on behaviour alone.

## 4. Compatibility

An implementation conforming to KEE v0.8.2 conforms to KEE v0.9.0 **without implementation change**, subject only to identifying the baseline in new conformance declarations or release metadata.

Existing declarations naming v0.8.2 or earlier remain historical facts and MUST NOT be silently rewritten.

No migration of governed data is required by this release. New writes use canonical KEE surfaces; registered legacy forms remain readable according to the compatibility registry and window. Exact migration MUST NOT be inferred from labels, and `owl:sameAs` MUST NOT be used as a convenience for it.

## 5. Normative content carried unchanged from v0.8.2

Except for the additions in Section 3 and the version metadata required by this release, every normative obligation of `KEE-Specification-v0.8.2.md` is carried unchanged, including:

- Prior Art First and the KEE-owned-term admission test;
- the KnoEdg + Eidos responsibility boundaries;
- requirement categories and ownership rules;
- all seventeen Section 7.1 non-collapse rules;
- source and consumer neutrality, including that producer or consumer type may change required provenance, evidence, disclosure, validation, review or governance without establishing epistemic standing by itself;
- the shared-dimension ownership contract, including temporal qualification as a cross-cutting dimension;
- governance, authority/delegation, evidence/confidence, contradiction/promotion, retrieval, archival and historical-query rules;
- the five conformance dimensions;
- profile statuses as published under v0.8.2 — **no profile is promoted by this release**;
- terminology and Capability Levels; and
- the v0.8.2 compatibility and migration obligations.

The v0.8 release control rule is carried unchanged and governs this release:

> **A KEE term may disappear; its audited obligation may not disappear silently.**

## 6. Historical provenance

Preserved and citable, and not rewritten by this release: the v0.8.2 published baseline; v0.8.1 and its amendments 01 and 02; all frozen denominators, living-control history, ADRs, tests and evidence that established them.

The v0.9 audit lineage is likewise append-only. Each pass is a superseding overlay; no prior overlay or frozen registry is edited in place, per Amendment 01 §18.9. That the classification layer of an earlier pass **failed replication** is part of the record, not a defect to be tidied out of it.

## 7. Open items at this candidate

Stated here so that a reader of this document does not have to reconstruct them:

1. **ADR-0076 gate 2 is undecided.** No further convergence experiment is authorized.
2. **Predicate defects PD-05..PD-17 and overlay defects OD-01..OD-03 are open**, along with standing limitation SL-01 and the disclosed sensitivity band.
3. **48 of 120 registry rows have an undecided class placement.** Their shared-contract status is decided; only their placement among the non-shared classes is not.
4. **KEEpack remains Experimental / Non-Normative** and requires genuine independent producer/consumer evidence before any graduation claim.
5. **NC-03 and NC-06 remain representationally non-demonstrable.**

None of these blocks the additions in Section 3, because none of them is depended upon by a published surface. All of them block any attempt to restate the Section 2 count as settled.

## 8. Change discipline

Published v0.9.0 is immutable. Corrections follow ADR-0074 and the governed pipeline:

`Observation -> Evidence / Research Question -> Research Brief -> ADR -> PATCH / MINOR / MAJOR release -> Profile or Implementation`

The publication record for this release is `docs/release/KEE-v0.9.0-publication.md`.
