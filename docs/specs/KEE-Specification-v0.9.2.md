# KEE Specification v0.9.2

Status: Published Normative Baseline  
Version: 0.9.2  
Date: 2026-09-18  
SemVer classification: PATCH  
Supersedes as current version identifier: KEE v0.9.1  
Published public API: `normative-api/v0.9.2.json`

---

## 0. Document status and authority

This document is the published KEE v0.9.2 normative baseline and the current version identifier for the KEE public normative contract.

KEE v0.9.2 is a **Semantic Versioning PATCH release**. It consolidates the already-effective normative contract published as v0.9.0 and v0.9.1 into one self-contained document. It adds no new KEE requirement, no new Accepted / Normative profile, no new KEE-owned semantic term, no new Capability Level, and no incompatible conformance behaviour. An implementation conforming to KEE v0.9.1 conforms to KEE v0.9.2 without implementation change.

KEE is a governed application-profile family and interoperability framework for knowledge artifacts. It composes established standards, publishes explicit non-collapse and behavioural rules, maintains only narrowly justified local controlled vocabularies where exact prior art is absent, and provides executable conformance and reference assets.

KEE remains the combined KnoEdg + Eidos framework. KnoEdg and Eidos are architectural responsibility boundaries, not mandatory duplicate semantic layers.

KEE SHALL NOT claim ownership of a distinct foundational ontology, provenance model, temporal model, lifecycle model, authority model, confidence model, evidence model, identity model, scientific-claim model, organizational-memory model, query language, graph model, storage model, canonicalization algorithm, or general profile meta-model when established prior art already supplies the required semantics.

The release control rule is:

> **A KEE term may disappear; its audited obligation may not disappear silently.**

When this specification delegates detail to an Accepted / Normative profile, that profile is part of the applicable normative contract only for implementations that claim conformance to it. Draft shapes, examples, fixtures, validators, or implementation assets MUST NOT acquire normative force merely by existing or executing.

### 0.1 Normative language

The key words MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY, and OPTIONAL are to be interpreted in the sense of RFC 2119 and RFC 8174 when, and only when, they appear in uppercase.

### 0.2 Self-containment

This specification is self-contained. A reader SHALL NOT need any other document to determine the ordinary normative meaning of a KEE obligation stated here.

Where this specification names a repository artifact — a SHACL shape graph in `shacl/`, a SKOS concept scheme in `schemas/skos/`, a JSON Schema in `schemas/json-schema/`, the JSON-LD context in `context/`, the term-declaration document `vocab/kee.ttl`, or the published public-API manifest in `normative-api/` — that artifact is published alongside this specification and is the machine-readable expression of an obligation this document states in prose. The prose controls where the two differ, except where this document explicitly delegates a machine-checkable decision to a named shape.

The shape graphs published here are byte-identical to those the reference validator executes. A shape graph carries a shape-contract version, which Section 15.5 requires status-aware tooling to report.

### 0.3 KEE's role and ownership boundary

KEE v0.9 is a **published, versioned, testable shared contract over prior art**, and **not a semantic foundation**.

The ownership boundary is:

1. **Prior art owns foundational semantics.** KEE does not restate, replace, or shadow what an established standard already defines.
2. **Specialized profiles own domain and artifact-type behaviour.**
3. **The KEE family contract owns the published cross-profile rules** that make independently designed profiles interpretable to one another.
4. **KEE framework governance owns the standing of KEE's own normative instruments** — the distinction between a decision being accepted and its being integrated as a binding requirement.

**No genuinely KEE-specific semantic primitive is claimed.** The class of obligations that would require a KEE-owned semantic surface not supplied by prior art, and not dissolved by publishing the same surface under a neutral name, is empty at this baseline.

### 0.4 What this specification deliberately does not state

**This specification states no count of shared-contract requirements, and no future release may introduce one without new evidence of the kind described below.**

That omission is deliberate and is a statement of this section rather than an oversight. Successive audits of the same frozen evidence set produced materially different counts under differently worded classification predicates. A blind replication of the classification predicate **failed**: independent replicators working from the predicate and a withheld-classification sample agreed with the original audit on roughly half the sampled items, at a chance-corrected agreement well below any threshold that would support publishing a settled figure. A disagreement audit attributed roughly three quarters of the divergence to **discrimination failure** — two parties applying the same named condition to the same quoted evidence and reaching different answers — rather than to under-specification that better drafting could repair.

The figure is therefore carried as a **band**, and that band MUST NOT be narrowed by drafting alone. Narrowing it requires new evidence of a kind that demonstrates the classification predicate can be applied reproducibly by parties who did not author it.

A count, where one is discussed at all, is **evidence for** the role claim in Section 0.3. It is not part of the normative contract, and nothing in `vocab/`, `shacl/`, `schemas/`, `context/` or this document depends on it. A consumer implements the published surfaces named in this specification; it never implements a number.

The emptiness claim in Section 0.3 is a different kind of claim and does not rest on the contested predicate: it is supported by executable demonstrations that reproduced the behaviour using zero KEE-owned terms, and by the concession that the surviving contract survives renaming its publishing body.

### 0.5 Time is a first-class cross-cutting concern

A governed claim may have distinct valid, observation, assertion, recording, publication, review, invalidation, deprecation, supersession and archival times. Relevant temporal roles MUST NOT be silently collapsed into one generic timestamp. Section 14 governs the representation of these roles.

### 0.6 Non-collapse means preserving important distinctions

A non-collapse rule states that two related concepts are not automatically identical, and that an implementation MUST NOT infer one from the other merely because they co-occur, share a label, or are commonly discussed together. Section 7.1 is the normative list.

---

## 1. Scope

KEE defines a governed interoperability framework for systems that compose established knowledge-representation, provenance, temporal, governance, lifecycle, evidence, records, archival, identity, and domain standards into explicit application profiles.

KEE is concerned with the interoperability obligations that arise when independently governed profiles need to exchange, interpret, validate, preserve, or act on knowledge artifacts without relying on private assumptions.

KEE MAY define:

- application and domain profiles;
- shared-dimension ownership rules;
- non-collapse and non-inference rules;
- requirement categories;
- governance and behavioural constraints;
- local controlled vocabularies that pass the admission test in Section 4;
- migration mappings and compatibility rules;
- conformance declarations and layered conformance expectations; and
- executable reference and validation assets.

KEE does not require every profile to use every dimension. Provenance, lifecycle, authority, evidence, confidence, contradiction, promotion, archival, retrieval, temporal, and governance requirements apply according to the requirement categories and profile ownership rules in this specification.

### 1.1 Source and Consumer Neutrality

KEE is source-neutral and consumer-neutral.

Governed knowledge MAY be created, asserted, observed, derived, reviewed, approved, published, maintained, retrieved, or consumed by humans, organizations, software systems, artificial-intelligence systems, instruments, sensors, automated processes, or combinations of these.

KEE MUST NOT assign epistemic privilege or penalty solely on the basis of producer or consumer type.

Producer or consumer type MAY affect applicable provenance, evidence, review, disclosure, validation, assurance, and governance requirements. Different producer types MAY require different supporting metadata: an AI-derived artifact may require model and input provenance; a sensor observation may require calibration metadata; an automated test result may require environment and fixture metadata. These policy differences do not create separate epistemologies and do not determine epistemic standing by themselves.

Source neutrality MUST NOT be interpreted as source blindness. Implementations MUST preserve producer, consumer, activity, model, instrument, process, or workflow metadata when those distinctions are material to the applicable profile or governance policy, and SHALL NOT erase such metadata when it is relevant to provenance, evidence, review, accountability, or governance.

Implementations SHOULD model the epistemic or governance role performed (observer, asserter, generator, deriver, reviewer, approver, publisher, custodian, retriever, consumer, decision-maker) separately from the kind of agent, instrument, system, or process performing that role when both are material.

### 1.2 Implementation independence

A conforming implementation MAY use RDF stores, property graphs, relational databases, document stores, event logs, object stores, search indexes, or hybrid architectures.

Conformance depends on satisfying declared profile obligations and interoperability contracts, not on a particular storage technology or serialization.

---

## 2. Goals

KEE SHALL:

1. compose existing standards before introducing KEE-owned semantic terms;
2. make cross-profile assumptions explicit rather than private to implementations;
3. preserve distinctions that materially affect interoperability;
4. define application-profile obligations separately from foundational prior-art semantics;
5. preserve provenance and historical interpretability at profile-appropriate granularity;
6. support source- and consumer-neutral governance;
7. make profile status, ownership, and conformance claims explicit;
8. support explicit, provenance-preserving migration when terms or mappings change;
9. distinguish structural validation from semantic, procedural, governance, and interoperability conformance; and
10. remain vendor-neutral and implementation-independent.

KEE SHOULD be usable by domain-specific systems including engineering knowledge systems, organizational memory systems, scientific knowledge systems, decision systems, operational governance systems, records systems, and machine-assisted knowledge workflows.

---

## 3. Non-goals

KEE SHALL NOT:

- define a new graph data model, query language, serialization format, canonicalization algorithm, or storage engine;
- replace RDF, OWL, SKOS, SHACL, PROV-O, OWL-Time, SPARQL, Dublin Core Terms, DCAT, or applicable domain standards;
- require blockchain, a specific database, identity provider, DID method, credential system, key-management system, authentication system, or authorization engine;
- become a universal upper ontology or replace domain ontologies;
- treat artificial intelligence as a required implementation mechanism;
- treat producer or consumer type alone as epistemic standing;
- equate SHACL validity with truth, authority, policy authorization, evidence sufficiency, procedural execution, or full KEE conformance; or
- mint KEE-owned semantic terms merely to provide aliases for semantics already supplied by adopted prior art.

Profiles SHALL NOT provide an alternate path around the KEE-owned-term admission test.

---

## 4. Prior Art First and KEE-owned-term admission

### 4.1 Prior Art First

Before proposing a KEE-owned class, predicate, controlled value, semantic wrapper, lifecycle category, confidence category, authority construct, contradiction construct, governance construct, or other semantic surface, the proposer MUST perform and preserve a prior-art review.

The review MUST answer:

1. What observable interoperability or governance obligation is being addressed?
2. Which established standards, vocabularies, profiles, or implementation practices already address it?
3. Can the obligation be satisfied directly by prior art?
4. If not, can ordinary application-profile composition, qualification, mapping, or constraint practice satisfy it?
5. What material gap remains after composition?
6. Why would a shared KEE-owned identifier materially improve interoperability?

A prior-art review MUST preserve relevant source status, edition, and chronology. Later standards convergence MUST NOT be represented as historical influence when it post-dates the KEE decision under review.

### 4.2 KEE-owned-term admission test

A new or retained KEE-owned semantic term is admissible only when all of the following are documented:

1. precise observable obligation;
2. prior-art search;
3. residual gap after direct reuse and ordinary profile composition;
4. material interoperability value;
5. owning profile or normative contract;
6. normative/governance status;
7. external relationships or mappings at the strongest justified mapping strength; and
8. versioning and migration policy.

Failure of a required criterion means the proposal SHOULD use prior art, profile composition, an implementation convention, or an informative alias instead of a new normative KEE-owned term.

The record of these criteria for every retained KEE-owned term is the **term registry** (Section 18.3). A term absent from the registry, or whose registry row fails a criterion, is not admitted; it MAY remain legacy-readable under Section 17 while its retirement or admission is decided.

### 4.3 Local controlled vocabularies

A local controlled vocabulary MAY be retained when the jointly governed value set itself adds interoperability value and no exact external set exists.

Such a vocabulary SHALL have a declared owner, stable identifiers, definitions for each value, open/closed status, normative status, an extension/versioning policy, and external mappings or explanatory references where useful. "Stable identifier" here means a governed, versioned identifier that does not change; where that identifier belongs to a persistent-identifier scheme entry which is not yet registered, Section 18.7 governs what may be claimed about it. Where a value corresponds to established representation prior art, the scheme SHOULD record an explicit mapping or explanatory reference rather than implying KEE invented the representation.

A local controlled vocabulary is not evidence that KEE owns a foundational semantic model for the broader domain.

---

## 5. Architectural composition and profile framework

Established standards supply KEE's foundational semantic and representation capabilities. RDF implementations SHOULD compose applicable standards such as RDF (RDF 1.2 mechanisms where supported and where the implementation records their maturity status), OWL, SKOS, SHACL, PROV-O, OWL-Time, Dublin Core Terms, DCAT, SPARQL, W3C application-profile mechanisms, and appropriate domain standards rather than recreate their semantics. Domain profiles SHOULD use established domain vocabularies where they fit the required meaning.

KnoEdg is the project responsibility boundary for epistemic-governance and organizational-memory concerns. Eidos is the responsibility boundary for entity, agency, sovereignty, intent, identity, responsibility, policy, decision, and continuity concerns. These project boundaries SHALL NOT be interpreted as mandatory KEE-owned ontology layers or as requiring every conforming artifact or profile to instantiate KEE-owned semantic layers for identity, agency, provenance, policy, credentials, time, evidence, or decisions. A conforming profile MAY use suitable external identity, authorization, policy, credential, organizational, or domain mechanisms.

A KEE profile is a constrained, documented composition of adopted standards and explicitly admitted KEE contract material for a defined artifact type, domain, implementation context, or governance capability. Profiles are first-class architectural components.

A profile SHALL declare, as applicable:

- its managed artifact or exchange unit;
- its status and binding effect;
- requirement categories;
- external standards it composes;
- any KEE-owned terms and their admission rationale;
- required non-collapse rules;
- conformance expectations; and
- migration/version constraints.

Accepted / Normative profile rules bind only implementations that claim conformance to that profile, unless the core cross-profile contract independently imposes the same rule.

Stable KEE profile identifiers are profile identities. Their existence does not imply profile maturity or a foundational KEE ontology.

---

## 6. Requirement categories

Normative KEE requirements SHOULD be classified as:

- **universally required** — applies to every implementation or artifact within the stated KEE conformance scope;
- **conditionally required** — becomes mandatory when a declared capability, profile, artifact type, transition, assertion form, governance event, or other condition is present;
- **optional-standardized** — optional to implement, but an implementation that uses the dimension within a KEE conformance claim SHOULD use the adopted standard or owning profile rather than invent an incompatible private representation; or
- **domain-defined** — KEE preserves the distinction or extension point while the domain profile or implementation defines the concrete vocabulary, policy, threshold, state set, authorization rule, calibration method, or ranking method.

### 6.1 Universal requirements

Universal requirements MUST be used sparingly and MUST identify the scope over which they are universal. Examples include declaring the baseline and profiles against which a conformance claim is made and preserving mandatory non-collapse rules when their dimensions are present.

### 6.2 Conditional requirements

The triggering condition of a conditional requirement MUST be explicit and testable or reviewable.

### 6.3 Requirement ownership

A requirement SHALL have a clear normative owner: the core interoperability contract, an Accepted / Normative profile, or an explicitly identified domain/implementation policy.

A requirement SHOULD NOT be duplicated across multiple profiles when one owner can define it and other profiles can reference it.

### 6.4 Ownership of dimensions assigned to Draft profiles

Section 7 assigns several shared dimensions to profiles that are Draft or Draft / Non-Normative at this version. Such an assignment designates the **future owner**. Until the designated profile is Accepted / Normative in the applicable baseline, the owner of record for that dimension is the core interoperability contract, which carries:

- the dimension's non-collapse rules in Section 7.1 and the sections of this specification that address it; and
- the obligation that an implementation using the dimension within a KEE conformance claim declare its own vocabulary, policy, and structural contract for it.

Claiming a Draft profile does not create binding effect (Section 15); it records which designated contract the implementation intends to follow.

---

## 7. Cross-profile interoperability contract

This section is the normative architectural centre for shared KEE interoperability obligations.

### 7.0 Shared-dimension ownership rules

| Dimension | Primary normative owner | Requirement category | Core composition rule |
|---|---|---|---|
| Managed identity and granularity | Artifact-specific profile; Artifact Identity and Granularity Profile when claimed | Conditional | Identify the managed unit before attaching governed metadata; do not assume artifact, version, occurrence, container, and retrieval chunk are identical. |
| Assertion metadata attachment | Assertion/Assertion Metadata profile when claimed | Conditional | Reuse the owning assertion metadata contract rather than redefine generic provenance, scope, confidence, or managed-unit metadata. |
| Provenance | Adopted PROV-O/DCTerms composition plus owning profile | Conditional | Keep origin/derivation/attribution separate from authority, evidence, confidence, lifecycle, and correctness. |
| Temporal qualification | Owning artifact/profile temporal rules; Historical/Bitemporal Querying Profile when claimed | Conditional | Distinguish relevant temporal dimensions rather than collapsing them into one timestamp. |
| Lifecycle/status | Artifact-specific profile | Conditional | The artifact profile owns its lifecycle/status vocabulary; crosswalks map but do not impose one universal state machine. |
| Governance transition history | Governance Transition Profile when claimed | Conditional | Governed state-changing acts are provenance-bearing events/records, not mere final-state labels. |
| Authority/delegation | Authority and Delegation Profile or domain policy | Conditional | Record authorization basis separately from provenance and identity. |
| Responsibility/accountability | Authority/delegation profile plus provenance association | Conditional | Responsibility is not authority, authorship, trust, confidence, or correctness. |
| Confidence/uncertainty | Artifact/domain profile | Optional-standardized / domain-defined | KEE defines no universal numeric confidence scale, propagation model, or decay formula. |
| Evidence type/strength | Scientific/domain evidence profile | Conditional when evidence semantics are claimed | Evidence item/type/strength remain distinct from confidence, provenance, authority, lifecycle, and replication. |
| Contradiction/challenge | Contradiction Records Profile when claimed | Conditional | Preserve competing assertions without automatically inferring error, falsehood, rejection, or lifecycle change. |
| Promotion/scope expansion | Promotion Profile when claimed | Conditional | Promotion is a governed scope expansion, not popularity, truth, confidence, authority, or mere reuse. |
| Scope/context | Artifact/domain profile | Conditional | Scope constrains applicability; context constrains interpretation; neither is proxied through confidence, lifecycle, or authority. |
| Retention/review/archival | Organizational Memory and applicable artifact profiles | Conditional | Preservation or archival does not imply current validity, endorsement, or operational applicability. |
| Retrieval behaviour | Consumer profile or implementation policy | Optional-standardized | Retrieval eligibility is consumer behaviour/derived policy, not a universal lifecycle state or truth score. |
| Historical query sufficiency | Historical/Bitemporal Querying Profile or implementation | Conditional when claimed | Query executability does not prove retained-history completeness. |
| Structural validation | Applicable profile shape/schema | Conditional | Structural validity is not proof of semantic truth, process execution, authority, or full conformance. |
| Conformance declaration | Core specification/profile framework | Universal where conformance is claimed | Declare the baseline and profiles claimed; do not infer conformance from vocabulary use or file format. |

Section 6.4 applies to every owner listed as "when claimed" whose profile is not Accepted / Normative.

### 7.1 Core non-collapse rules

A conforming implementation MUST preserve the following distinctions whenever both sides are represented or material to the claimed profile.

Each rule carries a stable identifier `NC-01` through `NC-17`. The identifiers are a naming surface for tooling and evidence; they add no obligation, and an artifact that does not use them is not thereby non-conforming.

| ID | Rule |
|---|---|
| NC-01 | **identity vs. provenance** — what is referenced is separate from where it came from |
| NC-02 | **provenance vs. authority** — participation or attribution does not prove authorization |
| NC-03 | **authority vs. responsibility** — permission is separate from accountability |
| NC-04 | **authority vs. correctness** — authorized decisions may still be wrong, contested, or superseded |
| NC-05 | **confidence vs. evidence strength** — assessment is separate from evidential basis |
| NC-06 | **confidence vs. trust** — content assessment is separate from reliance on a source, credential, institution, or process |
| NC-07 | **lifecycle/status vs. epistemic standing** — workflow, publication, archival, or lifecycle state is not automatically truth, falsity, support, or refutation |
| NC-08 | **contradiction vs. logical inconsistency** — disagreement may arise from context, time, evidence, interpretation, scope, or genuine inconsistency |
| NC-09 | **promotion vs. popularity** — broader standing requires the governing promotion conditions, not mere reuse or retrieval frequency |
| NC-10 | **record preservation vs. current applicability** — retention does not imply current operational use or validity |
| NC-11 | **retrieval relevance vs. validity** — a query match does not establish currency, authority, evidence quality, or truth |
| NC-12 | **structural validation vs. full conformance** — shape/schema success does not establish procedural, governance, semantic, epistemic, or policy correctness |
| NC-13 | **producer/consumer type vs. epistemic standing** — human, AI, software, organization, sensor, instrument, or hybrid type alone cannot establish privilege or penalty |
| NC-14 | **accepted decision vs. specification integration** — an architectural decision and an integrated normative requirement are distinct governance states |
| NC-15 | **scope vs. context** — applicability and interpretation remain separate |
| NC-16 | **query executability vs. retained-history completeness** — an executable query may still lack adequate retained history |
| NC-17 | **retrieval exclusion vs. source/history deletion** — a consumer decision does not remove source or history |

A profile MAY add stricter non-collapse rules. It MUST NOT weaken a core rule without an accepted superseding architecture decision.

### 7.2 Identity is not authority

A KEE implementation MUST NOT assume that identity alone implies authority. Identity answers who or what a thing is; authority answers what that thing is recognized or permitted to do within a scope and on a declared basis (Section 12).

### 7.3 Source and Consumer Neutrality conformance

A conforming implementation:

- MUST NOT privilege or disqualify a knowledge artifact solely because of producer or consumer type;
- MUST evaluate governed artifacts through the applicable profile dimensions (provenance, evidence, authority, scope, context, temporal state, confidence, lifecycle, contradiction, governance) rather than producer type alone;
- MAY impose source- or process-specific provenance, evidence, disclosure, review, assurance, or accountability requirements; and
- SHOULD model role separately from actor/system/instrument type when both are material.

The AI-Grounded Retrieval Profile remains optional and consumer-specific. It does not alter the source-neutral core model, is not required for non-AI implementations, and MUST NOT be interpreted as making AI a privileged producer or consumer class within KEE.

### 7.4 Governance definition

Governance is the allocation and exercise of decision rights, responsibilities, rules, processes, authorities, constraints, accountability mechanisms, challenge mechanisms, and controls by which governed artifacts are created, reviewed, challenged, accepted, used, revised, promoted, deprecated, superseded, archived, or retired.

KEE distinguishes:

1. **Project and specification governance** — how the KEE specification, decisions, profiles, and conformance assets change.
2. **Epistemic governance** — how governed knowledge artifacts and their standing are created, evaluated, challenged, transitioned, and retained.
3. **Domain or implementation governance** — policies and decision rights established by a conforming organization, system, or application.

---

## 8. Canonical semantic carriers and migration

### 8.1 Profile conformance

New serialization MUST use `dcterms:conformsTo` for resource-to-specification/profile conformance declarations. Legacy `kee:profileConformance` remains readable only under the published compatibility policy.

The semantic obligation is unchanged by the carrier: a conformance claim MUST identify the specification/profile being claimed. Vocabulary use or file format alone MUST NOT be interpreted as proof of conformance.

Profile hierarchy or dependency SHOULD use established application-profile mechanisms such as the W3C Profiles Vocabulary (a Working Group Note, not a Recommendation; Section 23) where appropriate. KEE profile identifiers MAY remain stable KEE-owned identifiers; adopting `dcterms:conformsTo` does not require replacing them.

### 8.2 Controlled artifact classification

New serialization MUST use `dcterms:type` where a controlled artifact classification value is intended. RDF `rdf:type` remains class membership. `kee:artifactType` is legacy-readable compatibility input, not the canonical new-write carrier.

A resource MAY carry both an RDF class via `rdf:type` and a controlled classification via `dcterms:type`. When both are present, implementations MUST NOT assume the class IRI and the classification-value IRI are identical merely because labels are similar.

The canonical KEE artifact-classification value namespace is `https://w3id.org/kee/artifact#`. Its values are SKOS concepts. Implementations SHOULD load the DCMI Metadata Terms edition of 2020-01-20 or later; the 2012-06-14 edition declared `rdfs:range rdfs:Class` on `dcterms:type`, under which RDFS entailment would type every classification value as a class (Section 23).

### 8.3 Replacement and revision

New serialization MUST NOT use `kee:supersedes` or `kee:supersededBy`.

Use the adopted prior-art relations according to meaning:

- `dcterms:replaces` — direct replacement of an older resource by a newer resource;
- `dcterms:isReplacedBy` — inverse direct replacement direction; and
- `prov:wasRevisionOf` — revision lineage (a sub-property of `prov:wasDerivedFrom`) where revision, rather than generic replacement, is the intended relation.

They MUST NOT be treated as exact synonyms. Implementations MUST preserve the intended relationship semantics.

Because the historical `kee:supersedes` covered replacement, revision, update, correction, and succession, its registered mapping to `dcterms:replaces` is **close-approximate, not exact** (Section 17.2). Automatic rewrite is permitted only where the source record demonstrably meant direct replacement.

A terminal replacement-chain target is a derived result, not a direct replacement relation. Implementations SHOULD compute it through query/property-path traversal over authoritative replacement relations. If materialized (for example as legacy `kee:supersessionChainTarget`), it MUST NOT be interpreted as a direct replacement assertion, SHOULD be derivable from the retained replacement chain, SHOULD carry or be associated with sufficient provenance to identify the computation step when operationally material, and MUST NOT erase intermediate replacement history.

### 8.4 Record wrappers

Record-wrapper classes such as GovernanceTransitionRecord, ContradictionRecord, RetrievalResult, PointInTimeQuery, AuthorityRecord, AssertionMetadataRecord, and similar profile records are profile-local convenience identities, not foundational ontology machinery.

A profile retaining such a wrapper MUST document the prior-art components it composes, the observable obligation it packages, and whether equivalent structure plus an explicit conformance declaration may satisfy the profile without the exact wrapper class. A wrapper class MUST NOT be treated as evidence that KEE owns the underlying provenance, temporal, authority, evidence, retrieval, contradiction, or lifecycle semantics.

---

## 9. Lifecycle, review, archival, and mapping

### 9.1 No universal lifecycle axis

KEE MUST NOT define one universal lifecycle/status axis that combines distinct semantic dimensions merely because their values are commonly called "status".

At minimum, implementations MUST keep conceptually independent:

- workflow/lifecycle state;
- publication state;
- review/currency state;
- archival/disposition state;
- epistemic/evidential standing;
- ranking/preference standing; and
- replication state where applicable.

A profile MAY combine dimensions only when it explicitly documents the hybrid model and its interoperability consequences. Mere co-location in one vocabulary or similarity of labels is insufficient.

### 9.2 Profile ownership of lifecycle state

A profile that requires lifecycle state MUST own or explicitly adopt: the state vocabulary; the meaning of each state; transition constraints, if any; the semantic dimension represented by the state; mapping/crosswalk behaviour; and history/provenance requirements for transitions.

`kee:lifecycleState` is a retained profile-level carrier. Its value MUST be interpreted through the governing profile or declared lifecycle vocabulary. It MUST NOT be treated as a universal KEE state machine.

Profile-specific lifecycle schemes are authoritative for new writes. The historical generic `https://w3id.org/kee/lifecycle#` namespace is compatibility-only where registered. New writes MUST NOT mint or rely on generic lifecycle values where a profile-specific scheme owns the state dimension.

Canonical profile-specific lifecycle namespaces are:

- `https://w3id.org/kee/lifecycle/assertion#`;
- `https://w3id.org/kee/lifecycle/scientific-claim#`;
- `https://w3id.org/kee/lifecycle/organizational-memory#`;
- `https://w3id.org/kee/lifecycle/decision#`; and
- `https://w3id.org/kee/lifecycle/software-engineering#`.

Registration status of these namespaces is governed by Section 18.7; they are described as stable only once they dereference.

Mappings from legacy generic values to profile-specific concepts MUST be explicit and profile-qualified. A generic value such as `lifecycle:Active` MUST NOT be assumed to have one universal exact meaning across profiles.

### 9.3 Axis separations for the lifecycle-owning profiles

The Scientific Claim lifecycle scheme MUST NOT use `Supported`, `Qualified`, or `Challenged` as values on the same single lifecycle axis as publication/disposition states. The scheme is limited to publication/governance/disposition progression (Hypothesis, Submitted, Preprint, Published, Corrected, Retracted, Superseded, Archived). Support, challenge, qualification, and replication are represented by the profile's evidence, contradiction, confidence/assessment, qualification, and replication structures. A claim MAY be simultaneously Published and supported, or Published and challenged, without violating lifecycle cardinality.

The Assertion lifecycle scheme MUST NOT use `Preferred`, `Challenged`, or `Qualified` as values on the same lifecycle axis as lifecycle/disposition states. The scheme is limited to Proposed, Normal, Deprecated, Superseded, Rejected, Withdrawn, and Archived. Preference/ranking remains profile/application policy; challenge is represented through contradiction/dispute structures; qualification through explicit caveats, scope/context, evidence, or profile-defined assessment. Assertion lifecycle/disposition state MUST remain distinct from ranking, dispute, review, or qualification standing.

The Organizational Memory lifecycle scheme MUST NOT use `Under Review`, `Qualified`, or `Stale` as values on the same lifecycle axis as lifecycle/disposition states. The scheme is limited to Draft, Active, Deprecated, Superseded, Retired, and Archived. Review/currency assessment MAY use review timestamps, review-due policy, provenance, explicit profile-defined assessment, or other declared mechanisms. A stale artifact MUST NOT be inferred false merely because it is stale. An archived artifact MUST NOT be inferred currently applicable merely because it is preserved.

Validators SHOULD reject known legacy mixed-axis values where the active profile now defines them as another semantic dimension. `shacl/lifecycle-status-constraints.ttl` does so for the three schemes above, composed with the lifecycle-owning profile shapes (Section 17.4).

### 9.4 Crosswalks

Crosswalks MUST use explicit source vocabulary, target vocabulary, source term, target term, mapping relation, scope/context, provenance, and rationale as applicable. Examples based only on label resemblance, such as `Accepted ~= Approved ~= Published ~= Stable ~= Baselined`, MUST NOT be treated as semantic equivalence.

For Lifecycle Crosswalk new writes, the supported mapping relations are `skos:exactMatch`, `skos:closeMatch`, `skos:broadMatch`, `skos:narrowMatch`, and `skos:relatedMatch`, used according to documented meaning. `skos:exactMatch` MUST NOT be inferred from similar labels alone, and a producer MUST NOT upgrade a close, broad, narrow, or related mapping to exact merely because labels resemble one another.

The review state of a mapping record is itself a profile-owned governance dimension and MUST NOT be confused with the lifecycle states being mapped.

---

## 10. Local controlled vocabularies

KEE retains narrowly justified local vocabularies where the shared identifiers themselves add interoperability value.

The contradiction-cause scheme uses `https://w3id.org/kee/vocab/contradiction-cause#`. The canonical scheme MUST provide stable identifiers, definitions, version metadata, an extension policy, and explicit external mappings where justified. `kee:causeType` remains an open IRI-valued slot: implementations MAY use the canonical KEE scheme or another declared profile/domain taxonomy, and KEE conformance MUST NOT require the local scheme when another profile-declared vocabulary preserves the same obligation.

The managed assertion-unit-kind scheme uses `https://w3id.org/kee/vocab/assertion-unit-kind#`. Its initial values cover RDF triple / RDF-star triple term, reifier/reified statement, statement node, named graph, nanopublication assertion graph, document assertion, and application claim object. The slot MUST remain open; implementations MAY use additional IRIs for representation patterns not enumerated by KEE. Where a kind corresponds to established representation prior art, the scheme SHOULD record an explicit mapping or explanatory reference.

The generic confidence-status scheme is Informative / Non-Normative. Values such as Low, Moderate, and High MUST NOT be treated as interoperable confidence semantics without a profile-defined interpretation contract. The confidence-interpretation sentinel `confidence:ProfileDefined` indicates that interpretation belongs to the applicable profile; it is canonicalized in a scheme that holds no confidence level, and it is not itself a confidence level. The illustrative Low/Moderate/High labels remain registered legacy.

A declared namespace prefix is only a serialization convenience. It is not evidence that KEE publishes a governed vocabulary at that namespace. The registration and resolution status of the namespaces named in this section is governed by Section 18.7; at this baseline they are canonical for new writes but unregistered and non-resolvable. The canonical JSON-LD context and active SHACL assets MUST avoid unused KEE-owned namespace declarations where practical; in particular, `governance#` and `contradiction#` MUST NOT be presented as current governed vocabulary families unless concrete canonical terms are actually defined there.

The Governance Action Type scheme and its concepts are **retired** (`deprecated-without-direct-replacement`), and `kee:managedUnit` is **retired** (`exact-replacement` to `kee:managedAssertionUnit`). All retired surfaces remain declared and readable under Section 17.

---

## 11. Confidence, evidence, and replication

KEE defines no universal confidence scale, propagation model, calibration model, aggregation model, or cross-domain confidence interpretation.

A profile that uses confidence MUST define enough semantics for a consumer to interpret the representation it accepts or emits. A profile that permits a confidence value, label, category, probability, score, interval, or other confidence representation MUST declare, as applicable: its value type and permitted scale/range or vocabulary; the interpretation of the value; the assignment or estimation method; the assigning agent, software process, or other responsible process; the assignment time and any validity interval or temporal interpretation; how evidence relates to the confidence assessment; calibration or aggregation rules when relevant; and revision, supersession, decay, or re-assessment behaviour when relevant.

A bare numeric value or unqualified label MAY be structurally valid but MUST NOT be treated as semantically interoperable confidence merely because it passes datatype or vocabulary validation. A consumer MUST evaluate the declared profile's interpretation contract where the profile requires one.

Absence of a confidence assertion MUST NOT, by itself, be interpreted as low confidence, negative confidence, rejection, falsity, or lack of support.

Confidence MUST remain distinct from provenance, authority, trust, evidence strength, lifecycle/publication state, popularity, source reputation, SHACL severity, and an uncalibrated model score.

The base KEE Scientific Claim SHACL shape MUST NOT impose a universal `[0,1]` range on `kee:confidenceValue`. Profiles that choose a bounded scale MAY impose their own range constraints.

Evidence is not provenance. Evidence strength is not confidence. Profiles SHOULD use ECO, SEPIO, GRADE, another appropriate domain evidence model, or a declared profile/domain vocabulary when generic links are insufficient. KEE's normative role is the profile composition and interoperability boundary: a profile declares which evidence model or vocabulary it uses, how evidence bears on the managed claim/assertion, and how evidence-specific assessment relates to confidence and provenance. `kee:evidenceStrength` MAY remain readable as a profile convenience/compatibility slot; its presence does not establish a KEE-owned evidence-strength semantics and it MUST remain open to externally defined IRI values.

Replication attempts and outcomes are evidence/scientific-assessment structures independent of publication/governance lifecycle. A summarized replication status, if used, is profile-defined, MUST NOT be inferred solely from publication/governance lifecycle, MUST NOT replace the underlying replication evidence when the claimed profile requires it, and MUST remain a separate dimension from lifecycle state.

---

## 12. Authority and delegation

### 12.1 Delegation and authorization evidence

`prov:actedOnBehalfOf` is an Agent-to-Agent delegation relation: the delegate Agent is the subject and the responsible/delegating Agent is the object. AuthorityRecord resources MUST NOT use it in a way that entails that the record itself is a PROV Agent. A profile MAY additionally use `prov:qualifiedDelegation` or another declared authorization/grant representation when qualification is required.

Provenance does not authorize. PROV participation or history does not by itself authorize an action. A profile asserting authority MUST distinguish: the agent and role/capacity involved; the authorization basis (policy, grant, credential, capability, charter, organizational record, workflow decision, or other declared authority evidence); the authority scope, action, and target/resource semantics required by that profile; validity, expiration, and revocation where applicable; and provenance of the grant, record, and governed action.

`prov:wasAttributedTo`, `prov:wasAssociatedWith`, `prov:qualifiedAssociation`, generation history, authorship, contribution, or derivation MUST NOT be interpreted as authorization merely because they identify an agent.

### 12.2 Scope, expiration, and revocation

Authority scope and artifact applicability scope are separate claims even when they use the same value vocabulary or reference the same contextual resource. Profiles MUST represent them separately; value equality by itself MUST NOT collapse the two meanings. Worked examples and fixtures SHOULD demonstrate the distinction with visibly different values where practical so that implementers do not infer equivalence from example reuse.

Expiration (the automatic end of a grant's stated validity period) and revocation (a later governance act or invalidation that withdraws previously granted authority) are distinct authority-ending mechanisms. A grant MAY expire without being revoked, MAY be revoked before its scheduled expiration, or MAY have neither event. Revocation MUST preserve the original grant/assignment history; a revocation event MUST NOT erase the fact that authority was previously granted or exercised. Profiles that record both validity end and revocation MUST keep their semantics separately queryable.

### 12.3 Accountable root for non-person agents

Any agent receiving governance authority that does not itself resolve to an accountable `prov:Person` or `prov:Organization` MUST resolve through the declared delegation/authorization chain to such a root. Absence of a `prov:SoftwareAgent` (or any other) type assertion does not exempt an agent from this obligation; the Authority and Delegation shape evaluates the chain for every grantee that is not typed as a Person or Organization.

A boolean advisory assertion such as `kee:softwareAgentNonSovereign` does not establish this invariant and MUST NOT be treated as sufficient conformance evidence; it remains legacy-readable advisory metadata with no conformance effect.

A direct grant to a person or organization satisfies the root requirement without an intervening delegation hop. For a delegated chain, the accountable root is the terminal person or organization for the chain being evaluated.

This obligation is normative at this baseline. The reference shape reports it at `sh:Warning` severity, so that data which was structurally valid under an earlier baseline does not become structurally invalid without a release that says so. Escalation to `sh:Violation` requires a MINOR release that declares the change; this PATCH release does not make it, and the outstanding escalation is recorded in Section 24. An implementation claiming the Authority and Delegation profile SHOULD treat the warning as a defect to be corrected before that release.

### 12.4 Explicit pairing

Flat repeated agent, role, and evidence properties MUST NOT be relied upon when their intended pairings would be ambiguous. An authority-grant activity SHOULD use PROV qualified association or an equivalent explicit pairing structure; where `prov:qualifiedAssociation` is used, each association identifies its agent with `prov:agent` and its role/capacity with `prov:hadRole`. If different agents or roles rely on different authority evidence, the profile MUST make those pairings explicit. A consumer MUST NOT infer which role or authority basis belongs to which agent solely from parallel repeated flat properties. Qualified association is not the only conforming representation; another profile-declared explicit pairing structure is permitted.

### 12.5 Structural validation is not authorization

Structural validation does not establish legal validity, enforceable runtime authorization, correctness, exclusivity, or trust. A profile or implementation that needs enforceable permission decisions MUST compose an appropriate policy/authorization mechanism outside the structural profile.

---

## 13. Contradiction and promotion

### 13.1 Contradiction

A contradiction representation that cites evidence for multiple conflicting sides MUST make each evidence-to-side pairing mechanically identifiable. Flat repeated `kee:evidenceForSide` values are insufficient when pairing is ambiguous; the legacy predicate remains readable but does not by itself satisfy the pairing obligation when more than one side/evidence relation is present. Composition from existing annotation, evidence-line, or argument-position structures is preferred; a profile MAY use another explicit representation, but consumers MUST NOT infer pairing from parallel repeated lists.

Contradiction is not resolution or lifecycle disposition. Conflict detection, contradiction review, resolution/disposition, deprecation, rejection, supersession, withdrawal, and lifecycle change are separate facts or events. Recording conflict MUST NOT by itself imply rejection, deprecation, supersession, withdrawal, deletion, or another disposition of either side. A later resolution/disposition MUST be separately represented, through a governance transition, resolution record, or equivalent profile-declared event/record with its own provenance; a link such as `kee:resolutionOutcome` MAY connect the contradiction record to that separate record, and the contradiction relation and its history remain preserved.

### 13.2 Promotion

Promotion means an authorized, deliberate governance transition that expands the applicability scope of a governed artifact. Promotion does not mean stronger authority, greater popularity, usage, adoption, retrieval frequency or reuse, higher confidence or epistemic standing, a lifecycle change by itself, or merely a different scope value. Authority changes remain authority/governance transitions; epistemic standing changes remain assessment or other profile-owned transitions; popularity and adoption remain signals/evidence unless an authorized promotion decision uses them as inputs.

A promotion record MUST NOT conform merely because source and target scopes are different. The applicable profile/domain MUST declare a machine-checkable scope ordering relation or decision procedure demonstrating that the target scope is broader than the source scope: for example a declared SKOS broader/narrower hierarchy, a containment relation over organizational, geographic, jurisdictional, audience, or applicability scopes, another profile-declared partial order, or a deterministic decision procedure with equivalent behaviour. The ordering mechanism is profile/domain-owned; KEE defines no universal scope lattice. A narrowing, incomparable scope change, equal scopes, or a mere unequal pair MUST NOT be classified as Promotion, and **an ordering that is cyclic between source and target cannot demonstrate breadth**.

`shacl/promotion-profile.ttl` implements the cyclic case: a `skos:broader` ordering in which `kee:sourceScope` and `kee:scope` are mutually broader is rejected. A record whose scopes are related only by such a cycle does not conform to the Promotion shape.

Promotion MUST NOT suppress, erase, hide, or silently detach known contradictions associated with the source artifact, and does not resolve a contradiction merely by broadening scope. This is a procedural obligation; structural validation of a supplied `kee:knownContradiction` link cannot prove that every known contradiction was carried forward. Executable conformance evidence MUST detect omission where the applicable procedure requires carry-forward.

Executable coverage for a Promotion contract MUST prove at minimum that scope narrowing is not Promotion; that popularity, usage count, adoption, retrieval frequency, or reuse alone cannot establish Promotion; that an unauthorized promotion fails the applicable contract; and that suppression or omission of a known contradiction is detected.

---

## 14. Temporal, history, and retrieval semantics

### 14.1 Temporal roles

The historical `kee:assertionTime` predicate is legacy-readable but MUST NOT be used for new writes as an ambiguous catch-all. A consumer MUST NOT infer whether a legacy value means assertion time or valid time without additional profile/context evidence.

RDF implementations SHOULD use role-specific prior art instead:

- `prov:generatedAtTime` on an assertion-metadata record means when that record was generated/recorded (note PROV-O erratum o-5: this property has no PROV-DM equivalent; profiles that require cross-serialization portability SHOULD use `prov:qualifiedGeneration` with `prov:atTime`);
- when the act of asserting itself must be timed, model the asserting act as a `prov:Activity` and use `prov:startedAtTime` / `prov:endedAtTime` as appropriate;
- valid/applicability time SHOULD use `dcterms:valid` (a literal-valued property) for simple cases or OWL-Time resources/relations for explicit instants and intervals; and
- observation, publication, review, invalidation, deprecation, supersession, and archival time remain separately owned by the applicable profile/domain semantics.

No replacement KEE predicate is introduced because prior-art temporal/provenance terms cover the corrected roles.

### 14.2 Historical query intent

A historical/point-in-time query record MUST make query intent mechanically identifiable independently of its execution language. It MUST declare:

1. the requested temporal target — an instant or interval;
2. exactly one time dimension identifying what that temporal target means, including at least valid/active-at versus transaction/known-as-of semantics where those modes are supported;
3. the query pattern/capability being requested; and
4. the history source/coverage assumptions against which the answer is evaluated.

SPARQL, SQL, Cypher, APIs, event projections, Memento access, and similar mechanisms are execution mechanisms; they do not by themselves define semantic query intent. In the RDF reference representation, `dcterms:temporal` identifies the requested OWL-Time instant or interval, `kee:queryTimeDimension` and `kee:queryPattern` are the profile-owned open classifiers, and `dcterms:source` identifies the history/dataset source whose temporal coverage is asserted separately. Legacy `kee:queryInstant` remains readable but is not the new-write representation.

### 14.3 Query capability is not history sufficiency

Query executability is not evidence that retained history is sufficient. A system MUST NOT report a point-in-time answer as complete merely because its query engine can express or execute the requested pattern.

The history source used by a historical query MUST expose temporal coverage sufficient to evaluate whether the requested instant/interval falls within the retained history relevant to that query. RDF implementations SHOULD use established dataset/resource coverage metadata such as `dcterms:temporal` and OWL-Time resources where sufficient. Legacy `kee:historyCompleteness` may remain readable as an advisory assertion but MUST NOT substitute for actual coverage evidence.

Conformance evidence MUST include a procedural case where a syntactically valid point-in-time query is executable but the retained history does not cover the requested time; that case MUST be reported as history-insufficient rather than as a complete historical answer.

### 14.4 AI retrieval time semantics

`prov:generatedAtTime` on a retrieval query or result means when that retrieval resource was generated. It does not encode the historical instant being requested and does not distinguish valid-time from transaction-time intent. AI/RAG answer-generation time is not historical query time.

When an AI/RAG retrieval operation asks a historical question, the retrieval record MUST compose with the Historical/Bitemporal Querying Profile (Section 6.4 applies while that profile is Draft) or an equivalent explicit query-intent representation. In the RDF reference representation, a retrieval query MAY use `dcterms:references` to identify the associated point-in-time query record. A current/non-historical retrieval query does not need a point-in-time query record merely because it has an answer-generation timestamp.

### 14.5 Retrieval eligibility

Retrieval eligibility is a decision about one consumer/use operation. It MUST NOT mutate or silently redefine source truth, lifecycle state, authority, validity, identity, existence, or retained history. Exclusion from a current-answer grounding operation does not delete the artifact and does not make it universally unqueryable.

A retrieval decision record MUST make explicit: the governed artifact/result being evaluated; the consumer or use context for which eligibility was decided; the eligibility result/category; the decision basis; decision provenance and decision time; and warning/review routing when the applicable eligibility policy requires them.

Retrieval conformance evidence MUST go beyond declarative field presence. Executable tests MUST demonstrate at minimum that the declared eligibility basis materially affects the decision outcome; that warning/review requirements are triggered by the applicable eligibility category/policy; that exclusion from current-answer grounding does not delete the source artifact or its history; and that citation precision is no finer than the governed/indexed unit actually mapped by the retrieval system.

### 14.6 Query capabilities, not a query language

KEE defines query capabilities, not a KEE query language. Implementations MAY use SPARQL, SQL, Cypher, GraphQL, APIs, event projections, search services, or other mechanisms.

Implementations SHOULD support operationally equivalent queries for: artifact by identifier; artifact provenance; artifact lifecycle state and state history; artifacts active at a point in time; artifacts valid during an interval; deprecated artifacts and reasons; supersession chains; contradictions involving an artifact; artifacts by authority; artifacts by scope and context; artifacts pending or due for review; and confidence-related queries when the applicable profile implements confidence.

A system claiming an operational capability MUST be able to demonstrate the behaviour; storing equivalent metadata alone is not sufficient.

---

## 15. Conformance framework

### 15.1 Conformance declaration

A conformance claim MUST use `dcterms:conformsTo` for new writes. A KEE conformance declaration MUST identify:

- the KEE specification baseline claimed;
- each Accepted / Normative profile claimed (and any Draft profile the implementation intends to follow, without binding effect);
- representation or serialization assumptions material to interoperability;
- applicable validation/conformance assets; and
- known implementation-policy dependencies or limitations that affect interpretation of the claim.

### 15.2 Conformance dimensions

KEE reports conformance as separate dimensions rather than one PASS/FAIL label:

| Dimension | Machine-safe token | Meaning |
|---|---|---|
| structural | `structural` | machine-checkable representation constraints such as SHACL/JSON Schema |
| profile-semantic | `profile-semantic` | profile-specific meaning/non-collapse obligations not reducible to field presence |
| procedural | `procedural` | required behaviours, transitions, preservation rules, or decision procedures |
| governance/policy | `governance-policy` | authority, review, approval, policy, or other governance obligations |
| interoperability | `interoperability` | exchange/consumer behaviour across independently implemented systems or representations |

The human label `governance/policy` and the machine-safe token `governance-policy` are both accepted. The human spelling is **not** deprecated, and historical declarations using it MUST NOT be rewritten.

A structural PASS MUST NOT be reported as proof of the other four dimensions unless they were separately evaluated. An implementation MAY report a dimension as `passed`, `failed`, `not-tested`, or `not-applicable` where the applicable profile defines that outcome.

### 15.3 Capability Levels

The Level 0-4 ladder is retained only as Capability Levels (Section 22): cumulative packaging of implementation capabilities. Capability Level and conformance dimensions are independent axes. A system MUST NOT describe Level 0-4 as the sole KEE conformance result and MUST NOT infer that a higher Capability Level proves all five conformance dimensions. Implementations MAY instead publish explicit capability declarations.

### 15.4 Declaration status

The JSON declaration-maturity field is `declarationStatus` (values `experimental`, `partial`, `conformant`, `extended`), not the historical ambiguous `conformanceLevel` field, for new writes. It describes declared support maturity; it is neither a Capability Level nor a five-dimension conformance result. Legacy documents using `conformanceLevel` remain migration inputs.

### 15.5 Status-aware tooling

Reference validation/conformance tooling MUST report, for each evaluated fixture/profile pairing: profile identity; profile governance status; shape or shape-contract version; structural result; whether the result has normative effect for the evaluated conformance claim; and which of the five conformance dimensions were not tested by that validation action. `structural = passed` is a scoped statement about structural validation only; a Draft or Non-Normative profile may structurally pass while `normative_effect = false`. Reference tooling MUST make the claim-scoped binding distinction (Section 15.6) explicit in status-aware output.

### 15.6 Validator composition and claim-scoped binding

A producer MUST NOT be required to duplicate RDF type assertions solely because a validator runs without inference. Where one KEE profile is a specialization of another, the validation layer MUST compose the applicable parent and specialized constraints explicitly; Promotion and Authority/Delegation validation MUST apply Governance Transition parent constraints to records typed only as their specialized record class.

A profile has binding normative effect for a result only when the profile is Accepted / Normative in the applicable baseline and the implementation/resource actually claims conformance to it. The existence of a profile IRI, profile document, SHACL file, example, fixture, manifest entry, or successful structural validation does not by itself create normative force.

### 15.7 Independent interoperability evidence

A **new profile promotion or graduation claim** MUST be supported by independent interoperability evidence.

Reference self-roundtrip is insufficient: a producer and a consumer that share an implementation demonstrate that the implementation is self-consistent, not that the contract is interoperable. Evidence MUST come from at least two independently implemented producers/consumers, or from one implementation independent of the KEE reference assets.

This requirement applies to promotion and graduation claims made at or after this baseline. It is **not** retroactive: an existing conformance claim does not become non-conforming for want of it.

---

## 16. Domain-profile contracts

### 16.1 Software Engineering

The Software Engineering Profile is Accepted / Normative. Its profile and executable assets MUST NOT describe that contract as a Working Draft or leave resolved design questions described as open.

Generic DCTerms links are permitted fallbacks. When relationship kind materially affects machine-queryable behaviour, implementations SHOULD use established domain prior art/identifiers such as OSLC Requirements Management relations, W3C Trace Context identifiers or durable trace links, Package-URL, SPDX/CycloneDX, OSV, and platform-canonical source URLs or SWHIDs rather than minting new KEE predicates (editions in Section 23).

A generic `dcterms:relation` MUST NOT be interpreted as carrying a more specific relation unless that relation is actually declared.

### 16.2 Organizational Memory

The Organizational Memory Profile is Draft unless separately promoted.

Its residual contract centres on stewardship and review, not a universal knowledge-decay formula. An adopting implementation SHOULD explicitly publish, where applicable: steward/owner responsibility, review cadence/next-review policy, staleness signals, renewal criteria, retirement criteria, archival criteria, escalation policy, and risk classification/handling.

Provenance attribution is not stewardship. RDF representations SHOULD keep source/provenance attribution separate from stewardship; `prov:wasAttributedTo` MAY identify origin, while stewardship SHOULD use an explicit qualified attribution/role pattern or another declared implementation mechanism. Stale does not imply false. Archived/preserved does not imply currently applicable, recommended, or endorsed. KEE defines no universal decay score, half-life, or automatic truth judgment.

### 16.3 Decision

The Decision Profile is Draft unless separately promoted.

The profile MUST preserve the ADR-style decision contract: title, context, decision, status, rationale, consequences, and append-only supersession/replacement history. DCTerms replacement relations and PROV revision/history remain the preferred mechanisms for supersession/revision.

Legacy SKOS annotation fields remain readable where supported but MUST NOT be described as if they precisely mean ADR context, rationale, or consequences. Native explicit fields, or structured sections linked with standard metadata/container relations such as `dcterms:hasPart` with explicit application/profile role identifiers, MAY be used; `dcterms:description` MAY carry a prose context summary when separately queryable sections are not required.

### 16.4 Assertion Metadata

The Assertion Metadata Profile is Accepted / Normative.

The profile MUST remain representation-neutral and preserve distinctions among managed assertion-unit identity, assertion content/proposition identity, assertion metadata-record identity, assertion occurrence identity, and representation/container identity. These identities MAY coincide in a representation but MUST NOT be inferred identical merely from serialization shape.

The managed-unit-kind vocabulary remains open. JSON-LD context coverage MUST expose direct aliases/type coercions for the current managed-unit surfaces, including `kee:managedAssertionUnit` and `kee:managedAssertionUnitKind`, and SHOULD expose assertion content and the role-specific temporal mechanisms of Section 14.1, without re-promoting ambiguous `kee:assertionTime` as a canonical new-write alias. If a convenience alias for legacy `kee:assertionTime` is retained, it MUST be labelled as legacy rather than canonical.

### 16.5 Lifecycle Crosswalk

The Lifecycle Crosswalk Profile is Draft / Non-Normative unless separately promoted. It maps vocabularies; it does not merge them or authorize source-data replacement merely because a mapping exists. Crosswalk records SHOULD carry source/target vocabulary identity, source/target terms, rationale, provenance, scope/context, temporal qualification, and review status as applicable. KEE does not create a separate mapping-relation code list.

---

## 17. Migration and compatibility policy

### 17.1 Policy

KEE uses **single-write canonical / dual-read registered legacy+canonical** compatibility.

1. New data MUST use the canonical form named by the migration registry.
2. Legacy forms are readable only where the registry explicitly records a compatibility policy.
3. Registered legacy use SHOULD produce a migration warning when tooling can do so without treating historical data as invalid.
4. Automatic migration tooling MAY rewrite only entries explicitly classified safe.
5. Conditional mappings require their explicit reviewed mapping evidence.
6. Unsafe semantic splits require contextual/profile-specific migration or remain unchanged.
7. Similar labels, local names, or structural resemblance never establish exact equivalence by themselves.
8. Migration MUST be explicit and provenance-preserving: it MUST preserve source-representation provenance or record sufficient migration provenance to reconstruct the transformation.
9. `owl:sameAs` MUST NOT be used merely to simplify migration.

### 17.2 Registry

Every changed KEE IRI or legacy exchanged field/pattern MUST be classified in the migration registry as exact replacement; close/approximate mapping; broader mapping; narrower mapping; deprecated without direct replacement; tooling-only/removed; or intentionally unmapped because semantics changed. The registry MUST record write policy, read policy, rewrite safety, governing package/decision, and notes sufficient to prevent false equivalence.

`kee:supersedes` → `dcterms:replaces` and `kee:supersededBy` → `dcterms:isReplacedBy` are classified `close-approximate-mapping` with `rewrite_safe=conditional` (Section 8.3).

The migration registry is a **living control** (Section 18.9). It MUST gain a row whenever a surface is retired, replaced, or reclassified, because a compatibility window that cannot record a new legacy surface cannot govern reading it. Rows MAY be appended; existing rows MUST NOT be reclassified without a governed decision, and a row MUST NOT be removed while any registered surface depends on it.

### 17.3 Compatibility window

Retirement of a legacy read after publication requires a separately versioned decision and migration notice identifying the exact legacy surface, migration evidence, last dual-read version, first rejecting version, and migration path or explicit statement that no safe automatic migration exists.

A legacy-read record is not structurally invalid merely because it uses a registered deprecated carrier. This does not extend to registered mixed-axis lifecycle values (Section 9.3), which validators reject on `kee:lifecycleState` while remaining readable as evidence/assessment standing on a separate slot.

### 17.4 Executable compatibility behaviour

Reference tooling SHOULD: report every registered legacy surface present in an input with its canonical surface, read policy, and rewrite safety; apply only `rewrite_safe=true` carrier renames on request, never changing values, class membership, graph identity, provenance, or lifecycle meaning; and compose the lifecycle-axis constraints of Section 9.3 with the lifecycle-owning profile shapes.

---

## 18. Release completeness and provenance

### 18.1 Package atomicity

A change package is release-complete only when all applicable surfaces agree: specification; Accepted / Normative profile text; SHACL; SKOS/value vocabularies; JSON-LD context; examples; positive/negative fixtures; conformance manifest; reference tooling; migration control; decision/provenance evidence; and onboarding/current-state traceability documentation. A surface MAY be marked not-applicable, but omission MUST be explicit rather than silent.

### 18.2 Published public API

Each release MUST publish a machine-readable manifest of its public normative API. The manifest for this release is `normative-api/v0.9.2.json`.

The public normative API comprises the published specification, Accepted / Normative profiles, admitted semantic surfaces, normative non-collapse and interoperability rules, conformance semantics, migration/compatibility behaviour, and other externally relied-upon requirements explicitly made normative. Draft and Non-Normative profiles are **excluded** from the public normative API.

A change to any surface inside the public normative API MUST be classified against the release rules in Section 20. A change to a surface outside it MUST still be recorded where it alters observable conformance behaviour, and MUST NOT be presented as no change at all.

Tooling that diffs release manifests sees only the surfaces those manifests enumerate. Where a change lies outside the manifest — in a shape graph, a concept scheme, the JSON-LD context, or an example package — manifest diffing MUST NOT be relied upon as the sole classification evidence, and the change MUST be classified by inspection.

### 18.3 Term registry

The term registry required by Section 4.2 records, for every KEE-owned semantic surface: IRI, kind, owner, status, definition, the eight admission criteria, introduced and deprecated versions, migration policy, evidence sources, admission verdict, and the surface's **disposition** and the decision that made it.

The disposition takes one of: `carried`, `admitted`, `retired (<migration relation>)`, or a named standing such as `canonical-informative`. A term's current standing is therefore one lookup, not a frozen row plus a chain of override records.

`vocab/kee.ttl` is the term-declaration document for the KEE-owned classes, properties, and undeclared registered-legacy values. It is generated from the term registry and asserts no axiom: no `rdfs:domain`, `rdfs:range`, `rdfs:subClassOf`, `rdfs:subPropertyOf`, `owl:equivalentClass`, `owl:equivalentProperty`, `owl:inverseOf`, `owl:disjointWith`, or `owl:sameAs`, and properties are typed `rdf:Property` rather than as object or datatype properties. Declaring a retained term is not a semantic claim; those axioms would be.

### 18.4 Prior-art provenance

Every adopted external replacement used by a KEE change, and every external standard this specification names as a SHOULD-level replacement, MUST have release evidence recording, where available: exact source/document; governing body; version or edition; issuance/publication date; maturity/status; lineage; temporal relation to the KEE baseline being changed; and evidence role. That evidence supports the normative change chain; it does not make a cited source part of KEE's normative text unless a profile or this specification explicitly adopts it.

### 18.5 Non-collapse behavioural coverage

The release suite MUST preserve executable evidence for the Section 7.1 non-collapse rules. The suite MUST demonstrate changed consumer outcomes when the independently governed input changes, over repository fixtures, shapes, or tooling output, rather than merely searching documentation for phrases or evaluating a lookup over declared inputs.

Behavioural coverage of the seventeen rules at this baseline is **fifteen of seventeen**. NC-01, NC-02, NC-04, NC-05, NC-07 through NC-17 are demonstrated.

**NC-03 (authority vs. responsibility) and NC-06 (confidence vs. trust) are not demonstrable at this baseline, and the reason is representational rather than epistemic.** A non-collapse rule can be demonstrated only where both of its sides are represented, as Section 7.1's own preamble scopes them. KEE represents authority and it represents confidence. It represents neither accountability as a surface distinct from authority, nor trust as a surface distinct from confidence. No shape, concept scheme, vocabulary document or example carries one. The obstacle is an absent vocabulary, not a judgment a consumer would have to make, and it lifts if and only if such a surface is introduced — which is a Section 4.2 admission question, not a testing question.

NC-04, NC-08 and NC-14 **are** demonstrable. In each case the judgment involved is recorded data. NC-08's distinction between a genuine inconsistency and a disagreement arising from time, scope, context, evidence, interpretation or method is carried by `kee:causeType` over the KEE Contradiction Cause Scheme, whose `DirectContradiction` concept is defined as "incompatible claims within the same scope, context, and time frame" and whose other concepts are the alternatives NC-08 enumerates. NC-04's contestation is carried by contradiction records, `kee:knownContradiction`, `kee:ContestedAuthorityClaim` and the `Superseded` lifecycle values. NC-14's two states are carried by a decision record's own status metadata and by a published specification's integration of it, which are separate documents by governance design.

A consumer reading any of these three reads a recorded classification. It does not judge whether an authorized decision is correct, whether a disagreement is genuine, or whether a decision ought to have been integrated — and it must not, because those are the judgments Section 7.1 keeps separate.

### 18.6 Release closure

A release-closure check MUST fail if a frozen denominator changes, an evidence identifier is missing or duplicated, any required column of a release control is empty or a sentinel, or any row lacks a resolved implementation and evidence disposition. Placeholder sentinels are not admissible values.

### 18.7 Namespace registration

The canonical namespaces of Sections 8.2, 9.2, 10, and the profile identifiers of Section 5 are persistent identifiers under `https://w3id.org/kee/`.

Registration under the W3ID project has been submitted and is pending review. Until that registration is merged and resolution is independently verified, these identifiers MUST NOT be described as operationally persistent or dereferenceable.

While registration is outstanding:

- this specification, its profiles, and its release evidence MUST NOT describe these namespaces as stable, resolvable, or dereferenceable;
- a consumer MUST NOT rely on dereferencing a KEE IRI to retrieve its definition, and SHOULD read the term-declaration document `vocab/kee.ttl` and the SKOS and SHACL assets published with this specification instead;
- the identifiers remain canonical for new writes under Sections 8.2, 9.2, and 10 — an identifier can be canonical without yet being resolvable; and
- exclusive control of the `w3id.org/kee` path is not yet secured, so the Section 4.3 "stable identifiers" criterion is satisfied only in the sense of a governed, versioned, non-changing identifier, not in the sense of a guaranteed persistent-resolution commitment.

### 18.8 Current-state drift

Living/current-state surfaces are synchronized at each release. Retained legacy compatibility examples remain historical evidence; legacy examples MUST NOT be presented as canonical new-write guidance merely because they remain executable during the compatibility window, and every registered example or fixture SHALL either use canonical new-write forms or carry an in-file compatibility marker.

### 18.9 Frozen denominators and living controls

Release evidence divides into two kinds, and an artifact's file name does not decide which it is.

**Frozen denominators** are fixed at publication and MUST NOT be edited afterwards: the term registry named at a publication, an audit denominator, an obligation restoration map, a legacy-surface census, a package-atomicity record, and a prior-art provenance register. Their purpose is to be a fixed set that later work is measured against, so editing one destroys the measurement. A correction to a frozen denominator is issued as a new artifact that supersedes it, and the superseded artifact is retained.

**Living controls** MUST be updated as governed decisions are made: the semantic migration registry, the compatibility window, and the reference tooling and tests that enforce them. Their purpose is to describe the repository's current behaviour, so a stale one is a defect.

A specification or amendment MUST state which kind each release artifact is. Where it does not, the artifact is a frozen denominator by default, because treating a denominator as living is the more damaging error.

### 18.10 Optional candidate surfaces

The following are published as optional, non-required surfaces. An implementation that ignores all of them remains conforming:

- obligation lineage registry;
- JSON profile declaration and its schema (`schemas/json-schema/v0.9-profile-declaration.schema.json`);
- EARL / PROV / SHACL evidence graph;
- RO-Crate KEEpack packaging experiment — **Experimental / Non-Normative**;
- public API diff.

KEEpack remains Experimental / Non-Normative and requires independent producer/consumer evidence under Section 15.7 before any graduation claim.

---

## 19. Profile status at publication

At v0.9.2:

- Software Engineering Profile — Accepted / Normative;
- Scientific Claim Profile — Accepted / Normative;
- Assertion Metadata Profile — Accepted / Normative;
- Assertion Profile — Draft;
- Lifecycle Crosswalk Profile — Draft / Non-Normative;
- Governance Transition Profile — Draft / Non-Normative;
- Promotion Profile — Draft / Non-Normative;
- Authority and Delegation Profile — Draft / Non-Normative;
- Contradiction Records Profile — Draft / Non-Normative;
- AI-Grounded Retrieval Profile — Draft / Non-Normative;
- Artifact Identity and Granularity Profile — Draft / Non-Normative;
- Historical and Bitemporal Querying Profile — Draft / Non-Normative;
- Decision Profile — Draft; and
- Organizational Memory Profile — Draft.

v0.9.2 promotes no profile. Executable assets for a Draft profile remain design/structural evidence only and do not promote it.

---

## 20. Release policy and change discipline

### 20.1 Semantic Versioning

Version numbers communicate compatibility:

- **PATCH** — backward-compatible correction or consolidation;
- **MINOR** — backward-compatible addition or material extension; and
- **MAJOR** — incompatible change to the public normative contract.

For pre-1.0 KEE releases, published `0.y.z` baselines deliberately follow a stricter compatibility policy than vanilla major-zero SemVer: a published PATCH release MUST NOT hide an incompatible change.

### 20.2 Change discipline after publication

Published v0.9.2 is immutable and MUST NOT be substantively rewritten in place. Future corrections or compatible/incompatible changes follow the governed pipeline:

`Observation -> Evidence / Research Question -> Research Brief -> Decision Record -> PATCH / MINOR / MAJOR release -> Profile or Implementation`

Accepted historical decision records remain append-only. Corrections to accepted decisions use new decision records rather than rewriting historical rationale.

An amendment MAY be used as an exceptional compatibility instrument, but the next applicable SemVer release SHOULD consolidate it so ordinary consumers can identify one current KEE version.

Current-state documentation MAY be updated to point to the published baseline. Such publication synchronization MUST NOT be used to hide semantic changes.

---

## 21. Terminology

These definitions are normative for the interpretation of this specification.

- **Knowledge Artifact** — a managed unit of knowledge or knowledge-bearing content whose provenance, lifecycle, authority, temporal state, or governance matters. It is a convenience abstraction, not a foundational ontology primitive; a profile identifies its managed unit through existing domain classes, profile conformance, and/or local convenience classes.
- **Claim** — a knowledge artifact that asserts something about the world, a model, an entity, a system, a policy, or another artifact.
- **Assertion** — an expressed claim by an agent or source in a specific context, at a specific time, with provenance.
- **Observation** — an artifact representing something perceived, measured, detected, experienced, or recorded by an agent, instrument, system, or process.
- **Evidence** — a knowledge artifact used to support, refute, qualify, or contextualize a claim. Evidence is not provenance.
- **Epistemic standing** — the current standing of a claim or artifact with respect to evidential support, challenge, qualification, assessment, or acceptance within a governance context. It is distinct from lifecycle/status, publication state, confidence, authority, trust, and producer type (Section 7.1). KEE defines no universal epistemic-standing vocabulary; profiles represent it through evidence, contradiction, assessment, and qualification structures.
- **Confidence** — a profile-defined estimate or classification of how strongly a claim should currently be believed, trusted, relied upon, or used within a defined scope and context (Section 11).
- **Lifecycle state** — the profile-owned governed workflow/publication/disposition state of an artifact at a point or interval in time (Section 9).
- **Lifecycle transition** — an event or activity that changes lifecycle state; represented as a provenance-bearing activity or record.
- **Deprecation** — marking an artifact as no longer recommended, no longer current, known to be problematic, outdated, superseded, or otherwise unsuitable for ordinary use. Deprecation does not require deletion and preserves the artifact historically unless legal, safety, privacy, or security requirements require removal.
- **Supersession / replacement / revision** — relationships between an older artifact and a newer one, represented with `dcterms:replaces`/`dcterms:isReplacedBy` (replacement) and `prov:wasRevisionOf` (revision) according to their distinct meanings (Section 8.3).
- **Promotion** — an authorized, deliberate governance transition that expands the applicability scope of a governed artifact (Section 13.2).
- **Profile** — a constrained, documented composition of adopted standards and explicitly admitted KEE contract material for a defined artifact type, domain, implementation context, or governance capability (Section 5).
- **Provenance** — the record of origin, derivation, attribution, and activity history of an artifact. Provenance is not authority, evidence, confidence, or correctness.
- **Temporal qualification** — the explicit representation of which temporal role a time value plays — valid, observation, assertion, recording, publication, review, invalidation, deprecation, supersession, or archival (Sections 0.5, 14.1).
- **Interoperability** — the ability of independently governed systems and profiles to exchange, interpret, validate, preserve, or act on knowledge artifacts without relying on private assumptions.
- **Scope** — where, to whom, or under what boundary an artifact applies (universal, jurisdictional, organizational, community, project, personal, geographic, temporal, system-specific, domain-specific).
- **Context** — the interpretive frame or circumstances in which an artifact should be understood (domain, situation, task, semantic frame, operating condition, audience, environment, purpose).
- **Authority** — the recognized power or legitimacy, on a declared basis, to assert, approve, modify, promote, deprecate, supersede, or retire an artifact within an authority scope (Section 12).
- **Responsibility / accountability** — the obligation of an agent to answer for a governed act; distinct from authority, authorship, trust, confidence, and correctness.
- **Governance** — as defined in Section 7.4.
- **Organizational memory** — the retained knowledge of an organization across people, processes, systems, decisions, documents, tools, routines, and historical experience.
- **Contradiction** — a recorded conflict between artifacts or positions; not itself a resolution, disposition, or logical inconsistency (Section 13.1).
- **Retrieval eligibility** — a consumer-scoped, derived decision about whether and how an artifact may be used in one retrieval or grounding operation (Section 14.5).

---

## 22. Capability Levels

Capability Levels are cumulative packaging of implementation capabilities. They are reported separately from the five conformance dimensions and are neither an aggregate conformance result nor a substitute for a conformance declaration (Section 15.3). Each level presumes the capabilities of the levels below it.

- **Level 0 — Informational alignment.** Uses KEE terminology and principles without machine-actionable governance.
- **Level 1 — Artifact registry.** Manages identifiable artifacts with stable identifiers, classification, profile-owned lifecycle state where the profile requires it, source or creator, timestamps, and basic retrieval.
- **Level 2 — Governed lifecycle.** Adds transition records, responsible agents, authority metadata with a declared authorization basis, deprecation support, replacement/revision support, and validation of required metadata.
- **Level 3 — Temporal and provenance-aware governance.** Adds a PROV-compatible provenance model or equivalent, temporal validity, invalidation, lifecycle history, and point-in-time or event-log reconstruction with declared history coverage.
- **Level 4 — Epistemic governance.** Adds contradiction records, profile-defined confidence or epistemic-standing structures, promotion records with machine-checkable scope ordering, review intervals, staleness handling, and machine-actionable governance constraints.

A Capability Level claim MUST name the profiles and dimensions through which each capability is realized; a level does not imply conformance to any profile.

---

## 23. References

Editions and dates are those in force on 2026-09-18. Status is recorded so that later convergence is not represented as historical influence (Section 4.1).

### 23.1 Normative references

- RFC 2119 (1997) and RFC 8174 (2017), IETF.
- RDF 1.1 Concepts and Abstract Syntax, W3C Recommendation, 2014-02-25. RDF 1.2 Concepts, W3C Candidate Recommendation Snapshot, 2026-04-07 (referenced only "where supported").
- SPARQL 1.1 Query Language, W3C Recommendation, 2013-03-21.
- Shapes Constraint Language (SHACL), W3C Recommendation, 2017-07-20.
- SKOS Simple Knowledge Organization System Reference, W3C Recommendation, 2009-08-18.
- PROV-O: The PROV Ontology, W3C Recommendation, 2013-04-30, with PROV errata (o-1 to o-6, last updated 2023-08-23).
- Time Ontology in OWL, W3C Recommendation, 2017-10-19 (Candidate Recommendation Draft 2022-11-15 noted, not adopted).
- DCMI Metadata Terms, Dublin Core Metadata Initiative, edition issued 2020-01-20.
- Web Annotation Data Model, W3C Recommendation, 2017-02-23.
- OWL 2 Web Ontology Language, W3C Recommendation (Second Edition), 2012-12-11.

### 23.2 Informative references

- Data Catalog Vocabulary (DCAT) Version 3, W3C Recommendation, 2024-08-22.
- The Profiles Vocabulary (PROF), W3C Working Group Note, 2019-12-18.
- The Organization Ontology, W3C Recommendation, 2014-01-16.
- ODRL Information Model 2.2, W3C Recommendation, 2018-02-15.
- eXtensible Access Control Markup Language (XACML) Version 3.0 Plus Errata 01, OASIS Standard, 2017-07-12; XACML v3.0 Administration and Delegation Profile v1.0, Committee Specification Draft 04, 2014-11-13.
- Memento: Time Travel for the Web, IETF RFC 7089, Informational, 2013-12.
- Evidence & Conclusion Ontology (ECO), OBO Foundry, release 2026-07-10; SEPIO, Monarch Initiative, v2023-06-13; GRADE Handbook (2013) and GRADE Book v1.0 (2024).
- OSLC Requirements Management 2.1, OASIS Standard, 2021-06-21; W3C Trace Context Level 1, Recommendation, 2021-11-23 (Level 2 Candidate Recommendation Draft 2024-03-28); Package-URL, ECMA-427 1st edition, 2025-12; SPDX 3.0.1 (2024-12) and ISO/IEC 5962:2021; CycloneDX, ECMA-424 2nd edition, 2025-12; OSV Schema 1.7; SWHID, ISO/IEC 18670:2025.
- ISO 14721:2025 (OAIS); ISO 15489-1:2016; ISO 30401:2018 with Amd 1:2022; ISO/IEC 9075-2:2023 (SQL, temporal features).
- Documenting Architecture Decisions, M. Nygard, 2011-11-15.
- Nanopublication Guidelines (community working draft); RO-Crate 1.2, 2025-06-04.
- W3C Verifiable Credentials Data Model 2.0, Recommendation, 2025-05-15; W3C DID Core 1.0, Recommendation, 2022-07-19.
- RDF Dataset Canonicalization (RDFC-1.0), W3C Recommendation, 2024-05-21; W3C EARL 1.0 Schema, Working Group Note, 2017-02-02; ISO/IEC 11179-3:2023; GNAP, IETF RFC 9635, 2024-10; C2PA Specification 2.4, 2026-04; PAV 2.3.1, 2014-08-28.

---

## 24. Open items at this baseline

Stated here so that a reader of this document does not have to reconstruct them. None of these is depended upon by a published surface, and none blocks conformance to this baseline.

1. **The Section 0.4 band is not settled**, and no drafting-only narrowing of it is authorized.
2. **NC-03 and NC-06 remain representationally non-demonstrable** (Section 18.5). Closing the gap is a Section 4.2 admission question.
3. **The Section 12.3 accountable-root escalation is outstanding.** The obligation is normative; the reference shape still reports it at `sh:Warning`. Escalation to `sh:Violation` requires a MINOR release that declares it.
4. **KEEpack remains Experimental / Non-Normative** and requires independent producer/consumer evidence under Section 15.7 before any graduation claim.
5. **w3id registration is submitted but not yet merged or independently verified** (Section 18.7).

---

## 25. Release notes

### v0.9.2

- Consolidates v0.9.0 and v0.9.1 into one self-contained published baseline under a single current version identifier.
- Inlines the full normative contract, so that determining the meaning of a KEE obligation requires no other document.
- Adds no requirement, no KEE-owned semantic term, no profile promotion, no Capability Level, and no conformance-behaviour change.
- Requires no implementation change and no governed-data migration.

### Contract carried unchanged

Carried unchanged from v0.9.1 and v0.9.0: Prior Art First and the KEE-owned-term admission test; the KnoEdg + Eidos responsibility boundaries; requirement categories and ownership rules; all seventeen Section 7.1 non-collapse rules and their `NC-01`..`NC-17` identifiers; source and consumer neutrality; the shared-dimension ownership contract, including temporal qualification as a cross-cutting dimension; governance, authority/delegation, evidence/confidence, contradiction/promotion, retrieval, archival and historical-query rules; the five conformance dimensions and their machine-safe tokens; independent interoperability evidence as a promotion requirement; the optional candidate surfaces; the Promotion shape's cyclic-scope constraint; profile statuses; terminology and Capability Levels; the compatibility and migration obligations; and the rule that no settled shared-contract count is published.
