```markdown
# KEE

**Knowledge, Epistemics & Eidos**

KEE is a **governed application-profile family and interoperability framework for knowledge artifacts**.

It provides a disciplined way to combine established standards for representing knowledge, provenance, time, evidence, lifecycle, governance, and conformance without inventing a new semantic foundation.

> **Prior art supplies the building blocks.  
> Domains decide what is being modeled.  
> KEE supplies the interoperability and governance discipline.**

## Current Release

**KEE v0.9.0**

Status: **Published Normative Baseline**

KEE is currently pre-1.0.

The project is working toward a future **v1.0.0 stability baseline**, at which point the public normative contract will be treated as sufficiently mature for long-term downstream reliance.

## What KEE Is

KEE provides common rules for building and exchanging governed knowledge artifacts.

It addresses concerns such as:

- identity and granularity
- provenance
- time
- scope and context
- lifecycle and history
- evidence
- confidence
- authority and responsibility
- contradiction
- governance
- conformance
- interoperability

KEE separates these concerns rather than collapsing them into one another.

For example:

- provenance is not truth;
- confidence is not trust;
- authority is not responsibility;
- preservation is not current validity;
- retrieval relevance is not epistemic validity;
- contradiction does not automatically mean one side is false.

These distinctions are part of KEE's interoperability discipline.

## Prior Art First

KEE deliberately builds on established standards and practices.

Important foundations include:

- RDF
- OWL
- SHACL
- SPARQL
- PROV-O
- OWL-Time
- SKOS
- Dublin Core Terms
- Web Annotation
- RO-Crate and related packaging approaches
- domain-specific standards and application profiles

KEE does **not** claim to replace these technologies.

KEE v0.9.0 claims **no genuinely KEE-specific foundational semantic primitive**.

Its role is primarily in the governed composition of prior art, cross-profile interoperability rules, conformance, and framework governance.

## Profiles

KEE uses profiles to specialize the framework for particular kinds of knowledge artifacts or domains.

Profiles may be:

- **Accepted / Normative**
- **Draft / Non-Normative**
- experimental or under research

A profile's existence does not imply that it is normative.

The profile itself defines the additional requirements appropriate to its subject area.

## Conformance

KEE distinguishes several dimensions of conformance:

1. structural
2. profile-semantic
3. procedural
4. governance/policy
5. interoperability

Passing structural validation alone does not prove that information is true, authoritative, sufficiently supported, procedurally valid, or fully interoperable.

Conformance means only what the applicable KEE specification and profile explicitly claim it means.

## Repository Purpose

This repository is the **public publication surface for KEE**.

It contains the artifacts intended for public use, citation, implementation, interoperability, and long-term reference.

Published release artifacts are treated as immutable historical records.

Development, research, experiments, release preparation, and other working material may occur outside this public repository before publication.

## Specification

Current normative specification:

[`docs/specs/KEE-Specification-v0.9.0.md`](docs/specs/KEE-Specification-v0.9.0.md)

Public normative API:

[`normative-api/v0.9.0.json`](normative-api/v0.9.0.json)

Release history:

[`CHANGELOG.md`](CHANGELOG.md)

## Persistent Identifiers

KEE is preparing persistent identifiers under:

`https://w3id.org/kee`

Until registration is completed and verified, these identifiers MUST NOT be described as operationally persistent or dereferenceable.

Registration status will be recorded in this repository.

## Versioning

KEE follows Semantic Versioning.

- **PATCH** — backward-compatible corrections or consolidations
- **MINOR** — backward-compatible additions or material extensions
- **MAJOR** — incompatible changes to the public normative contract

Published versions are immutable.

Once KEE reaches **v1.0.0**, incompatible changes to the protected public normative contract will require a new major version.

## Governance

KEE evolves through an evidence-driven process:

**Observation → Evidence / Research → Decision → Specification / Profile → Release**

Prior Art First applies before introducing KEE-owned semantic surfaces.

A core project rule is:

> **A KEE term may disappear; its governed obligation may not disappear silently.**

## Project

KEE is maintained by the **KnoEdg** project.

Primary maintainer: **René Yap**

Repository:

https://github.com/KnoEdg/kee

---

**Current baseline: KEE v0.9.0**
```
