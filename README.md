# KEE

**Knowledge, Epistemics & Eidos**

KEE is a framework for keeping knowledge understandable as it moves between people, organizations, software systems, and through time.

---

# For the General Public

## What problem is KEE trying to solve?

Knowledge does not stay still.

It gets copied, summarized, challenged, corrected, superseded, reviewed, combined with other information, moved between organizations, and interpreted by different software systems.

During that process, important distinctions can disappear.

A source can become confused with evidence.

Confidence can become confused with certainty.

Authority can become confused with correctness.

A current statement can replace an older statement without preserving the history.

A date can be reduced to one generic timestamp even though several different times matter.

KEE exists to help prevent that loss of meaning.

It asks systems to preserve the distinctions necessary to understand not only what a piece of knowledge says, but also where it came from, when it applied, what supports it, what happened to it over time, and what standing it currently has.

## The basic questions

A useful way to understand KEE is through a small set of questions.

- What is this?
- Where did it come from?
- When was it true, observed, asserted, recorded, published, reviewed, or applicable?
- What supports it?
- What challenges it?
- How confident are we in it?
- Who had authority to act or decide?
- Who is responsible?
- What changed?
- What came before it?
- What replaced it?
- What must remain part of the historical record?

These questions are related.

But they do not mean the same thing.

KEE calls the discipline of preserving these differences **non-collapse**.

## Non-collapse

Non-collapse means that two related ideas should not be treated as identical when the difference matters.

For example:

A respected source is not automatically correct.

Strong confidence is not the same thing as strong evidence.

Having authority to make a decision does not prove the decision was correct.

Something that was true in the past is not automatically true now.

Something that has been superseded may no longer be current, but it can still be historically important.

A search result can be relevant without being valid.

Removing something from current search does not mean it should disappear from history.

KEE tries to preserve these distinctions as knowledge moves between systems.

## Time is part of the knowledge

KEE does not treat knowledge as frozen.

Consider a general scientific claim.

An observation may have been made in January.

A researcher may have interpreted it in February.

A report may have been written in March.

The report may have been published in April.

Another group may have reviewed it in June.

New evidence may have challenged it in September.

A later result may have superseded it the following year.

All of those dates describe different things.

Reducing them to one timestamp can destroy important information.

KEE therefore treats time as a first-class concern.

Time can affect provenance, evidence, confidence, authority, applicability, lifecycle, retrieval, validity, history, and governance.

KEE does not claim to have invented a new theory of time.

It uses established approaches for representing these distinctions.

## What does epistemic mean?

Epistemic simply means relating to knowledge.

It concerns questions such as:

How do we know this?

What supports it?

What challenges it?

How certain or uncertain are we?

Who made the claim?

Under what conditions?

Has it been reviewed?

Has it been superseded?

What standing should it currently have?

KEE is therefore concerned not only with storing information, but with preserving enough context to understand how that information should be treated as knowledge.

## What does Eidos mean?

Eidos is an old philosophical term associated with form, structure, or the recognizable character of something.

In KEE, Eidos points toward the thing being described.

Epistemics concerns how we know something about it.

Eidos concerns what the knowledge is about and how that thing is identified or structured.

KEE tries to keep these concerns connected without collapsing them into one another.

A simple way to put it is:

**Eidos concerns what we are talking about.**

**Epistemics concerns how we know what we say about it.**

## Does KEE invent these ideas?

Mostly, no.

KEE deliberately follows a principle called **Prior Art First**.

Many of the capabilities KEE needs already exist in established standards, technologies, research traditions, and other frameworks.

KEE uses those rather than replacing them unnecessarily.

Its proposed value is not that it invented provenance, time, evidence, semantic modeling, validation, or knowledge representation.

Its proposed value is that it brings selected pieces of prior art together under a governed contract that says which distinctions must survive when knowledge moves between independently designed systems.

That proposition remains open to testing.

If existing frameworks can provide the same governed behavior without KEE, they should be preferred where appropriate.

KEE should exist only where it provides useful discipline that is not already adequately supplied elsewhere.

## What KEE does not decide

KEE does not decide what is true in medicine, law, science, engineering, finance, history, philosophy, or any other field.

Those domains define their own concepts, evidence, methods, and standards.

KEE is concerned with how knowledge artifacts can preserve important distinctions while being exchanged, reviewed, revised, governed, and interpreted across systems.

---

# For Implementers

## Formal definition

KEE is a **governed application-profile family and interoperability framework for knowledge artifacts**.

It is not a semantic foundation.

KEE composes existing prior art and adds a governed cross-profile contract for preserving distinctions needed for interoperability.

## What KEE owns — and what it does not

KEE does not claim ownership of the foundational semantic technologies it uses.

Prior art provides much of the underlying machinery, including:

- RDF
- OWL
- SHACL
- PROV-O
- OWL-Time
- SKOS
- SPARQL
- Dublin Core
- related standards and established practices

Domains and specialized profiles own domain-specific knowledge and artifact-specific behavior.

KEE does not define what the concepts of a particular scientific, legal, technical, historical, philosophical, or commercial domain mean.

The KEE family contract owns the published cross-profile obligations required for independently developed profiles to remain interpretable to one another.

KEE framework governance owns the standing of KEE's own normative instruments, including:

- proposals
- accepted decisions
- specifications
- profiles
- releases
- compatibility rules
- migration requirements

## Source neutrality

KEE is source-neutral and consumer-neutral.

The fact that information came from a human, organization, software system, machine process, model, database, or another source does not by itself establish its epistemic standing.

Producer or consumer type may affect requirements concerning:

- provenance
- evidence
- disclosure
- validation
- review
- authority
- governance

But source type alone does not determine whether a claim should be accepted.

## Profiles

KEE uses profiles to specialize the framework for particular kinds of knowledge artifacts, domains, or uses.

Profiles may be:

- Accepted / Normative
- Draft / Non-Normative
- Experimental
- Research-stage

The existence of a profile does not imply that it is normative.

Current profile status is documented in:

[`docs/profiles/README.md`](docs/profiles/README.md)

## Non-collapse rules

KEE defines a set of cross-profile non-collapse obligations.

Their purpose is to prevent independently designed profiles from silently treating meaningfully different concepts as equivalent.

These rules concern areas such as:

- identity
- granularity
- provenance
- time
- evidence
- confidence
- authority
- responsibility
- lifecycle
- supersession
- retrieval
- validity
- governance

The current normative specification defines the binding behavior.

## Conformance

KEE distinguishes five conformance dimensions:

1. structural
2. profile-semantic
3. procedural
4. governance and policy
5. interoperability

Passing structural validation alone does not prove that information is:

- true
- authoritative
- sufficiently evidenced
- procedurally valid
- current
- fully interoperable

Conformance means only what the applicable KEE specification and profile explicitly define.

## Documentation

Full documentation index: [`docs/`](docs/). Conceptual overview and tree diagram: [`docs/CONCEPTS.md`](docs/CONCEPTS.md).

## Current release

**KEE v0.10.0**

Status: **Published Normative Baseline**

KEE v0.10.0 is a backward-compatible minor release.

It carries exactly one conformance-behaviour change: the Section 12.3 accountable-root constraint is enforced as a violation rather than a warning. A grantee that resolves to no accountable person or organization conformed structurally under v0.9.2 and does not conform under v0.10.0. The change is confined to the Authority and Delegation profile, which is Draft / Non-Normative and outside the public normative API. It adds no new normative requirement, KEE-owned semantic term, profile promotion, or Capability Level.

Current normative specification:

[`docs/specs/KEE-Specification-v0.10.0.md`](docs/specs/KEE-Specification-v0.10.0.md)

Public normative API:

[`normative-api/v0.10.0.json`](normative-api/v0.10.0.json)

Release history:

[`CHANGELOG.md`](CHANGELOG.md)

Previous published baseline:

[`docs/specs/KEE-Specification-v0.9.2.md`](docs/specs/KEE-Specification-v0.9.2.md) / [`normative-api/v0.9.2.json`](normative-api/v0.9.2.json)

Published normative releases are immutable historical records.

## Repository purpose

This repository is the public publication surface for KEE.

It contains artifacts intended for:

- public use
- citation
- implementation
- interoperability
- conformance
- long-term reference

Development, research, experiments, release preparation, and other working material may occur outside this repository before publication.

## Persistent identifiers

KEE publishes persistent identifiers under:

`https://w3id.org/kee`

The registration is merged with the W3ID project, and resolution was independently verified on 2026-09-19: every registered path was followed to its final response, and the bytes served were compared against the artifact published here.

The base identifier content-negotiates. Turtle returns the term declarations, JSON-LD or JSON returns the context, and anything else returns this repository:

```
curl -H 'Accept: text/turtle'        https://w3id.org/kee/   # vocab/kee.ttl
curl -H 'Accept: application/ld+json' https://w3id.org/kee/   # context/kee-context.jsonld
```

The concept schemes, the profile identifiers, and the artifact classification each dereference to the file published here — for example `https://w3id.org/kee/artifact` returns `schemas/skos/artifact-types.ttl`.

The identifiers redirect to this repository's default branch, so they serve the current published artifact rather than a pinned version. Cite a release when you need a fixed one.

Starting with v0.10.0, the published term declarations also carry a version-specific identifier (`owl:versionIRI`), meant to keep denoting the release it was minted for even after the unversioned identifier moves on. That redirect is registered separately from the base identifier above and may not yet resolve for every past or current release; an identifier that does resolve may be described as registered, resolvable, and dereferenceable, and no identifier is described as guaranteed-persistent.

## Versioning

KEE follows Semantic Versioning.

- **PATCH** — backward-compatible corrections or consolidations
- **MINOR** — backward-compatible additions or material extensions
- **MAJOR** — incompatible changes to the public normative contract

Published versions are immutable.

KEE is currently pre-1.0.

A future **v1.0.0** will represent a stability decision: that the protected public normative contract is mature enough for long-term downstream reliance.

## Governance discipline

KEE evolves through an evidence-driven process:

**Observation → Evidence / Research → Decision → Specification / Profile → Release**

Prior Art First applies before introducing KEE-owned semantic surfaces.

A core project rule is:

**A KEE term may disappear; its governed obligation may not disappear silently.**

## Project

KEE is maintained by the **KnoEdg** project.

Primary maintainer: **René Yap**

Repository:

https://github.com/KnoEdg/kee

---

**Current baseline: KEE v0.10.0**
