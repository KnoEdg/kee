# KEE Specification v0.11.0

Status: Published Normative Baseline\
Version: 0.11.0\
Date: 2026-10-12\
SemVer classification: MINOR\
Supersedes as current version identifier: KEE v0.10.0\
Published public API: `normative-api/v0.11.0.json`\
Informative annex: `docs/specs/KEE-Specification-v0.11.0-release-governance-annex.md`

---

## 0. Document status and authority (Normative)

This document is the published KEE v0.11.0 normative baseline and the current version identifier for the KEE public normative contract.

KEE v0.11.0 is a **Semantic Versioning MINOR release**. It is MINOR rather than PATCH because it adds three admitted KEE-owned controlled value sets to the public normative API: the governance-record review-status scheme (Section 9.2), the query-time-dimension scheme (Section 14.2) and the retrieval-eligibility scheme (Section 14.5). An implementation that conformed to v0.10.0 remains conforming without change unless it opts into a capability one of these schemes serves.

It carries two conformance-behaviour changes, recorded here as Section 18.2 requires. First, a composed shape graph, `shacl/governance-record-review-status-constraints.ttl`, checks that `kee:lifecycleState` on the four governance-record classes named in Section 9.2 takes a value from the governance-record review-status scheme, and reports at `sh:Warning`. No conformance outcome changes for those classes at this baseline. **v0.11.0 is the last dual-read version** for generic `https://w3id.org/kee/lifecycle#` values on those classes, and **v0.12.0 is the first rejecting version**, in which the same shape reports at `sh:Violation` (Sections 9.2 and 17.3). Second, the `kee:queryTimeDimension` and `kee:eligibilityCategory` slots are closed by `sh:in` over their schemes in `shacl/historical-bitemporal-querying-profile.ttl` and `shacl/ai-grounded-retrieval-profile.ttl`, and the membership check on a new-write record reports at `sh:Violation` from this baseline: a point-in-time query record or retrieval result that wrote an identifier of its own in either slot conformed structurally under v0.10.0, whose Section 14.2 called the slot an open classifier, and does not conform under v0.11.0. **v0.10.0 is the last version in which such a value conforms and v0.11.0 the first rejecting version** (Sections 14.2, 14.5 and 17.3); a registered-legacy record, one declaring only `kee:profileConformance`, is reported at `sh:Warning` and remains readable for as long as that carrier is (Section 17). In both cases the versions are named rather than promised relatively, and a release control enforces each schedule. The owning profiles are Draft / Non-Normative and excluded from the public normative API, which is the ground on which the v0.11.0 rejection and the scheduled v0.12.0 rejection are classified MINOR-compatible rather than MAJOR; the public normative contract is unchanged by either (informative annex, Section A.11).

Beyond the three schemes and the sentences that bind them to their slots, it adds no requirement, promotes no profile and adds no Capability Level. The rest of this release is consolidation that keeps the meaning of every v0.10.0 obligation: it marks every top-level section Normative or Informative, names the conformance targets its obligations fall on (Section 15.8), defines the terms the text relied on without defining (Section 21), lists its namespaces (Section 0.7), adds security and privacy considerations (Section 26), and moves text that governs only the project's own release process to an informative annex, leaving a pointer in place of each moved section so that section numbering is unchanged from v0.10.0. Like v0.10.0, it is self-contained: a reader needs no other document to determine the ordinary normative meaning of a KEE obligation.

KEE is a governed application-profile family and interoperability framework for knowledge artifacts. It composes established standards, publishes explicit non-collapse and behavioural rules, maintains only narrowly justified local controlled vocabularies where exact prior art is absent, and provides executable conformance and reference assets.

KEE remains the combined KnoEdg + Eidos framework. KnoEdg and Eidos are architectural responsibility boundaries, not mandatory duplicate semantic layers.

KEE SHALL NOT claim ownership of a distinct foundational ontology, provenance model, temporal model, lifecycle model, authority model, confidence model, evidence model, identity model, scientific-claim model, organizational-memory model, query language, graph model, storage model, canonicalization algorithm, or general profile meta-model when established prior art already supplies the required semantics.

The release control rule is:

> **A KEE term may disappear; its audited obligation may not disappear silently.**

When this specification delegates detail to an Accepted / Normative profile, that profile is part of the applicable normative contract only for implementations that claim conformance to it. Draft shapes, examples, fixtures, validators, or implementation assets MUST NOT acquire normative force merely by existing or executing.

### 0.1 Normative language

The key words MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY, and OPTIONAL are to be interpreted in the sense of RFC 2119 and RFC 8174 when, and only when, they appear in uppercase.

Each top-level section of this specification is marked **Normative** or **Informative** in its heading. Text in an Informative section, in the informative annex named above, in an example, or in a note creates no obligation on an implementation, even where it uses a key word in uppercase to describe an obligation that binds the KEE project's own release process. Where a Normative section contains a subsection that is a pointer to the annex, the pointer paragraph is normative and the annex text it points to is informative.

### 0.2 Self-containment

This specification is self-contained. A reader SHALL NOT need any other document to determine the ordinary normative meaning of a KEE obligation stated here.

Where this specification names a repository artifact — a SHACL shape graph in `shacl/`, a SKOS concept scheme in `schemas/skos/`, a JSON Schema in `schemas/json-schema/`, the JSON-LD context in `context/`, the term-declaration document `vocab/kee.ttl`, or the published public-API manifest in `normative-api/` — that artifact is published alongside this specification and is the machine-readable expression of an obligation this document states in prose. The prose controls where the two differ, except where this document explicitly delegates a machine-checkable decision to a named shape.

The shape graphs published here are byte-identical to those the reference validator executes. The shape-contract version of the published shape graphs is declared by the public-API manifest named above (`shapeContractVersion`); the shape graphs carry no version statement of their own. Section 15.5 requires status-aware tooling to report it.

### 0.3 KEE's role and ownership boundary

KEE is a **published, versioned, testable shared contract over prior art**, and **not a semantic foundation**.

The ownership boundary is:

1. **Prior art owns foundational semantics.** KEE does not restate, replace, or shadow what an established standard already defines.
2. **Specialized profiles own domain and artifact-type behaviour.**
3. **The KEE family contract owns the published cross-profile rules** that make independently designed profiles interpretable to one another.
4. **KEE framework governance owns the standing of KEE's own normative instruments** — the distinction between a decision being accepted and its being integrated as a binding requirement.

**No genuinely KEE-specific semantic primitive is claimed.** The class of obligations that would require a KEE-owned semantic surface not supplied by prior art, and not dissolved by publishing the same surface under a neutral name, is empty at this baseline.

### 0.4 What this specification deliberately does not state (pointer to the annex)

This specification states no count of shared-contract requirements. A count, where one is discussed at all, is **evidence for** the role claim in Section 0.3. It is not part of the normative contract, and nothing in `vocab/`, `shacl/`, `schemas/`, `context/` or this document depends on it. A consumer implements the published surfaces named in this specification; it never implements a number. Why the figure is carried as a band, the rule that the band is not narrowed by drafting alone, and the evidence behind the emptiness claim of Section 0.3 govern the project's own evidence rather than any implementation, and are carried unchanged in the informative annex, Section A.1.

### 0.5 Time is a first-class cross-cutting concern

A governed claim may have distinct valid, observation, assertion, recording, publication, review, invalidation, deprecation, supersession and archival times. Relevant temporal roles MUST NOT be silently collapsed into one generic timestamp. Section 14 governs the representation of these roles.

### 0.6 Non-collapse means preserving important distinctions

A non-collapse rule states that two related concepts are not automatically identical, and that an implementation MUST NOT infer one from the other merely because they co-occur, share a label, or are commonly discussed together. Section 7.1 is the normative list.

### 0.7 Namespaces used by this baseline

The following table lists every KEE-owned namespace this baseline uses. Each row names the section that governs the namespace and its standing for new writes. Registration and resolution of each identifier are stated in Section 18.7 and nowhere else; a row here is not a resolution claim. Where a row names a scheme, the scheme published at that namespace defines its own concepts, and this table does not restate them.

| Namespace | What it identifies | Governing section | Standing for new writes |
|---|---|---|---|
| `https://w3id.org/kee#` | KEE-owned classes, properties and registered-legacy values declared in `vocab/kee.ttl` | Sections 4.2, 18.2, 18.3 | canonical for the admitted terms the term declarations list |
| `https://w3id.org/kee/profile#` | KEE profile identifiers | Section 5 | canonical |
| `https://w3id.org/kee/artifact#` | artifact-classification concept scheme, used with `dcterms:type` | Section 8.2 | canonical |
| `https://w3id.org/kee/confidence#` | confidence-interpretation scheme, holding the `confidence:ProfileDefined` sentinel and no confidence level | Section 10 | canonical |
| `https://w3id.org/kee/lifecycle#` | historical generic lifecycle values | Section 9.2 | compatibility-only; MUST NOT be minted for new writes where a profile scheme owns the dimension |
| `https://w3id.org/kee/lifecycle/assertion#` | Assertion lifecycle scheme; default scheme for the Assertion Metadata slot | Sections 9.2, 9.3, 16.4 | canonical |
| `https://w3id.org/kee/lifecycle/scientific-claim#` | Scientific Claim lifecycle scheme | Sections 9.2, 9.3 | canonical |
| `https://w3id.org/kee/lifecycle/organizational-memory#` | Organizational Memory lifecycle scheme | Sections 9.2, 9.3 | canonical |
| `https://w3id.org/kee/lifecycle/decision#` | Decision lifecycle scheme | Section 9.2 | canonical |
| `https://w3id.org/kee/lifecycle/software-engineering#` | Software Engineering lifecycle scheme | Section 9.2 | canonical |
| `https://w3id.org/kee/lifecycle/governance-record#` | governance-record review-status scheme, owned by the Governance Transition Profile and adopted by three other profiles | Section 9.2 | canonical; added at this baseline |
| `https://w3id.org/kee/vocab/contradiction-cause#` | contradiction-cause scheme, used with `kee:causeType` | Section 10 | canonical |
| `https://w3id.org/kee/vocab/assertion-unit-kind#` | managed assertion-unit-kind scheme, used with `kee:managedAssertionUnitKind` | Sections 10, 16.4 | canonical |
| `https://w3id.org/kee/vocab/query-time-dimension#` | query-time-dimension scheme, used with `kee:queryTimeDimension` | Sections 10, 14.2 | canonical; added at this baseline |
| `https://w3id.org/kee/vocab/retrieval-eligibility#` | retrieval-eligibility scheme, used with `kee:eligibilityCategory` | Sections 10, 14.5 | canonical; added at this baseline |

`https://w3id.org/kee/governance#` and `https://w3id.org/kee/contradiction#` are not current governed vocabulary families (Section 10). The retired Governance Action Type scheme remains declared and readable under Section 17 and is not a namespace for new writes.

---

## 1. Scope (Normative)

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

Producer or consumer type MAY affect applicable provenance, evidence, review, disclosure, validation, assurance, and governance requirements. Different producer types MAY require different supporting metadata: an AI-derived artifact may require model and input provenance; a sensor observation may require calibration metadata; an automated test result may require environment and fixture metadata. These policy differences do not create separate epistemologies and do not determine epistemic standing (Section 21) by themselves.

Source neutrality MUST NOT be interpreted as source blindness. Implementations MUST preserve producer, consumer, activity, model, instrument, process, or workflow metadata when those distinctions are material to the applicable profile or governance policy, and SHALL NOT erase such metadata when it is relevant to provenance, evidence, review, accountability, or governance.

Implementations SHOULD model the epistemic or governance role performed (observer, asserter, generator, deriver, reviewer, approver, publisher, custodian, retriever, consumer, decision-maker) separately from the kind of agent, instrument, system, or process performing that role when both are material.

### 1.2 Implementation independence

A conforming implementation MAY use RDF stores, property graphs, relational databases, document stores, event logs, object stores, search indexes, or hybrid architectures.

Conformance depends on satisfying declared profile obligations and interoperability contracts, not on a particular storage technology or serialization.

---

## 2. Goals (Normative)

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

## 3. Non-goals (Normative)

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

## 4. Prior Art First and KEE-owned-term admission (Normative)

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

Such a vocabulary SHALL have a declared owner, stable identifiers, definitions for each value, open/closed status, normative status, an extension/versioning policy, and external mappings or explanatory references where useful. "Stable identifier" here means a governed, versioned identifier that does not change; where that identifier belongs to a persistent-identifier scheme entry, Section 18.7 governs what may be claimed about its registration, resolution, and persistence. Where a value corresponds to established representation prior art, the scheme SHOULD record an explicit mapping or explanatory reference rather than implying KEE invented the representation.

A local controlled vocabulary is not evidence that KEE owns a foundational semantic model for the broader domain.

---

## 5. Architectural composition and profile framework (Normative)

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

## 6. Requirement categories (Normative)

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

## 7. Cross-profile interoperability contract (Normative)

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

## 8. Canonical semantic carriers and migration (Normative)

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

## 9. Lifecycle, review, archival, and mapping (Normative)

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
- `https://w3id.org/kee/lifecycle/decision#`;
- `https://w3id.org/kee/lifecycle/software-engineering#`; and
- `https://w3id.org/kee/lifecycle/governance-record#`, added at this baseline.

Registration and resolution status of these namespaces is stated in Section 18.7, which confirms resolution only for the identifiers it names; a namespace is canonical for new writes whether or not its resolution has been confirmed.

**Governance-record review status.** The scheme published at `https://w3id.org/kee/lifecycle/governance-record#` (`schemas/skos/governance-record-lifecycle.ttl`) carries one dimension: the review status of a record *about* governing knowledge, meaning the record's own standing as a record, as accepted or not by whatever review governs records of its kind. It is not the state of anything the record describes. Its five values are Proposed, Accepted, Rejected, Withdrawn and Superseded, each defined in terms of the record only; a value's label shared with the Assertion or Decision scheme does not establish equivalence, and the scheme asserts no mapping. The **Governance Transition Profile owns** the scheme. It is explicitly adopted, satisfying the first paragraph of this section, for `kee:lifecycleState` on `kee:GovernanceTransitionRecord` (including a record also typed `kee:AuthorityRecord` or `kee:PromotionRecord`) by its owner, on `kee:ContradictionRecord` by the Contradiction Records Profile, on `kee:ContestedAuthorityClaim` by the Authority and Delegation Profile, and on `kee:LifecycleCrosswalkMapping` by the Lifecycle Crosswalk Profile. All four profiles are Draft / Non-Normative. The review-status axis MUST NOT carry: (1) a dispute's resolution or disposition (Section 13.1); (2) a grant's expiry, revocation or suspension (Section 12.2); (3) the recorded or target state a transition or crosswalk record describes (Section 9.4); (4) mapping strength (Section 9.4); or (5) epistemic standing, confidence, authority or correctness (Sections 9.1, 11, 12.5). The scheme defines no transition constraints. A change of a record's review status MUST NOT erase the earlier value or its provenance; it is recorded by a governance transition whose governed artifact is the record, or by a revision linked with `prov:wasRevisionOf`, as the adopting profile chooses. No generic `https://w3id.org/kee/lifecycle#` value maps to any concept in this scheme: a generic value on one of these four classes is reported as a review status not stated in the adopted scheme, never read as Accepted or any other concept. The membership check is one composed shape graph, `shacl/governance-record-review-status-constraints.ttl`, closed by `sh:in` over the five concepts and composed with the four owning shapes but not with the Assertion Metadata shape (Section 16.4). At **v0.11.0** it reports at `sh:Warning`, and v0.11.0 is the **last dual-read version** for generic values on these classes; at **v0.12.0** it reports at `sh:Violation`, and v0.12.0 is the **first rejecting version** (Section 17.3). This is the migration notice those sections require.

Mappings from legacy generic values to profile-specific concepts MUST be explicit and profile-qualified. A generic value such as `lifecycle:Active` MUST NOT be assumed to have one universal exact meaning across profiles.

### 9.3 Axis separations for the lifecycle-owning profiles

The Scientific Claim lifecycle scheme MUST NOT use `Supported`, `Qualified`, or `Challenged` as values on the same single lifecycle axis as publication/disposition states. The scheme is limited to publication/governance/disposition progression (Hypothesis, Submitted, Preprint, Published, Corrected, Retracted, Superseded, Archived). Support, challenge, qualification, and replication are represented by the profile's evidence, contradiction, confidence/assessment, qualification, and replication structures. A claim MAY be simultaneously Published and supported, or Published and challenged, without violating lifecycle cardinality.

The Assertion lifecycle scheme MUST NOT use `Preferred`, `Challenged`, or `Qualified` as values on the same lifecycle axis as lifecycle/disposition states. The scheme is limited to Proposed, Normal, Deprecated, Superseded, Rejected, Withdrawn, and Archived. Preference/ranking remains profile/application policy; challenge is represented through contradiction/dispute structures; qualification through explicit caveats, scope/context, evidence, or profile-defined assessment. Assertion lifecycle/disposition state MUST remain distinct from ranking, dispute, review, or qualification standing.

The Organizational Memory lifecycle scheme MUST NOT use `Under Review`, `Qualified`, or `Stale` as values on the same lifecycle axis as lifecycle/disposition states. The scheme is limited to Draft, Active, Deprecated, Superseded, Retired, and Archived. Review/currency assessment MAY use review timestamps, review-due policy, provenance, explicit profile-defined assessment, or other declared mechanisms. A stale artifact MUST NOT be inferred false merely because it is stale. An archived artifact MUST NOT be inferred currently applicable merely because it is preserved.

Validators SHOULD reject known legacy mixed-axis values where the active profile now defines them as another semantic dimension. `shacl/lifecycle-status-constraints.ttl` does so for the three schemes above, composed with the lifecycle-owning profile shapes (Section 17.4). The same file also guards the `kee:lifecycleState` slot of an Assertion Metadata record (Section 16.4), reporting a mixed-axis value or a generic `https://w3id.org/kee/lifecycle#` value at `sh:Warning`: because that profile is Accepted / Normative, no value that conforms at this baseline stops conforming, and whether and when that profile rejects such a value is a separately versioned decision with its own migration notice under Section 17.3, not yet taken.

### 9.4 Crosswalks

Crosswalks MUST use explicit source vocabulary, target vocabulary, source term, target term, mapping relation, scope/context, provenance, and rationale as applicable. Examples based only on label resemblance, such as `Accepted ~= Approved ~= Published ~= Stable ~= Baselined`, MUST NOT be treated as semantic equivalence.

For Lifecycle Crosswalk new writes, the supported mapping relations are `skos:exactMatch`, `skos:closeMatch`, `skos:broadMatch`, `skos:narrowMatch`, and `skos:relatedMatch`, used according to documented meaning. `skos:exactMatch` MUST NOT be inferred from similar labels alone, and a producer MUST NOT upgrade a close, broad, narrow, or related mapping to exact merely because labels resemble one another.

The review state of a mapping record is itself a profile-owned governance dimension and MUST NOT be confused with the lifecycle states being mapped. For a Lifecycle Crosswalk mapping record that dimension is carried on `kee:lifecycleState` with a value from the governance-record review-status scheme, which the Lifecycle Crosswalk Profile adopts (Section 9.2); accepting a mapping record does not upgrade its mapping relation.

---

## 10. Local controlled vocabularies (Normative)

KEE retains narrowly justified local vocabularies where the shared identifiers themselves add interoperability value.

The contradiction-cause scheme uses `https://w3id.org/kee/vocab/contradiction-cause#`. The canonical scheme MUST provide stable identifiers, definitions, version metadata, an extension policy, and explicit external mappings where justified. `kee:causeType` remains an open IRI-valued slot: implementations MAY use the canonical KEE scheme or another declared profile/domain taxonomy, and KEE conformance MUST NOT require the local scheme when another profile-declared vocabulary preserves the same obligation.

The managed assertion-unit-kind scheme uses `https://w3id.org/kee/vocab/assertion-unit-kind#`. Its initial values cover RDF triple / RDF-star triple term, reifier/reified statement, statement node, named graph, nanopublication assertion graph, document assertion, and application claim object. The slot MUST remain open; implementations MAY use additional IRIs for representation patterns not enumerated by KEE. Where a kind corresponds to established representation prior art, the scheme SHOULD record an explicit mapping or explanatory reference.

Two value sets are added at this baseline, each by a recorded decision under Section 4.2. The query-time-dimension scheme uses `https://w3id.org/kee/vocab/query-time-dimension#` and is the value set of `kee:queryTimeDimension` (Section 14.2). The retrieval-eligibility scheme uses `https://w3id.org/kee/vocab/retrieval-eligibility#` and is the value set of `kee:eligibilityCategory` (Section 14.5). Unlike the two slots above, both slots are **closed** by `sh:in` in their profile shapes; a new concept requires a governed decision and is a MINOR addition. Each scheme defines its own concepts and satisfies Section 4.3 on its own terms.

The generic confidence-status scheme is Informative / Non-Normative. Values such as Low, Moderate, and High MUST NOT be treated as interoperable confidence semantics without a profile-defined interpretation contract. The confidence-interpretation sentinel `confidence:ProfileDefined` indicates that interpretation belongs to the applicable profile; it is canonicalized in a scheme that holds no confidence level, and it is not itself a confidence level. The illustrative Low/Moderate/High labels remain registered legacy.

A declared namespace prefix is only a serialization convenience. It is not evidence that KEE publishes a governed vocabulary at that namespace. The namespaces named in this section are canonical for new writes; their registration and resolution status is stated in Section 18.7, which confirms resolution only for the identifiers it names. The canonical JSON-LD context and active SHACL assets MUST avoid unused KEE-owned namespace declarations where practical; in particular, `governance#` and `contradiction#` MUST NOT be presented as current governed vocabulary families unless concrete canonical terms are actually defined there.

The Governance Action Type scheme and its concepts are **retired** (`deprecated-without-direct-replacement`), and `kee:managedUnit` is **retired** (`exact-replacement` to `kee:managedAssertionUnit`). All retired surfaces remain declared and readable under Section 17.

---

## 11. Confidence, evidence, and replication (Normative)

KEE defines no universal confidence scale, propagation model, calibration model, aggregation model, or cross-domain confidence interpretation.

A profile that uses confidence MUST define enough semantics for a consumer to interpret the representation it accepts or emits. A profile that permits a confidence value, label, category, probability, score, interval, or other confidence representation MUST declare, as applicable: its value type and permitted scale/range or vocabulary; the interpretation of the value; the assignment or estimation method; the assigning agent, software process, or other responsible process; the assignment time and any validity interval or temporal interpretation; how evidence relates to the confidence assessment; calibration or aggregation rules when relevant; and revision, supersession, decay, or re-assessment behaviour when relevant.

A bare numeric value or unqualified label MAY be structurally valid but MUST NOT be treated as semantically interoperable confidence merely because it passes datatype or vocabulary validation. A consumer MUST evaluate the declared profile's interpretation contract where the profile requires one.

Absence of a confidence assertion MUST NOT, by itself, be interpreted as low confidence, negative confidence, rejection, falsity, or lack of support.

Confidence MUST remain distinct from provenance, authority, trust, evidence strength, lifecycle/publication state, popularity, source reputation, SHACL severity, and an uncalibrated model score.

The base KEE Scientific Claim SHACL shape MUST NOT impose a universal `[0,1]` range on `kee:confidenceValue`. Profiles that choose a bounded scale MAY impose their own range constraints.

Evidence is not provenance. Evidence strength is not confidence. Profiles SHOULD use ECO, SEPIO, GRADE, another appropriate domain evidence model, or a declared profile/domain vocabulary when generic links are insufficient. KEE's normative role is the profile composition and interoperability boundary: a profile declares which evidence model or vocabulary it uses, how evidence bears on the managed claim/assertion, and how evidence-specific assessment relates to confidence and provenance. `kee:evidenceStrength` MAY remain readable as a profile convenience/compatibility slot; its presence does not establish a KEE-owned evidence-strength semantics and it MUST remain open to externally defined IRI values.

Replication attempts and outcomes are evidence/scientific-assessment structures independent of publication/governance lifecycle. A summarized replication status, if used, is profile-defined, MUST NOT be inferred solely from publication/governance lifecycle, MUST NOT replace the underlying replication evidence when the claimed profile requires it, and MUST remain a separate dimension from lifecycle state.

---

## 12. Authority and delegation (Normative)

### 12.1 Delegation and authorization evidence

`prov:actedOnBehalfOf` is an Agent-to-Agent delegation relation: the delegate Agent is the subject and the responsible/delegating Agent is the object. AuthorityRecord resources MUST NOT use it in a way that entails that the record itself is a PROV Agent. A profile MAY additionally use `prov:qualifiedDelegation` or another declared authorization/grant representation when qualification is required.

Provenance does not authorize. PROV participation or history does not by itself authorize an action. A profile asserting authority MUST distinguish: the agent and role/capacity involved; the authorization basis (policy, grant, credential, capability, charter, organizational record, workflow decision, or other declared authority evidence); the authority scope, action, and target/resource semantics required by that profile; validity, expiration, and revocation where applicable; and provenance of the grant, record, and governed action.

`prov:wasAttributedTo`, `prov:wasAssociatedWith`, `prov:qualifiedAssociation`, generation history, authorship, contribution, or derivation MUST NOT be interpreted as authorization merely because they identify an agent.

### 12.2 Scope, expiration, and revocation

Authority scope and artifact applicability scope are separate claims even when they use the same value vocabulary or reference the same contextual resource. Profiles MUST represent them separately; value equality by itself MUST NOT collapse the two meanings. Worked examples and fixtures SHOULD demonstrate the distinction with visibly different values where practical so that implementers do not infer equivalence from example reuse.

Expiration (the automatic end of a grant's stated validity period) and revocation (a later governance act or invalidation that withdraws previously granted authority) are distinct authority-ending mechanisms. A grant MAY expire without being revoked, MAY be revoked before its scheduled expiration, or MAY have neither event. Revocation MUST preserve the original grant/assignment history; a revocation event MUST NOT erase the fact that authority was previously granted or exercised. Profiles that record both validity end and revocation MUST keep their semantics separately queryable. A grant record's review status (Section 9.2) is not the grant's validity: expiry, revocation and suspension are never carried by it, and a revoked grant's record ordinarily remains an accepted record.

### 12.3 Accountable root for non-person agents

Any agent receiving governance authority that does not itself resolve to an accountable `prov:Person` or `prov:Organization` MUST resolve through the declared delegation/authorization chain to such a root. Absence of a `prov:SoftwareAgent` (or any other) type assertion does not exempt an agent from this obligation; the Authority and Delegation shape evaluates the chain for every grantee that is not typed as a Person or Organization.

A boolean advisory assertion such as `kee:softwareAgentNonSovereign` does not establish this invariant and MUST NOT be treated as sufficient conformance evidence; it remains legacy-readable advisory metadata with no conformance effect.

A direct grant to a person or organization satisfies the root requirement without an intervening delegation hop. For a delegated chain, the accountable root is the terminal person or organization for the chain being evaluated.

This obligation is normative at this baseline, and the reference shape reports it at `sh:Violation` severity. The escalation was scheduled for, and performed at, v0.10.0. Earlier baselines reported the same obligation at `sh:Warning`, so that data which was structurally valid under them did not become structurally invalid without a release that says so; v0.10.0 said so. A grantee that resolves to no accountable person or organization conformed structurally under v0.9.2 and does not conform from v0.10.0. An implementation claiming the Authority and Delegation profile that relied on warning-level behaviour MUST resolve its delegation chains to conform at this baseline.

### 12.4 Explicit pairing

Flat repeated agent, role, and evidence properties MUST NOT be relied upon when their intended pairings would be ambiguous. An authority-grant activity SHOULD use PROV qualified association or an equivalent explicit pairing structure; where `prov:qualifiedAssociation` is used, each association identifies its agent with `prov:agent` and its role/capacity with `prov:hadRole`. If different agents or roles rely on different authority evidence, the profile MUST make those pairings explicit. A consumer MUST NOT infer which role or authority basis belongs to which agent solely from parallel repeated flat properties. Qualified association is not the only conforming representation; another profile-declared explicit pairing structure is permitted.

### 12.5 Structural validation is not authorization

Structural validation does not establish legal validity, enforceable runtime authorization, correctness, exclusivity, or trust. A profile or implementation that needs enforceable permission decisions MUST compose an appropriate policy/authorization mechanism outside the structural profile.

---

## 13. Contradiction and promotion (Normative)

### 13.1 Contradiction

A contradiction representation that cites evidence for multiple conflicting sides MUST make each evidence-to-side pairing mechanically identifiable. Flat repeated `kee:evidenceForSide` values are insufficient when pairing is ambiguous; the legacy predicate remains readable but does not by itself satisfy the pairing obligation when more than one side/evidence relation is present. Composition from existing annotation, evidence-line, or argument-position structures is preferred; a profile MAY use another explicit representation, but consumers MUST NOT infer pairing from parallel repeated lists.

Contradiction is not resolution or lifecycle disposition. Conflict detection, contradiction review, resolution/disposition, deprecation, rejection, supersession, withdrawal, and lifecycle change are separate facts or events. Recording conflict MUST NOT by itself imply rejection, deprecation, supersession, withdrawal, deletion, or another disposition of either side. A later resolution/disposition MUST be separately represented, through a governance transition, resolution record, or equivalent profile-declared event/record with its own provenance; a link such as `kee:resolutionOutcome` MAY connect the contradiction record to that separate record, and the contradiction relation and its history remain preserved. A contradiction record's review status (Section 9.2) is not resolution or disposition of the contradiction: an accepted contradiction record is an accepted record of a conflict, and says nothing about whether the conflict is resolved or which side prevails.

### 13.2 Promotion

Promotion means an authorized, deliberate governance transition that expands the applicability scope of a governed artifact. Promotion does not mean stronger authority, greater popularity, usage, adoption, retrieval frequency or reuse, higher confidence or epistemic standing, a lifecycle change by itself, or merely a different scope value. Authority changes remain authority/governance transitions; epistemic standing changes remain assessment or other profile-owned transitions; popularity and adoption remain signals/evidence unless an authorized promotion decision uses them as inputs.

A promotion record MUST NOT conform merely because source and target scopes are different. The applicable profile/domain MUST declare a machine-checkable scope ordering relation or decision procedure demonstrating that the target scope is broader than the source scope: for example a declared SKOS broader/narrower hierarchy, a containment relation over organizational, geographic, jurisdictional, audience, or applicability scopes, another profile-declared partial order, or a deterministic decision procedure with equivalent behaviour. The ordering mechanism is profile/domain-owned; KEE defines no universal scope lattice. A narrowing, incomparable scope change, equal scopes, or a mere unequal pair MUST NOT be classified as Promotion, and **an ordering that is cyclic between source and target cannot demonstrate breadth**.

`shacl/promotion-profile.ttl` implements the cyclic case: a `skos:broader` ordering in which `kee:sourceScope` and `kee:scope` are mutually broader is rejected. A record whose scopes are related only by such a cycle does not conform to the Promotion shape.

Promotion MUST NOT suppress, erase, hide, or silently detach known contradictions associated with the source artifact, and does not resolve a contradiction merely by broadening scope. This is a procedural obligation; structural validation of a supplied `kee:knownContradiction` link cannot prove that every known contradiction was carried forward. Executable conformance evidence MUST detect omission where the applicable procedure requires carry-forward.

Executable coverage for a Promotion contract MUST prove at minimum that scope narrowing is not Promotion; that popularity, usage count, adoption, retrieval frequency, or reuse alone cannot establish Promotion; that an unauthorized promotion fails the applicable contract; and that suppression or omission of a known contradiction is detected.

---

## 14. Temporal, history, and retrieval semantics (Normative)

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

SPARQL, SQL, Cypher, APIs, event projections, Memento access, and similar mechanisms are execution mechanisms; they do not by themselves define semantic query intent. In the RDF reference representation, `dcterms:temporal` identifies the requested OWL-Time instant or interval, `kee:queryTimeDimension` identifies the time dimension, `kee:queryPattern` is the profile-owned open classifier of the pattern, and `dcterms:source` identifies the history/dataset source whose temporal coverage is asserted separately. Legacy `kee:queryInstant` remains readable but is not the new-write representation.

From this baseline, by a recorded decision, `kee:queryTimeDimension` takes its value from the query-time-dimension scheme published at `https://w3id.org/kee/vocab/query-time-dimension#` (`qtd:` below; Section 10; `schemas/skos/query-time-dimension.ttl`), so that item 2 above is identifiable from the value itself. The scheme has exactly two concepts: `qtd:RecordedTime`, recorded, transaction or known-as-of time, on which the query asks what the history source had recorded at the requested time; and `qtd:ValidTime`, valid, application or active-at time, on which the query asks what applied in the modelled world at that time regardless of when it was recorded. A bitemporal question is two query records over the same history source. The slot is closed: `shacl/historical-bitemporal-querying-profile.ttl` constrains it by `sh:in` over those two concepts, and the check on a new-write record (one declaring `dcterms:conformsTo`, or no conformance carrier) reports at `sh:Violation` from this baseline. Because that profile is Draft / Non-Normative, a point-in-time query record that wrote a dimension IRI of its own conformed structurally to that shape under v0.10.0, whose text called the slot an open classifier, and does not conform under v0.11.0; v0.10.0 is the last version in which such a value conforms and v0.11.0 the first rejecting version (Section 17.3). A registered-legacy record, one declaring only `kee:profileConformance`, is reported at `sh:Warning` and stays readable for as long as that carrier is (Section 17); a consumer MUST NOT infer a scheme concept from such a value. The public normative contract is unchanged (Sections 18.2, 25). `kee:queryPattern` remains open.

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

From this baseline, by a recorded decision, `kee:eligibilityCategory` takes its value from the retrieval-eligibility scheme published at `https://w3id.org/kee/vocab/retrieval-eligibility#` (`elig:` below; Section 10; `schemas/skos/retrieval-eligibility.ttl`), so that two independent implementations name the same category by the same identifier. The scheme has exactly seven concepts: `elig:EligibleForNormalGrounding`, `elig:EligibleOnlyWithWarning`, `elig:EligibleOnlyForHistoricalExplanation`, `elig:EligibleOnlyAsSupersededContext`, `elig:EligibleOnlyAsContradictoryEvidence`, `elig:ExcludedFromCurrentAnswerGrounding` and `elig:RequiresHumanReview`. Each is a decision about one consumer/use operation; none is a lifecycle state, a confidence level, an authority claim or a statement about truth, and the warning and review routing a category calls for is carried by `kee:warningContent`, `kee:humanReviewRequired` and `kee:excludedFromCurrentAnswerGrounding`, which the category does not replace. The slot is closed: `shacl/ai-grounded-retrieval-profile.ttl` constrains it by `sh:in` over those seven concepts, and the check on a new-write result (one declaring `dcterms:conformsTo`, or no conformance carrier) reports at `sh:Violation` from this baseline. Because that profile is Draft / Non-Normative, a retrieval result that wrote a category IRI of its own conformed structurally to that shape under v0.10.0 and does not conform under v0.11.0; v0.10.0 is the last version in which such a value conforms and v0.11.0 the first rejecting version (Section 17.3). A registered-legacy result, one declaring only `kee:profileConformance`, is reported at `sh:Warning` and stays readable for as long as that carrier is (Section 17); a consumer MUST NOT infer a scheme concept from such a value. The public normative contract is unchanged (Sections 18.2, 25). An eligibility category is derived from upstream lifecycle, contradiction, supersession and related metadata of the governed artifact; a governance record's review status (Section 9.2) is not the lifecycle state of the artifact the record governs and MUST NOT be read as such an input.

Retrieval conformance evidence MUST go beyond declarative field presence. Executable tests MUST demonstrate at minimum that the declared eligibility basis materially affects the decision outcome; that warning/review requirements are triggered by the applicable eligibility category/policy; that exclusion from current-answer grounding does not delete the source artifact or its history; and that citation precision is no finer than the governed/indexed unit actually mapped by the retrieval system.

### 14.6 Query capabilities, not a query language

KEE defines query capabilities, not a KEE query language. Implementations MAY use SPARQL, SQL, Cypher, GraphQL, APIs, event projections, search services, or other mechanisms.

Implementations SHOULD support operationally equivalent queries for: artifact by identifier; artifact provenance; artifact lifecycle state and state history; artifacts active at a point in time; artifacts valid during an interval; deprecated artifacts and reasons; supersession chains; contradictions involving an artifact; artifacts by authority; artifacts by scope and context; artifacts pending or due for review; and confidence-related queries when the applicable profile implements confidence.

A system claiming an operational capability MUST be able to demonstrate the behaviour; storing equivalent metadata alone is not sufficient.

---

## 15. Conformance framework (Normative)

### 15.1 Conformance declaration

A conformance claim MUST use `dcterms:conformsTo` for new writes. A KEE conformance declaration MUST identify:

- the KEE specification baseline or release candidate claimed;
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

### 15.8 Conformance targets

The obligations of this specification fall on four targets: a **producer**, a **consumer**, a **validator** and a **profile claimant**. One implementation is often more than one target at once, and an obligation on "an implementation" or "a conforming implementation" in the sections above binds every target to which it applies. This section names each target and collects, with the section that states it, what that target MUST and MUST NOT do. It adds no obligation and changes none: where this section and a cited section differ, the cited section controls, and an obligation the cited section states as SHOULD or MAY keeps that force. Obligations stated on a profile rather than on an implementation (Sections 5, 8.4, 9.1, 9.2, 11, 12.1 and 16) bind the profile's definer; a claimant of that profile relies on them through the profile it claims.

**Producer** — an implementation that creates or serializes governed artifacts, records or declarations for exchange. A producer:

- MUST use `dcterms:conformsTo` for a new conformance declaration and `dcterms:type` for a new controlled artifact classification, and MUST NOT use `kee:supersedes` or `kee:supersededBy` in new serialization (Sections 8.1, 8.2, 8.3);
- MUST use the canonical form named by the migration registry for new data (Section 17.1), MUST NOT mint or rely on generic lifecycle values where a profile-specific scheme owns the state dimension (Section 9.2), and MUST NOT use `kee:assertionTime` for new writes as an ambiguous catch-all (Section 14.1);
- MUST NOT silently collapse distinct temporal roles into one timestamp (Section 0.5), and MUST preserve producer, consumer, activity, model, instrument, process or workflow metadata where it is material to the applicable profile or governance policy (Section 1.1);
- MUST make each evidence-to-side pairing in a contradiction representation, and each agent, role and authority-evidence pairing in an authority grant, mechanically identifiable rather than relying on flat repeated properties (Sections 12.4, 13.1);
- MUST NOT collapse authority scope and artifact applicability scope on value equality alone (Section 12.2), MUST NOT upgrade a close, broad, narrow or related crosswalk mapping to exact on label resemblance (Section 9.4), and MUST NOT put a dispute's resolution, a grant's expiry or revocation, a recorded state, a mapping strength or epistemic standing on the governance-record review-status axis (Section 9.2);
- MUST declare, in a historical query record, the temporal target, exactly one time dimension, the pattern and the coverage assumptions (Section 14.2), and in a retrieval decision record the artifact, the consumer context, the category, the basis, the provenance and time, and routing where the policy requires it (Section 14.5);
- MUST preserve history: a revocation MUST NOT erase a prior grant (Section 12.2), a materialized chain target MUST NOT erase intermediate replacement history (Section 8.3), a review-status change MUST NOT erase the earlier value or its provenance (Section 9.2), and migration MUST be explicit and provenance-preserving (Section 17.1).

**Consumer** — an implementation that reads, interprets, queries or acts on governed artifacts. A consumer:

- MUST preserve the seventeen non-collapse distinctions whenever both sides are represented or material to the claimed profile (Section 7.1), and MUST NOT infer one of two related concepts from the other merely because they co-occur or share a label (Section 0.6);
- MUST NOT assign epistemic privilege or penalty solely on the basis of producer or consumer type (Section 1.1), MUST NOT assume identity implies authority (Section 7.2), and MUST NOT interpret attribution, association, authorship or derivation as authorization (Section 12.1);
- MUST interpret `kee:lifecycleState` through the governing profile or declared vocabulary, MUST NOT treat it as a universal state machine, MUST NOT assume a generic value has one meaning across profiles, and MUST NOT infer a review-status concept from a generic lifecycle value (Section 9.2); MUST NOT read a governance record's review status as resolution, validity, recorded state, mapping strength, epistemic standing or the governed artifact's lifecycle (Sections 9.2, 12.2, 13.1, 14.5);
- MUST NOT assume a class IRI and a classification value are identical because labels are similar (Section 8.2), MUST NOT treat replacement and revision as synonyms (Section 8.3), and MUST NOT infer which temporal role a legacy `kee:assertionTime` value plays without further evidence (Section 14.1);
- MUST NOT treat absence of a confidence assertion as low confidence, rejection, falsity or lack of support, MUST NOT treat a bare value or unqualified label as interoperable confidence, and MUST evaluate the declared interpretation contract where the profile requires one (Section 11);
- MUST NOT infer pairings from parallel repeated lists (Sections 12.4, 13.1), MUST NOT treat recorded conflict as rejection, deprecation, supersession, withdrawal, deletion or another disposition of either side (Section 13.1), and MUST NOT infer a stale artifact false or an archived artifact currently applicable (Section 9.3);
- MUST NOT report a point-in-time answer as complete merely because the query is executable (Section 14.3), MUST compose a historical retrieval question with an explicit query-intent representation (Section 14.4), and MUST NOT mutate or silently redefine source truth, lifecycle state, authority, validity, identity, existence or retained history by a retrieval decision (Section 14.5);
- reads a registered legacy form only where the registry records a compatibility policy, and MUST NOT use `owl:sameAs` merely to simplify migration (Section 17.1); SHOULD NOT rely on dereferencing exclusively for any identifier (Section 18.7).

**Validator** — tooling that evaluates artifacts against shapes, schemas or conformance assets and reports the result. A validator:

- MUST NOT report a structural PASS as proof of the profile-semantic, procedural, governance/policy or interoperability dimensions unless they were separately evaluated (Section 15.2); structural validation establishes none of legal validity, enforceable runtime authorization, correctness, exclusivity or trust (Section 12.5);
- MUST compose applicable parent and specialized constraints explicitly, MUST apply Governance Transition parent constraints to records typed only as Promotion or Authority records, and MUST NOT require a producer to duplicate type assertions because it runs without inference (Section 15.6);
- as reference tooling, MUST report for each fixture/profile pairing the profile identity, governance status, shape-contract version, structural result, normative effect and the dimensions not tested, and MUST make the claim-scoped binding distinction explicit (Section 15.5);
- SHOULD reject known legacy mixed-axis lifecycle values where the active profile defines them as another dimension (Section 9.3), and SHOULD report every registered legacy surface present, apply only `rewrite_safe=true` carrier renames on request, and compose the lifecycle-axis constraints with the lifecycle-owning shapes (Section 17.4); MUST NOT infer a review-status concept from a generic lifecycle value (Section 9.2);
- MUST NOT interpret vocabulary use or file format as proof of conformance (Section 8.1), and MUST NOT treat a Draft shape, fixture, example or successful structural validation as creating normative force (Sections 0, 15.6).

**Profile claimant** — an implementation, resource or organization that declares conformance to this specification or to a profile. A claimant:

- MUST identify the baseline claimed, each Accepted / Normative profile claimed and any Draft profile it intends to follow without binding effect, material representation assumptions, applicable validation assets, and known policy dependencies or limitations (Section 15.1), using `dcterms:conformsTo` for new writes (Sections 8.1, 15.1); a new JSON declaration carries `declarationStatus` rather than the historical `conformanceLevel` (Section 15.4);
- is bound by an Accepted / Normative profile's rules only when it claims that profile (Sections 5, 15.6), and when it uses within its claim a dimension that Section 7 assigns to a Draft profile, MUST declare its own vocabulary, policy and structural contract for it (Section 6.4);
- MUST meet the obligations Section 16 states for each profile it claims (Section 16), and takes on none from a profile it does not claim (Section 15.6);
- MUST NOT describe a Capability Level as the sole conformance result or infer that a level proves all five dimensions (Section 15.3), and in a Capability Level claim MUST name the profiles and dimensions through which each capability is realized (Section 22);
- MUST be able to demonstrate any operational query capability it claims (Section 14.6), and MUST include the executable and procedural evidence that Sections 13.2, 14.3 and 14.5 require for the contracts it claims;
- MUST support a new profile promotion or graduation claim with independent interoperability evidence (Section 15.7).

---

## 16. Domain-profile contracts (Normative)

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

`kee:lifecycleState` on an Assertion Metadata record denotes the lifecycle of the **managed assertion unit** the record governs; it is not a review status of the metadata record. Its value is drawn from the lifecycle scheme of the profile governing the managed unit, and when no other profile governs the unit, new writes SHOULD use `https://w3id.org/kee/lifecycle/assertion#`. The governance-record review-status scheme (Section 9.2) is not adopted by this profile and SHALL NOT be used on this slot. This paragraph adds no constraint: the profile shape keeps `sh:nodeKind sh:IRI` without `sh:in`, the composed review-status shape is not composed with it, and generic `https://w3id.org/kee/lifecycle#` values on this slot remain dual-read under their existing registry row and are reported at `sh:Warning` only (Section 9.3).

### 16.5 Lifecycle Crosswalk

The Lifecycle Crosswalk Profile is Draft / Non-Normative unless separately promoted. It maps vocabularies; it does not merge them or authorize source-data replacement merely because a mapping exists. Crosswalk records SHOULD carry source/target vocabulary identity, source/target terms, rationale, provenance, scope/context, temporal qualification, and review status as applicable; the review status is a value from the governance-record review-status scheme the profile adopts (Sections 9.2, 9.4). KEE does not create a separate mapping-relation code list.

---

## 17. Migration and compatibility policy (Normative)

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

## 18. Release completeness and provenance (Normative)

### 18.1 Package atomicity

A change package is release-complete only when all applicable surfaces agree: specification; Accepted / Normative profile text; SHACL; SKOS/value vocabularies; JSON-LD context; examples; positive/negative fixtures; conformance manifest; reference tooling; migration control; decision/provenance evidence; and onboarding/current-state traceability documentation. A surface MAY be marked not-applicable, but omission MUST be explicit rather than silent.

### 18.2 Published public API

Each release MUST publish a machine-readable manifest of its public normative API. The manifest for this release is `normative-api/v0.11.0.json`.

The public normative API comprises the published specification, Accepted / Normative profiles, admitted semantic surfaces, normative non-collapse and interoperability rules, conformance semantics, migration/compatibility behaviour, and other externally relied-upon requirements explicitly made normative. Draft and Non-Normative profiles are **excluded** from the public normative API.

A change to any surface inside the public normative API MUST be classified against the release rules in Section 20. A change to a surface outside it MUST still be recorded where it alters observable conformance behaviour, and MUST NOT be presented as no change at all.

Tooling that diffs release manifests sees only the surfaces those manifests enumerate. Where a change lies outside the manifest — in a shape graph, a concept scheme, the JSON-LD context, or an example package — manifest diffing MUST NOT be relied upon as the sole classification evidence, and the change MUST be classified by inspection.

### 18.3 Term registry (pointer to the annex)

The term registry required by Section 4.2 is the project's record of every KEE-owned semantic surface, its admission criteria and its disposition; what the registry records, and the dispositions it uses, are stated in the informative annex, Section A.2. A term's current standing is one lookup in that registry (Section 4.2).

`vocab/kee.ttl` is the term-declaration document for the KEE-owned classes, properties, and undeclared registered-legacy values. It is generated from the term registry and asserts no axiom: no `rdfs:domain`, `rdfs:range`, `rdfs:subClassOf`, `rdfs:subPropertyOf`, `owl:equivalentClass`, `owl:equivalentProperty`, `owl:inverseOf`, `owl:disjointWith`, or `owl:sameAs`, and properties are typed `rdf:Property` rather than as object or datatype properties. Declaring a retained term is not a semantic claim; those axioms would be.

### 18.4 Prior-art provenance (pointer to the annex)

The release evidence the project keeps for every adopted external replacement, and for every external standard this specification names as a SHOULD-level replacement, is described in the informative annex, Section A.3. That evidence supports the normative change chain; it does not make a cited source part of KEE's normative text unless a profile or this specification explicitly adopts it.

### 18.5 Non-collapse behavioural coverage (pointer to the annex)

The release suite preserves executable evidence for the Section 7.1 non-collapse rules. Which of the seventeen rules the suite demonstrates at this baseline, and why NC-03 and NC-06 are not demonstrable for a representational rather than an epistemic reason, are stated in the informative annex, Section A.4. Coverage does not alter binding effect: every rule in Section 7.1 binds a conforming implementation whether or not the release suite demonstrates it, and a consumer reading a recorded classification such as `kee:causeType` reads data and does not thereby judge correctness, genuineness or integration, which are the judgments Section 7.1 keeps separate.

### 18.6 Release closure (pointer to the annex)

The release-closure check a release of this specification passes before publication is described in the informative annex, Section A.5. It binds the project's release process, not an implementation.

### 18.7 Namespace registration and dereference

The canonical namespaces of Sections 8.2, 9.2, 10, and the profile identifiers of Section 5 are persistent identifiers under `https://w3id.org/kee/`.

Registration under the W3ID project is merged for every identifier v0.10.0 carried. Resolution was re-verified on 2026-10-12, from a network path outside the publishing infrastructure, by requesting each identifier with an RDF media type and with `text/html` and following every redirect to its final response. The result, which this section records and does not generalize:

- `https://w3id.org/kee` **content-negotiates**: a request for `text/turtle` resolves to the published term declarations (`vocab/kee.ttl` on the public repository's default branch; on the verification date, byte-identical to the term declarations v0.10.0 published, which this release's declarations replace on publication), a request for `application/ld+json` to the published JSON-LD context, and any other request to the public repository's human-readable page.
- `https://w3id.org/kee/artifact`, `https://w3id.org/kee/confidence`, the five profile-specific lifecycle namespaces that v0.10.0 carried (`https://w3id.org/kee/lifecycle/assertion`, `/scientific-claim`, `/organizational-memory`, `/decision` and `/software-engineering`) and the two local vocabulary namespaces that it carried (`https://w3id.org/kee/vocab/contradiction-cause` and `https://w3id.org/kee/vocab/assertion-unit-kind`) each **resolve to their published SKOS concept scheme** by one unconditional redirect: the same document is served whatever media type is requested, so these identifiers resolve but do not content-negotiate.
- The RDF documents above are served under the media type `text/plain; charset=utf-8`, not under an RDF media type. A consumer that dereferences one MUST parse the response as Turtle (or, for the context, as JSON-LD) on the strength of the published format rather than of the served media type, and MUST NOT treat the served media type as evidence that the document is not RDF.
- The generic `https://w3id.org/kee/lifecycle` namespace and the profile identifiers of Section 5 (`https://w3id.org/kee/profile`) redirect to human-readable pages of the public repository (the published specification directory and the profile status index) whatever media type is requested; neither resolves to RDF.
- The three namespaces added at this baseline, `https://w3id.org/kee/lifecycle/governance-record#`, `https://w3id.org/kee/vocab/query-time-dimension#` and `https://w3id.org/kee/vocab/retrieval-eligibility#`, are **registration pending**: on 2026-10-12 each returned `404`. Each needs its own redirect rule registered upstream and verified from outside the publishing infrastructure, and this specification does not describe any of them as resolving.
- The version identifier of the previous release, `https://w3id.org/kee/v0.10.0`, returned `404` on 2026-10-12: no version-pattern rule is registered, and this specification does not describe its own version identifier, or any earlier one, as resolving.

This specification MUST NOT be read as claiming more than the list above for any identifier, and a future baseline SHOULD record when any item changes. A consumer needing a machine-readable definition for a namespace not confirmed to resolve to RDF SHOULD read the corresponding SKOS scheme or shape graph from the repository directly rather than rely on dereferencing.

What a resolving identifier resolves to is governed rather than incidental:

- the unversioned identifier `https://w3id.org/kee` denotes the **current published baseline**, and its meaning changes only when a release is published;
- each published release also carries a **version identifier** denoting the vocabulary as that release published it, which does not change afterwards and is a frozen artifact under Section 18.9;
- the served term-declaration document names the version it is, so a consumer can tell which release it received without comparing bytes; and
- the base identifier content-negotiates as stated above, and each scheme namespace that resolves serves its published concept scheme regardless of the requested media type.

Two limits are normative, because resolution and persistence are different claims:

- **Resolution is not durable persistence.** That an identifier resolves today is verified for the identifiers named above. Durable operational persistence is a claim about future behaviour, and this specification, its profiles, and its release evidence MUST NOT describe any KEE identifier as guaranteed-persistent on the strength of a verified resolution alone.
- **A consumer MAY rely on dereferencing a confirmed identifier and SHOULD NOT rely on dereferencing exclusively, for any identifier.** A consumer whose correctness depends on obtaining a definition SHOULD also be able to read the term-declaration document `vocab/kee.ttl` and the SKOS and SHACL assets published with this specification, because a redirect service is an operational dependency that this specification does not control.

The identifiers remain canonical for new writes under Sections 8.2, 9.2, and 10, whether or not resolution for a given one has yet been confirmed; an identifier can be canonical without being resolvable, and confirming resolution for one identifier does not confirm it for another in the same family.

The Section 4.3 "stable identifiers" criterion is satisfied as a governed, versioned, non-changing identifier; it is additionally satisfied as a resolvable one for the specific identifiers named above. Control of the `w3id.org/kee` path is exercised through the registered redirect and is not exclusive control of the resolving infrastructure, which is why the persistence limit above holds regardless of which identifiers currently resolve.

### 18.8 Current-state drift (pointer to the annex)

Living/current-state surfaces are synchronized at each release, and the rule the project's registered examples and fixtures follow is in the informative annex, Section A.6. Retained legacy compatibility examples remain historical evidence; a legacy example MUST NOT be presented as canonical new-write guidance merely because it remains executable during the compatibility window.

### 18.9 Frozen denominators and living controls (pointer to the annex)

Release evidence divides into **frozen denominators** and **living controls**; both terms are defined in Section 21, and the rule for each kind, which artifacts are of which kind, and the default where a specification does not state an artifact's kind are in the informative annex, Section A.7. Section 17.2, which makes the migration registry a living control, and Section 18.7, which makes a version identifier a frozen artifact, are read under those definitions.

### 18.10 Optional candidate surfaces (pointer to the annex)

The optional candidate surfaces this release publishes are listed in the informative annex, Section A.8. They are non-required: an implementation that ignores all of them remains conforming. The RO-Crate KEEpack packaging experiment among them remains **Experimental / Non-Normative** and requires independent producer/consumer evidence under Section 15.7 before any graduation claim.

---

## 19. Profile status at publication (Normative)

At v0.11.0:

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

v0.11.0 promotes no profile. Executable assets for a Draft profile remain design/structural evidence only and do not promote it. Draft and Draft / Non-Normative have identical normative effect at this baseline (Section 21).

---

## 20. Release policy and change discipline (Normative; pointer to the annex)

Version numbers communicate compatibility: **PATCH** is a backward-compatible correction or consolidation; **MINOR** is a backward-compatible addition or material extension; and **MAJOR** is an incompatible change to the public normative contract. For pre-1.0 KEE releases, published `0.y.z` baselines deliberately follow a stricter compatibility policy than vanilla major-zero SemVer: a published PATCH release MUST NOT hide an incompatible change. Once published, v0.11.0 is immutable and MUST NOT be substantively rewritten in place. The governed pipeline a change follows, the append-only rule for decision records, the use of amendments, and the rule that publication synchronization MUST NOT be used to hide semantic changes govern the project's own process and are carried unchanged in the informative annex, Section A.9.

---

## 21. Terminology (Normative)

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
- **Governed artifact** — a knowledge artifact within a declared KEE conformance scope: identified as a managed unit (Section 7.0) and carrying, or evaluated through, the applicable profile dimensions (Section 7.3). An artifact is governed by virtue of being within a declared conformance scope, not by carrying any particular KEE term. "Governed claim" (Section 0.5) and "governed knowledge" (Section 1.1) are used in the same sense.
- **Dual-read** — the compatibility posture in which tooling reads both a registered legacy surface and its canonical replacement, while new writes use only the canonical surface (Section 17.1). A legacy surface is dual-read only where the migration registry records a read policy for it (Section 17.2); when a legacy read is retired, the migration notice names the last dual-read version and the first rejecting version (Section 17.3).
- **Rewrite-safe** — a migration-registry classification of a legacy-to-canonical mapping stating whether automatic rewriting preserves meaning (Section 17.2). `rewrite_safe=true` permits tooling to rename the carrier on request without changing values, class membership, graph identity, provenance or lifecycle meaning (Section 17.4); `conditional` requires the reviewed mapping evidence for the specific record (Section 8.3); an unsafe semantic split is not rewritten (Section 17.1). Rewrite safety is a property of the mapping, not of the term.
- **Release control** — a machine-checked test or artifact that asserts a property of a release against the baseline, so that a scheduled or promised change cannot lapse unobserved. The controls that enforce the v0.10.0 accountable-root escalation (Section 12.3) and the v0.12.0 review-status escalation (Section 9.2) are release controls. The rule the controls exist to enforce is stated in Section 0: a KEE term may disappear; its audited obligation may not disappear silently.
- **Frozen denominator** — a release artifact fixed at publication and not edited afterwards, whose purpose is to be the fixed set that later work is measured against; a correction is issued as a new artifact that supersedes it (Section 18.9). A release's version identifier is one (Section 18.7).
- **Living control** — a release artifact that is updated as governed decisions are made, whose purpose is to describe current behaviour, so that a stale one is a defect (Section 18.9). The migration registry (Section 17.2) and the compatibility window (Section 17.3) are living controls.
- **Profile status ladder** — the statuses a profile or candidate surface carries at publication (Section 19), and their normative effect. **Accepted / Normative**: binding on an implementation that claims the profile (Sections 5, 15.6) and part of the public normative API (Section 18.2). **Draft** and **Draft / Non-Normative**: identical normative effect at this baseline. Claiming either records intent without binding effect (Sections 6.4, 15.1); both are excluded from the public normative API (Section 18.2); where Section 7 assigns a dimension to such a profile, the profile is the future owner and the core contract the owner of record (Section 6.4); executable assets do not promote it (Section 19). The suffix is historical: an earlier baseline distinguished a Draft that no decision record had adopted from one adopted as recorded design direction. That distinction has no effect at this baseline, and collapsing the two labels into one is recommended as a later recorded decision, because the labels also appear in the public-API manifest's profile statuses and in the profile status index, which a label change must update together. **Experimental / Non-Normative**: an optional candidate surface an implementation may ignore and remain conforming (Section 18.10). **Informative / Non-Normative**: applied to a vocabulary rather than a profile, whose values are not interoperable semantics without a profile-defined interpretation contract (Section 10). Movement up the ladder is a governed act that requires independent interoperability evidence (Section 15.7). Declaration status (Section 15.4) is a different axis: it describes an implementation's declared support maturity, not a profile's status.
- **KnoEdg** — the project responsibility boundary for epistemic-governance and organizational-memory concerns (Section 5).
- **Eidos** — the project responsibility boundary for entity, agency, sovereignty, intent, identity, responsibility, policy, decision, and continuity concerns (Section 5). KnoEdg and Eidos are architectural responsibility boundaries, not mandatory KEE-owned semantic layers (Sections 0, 5); a conforming profile may use external identity, authorization, policy, credential, organizational or domain mechanisms for the concerns Eidos names. The Eidos specification is versioned separately and is not part of the KEE normative contract.

---

## 22. Capability Levels (Normative)

Capability Levels are cumulative packaging of implementation capabilities. They are reported separately from the five conformance dimensions and are neither an aggregate conformance result nor a substitute for a conformance declaration (Section 15.3). Each level presumes the capabilities of the levels below it.

- **Level 0 — Informational alignment.** Uses KEE terminology and principles without machine-actionable governance.
- **Level 1 — Artifact registry.** Manages identifiable artifacts with stable identifiers, classification, profile-owned lifecycle state where the profile requires it, source or creator, timestamps, and basic retrieval.
- **Level 2 — Governed lifecycle.** Adds transition records, responsible agents, authority metadata with a declared authorization basis, deprecation support, replacement/revision support, and validation of required metadata.
- **Level 3 — Temporal and provenance-aware governance.** Adds a PROV-compatible provenance model or equivalent, temporal validity, invalidation, lifecycle history, and point-in-time or event-log reconstruction with declared history coverage.
- **Level 4 — Epistemic governance.** Adds contradiction records, profile-defined confidence or epistemic-standing structures, promotion records with machine-checkable scope ordering, review intervals, staleness handling, and machine-actionable governance constraints.

A Capability Level claim MUST name the profiles and dimensions through which each capability is realized; a level does not imply conformance to any profile.

---

## 23. References (Normative; Section 23.2 is informative)

Editions and dates are those verified on 2026-09-18 and carried unchanged into this release. Status is recorded so that later convergence is not represented as historical influence (Section 4.1).

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

## 24. Open items at this baseline (Informative; pointer to the annex)

The open items at this baseline are listed in the informative annex, Section A.10, so that a reader does not have to reconstruct them. None of them is depended upon by a published surface, and none blocks conformance to this baseline. Two concern obligations stated in this document: the governance-record review-status escalation scheduled for v0.12.0 (Section 9.2), and the undecided question of whether the Assertion Metadata lifecycle slot will ever reject a generic or mixed-axis value (Sections 9.3, 16.4).

---

## 25. Release notes (Informative; pointer to the annex)

The release notes for v0.11.0, the retained notes for v0.10.0 and v0.9.2, and the statement of the contract carried unchanged are in the informative annex, Section A.11. The notes record, as Section 18.2 requires, the conformance-behaviour change of the composed review-status shape (Section 9.2) and the closing of the `kee:queryTimeDimension` and `kee:eligibilityCategory` slots in two Draft / Non-Normative shapes (Sections 14.2, 14.5), each with its negative case. Section 0 states this release's classification; the notes add no obligation.

---

## 26. Security and Privacy Considerations (Informative)

This section states no obligation. It names where the obligations stated elsewhere in this specification meet security and privacy, so that an implementer or a profile definer can plan for them. Key words in this section are not used in the Section 0.1 sense.

### 26.1 Dereference depends on infrastructure this specification does not control

The canonical identifiers are persistent identifiers under a community redirect service, and the registered redirects resolve to a hosting platform the project does not operate (Section 18.7). A consumer that fetches a definition at run time depends on both: on their availability, and on their returning the bytes the project published. Section 18.7 already says a consumer should not rely on dereferencing exclusively and may read the published term declarations, SKOS schemes and shape graphs directly. The security corollaries are these. Pin the published artifacts an implementation validates against, by release and by content; the public-API manifest names the release and the shape-contract version (Section 0.2), and each release's term declarations name the version they are (Section 18.7). Verify what a resolving identifier returns against the published artifact before trusting it, because a redirect can be changed by whoever controls the registry entry or the target. Treat an unexpected change in served content as a reason to stop rather than as a new version, since the unversioned identifier's meaning changes only when a release is published (Section 18.7). Prefer the version identifier where reproducibility matters, and note that Section 18.7 does not yet confirm that version identifiers resolve.

### 26.2 Personal data in accountable roots, attribution and provenance

Section 12.3 requires every grantee of governance authority to resolve, directly or through a delegation chain, to an accountable `prov:Person` or `prov:Organization`. Sections 1.1 and 12 require producer, reviewer, approver and delegation metadata to be preserved where it is material; Section 11 requires the assigning agent of a confidence assessment to be declared; Section 14.5 requires decision provenance on a retrieval decision. A governed graph therefore ordinarily identifies natural persons, and that is the point: accountability (Section 7.1, NC-03) cannot be established against an anonymous root. Wherever a natural person is identified, the graph is personal data under data-protection law, and nothing in this specification decides the lawful basis, the minimisation, the access control or the retention period for it; those belong to domain or implementation governance (Section 7.4). The obligations leave room for them. Section 12.3 requires that the accountable root be resolvable through the declared chain; it does not require that every consumer be able to resolve the chain, that the root be identified by a globally public identifier, or that the identifier be a name. An organisation-scoped or pseudonymous identifier whose resolution is controlled by the party that governs the record satisfies the obligation for every party that can resolve it. Attribution and association (Section 12.1) likewise identify an agent without requiring that the agent's identity be exposed beyond the parties that need it. A profile for a domain where this matters should say which parties can resolve its agents, and an implementation should treat the agent identifiers it exports as the personal data they are.

### 26.3 Retention, deletion and erasure against history preservation

Several obligations preserve history: a revocation does not erase a prior grant (Section 12.2); a resolution does not erase the contradiction relation and its history (Section 13.1); promotion does not suppress or detach known contradictions (Section 13.2); a materialized chain target does not erase intermediate replacement history (Section 8.3); a review-status change does not erase the earlier value (Section 9.2); retrieval exclusion does not delete the artifact or its history (Section 14.5; NC-17); migration preserves source provenance (Section 17.1); and deprecation preserves the artifact historically (Section 21). An erasure request, a legal hold, a records-disposition schedule or a security incident may nonetheless require actual deletion. The specification anticipates this in its definition of deprecation, which preserves an artifact "unless legal, safety, privacy, or security requirements require removal", and it nowhere forbids a deletion that such a requirement compels. What it asks is that deletion be a recorded governance act rather than a silent mutation of history: NC-10 (record preservation vs. current applicability) and NC-17 (retrieval exclusion vs. deletion) exist so that a consumer can tell retention, exclusion and deletion apart. An implementation that must delete can keep a governance record of the deletion (what was removed, under whose authority, under which requirement, and when) without keeping the content, and that record also serves Section 14.3: a point-in-time query whose requested instant falls within a deleted range should be reported as history-insufficient rather than answered as though the record never existed. A profile for a domain where erasure is routine should state what its records keep after deletion.

### 26.4 Validating untrusted RDF

A validator consumes graphs from parties it may not trust. Parsing and SHACL evaluation are not free: a crafted input can be large or deeply nested, can contain blank-node structures and property paths that make evaluation expensive, and can declare prefixes or IRIs that mimic the canonical namespaces (Section 10 notes that a declared prefix is only a serialization convenience and proves nothing). The published shape graphs include one SPARQL-based constraint, the Promotion shape's cyclic-scope check (Section 13.2); a SPARQL-based constraint runs a query pattern against the data graph, and a SHACL processor that also accepts shapes supplied with the input, or that follows `owl:imports` or fetches a remote JSON-LD context, extends the surface it evaluates to whatever the input names. Implementers should run validation under resource limits (input size, triple count, time and memory); validate only against the published shape graphs, which are byte-identical to those the reference validator executes (Section 0.2), and never against shapes supplied with the data; disable or sandbox network access during parsing and validation; treat literals from the data, and any message text derived from them, as untrusted when rendering a report; and record the severity policy a result was computed under (Section 15.5), since a report that omits it cannot be compared with one that states it. None of this changes what conformance means (Section 15); it concerns evaluating it safely.
