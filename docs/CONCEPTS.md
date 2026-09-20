# KEE Concept Map

**Informative / Non-Normative — canonical conceptual snapshot, kept in sync with the current published baseline.**

This snapshot is an orientation aid, not a substitute for the published KEE specification, Accepted / Normative profiles, or ADRs. Representing a concept using KEE does not make it a KEE concept, and does not imply KEE endorsement of it. Later governed KEE changes supersede this snapshot where they differ.

The ownership boundary it reflects is stated in root [`README.md`](../README.md#what-kee-owns--and-what-it-does-not).

## KEE conceptual tree

```text
KEE
│
├── Architectural discipline
│   ├── Prior Art First
│   ├── Composition
│   ├── Non-collapse — related does not mean identical
│   ├── Source and Consumer Neutrality
│   ├── Explicit requirement ownership
│   ├── Explicit conformance claims
│   └── Open-world discipline where applicable
│
├── Cross-cutting dimensions
│   ├── Identity and granularity       — what thing / at what level?
│   ├── Time / temporal qualification  — when was it true, known, or applicable?
│   ├── Provenance                     — where from / how produced?
│   ├── Scope                          — where does it apply?
│   ├── Context                        — how should it be interpreted?
│   ├── Lifecycle and history          — how has it changed?
│   ├── Authority and delegation       — who may do what, on what basis?
│   ├── Responsibility/accountability  — who answers for the act?
│   ├── Evidence                       — what supports or challenges it?
│   ├── Confidence                     — profile-defined assessment
│   ├── Epistemic standing             — how does it stand as knowledge?
│   ├── Trust                          — reliance on source/process/credential
│   ├── Contradiction                  — preserved conflict, not automatic falsehood
│   ├── Retention/review/archival      — preserved is not necessarily current
│   ├── Retrieval eligibility          — consumer/use decision, not source truth
│   ├── Historical sufficiency         — queryable is not necessarily complete
│   └── Replication                    — separate from lifecycle/publication state
│
├── Responsibility boundaries
│   ├── Eidos
│   │   └── entity, agency, sovereignty, intent, identity,
│   │       responsibility, policy, decision, continuity
│   └── KnoEdg
│       └── epistemic governance and organizational memory
│
├── Prior art supplies foundational LEGO pieces
│   ├── RDF / OWL / SPARQL
│   ├── PROV-O
│   ├── OWL-Time
│   ├── Dublin Core Terms
│   ├── SKOS
│   ├── SHACL
│   ├── Web Annotation
│   ├── RO-Crate and other package prior art
│   └── domain standards
│
├── Profiles = specialized instruction books
│   ├── Accepted / Normative where explicitly promoted
│   ├── Draft / Non-Normative where still experimental
│   └── domain/application profiles own concrete rules where appropriate
│
├── Knowledge artifacts = the governed things being built
│
├── Conformance
│   ├── structural
│   ├── profile-semantic
│   ├── procedural
│   ├── governance/policy
│   └── interoperability
│
└── KEEpack
    └── informative portable assembled model / composition pattern;
        not a separate universal KEE semantic layer
```

## LEGO shorthand

- **Prior art supplies the bricks.**
- **The domain decides what is being built.**
- **KEE supplies the building discipline.**
- **Profiles supply specialized instructions.**
- **A knowledge artifact is the built model.**
- **Conformance checks what was claimed.**
- **Interoperability checks whether another builder can understand/use it.**
- **A KEEpack may be a portable assembled model.**
