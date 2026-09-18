# KEE

**Knowledge, Epistemics & Eidos**  
**KnoEdg + Eidos**

## KEE in plain language

KEE is a framework for keeping knowledge understandable as it moves between people, organizations, software, and time.

A useful way to understand KEE is to start with a small set of questions:

- **What is this?** — identity and granularity.
- **Where did it come from?** — provenance.
- **When was it true, known, recorded, published, reviewed, or applicable?** — time.
- **What supports or challenges it?** — evidence and confidence.
- **Who had authority to act, and who is responsible?** — authority, delegation, and accountability.
- **What changed, and what must remain part of history?** — lifecycle, revision, supersession, retention, and archival.

These questions are related, but they are not interchangeable.

A respected source is not automatically correct. A highly confident claim is not automatically strongly evidenced. An authorized decision is not automatically a correct decision. A record that was true five years ago is not automatically current today. A search result can be relevant without being valid. Removing something from current search does not mean it should be erased from history.

KEE calls this discipline **non-collapse**: do not collapse two related but meaningfully different ideas into one.

### Time is a first-class concern

KEE does not treat knowledge as frozen.

A claim may have one time when it was true, another when it was observed, another when it was asserted, another when it was recorded, another when it was published, another when it was reviewed, and another when it stopped applying.

Those times answer different questions and must not be silently treated as one generic timestamp when the distinction matters.

Time therefore cuts across provenance, evidence, confidence, authority, lifecycle, retrieval, validity, history, and governance. KEE composes established temporal prior art rather than claiming a new theory or ontology of time.

## A few terms used throughout KEE

- **Epistemic** — relating to knowledge: how something is known, what supports it, how it may be challenged, and what standing it has as knowledge.
- **Provenance** — where information came from, who or what produced it, and how it was derived or changed.
- **Temporal qualification** — identifying the relevant time or times for a claim, event, decision, record, or state.
- **Authority** — recognized permission or power to act or decide.
- **Responsibility / accountability** — who is answerable for an act or outcome.
- **Evidence** — information that supports or challenges a claim.
- **Confidence** — an assessment of how strongly a claim is supported or believed; it is not the evidence itself.
- **Epistemic standing** — the standing a claim has as knowledge: for example, how supported, challenged, qualified, provisional, or accepted it is.
- **Profile** — specialized rules for a particular kind of knowledge, artifact, domain, or use.
- **Interoperability** — whether independently built systems can exchange and use information without losing the distinctions needed to interpret it correctly.
- **Non-collapse** — preserving important distinctions instead of treating related concepts as though they were identical.

## What KEE owns — and what it does not

KEE does **not** claim ownership of the basic semantic building blocks used to represent knowledge.

- **Prior art owns foundational semantics.** RDF, OWL, SHACL, PROV-O, OWL-Time, SKOS, SPARQL, Dublin Core and related standards provide established machinery.
- **Domains and specialized profiles own domain knowledge and artifact-specific behaviour.** KEE does not decide what medicine, law, science, WordPress, finance, philosophy, or another field means.
- **The KEE family contract owns the published cross-profile rules** needed for independently designed profiles to remain interpretable to one another.
- **KEE framework governance owns the standing of KEE's own normative instruments**: which decisions are proposals, which are accepted, which are integrated into a binding release, and how compatibility is governed.

The formal definition is:

> KEE is a **governed application-profile family and interoperability framework for knowledge artifacts** — not a semantic foundation.

Its value is disciplined composition of prior art, explicit non-collapse and behavioral rules, narrowly justified local controlled vocabularies, profile governance, migration and compatibility controls, and executable conformance/reference assets.

KEE is source-neutral and consumer-neutral. Producer or consumer type may affect provenance, evidence, disclosure, validation, review, or governance requirements, but does not by itself establish epistemic standing.

## Current release

**KEE v0.9.1**

Status: **Published Normative Baseline**

v0.9.1 is a backward-compatible **PATCH** release under ADR-0074. It corrects the public explanation and stale current-state wording after v0.9.0 publication.

It adds:

- zero new normative requirements;
- zero new KEE-owned semantic terms;
- zero profile promotions or demotions;
- zero new Capability Levels;
- zero changes to the seventeen non-collapse rules;
- zero conformance-behaviour changes; and
- zero governed-data migration requirements.

An implementation conforming to KEE v0.9.0 conforms to KEE v0.9.1 without implementation change.

Current normative specification:

[`docs/specs/KEE-Specification-v0.9.1.md`](docs/specs/KEE-Specification-v0.9.1.md)

Public normative API:

[`normative-api/v0.9.1.json`](normative-api/v0.9.1.json)

Release history:

[`CHANGELOG.md`](CHANGELOG.md)

The immediately previous published baseline, KEE v0.9.0, remains immutable historical normative provenance.

## Profiles

KEE uses profiles to specialize the framework for particular kinds of knowledge artifacts or domains.

Profiles may be:

- **Accepted / Normative**
- **Draft / Non-Normative**
- experimental or under research

A profile's existence does not imply that it is normative.

Current profile status is documented in:

[`docs/profiles/README.md`](docs/profiles/README.md)

## Conformance

KEE distinguishes five conformance dimensions:

1. structural
2. profile-semantic
3. procedural
4. governance/policy
5. interoperability

Passing structural validation alone does not prove that information is true, authoritative, sufficiently supported, procedurally valid, or fully interoperable.

Conformance means only what the applicable KEE specification and profile explicitly claim it means.

## Repository purpose

This repository is the **public publication surface for KEE**.

It contains the artifacts intended for public use, citation, implementation, interoperability, and long-term reference.

Published release artifacts are treated as immutable historical records.

Development, research, experiments, release preparation, and other working material may occur outside this public repository before publication.

## Persistent identifiers

KEE is registering persistent identifiers under:

`https://w3id.org/kee`

The registration has been submitted to the W3ID project for review. Until that registration is merged and resolution is verified, these identifiers must not be described as operationally persistent or dereferenceable.

The public KEE repository already contains the redirect targets for the KEE core namespace, artifact classifications, lifecycle vocabularies, confidence interpretation sentinel, controlled vocabularies, profile index, and JSON-LD context.

## Versioning

KEE follows Semantic Versioning under ADR-0074.

- **PATCH** — backward-compatible corrections or consolidations
- **MINOR** — backward-compatible additions or material extensions
- **MAJOR** — incompatible changes to the public normative contract

Published versions are immutable.

KEE is currently pre-1.0. A future **v1.0.0** will be a stability baseline: a decision that the protected public normative contract is mature enough for long-term downstream reliance.

## Governance discipline

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

**Current baseline: KEE v0.9.1**
