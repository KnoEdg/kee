# KEE Profiles

Profiles adapt the KEE core specification to a specific artifact type, domain, or implementation context. Domain details remain outside the core wherever practical.

## Published baseline

The current published normative baseline is:

- [`docs/specs/KEE-Specification-v0.9.2.md`](../specs/KEE-Specification-v0.9.2.md).

v0.9.2 is a self-contained SemVer PATCH consolidation. It changes no profile status and promotes no profile.

Section 19 of the specification is the authoritative statement of profile status; this document restates it for convenience.

## Current profile status

| # | Profile | Status |
|---|---|---|
| 1 | Software Engineering Profile | Accepted / Normative |
| 2 | Scientific Claim Profile | Accepted / Normative |
| 3 | Assertion Metadata Profile | Accepted / Normative |
| 4 | Assertion Profile | Draft |
| 5 | Decision Profile | Draft |
| 6 | Organizational Memory Profile | Draft |
| 7 | Lifecycle Crosswalk Profile | Draft / Non-Normative |
| 8 | Governance Transition Profile | Draft / Non-Normative |
| 9 | Promotion Profile | Draft / Non-Normative |
| 10 | Authority and Delegation Profile | Draft / Non-Normative |
| 11 | Contradiction Records Profile | Draft / Non-Normative |
| 12 | AI-Grounded Retrieval Profile | Draft / Non-Normative |
| 13 | Artifact Identity and Granularity Profile | Draft / Non-Normative |
| 14 | Historical and Bitemporal Querying Profile | Draft / Non-Normative |

A profile is not promoted merely because it has executable shapes, fixtures, examples, or tests. The existence of a profile identifier, document, shape graph, or passing structural validation does not by itself create normative force.

## Binding effect

A profile has binding normative effect for a result only when both conditions hold:

1. the profile is Accepted / Normative in the applicable baseline; and
2. the implementation or resource actually claims conformance to it.

Draft and Non-Normative profiles are excluded from the public normative API. Claiming a Draft profile records which designated contract an implementation intends to follow; it creates no obligation.

Where a shared dimension is assigned to a profile that is not yet Accepted / Normative, the owner of record for that dimension is the core interoperability contract (specification Section 6.4).

## Cross-profile rules

Profiles MUST preserve Source and Consumer Neutrality. Producer or consumer type alone MUST NOT establish epistemic standing.

Profiles MUST NOT collapse independent lifecycle, publication, review/currency, archival/disposition, epistemic/evidential, ranking, confidence, evidence-strength, replication, authority, scope/context, retrieval, or retained-history dimensions merely because implementations call them "status" or store them together.

The conformance contract requires:

- new profile-conformance claims use `dcterms:conformsTo`;
- structural, profile-semantic, procedural, governance/policy, and interoperability conformance remain separate;
- Capability Levels are not aggregate conformance results;
- a Draft structural PASS creates no normative effect; and
- normative effect requires both Accepted / Normative status and an actual conformance claim.

## Promotion

A new profile promotion or graduation claim MUST be supported by independent interoperability evidence. Reference self-roundtrip is insufficient: a producer and a consumer that share an implementation demonstrate that the implementation is self-consistent, not that the contract is interoperable.

This requirement is not retroactive. An existing conformance claim does not become non-conforming for want of it.

## Non-collapse coverage

Behavioural coverage of the seventeen non-collapse rules at this baseline is fifteen of seventeen.

NC-03 (authority vs. responsibility) and NC-06 (confidence vs. trust) are not demonstrable, because KEE represents authority and confidence but does not represent accountability and trust as distinct semantic surfaces. The obstacle is representational, not epistemic, and closing it is a term-admission question rather than a testing question.

## Workflow

```text
Observation -> Evidence / Research Question -> Research Brief -> Decision Record -> PATCH / MINOR / MAJOR release -> Profile or Implementation
```

Future profile semantics that change the published contract require the appropriate governed PATCH, MINOR, or MAJOR release rather than an in-place semantic edit.
