# KEE Specification v0.11.0 — Release Governance Annex (Informative)

Status: Informative annex to `docs/specs/KEE-Specification-v0.11.0.md`\
Version: 0.11.0\
Date: 2026-10-12

---

## A.0 What this annex is

This annex carries the text of the KEE Specification that governs only the KEE project's own release process: how the project keeps its evidence, closes a release, versions its changes, and records what remains open. v0.10.0 carried this text in Sections 0.4, 18.3 to 18.6, 18.8 to 18.10, 20, 24 and 25 of the specification. v0.11.0 moves it here and leaves, in each of those sections, a one-paragraph pointer that keeps every sentence an implementer could rely on.

**Nothing in this annex creates an obligation on an implementation.** Where a key word appears in uppercase below, it binds the KEE project's release process in the sense the specification's Section 0.1 gives it, and no one else. Where this annex and the specification differ, the specification controls. Section numbers cited without a prefix are sections of the specification.

Each section below names the specification section it was moved from. The moved text is carried unchanged from v0.10.0, except that a reference to v0.10.0 as the current version reads v0.11.0, and Sections A.10 and A.11 are the open items and release notes of this release rather than of the previous one.

---

## A.1 What the specification deliberately does not state (from Section 0.4)

**This specification states no count of shared-contract requirements, and no future release may introduce one without new evidence of the kind described below.**

That omission is deliberate and is a statement of this section rather than an oversight. Successive audits of the same frozen evidence set produced materially different counts under differently worded classification predicates. A blind replication of the classification predicate **failed**: independent replicators working from the predicate and a withheld-classification sample agreed with the original audit on roughly half the sampled items, at a chance-corrected agreement well below any threshold that would support publishing a settled figure. A disagreement audit attributed roughly three quarters of the divergence to **discrimination failure** — two parties applying the same named condition to the same quoted evidence and reaching different answers — rather than to under-specification that better drafting could repair.

The figure is therefore carried as a **band**, and that band MUST NOT be narrowed by drafting alone. Narrowing it requires new evidence of a kind that demonstrates the classification predicate can be applied reproducibly by parties who did not author it.

A count, where one is discussed at all, is **evidence for** the role claim in Section 0.3. It is not part of the normative contract, and nothing in `vocab/`, `shacl/`, `schemas/`, `context/` or this document depends on it. A consumer implements the published surfaces named in this specification; it never implements a number.

The emptiness claim in Section 0.3 is a different kind of claim and does not rest on the contested predicate: it is supported by executable demonstrations that reproduced the behaviour using zero KEE-owned terms, and by the concession that the surviving contract survives renaming its publishing body.

---

## A.2 Term registry (from Section 18.3)

The term registry required by Section 4.2 records, for every KEE-owned semantic surface: IRI, kind, owner, status, definition, the eight admission criteria, introduced and deprecated versions, migration policy, evidence sources, admission verdict, and the surface's **disposition** and the decision that made it.

The disposition takes one of: `carried`, `admitted`, `retired (<migration relation>)`, or a named standing such as `canonical-informative`. A term's current standing is therefore one lookup, not a frozen row plus a chain of override records.

The statement that `vocab/kee.ttl` is generated from the term registry and asserts no axiom remains in Section 18.3 of the specification, because a consumer reads that document.

---

## A.3 Prior-art provenance (from Section 18.4)

Every adopted external replacement used by a KEE change, and every external standard this specification names as a SHOULD-level replacement, MUST have release evidence recording, where available: exact source/document; governing body; version or edition; issuance/publication date; maturity/status; lineage; temporal relation to the KEE baseline being changed; and evidence role. That evidence supports the normative change chain; it does not make a cited source part of KEE's normative text unless a profile or this specification explicitly adopts it.

---

## A.4 Non-collapse behavioural coverage (from Section 18.5)

The release suite MUST preserve executable evidence for the Section 7.1 non-collapse rules. The suite MUST demonstrate changed consumer outcomes when the independently governed input changes, over repository fixtures, shapes, or tooling output, rather than merely searching documentation for phrases or evaluating a lookup over declared inputs.

Behavioural coverage of the seventeen rules at this baseline is **fifteen of seventeen**. NC-01, NC-02, NC-04, NC-05, NC-07 through NC-17 are demonstrated.

**NC-03 (authority vs. responsibility) and NC-06 (confidence vs. trust) are not demonstrable at this baseline, and the reason is representational rather than epistemic.** A non-collapse rule can be demonstrated only where both of its sides are represented, as Section 7.1's own preamble scopes them. KEE represents authority and it represents confidence. It represents neither accountability as a surface distinct from authority, nor trust as a surface distinct from confidence. No shape, concept scheme, vocabulary document or example carries one. The obstacle is an absent vocabulary, not a judgment a consumer would have to make, and it lifts if and only if such a surface is introduced — which is a Section 4.2 admission question, not a testing question.

NC-04, NC-08 and NC-14 **are** demonstrable. In each case the judgment involved is recorded data. NC-08's distinction between a genuine inconsistency and a disagreement arising from time, scope, context, evidence, interpretation or method is carried by `kee:causeType` over the KEE Contradiction Cause Scheme, whose `DirectContradiction` concept is defined as "incompatible claims within the same scope, context, and time frame" and whose other concepts are the alternatives NC-08 enumerates. NC-04's contestation is carried by contradiction records, `kee:knownContradiction`, `kee:ContestedAuthorityClaim` and the `Superseded` lifecycle values. NC-14's two states are carried by a decision record's own status metadata and by a published specification's integration of it, which are separate documents by governance design.

A consumer reading any of these three reads a recorded classification. It does not judge whether an authorized decision is correct, whether a disagreement is genuine, or whether a decision ought to have been integrated — and it must not, because those are the judgments Section 7.1 keeps separate.

---

## A.5 Release closure (from Section 18.6)

A release-closure check MUST fail if a frozen denominator changes, an evidence identifier is missing or duplicated, any required column of a release control is empty or a sentinel, or any row lacks a resolved implementation and evidence disposition. Placeholder sentinels are not admissible values.

---

## A.6 Current-state drift (from Section 18.8)

Living/current-state surfaces are synchronized at each release. Retained legacy compatibility examples remain historical evidence; legacy examples MUST NOT be presented as canonical new-write guidance merely because they remain executable during the compatibility window, and every registered example or fixture SHALL either use canonical new-write forms or carry an in-file compatibility marker.

---

## A.7 Frozen denominators and living controls (from Section 18.9)

Release evidence divides into two kinds, and an artifact's file name does not decide which it is.

**Frozen denominators** are fixed at publication and MUST NOT be edited afterwards: the term registry named at a publication, an audit denominator, an obligation restoration map, a legacy-surface census, a package-atomicity record, and a prior-art provenance register. Their purpose is to be a fixed set that later work is measured against, so editing one destroys the measurement. A correction to a frozen denominator is issued as a new artifact that supersedes it, and the superseded artifact is retained.

**Living controls** MUST be updated as governed decisions are made: the semantic migration registry, the compatibility window, and the reference tooling and tests that enforce them. Their purpose is to describe the repository's current behaviour, so a stale one is a defect.

A specification or amendment MUST state which kind each release artifact is. Where it does not, the artifact is a frozen denominator by default, because treating a denominator as living is the more damaging error.

---

## A.8 Optional candidate surfaces (from Section 18.10)

The following are published as optional, non-required surfaces. An implementation that ignores all of them remains conforming:

- obligation lineage registry;
- JSON profile declaration and its schema (`schemas/json-schema/v0.9-profile-declaration.schema.json`);
- EARL / PROV / SHACL evidence graph;
- RO-Crate KEEpack packaging experiment — **Experimental / Non-Normative**;
- public API diff.

KEEpack remains Experimental / Non-Normative and requires independent producer/consumer evidence under Section 15.7 before any graduation claim.

---

## A.9 Release policy and change discipline (from Section 20)

### A.9.1 Semantic Versioning

Version numbers communicate compatibility:

- **PATCH** — backward-compatible correction or consolidation;
- **MINOR** — backward-compatible addition or material extension; and
- **MAJOR** — incompatible change to the public normative contract.

For pre-1.0 KEE releases, published `0.y.z` baselines deliberately follow a stricter compatibility policy than vanilla major-zero SemVer: a published PATCH release MUST NOT hide an incompatible change.

### A.9.2 Change discipline after publication

Published v0.11.0 is immutable and MUST NOT be substantively rewritten in place. Future corrections or compatible/incompatible changes follow the governed pipeline:

`Observation -> Evidence / Research Question -> Research Brief -> Decision Record -> PATCH / MINOR / MAJOR release -> Profile or Implementation`

Accepted historical decision records remain append-only. Corrections to accepted decisions use new decision records rather than rewriting historical rationale.

An amendment MAY be used as an exceptional compatibility instrument, but the next applicable SemVer release SHOULD consolidate it so ordinary consumers can identify one current KEE version.

Current-state documentation MAY be updated to point to the published baseline. Such publication synchronization MUST NOT be used to hide semantic changes.

---

## A.10 Open items at this baseline (from Section 24)

Stated here so that a reader does not have to reconstruct them. None of these is depended upon by a published surface, and none blocks conformance to this baseline.

1. **The Section 0.4 band is not settled**, and no drafting-only narrowing of it is authorized.
2. **NC-03 and NC-06 remain representationally non-demonstrable** (Section A.4). Closing the gap is a Section 4.2 admission question.
3. **The governance-record review-status escalation is scheduled, not yet performed.** The composed shape `shacl/governance-record-review-status-constraints.ttl` reports at `sh:Warning` at this baseline and reports at `sh:Violation` from v0.12.0 (Section 9.2). A release control asserts the severity against the baseline in both directions, so the schedule cannot lapse unobserved; changing it requires a superseding decision record.
4. **Whether the Assertion Metadata lifecycle slot will ever reject a generic or mixed-axis value is undecided.** `shacl/lifecycle-status-constraints.ttl` reports such a value on a `kee:AssertionMetadataRecord` at `sh:Warning` (Section 9.3). The profile is Accepted / Normative and inside the public normative API, so a rejection would make conforming data non-conforming: it needs its own separately versioned decision and migration notice under Section 17.3, naming the last dual-read and first rejecting versions, and an explicit pre-1.0 call-out. No such decision has been taken, and this baseline does not schedule one.
5. **Draft and Draft / Non-Normative are two labels for one normative effect.** Section 21 states that they have identical effect at this baseline; the suffix is historical. Collapsing the two labels into one is recommended for a later release, as its own recorded decision, because the labels also appear in the published public-API manifest's profile statuses and in the profile status index, which a label change must update together.
6. **KEEpack remains Experimental / Non-Normative** and requires independent producer/consumer evidence under Section 15.7 before any graduation claim.
7. **Durable persistence of the canonical identifiers is not established, and resolution is confirmed only as Section 18.7 lists it.** Registration is merged for the identifiers v0.10.0 carried, and on 2026-10-12 every one of them was re-verified: the base identifier content-negotiates; the artifact, confidence, five lifecycle and two local-vocabulary namespaces each resolve to their published concept scheme by an unconditional redirect, served as `text/plain`; the generic lifecycle namespace and the profile identifiers resolve to human-readable pages. The three namespaces added at this baseline are registration pending and return `404`. The version identifier of v0.10.0 returned `404`, because no version-pattern rule is registered, and this release's version identifier is not claimed to resolve. Persistence over time is a claim about future behaviour that a verified resolution does not settle.

The Section 12.3 accountable-root escalation, listed as closed at v0.10.0, is removed from this list because it is performed and its control holds.

---

## A.11 Release notes (from Section 25)

### v0.11.0

- Adds three admitted KEE-owned controlled value sets to the public normative API, which is why this release is MINOR rather than PATCH: the governance-record review-status scheme at `https://w3id.org/kee/lifecycle/governance-record#` (Section 9.2), the query-time-dimension scheme at `https://w3id.org/kee/vocab/query-time-dimension#` (Sections 10, 14.2), and the retrieval-eligibility scheme at `https://w3id.org/kee/vocab/retrieval-eligibility#` (Sections 10, 14.5). All three namespaces are registration pending (Section 18.7). An implementation that conformed to v0.10.0 remains conforming without change unless it opts into a capability one of these schemes serves.
- Carries two conformance-behaviour changes, recorded as Section 18.2 requires. The first: the composed shape `shacl/governance-record-review-status-constraints.ttl` checks, by `sh:in`, that `kee:lifecycleState` on `kee:GovernanceTransitionRecord`, `kee:ContradictionRecord`, `kee:ContestedAuthorityClaim` and `kee:LifecycleCrosswalkMapping` takes a value from the governance-record review-status scheme, and reports at `sh:Warning`. No conformance outcome changes for those classes at this baseline. **v0.11.0 is the last dual-read version and v0.12.0 is the first rejecting version**, in which the same shape reports at `sh:Violation`. Negative case: a record of one of those four classes that writes a generic `https://w3id.org/kee/lifecycle#` value conforms at this baseline with a warning and will not conform at v0.12.0. Classified MINOR-compatible because the four owning profiles are Draft / Non-Normative and excluded from the public normative API; the public normative contract is unchanged. A release control asserts the severity against the baseline in both directions.
- The second: closes the `kee:queryTimeDimension` slot of `shacl/historical-bitemporal-querying-profile.ttl` and the `kee:eligibilityCategory` slot of `shacl/ai-grounded-retrieval-profile.ttl` by `sh:in` over their schemes, and the membership check on a new-write record reports at `sh:Violation` from this baseline. Negative case: a point-in-time query record or retrieval result that wrote an IRI of its own in either slot conformed structurally to the Draft shape under v0.10.0, whose Section 14.2 called the slot an open classifier, and does not conform at this baseline; **v0.10.0 is the last version in which such a value conforms and v0.11.0 the first rejecting version** (Sections 14.2, 14.5, 17.3). A registered-legacy record, one declaring only `kee:profileConformance`, is reported at `sh:Warning` in both versions and retires with that carrier. Both profiles are Draft / Non-Normative and excluded from the public normative API, which is the ground for the MINOR-compatible classification; the change is recorded here because it alters observable conformance behaviour (Section 18.2). A release control asserts the severity against the baseline in both directions.
- Restates Section 18.7 on a verification of 2026-10-12: the base identifier content-negotiates to the term declarations, the context or the repository page; the artifact and confidence namespaces, the five lifecycle namespaces v0.10.0 carried and its two local-vocabulary namespaces each resolve to their published concept scheme by an unconditional redirect, which v0.10.0 had recorded as registered but unverified; the RDF documents are served as `text/plain`, which a consumer must not read as evidence that they are not RDF; the generic lifecycle namespace and the profile identifiers resolve to human-readable pages; the three namespaces added at this baseline and the v0.10.0 version identifier return `404`.
- States that `kee:lifecycleState` on an Assertion Metadata record denotes the lifecycle of the managed assertion unit, with `https://w3id.org/kee/lifecycle/assertion#` the default scheme for new writes when no other profile governs the unit, and that the governance-record review-status scheme is not a value set for that slot (Section 16.4). This adds no constraint: the Assertion Metadata shape is unchanged, the composed review-status shape is not composed with it, and `shacl/lifecycle-status-constraints.ttl` reports a generic or mixed-axis value on that slot at `sh:Warning` only. Whether that profile will ever reject such a value is a separate decision not yet taken (Section A.10, item 4).
- Consolidation that keeps the meaning of every v0.10.0 obligation: every top-level section is marked Normative or Informative (Section 0.1); the conformance targets each obligation falls on are named, with the section each obligation comes from and no new obligation (Section 15.8); the terms the text used without defining are defined (Section 21: governed artifact, dual-read, rewrite-safe, release control, frozen denominator, living control, profile status ladder, KnoEdg, Eidos); every namespace the baseline uses is listed (Section 0.7); security and privacy considerations are added (Section 26); and the text that governs only the project's release process is carried in this annex, with pointers in place so that section numbering is unchanged from v0.10.0.
- Editorial: the stale "KEE v0.9" in Section 0.3 reads "KEE"; Section 12.3 loses a duplicated sentence and speaks of the v0.10.0 escalation in the past tense; Section 0.2 states that the shape-contract version is declared by the public-API manifest rather than carried by each shape graph; Sections 9.2 and 10 no longer claim resolution for namespaces that Section 18.7 does not confirm.
- Promotes no profile, adds no Capability Level, and requires no governed-data migration. Implementers of the four Draft profiles named above get one release in which a generic review-status value is reported before it fails. Does not narrow the Section 0.4 band.

### v0.10.0

- Escalates the Section 12.3 accountable-root constraint from `sh:Warning` to `sh:Violation` in the reference shape. This is the one conformance-behaviour change, and the reason this release is MINOR rather than PATCH.
- A grantee that is not a `prov:Person` or `prov:Organization` and resolves through no delegation chain to one conformed structurally under v0.9.2 and does not conform at this baseline. An implementation claiming the Authority and Delegation profile and relying on warning-level behaviour must resolve its delegation chains.
- Classified MINOR-compatible because the owning Authority and Delegation profile is Draft / Non-Normative and excluded from the public normative API. The public normative contract is unchanged.
- Restates Section 18.7: registration is merged; the base identifier, the artifact scheme, and the confidence scheme resolve and are verified, other identifiers in the family do not yet content-negotiate to RDF and this baseline says so; the unversioned identifier denotes the current published baseline; each release also carries a version identifier; and durable persistence remains an unestablished claim distinct from verified resolution.
- Adds no requirement beyond the escalation, no KEE-owned semantic term, no profile promotion, and no Capability Level. Requires no governed-data migration.

### v0.9.2

- Consolidates v0.9.0 and v0.9.1 into one self-contained published baseline under a single current version identifier.
- Inlines the full normative contract, so that determining the meaning of a KEE obligation requires no other document.
- Adds no requirement, no KEE-owned semantic term, no profile promotion, no Capability Level, and no conformance-behaviour change.
- Requires no implementation change and no governed-data migration.

### Contract carried unchanged

Carried unchanged from v0.10.0, v0.9.2, v0.9.1 and v0.9.0: Prior Art First and the KEE-owned-term admission test; the KnoEdg + Eidos responsibility boundaries; requirement categories and ownership rules; all seventeen Section 7.1 non-collapse rules and their `NC-01`..`NC-17` identifiers; source and consumer neutrality; the shared-dimension ownership contract, including temporal qualification as a cross-cutting dimension; governance, authority/delegation, evidence/confidence, contradiction/promotion, retrieval, archival and historical-query rules; the five conformance dimensions and their machine-safe tokens; independent interoperability evidence as a promotion requirement; the optional candidate surfaces; the Promotion shape's cyclic-scope constraint; the Section 12.3 accountable-root constraint at `sh:Violation`; profile statuses; terminology and Capability Levels; the compatibility and migration obligations; and the rule that no settled shared-contract count is published.
