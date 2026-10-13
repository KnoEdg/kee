# One artifact, end to end

**Informative / Non-Normative.** This page follows one governed artifact through six of the published examples and names, at each step, the distinction the specification keeps separate (a Section 7.1 non-collapse rule), the shape that checks what can be checked structurally, and the command that reproduces the result. Nothing here adds an obligation; the specification at `docs/specs/KEE-Specification-v0.11.0.md` governs, and the rule identifiers it assigns are listed in `normative-api/v0.11.0.json`.

The artifact is `ex:runbook-incident-triage-v3`, an incident-triage runbook. It is recorded as an assertion; an authority grant lets a named person act on it; a contradiction with a sibling runbook is recorded and left unresolved; a promotion widens its scope from one team to the whole engineering organization; a point-in-time query asks what was known before the promotion; and a retrieval decision excludes a superseded draft from current-answer grounding without deleting it.

The examples were written one per profile, so they do not all name the same IRIs. Where the chain breaks, the step says so and shows the smallest set of triples a reader would add to join it. The example files themselves are not changed by this page.

## Before you start

Every command below is run from the repository root. The reference validator's `kee check` prints one summary line per file and the full report only for a file that fails; `pyshacl` is the SHACL engine anyone can install. The two agree once `pyshacl` is told to tolerate `sh:Warning` and `sh:Info` results (`-w --allow-infos`), which is the severity rule `shacl/README.md` states; without those flags a file that conforms to KEE reports `Conforms: False` on a tolerated warning. A shape that composes with another (the promotion and authority shapes compose with the governance-transition shape) needs both files loaded; `kee check` takes `--shapes` more than once, and `pyshacl` takes one shapes file, so concatenate.

Several steps edit an example on the way into the validator to show a distinction doing work. The edit is a `sed` expression over the published file and `-` reads the result from standard input, so no file is changed. With `pyshacl`, write the edited text to a file and validate that.

Quoted Turtle is verbatim from the named file and line range; the prefix block at the top of each file is omitted.

## Step 1. The assertion is recorded

`examples/assertion.ttl`, lines 39–57:

```turtle
ex:assertion-001
    a kee:Assertion ;
    rdfs:label "Example assertion about KEE governance"@en ;
    skos:definition "KEE assertion artifacts should preserve provenance and lifecycle metadata."@en ;

    kee:artifactType artifact:Assertion ;
    kee:lifecycleState alife:Normal ;
    kee:profileConformance profile:AssertionProfile ;
    kee:scope ex:scope-kee-repository ;
    kee:context ex:context-specification-dogfooding ;
    kee:authority ex:authority-kee-maintainers ;
    kee:confidenceStatus confidence:ProfileDefined ;
    kee:confidenceValue "0.80"^^xsd:decimal ;

    prov:wasAttributedTo ex:agent-reneyap ;
    prov:wasGeneratedBy ex:activity-capture-assertion-001 ;
    prov:generatedAtTime "2026-06-25T20:20:00Z"^^xsd:dateTime ;

    dcterms:source ex:source-kee-specification-v0-11-0 .
```

**What is kept separate.** The record carries its lifecycle state (`kee:lifecycleState alife:Normal`, a value from the assertion lifecycle scheme), its provenance (`prov:wasAttributedTo`, `prov:wasGeneratedBy`), the authority it claims to sit under (`kee:authority`), its applicability scope (`kee:scope`), its interpretive context (`kee:context`) and a confidence value, each on its own property. Lifecycle state is not epistemic standing (**NC-07**): the assertion lifecycle scheme is limited to disposition states, and Section 9.3 forbids writing a ranking, dispute or assessment standing such as `Challenged` as a lifecycle value. Provenance names who recorded the assertion and is not authority (**NC-02**, Section 12.1); scope and context stay on separate properties (**NC-15**).

**What checks it.** `kee:AssertionProfileShape` in `shacl/assertion-profile.ttl` requires the type, lifecycle state, profile declaration, label, definition, attribution and generation time at `sh:Violation`, recommends a source, scope and context at `sh:Warning`, and reports the legacy `kee:profileConformance` carrier at `sh:Warning`. `kee:AssertionLifecycleAxisShape` in `shacl/lifecycle-status-constraints.ttl` rejects `Preferred`, `Challenged` and `Qualified` as lifecycle values (Section 9.3).

```text
$ kee check examples/assertion.ttl --shapes shacl/assertion-profile.ttl --shapes shacl/lifecycle-status-constraints.ttl
PASS examples/assertion.ttl (sh:Violation 0, sh:Warning 1, sh:Info 0, other 0; focus nodes 1)
[exit 0]

$ pyshacl -s shacl/assertion-profile.ttl examples/assertion.ttl -w --allow-infos
Validation Report
Conforms: True
Results (1):
Validation Result in MaxCountConstraintComponent (http://www.w3.org/ns/shacl#MaxCountConstraintComponent):
	Severity: sh:Warning
	...
	Focus Node: ex:assertion-001
	Result Path: kee:profileConformance
	Message: Legacy surface kee:profileConformance is present; its canonical surface is dcterms:conformsTo (exact replacement, dual-read registered, rewrite-safe). ...
[exit 0]
```

The one warning is the legacy carrier the example keeps on purpose (its header says so). Run `pyshacl` without `-w` and the same file reports `Conforms: False` with exit 1: that is the severity rule, not a defect in the file.

Now write a dispute standing as the lifecycle state. The shape refuses it:

```text
$ sed "s|alife:Normal|<https://w3id.org/kee/lifecycle#Challenged>|" examples/assertion.ttl \
    | kee check - --shapes shacl/assertion-profile.ttl --shapes shacl/lifecycle-status-constraints.ttl
FAIL - (sh:Violation 1, sh:Warning 1, sh:Info 0, other 0; focus nodes 1)
...
Constraint Violation in NotConstraintComponent (http://www.w3.org/ns/shacl#NotConstraintComponent):
	Severity: sh:Violation
	Focus Node: ex:assertion-001
	Value Node: <https://w3id.org/kee/lifecycle#Challenged>
	Result Path: kee:lifecycleState
	Message: Preferred, Challenged, and Qualified are ranking/dispute/assessment standings, not Assertion lifecycleState values.
[exit 1]
```

A challenge is recorded through a contradiction record (step 3), not by changing what state the assertion is in.

**Where the chain breaks.** The assertion example's subject is `ex:assertion-001`; the runbook this page follows is first named in the contradiction, promotion and retrieval examples and is typed only `prov:Entity` there. To record the runbook as an assertion in the same form, a reader adds the properties the shape requires, in the canonical new-write carriers (`dcterms:type`, `dcterms:conformsTo`):

```turtle
ex:runbook-incident-triage-v3
    a kee:Assertion ;
    rdfs:label "Incident triage runbook v3"@en ;
    skos:definition "Escalate a payment-latency alert after 15 minutes."@en ;
    dcterms:type artifact:Assertion ;
    kee:lifecycleState alife:Normal ;
    dcterms:conformsTo profile:AssertionProfile ;
    kee:scope ex:scope-team-observability ;
    kee:context ex:context-specification-dogfooding ;
    prov:wasAttributedTo ex:agent-reneyap ;
    prov:generatedAtTime "2026-04-12T14:30:00Z"^^xsd:dateTime ;
    dcterms:source ex:postmortem-evidence-summary-2026-h1 .
```

Appended to `examples/assertion.ttl` and validated the same way, the file still passes with the same single warning and now reports `focus nodes 2`. The scope is the team scope the promotion in step 4 widens from, and the generation time is the instant the historical example in step 5 uses as the start of the runbook's valid interval.

## Step 2. An authority grant lets an agent act

`examples/authority-delegation.ttl`, lines 32–56:

```turtle
ex:authority-record-priya-standards-chair
    a kee:GovernanceTransitionRecord, kee:AuthorityRecord ;
    rdfs:label "Authority record: Priya, standards committee chair"@en ;
    kee:governedArtifact ex:standards-committee-charter ;
    kee:newLifecycleState ex:status-granted ;
    kee:lifecycleStatusVocabulary ex:authority-status-vocabulary ;
    kee:lifecycleState lifecycle:Supported ;
    kee:profileConformance profile:AuthorityDelegationProfile ;
    kee:authorityEvidence ex:charter-engineering-standards-committee ;
    kee:scope ex:scope-charter-applicability ;
    kee:grantedTo ex:agent-priya-standards-chair ;
    kee:authorityScope ex:scope-org-wide-engineering-governance ;
    kee:validFrom "2026-01-15"^^xsd:date ;
    kee:validUntil "2027-01-15"^^xsd:date ;
    prov:wasGeneratedBy ex:authority-grant-priya-activity ;
    prov:wasAttributedTo ex:governance-log-service ;
    prov:generatedAtTime "2026-01-15T09:05:00Z"^^xsd:dateTime .

ex:authority-grant-priya-activity
    a prov:Activity ;
    prov:qualifiedAssociation [
        a prov:Association ;
        prov:agent ex:agent-vp-engineering ;
        prov:hadRole ex:role-authority-grantor
    ] .
```

**What is kept separate.** The record is attributed to a logging service (`prov:wasAttributedTo ex:governance-log-service`) and was generated by an activity in which a vice-president acted as grantor. Neither of those is the authority. The authority is the grant: who holds it (`kee:grantedTo`), on what basis (`kee:authorityEvidence`, the committee charter), over which scope (`kee:authorityScope`) and for how long (`kee:validFrom`, `kee:validUntil`). Provenance does not authorize (**NC-02**, Section 12.1). The authority scope and the record's applicability scope (`kee:scope`) are different values on purpose (Section 12.2). The same file, lines 93–110, keeps the previous chair's grant with a `prov:invalidatedAtTime` five minutes before Priya's grant was recorded: revocation is a later event that preserves the earlier grant's history (Section 12.2), so the record is retained although it no longer applies (**NC-10**). Lines 86–89 grant a software agent authority through `prov:actedOnBehalfOf ex:agent-priya-standards-chair`, which terminates the chain at a person (Section 12.3).

**What checks it.** `kee:AuthorityProfileShape` in `shacl/authority-delegation-profile.ttl` requires `kee:grantedTo`, `kee:authorityScope` and, with the message "An authority record must identify authority-basis evidence separately from provenance", `kee:authorityEvidence`; it forbids `prov:actedOnBehalfOf` on the record itself. It composes `kee:GovernanceTransitionProfileShape` from `shacl/governance-transition-profile.ttl`, which requires the governed artifact, the new state, the vocabulary, the review status and the provenance triple. `kee:SoftwareAgentAuthorityRootShape` checks every grantee that is not a person or organization for an accountable root (Section 12.3; `sh:Violation` from v0.10.0).

```text
$ kee check examples/authority-delegation.ttl \
    --shapes shacl/authority-delegation-profile.ttl --shapes shacl/governance-transition-profile.ttl
PASS examples/authority-delegation.ttl (sh:Violation 0, sh:Warning 0, sh:Info 0, other 0; focus nodes 7)
[exit 0]
```

Delete line 40, the authority basis, and the record is still fully attributed and still generated by the grantor's activity. It no longer passes:

```text
$ sed "40d" examples/authority-delegation.ttl \
    | kee check - --shapes shacl/authority-delegation-profile.ttl --shapes shacl/governance-transition-profile.ttl
FAIL - (sh:Violation 1, sh:Warning 0, sh:Info 0, other 0; focus nodes 7)
...
	Focus Node: ex:authority-record-priya-standards-chair
	Result Path: kee:authorityEvidence
	Message: An authority record must identify authority-basis evidence separately from provenance.
[exit 1]
```

The accountable-root obligation has its own published negative case:

```text
$ kee check fixtures/invalid/authority-delegation-untyped-grantee-no-chain.ttl \
    --shapes shacl/authority-delegation-profile.ttl --shapes shacl/governance-transition-profile.ttl
FAIL fixtures/invalid/authority-delegation-untyped-grantee-no-chain.ttl (sh:Violation 1, sh:Warning 0, sh:Info 0, other 0; focus nodes 5)
...
	Source Shape: kee:SoftwareAgentAuthorityRootShape
	Focus Node: ex:software-grantee-test
	Message: A grantee that is not a prov:Person or prov:Organization must resolve through prov:actedOnBehalfOf to a terminal prov:Person or prov:Organization authority root. ...
[exit 1]
```

**Where the chain breaks.** The grant governs `ex:standards-committee-charter`, not the runbook. The promotion in step 4 cites the same charter as its authority basis but attributes itself to `ex:agent-standards-chair`, a different IRI from the grantee `ex:agent-priya-standards-chair`. The smallest join is one triple that puts the runbook under Priya's grant; `kee:governedArtifact` has no upper bound, so the record stays valid:

```turtle
ex:authority-record-priya-standards-chair kee:governedArtifact ex:runbook-incident-triage-v3 .
```

Appended to the file and validated as above, the result is unchanged: `PASS` with 7 focus nodes. The two chair IRIs are left as they are. Declaring them the same resource is a modelling decision the examples do not make, and an identity assertion is not the kind of bridge this page adds; a reader who needs the promotion attributed to the grantee writes that attribution with the grantee's IRI.

## Step 3. A contradiction is recorded, not resolved

`examples/contradiction-records.ttl`, lines 27–48:

```turtle
ex:contradiction-escalation-threshold
    a kee:ContradictionRecord ;
    rdfs:label "Contradiction: escalation threshold, payments vs. observability"@en ;
    kee:conflictingArtifact ex:runbook-incident-triage-v3, ex:runbook-incident-triage-payments ;
    kee:lifecycleState lifecycle:Supported ;
    kee:profileConformance profile:ContradictionRecordsProfile ;
    kee:causeType ex:cause-evidence-conflict ;
    dcterms:hasPart ex:side-evidence-org-runbook, ex:side-evidence-payments-runbook ;
    dcterms:description "The org-wide standard runbook recommends a 15-minute escalation threshold based on alert-fatigue postmortem data. The payments team's variant recommends a 5-minute threshold based on a cost analysis of SLA violations. Both recommendations are evidentially supported; the conflict is a difference in risk framing, not an error on either side."@en ;
    prov:wasGeneratedBy ex:detection-escalation-threshold-contradiction ;
    prov:wasAttributedTo ex:governance-log-service ;
    prov:generatedAtTime "2026-07-10T11:21:40Z"^^xsd:dateTime .

ex:side-evidence-org-runbook
    a oa:Annotation ;
    oa:hasTarget ex:runbook-incident-triage-v3 ;
    oa:hasBody ex:evidence-alert-fatigue-postmortem .

ex:side-evidence-payments-runbook
    a oa:Annotation ;
    oa:hasTarget ex:runbook-incident-triage-payments ;
    oa:hasBody ex:evidence-payments-sla-cost-analysis .
```

**What is kept separate.** The record names both sides, pairs each side with its evidence through a Web Annotation node so no pairing has to be inferred from parallel lists (Section 13.1), and classifies the cause: an evidence conflict, "a difference in risk framing, not an error on either side". A recorded contradiction is not a logical inconsistency (**NC-08**); which it is, is read from `kee:causeType`, and the published contradiction-cause scheme in `schemas/skos/contradiction-types.ttl` reserves `DirectContradiction` for "incompatible claims within the same scope, context, and time frame". The record's own `kee:lifecycleState` is its review status, "distinct from the lifecycle state of either conflicting artifact" (the shape's words), so recording the conflict changes neither runbook's state. Resolution is a separate record: the shape admits a `kee:resolutionOutcome` link to it at `sh:Info`, and the example has none, because nothing has been resolved (Section 13.1). An authorized artifact can be contested without losing its authority (**NC-04**): `examples/authority-delegation.ttl`, lines 120–130, records a `kee:ContestedAuthorityClaim` with two claimants over the escalation-threshold scope and links this very contradiction record through `kee:knownContradiction`, while Priya's grant above stands.

**What checks it.** `kee:ContradictionRecordsProfileShape` in `shacl/contradiction-records-profile.ttl` requires at least two `kee:conflictingArtifact` values, one review status, a profile declaration and the three provenance properties; validates each `dcterms:hasPart` node against `kee:ContradictionSideEvidenceShape` (exactly one target, at least one body); and recommends `kee:causeType` and a description at `sh:Warning`.

```text
$ kee check examples/contradiction-records.ttl --shapes shacl/contradiction-records-profile.ttl
PASS examples/contradiction-records.ttl (sh:Violation 0, sh:Warning 0, sh:Info 0, other 0; focus nodes 1)
[exit 0]

$ kee check fixtures/invalid/contradiction-records-missing-second-artifact.ttl --shapes shacl/contradiction-records-profile.ttl
FAIL fixtures/invalid/contradiction-records-missing-second-artifact.ttl (sh:Violation 1, sh:Warning 1, sh:Info 0, other 0; focus nodes 1)
...
	Result Path: kee:conflictingArtifact
	Message: A contradiction record must have at least two kee:conflictingArtifact IRIs.
[exit 1]
```

A contradiction needs two sides; a record with one is a complaint, not a contradiction. The cause classification is a `sh:Warning`-level recommendation, so the shape cannot tell an evidence conflict from a direct contradiction; the consumer-side test named for NC-08 in `docs/non-collapse-traceability.md` does, and shows the two readings moving independently.

**The chain holds here.** The record names `ex:runbook-incident-triage-v3` directly, and the authority and promotion examples each carry a copy of it (their files say so in a comment) so that they conform to the contradiction shape on their own.

## Step 4. A promotion widens the scope

`examples/promotion.ttl`, lines 26–47 and 61–68:

```turtle
ex:promotion-record-runbook-incident-triage-v3
    a kee:GovernanceTransitionRecord, kee:PromotionRecord ;
    rdfs:label "Promotion record: incident-triage runbook to org-wide standard"@en ;
    kee:governedArtifact ex:runbook-incident-triage-v3 ;
    kee:previousLifecycleState ex:local-status-accepted ;
    kee:newLifecycleState ex:org-status-adopted ;
    kee:lifecycleStatusVocabulary ex:lifecycle-profile-org-standards-2026 ;
    kee:lifecycleState lifecycle:Supported ;
    kee:profileConformance profile:PromotionProfile ;
    kee:authorityEvidence ex:charter-engineering-standards-committee ;
    kee:scope ex:scope-org-wide-engineering ;
    kee:context ex:context-standards-committee-q3-2026 ;
    kee:sourceScope ex:scope-team-observability ;
    kee:reasonCode ex:reason-standards-adopted ;
    kee:knownContradiction ex:contradiction-escalation-threshold ;
    skos:changeNote "Adopted as the organization-wide incident-triage standard after committee review of six months of postmortem evidence; a known escalation-threshold disagreement with the payments team's variant remains unresolved and is linked, not erased, by this promotion."@en ;
    dcterms:source ex:postmortem-evidence-summary-2026-h1 ;
    dcterms:valid "2026-08-01"^^xsd:date ;
    kee:reviewDue "2027-02-01T00:00:00Z"^^xsd:dateTime ;
    prov:wasGeneratedBy ex:promotion-activity-runbook-incident-triage-v3 ;
    prov:wasAttributedTo ex:agent-standards-chair ;
    prov:generatedAtTime "2026-07-09T16:31:15Z"^^xsd:dateTime .

ex:scope-team-observability
    a skos:Concept ;
    skos:prefLabel "Team observability scope"@en ;
    skos:broader ex:scope-org-wide-engineering .

ex:scope-org-wide-engineering
    a skos:Concept ;
    skos:prefLabel "Org-wide engineering scope"@en .
```

**What is kept separate.** A promotion is an authorized, deliberate transition that widens applicability scope (Section 13.2). It is not popularity, adoption or retrieval frequency (**NC-09**); none of those appear on the record, and adding a usage count would not make a record a promotion. It is not a stronger authority: the authority basis is the same charter as in step 2. The scope ordering is declared, not assumed: the source scope reaches the target through `skos:broader`, and a narrowing, an equal pair or a cycle is not a promotion. Scope (`kee:scope`, `kee:sourceScope`) and context (`kee:context`, the committee's third-quarter review) remain separate (**NC-15**). The known contradiction from step 3 is carried forward on `kee:knownContradiction` and the change note says why: widening the scope does not resolve the disagreement (Section 13.2). The transition happened on 2026-07-09 and takes effect on 2026-08-01 (`dcterms:valid`); those are different temporal roles (Section 14.1).

**What checks it.** `kee:PromotionProfileShape` in `shacl/promotion-profile.ttl` requires exactly one `kee:sourceScope`, exactly one `kee:scope` and, with the message "Promotion requires explicit authority evidence separate from provenance", `kee:authorityEvidence`; two `sh:sparql` constraints require that the source reach the target through one or more `skos:broader` edges and that the two scopes not be mutually broader. It composes `kee:GovernanceTransitionProfileShape`. Whether every known contradiction was carried forward is a procedural obligation the shape cannot check (Section 13.2); the traceability page names the test that does.

```text
$ kee check examples/promotion.ttl --shapes shacl/promotion-profile.ttl --shapes shacl/governance-transition-profile.ttl
PASS examples/promotion.ttl (sh:Violation 0, sh:Warning 0, sh:Info 0, other 0; focus nodes 1)
[exit 0]
```

Load the promotion shape alone and the inherited requirements are silently absent; `kee check` says so:

```text
$ kee check examples/promotion.ttl --shapes shacl/promotion-profile.ttl
kee check: warning: shapes referenced but not defined in the loaded shapes (they constrain nothing as loaded; pass the shapes file that defines them): https://w3id.org/kee#GovernanceTransitionProfileShape
PASS examples/promotion.ttl (sh:Violation 0, sh:Warning 0, sh:Info 0, other 0; focus nodes 1)
[exit 0]
```

Remove the authority basis (line 35) and the record is an unauthorized widening, which is not a promotion:

```text
$ sed "35d" examples/promotion.ttl \
    | kee check - --shapes shacl/promotion-profile.ttl --shapes shacl/governance-transition-profile.ttl
FAIL - (sh:Violation 1, sh:Warning 0, sh:Info 0, other 0; focus nodes 1)
...
	Focus Node: ex:promotion-record-runbook-incident-triage-v3
	Result Path: kee:authorityEvidence
	Message: Promotion requires explicit authority evidence separate from provenance.
[exit 1]
```

Swap the two scopes (lines 36 and 38) so the record narrows instead of widening:

```text
$ sed -e "36s|ex:scope-org-wide-engineering|ex:scope-team-observability|" \
      -e "38s|ex:scope-team-observability|ex:scope-org-wide-engineering|" examples/promotion.ttl \
    | kee check - --shapes shacl/promotion-profile.ttl --shapes shacl/governance-transition-profile.ttl
FAIL - (sh:Violation 1, sh:Warning 0, sh:Info 0, other 0; focus nodes 1)
...
Constraint Violation in SPARQLConstraintComponent (http://www.w3.org/ns/shacl#SPARQLConstraintComponent):
	Severity: sh:Violation
	Source Shape: kee:PromotionProfileShape
	Focus Node: ex:promotion-record-runbook-incident-triage-v3
	Message: Promotion requires the target scope to be broader than the source scope. In this SKOS reference representation, the source must reach the target through one or more skos:broader edges.
[exit 1]
```

**The chain holds here.** The record governs `ex:runbook-incident-triage-v3` and links the contradiction record from step 3 by its IRI. Its authority basis is the charter from step 2; see step 2 for the attribution IRI that differs.

## Step 5. A point-in-time query asks what was known as of a date

`examples/historical-bitemporal-querying.ttl`, lines 28–38 and 65–77:

```turtle
ex:query-known-as-of-2026-06-01
    a kee:PointInTimeQuery ;
    rdfs:label "Known-as-of query: 2026-06-01"@en ;
    kee:queryPattern ex:query-pattern-known-as-of ;
    kee:queryTimeDimension ex:dimension-transaction-recording-time ;
    dcterms:temporal ex:instant-2026-06-01 ;
    dcterms:source ex:history-source-runbook ;
    kee:profileConformance profile:HistoricalBitemporalQueryingProfile ;
    kee:historyCompleteness ex:completeness-complete ;
    kee:reconstructedArtifact ex:runbook-incident-triage-v2 ;
    dcterms:description "What escalation-threshold guidance did we know on 2026-06-01?"@en .

ex:history-source-runbook
    a prov:Entity ;
    rdfs:label "Retained runbook history"@en ;
    dcterms:temporal ex:history-coverage-2025-through-2026 .

ex:history-coverage-2025-through-2026
    a time:Interval ;
    time:hasBeginning ex:instant-history-start ;
    time:hasEnd ex:instant-history-end .

ex:instant-history-start a time:Instant ; time:inXSDDateTimeStamp "2025-01-01T00:00:00Z"^^xsd:dateTimeStamp .
ex:instant-history-end a time:Instant ; time:inXSDDateTimeStamp "2026-09-01T00:00:00Z"^^xsd:dateTimeStamp .
ex:instant-2026-06-01 a time:Instant ; time:inXSDDateTimeStamp "2026-06-01T00:00:00Z"^^xsd:dateTimeStamp .
```

**What is kept separate.** The query states its intent in data, independently of any query language (Section 14.2): the requested instant (`dcterms:temporal`), what that instant means (`kee:queryTimeDimension`, here recording time, "known as of", rather than valid time), the pattern, and the history source whose coverage is asserted on the source itself. On 2026-06-01 the promotion of step 4 had not happened (it was recorded on 2026-07-09 and takes effect on 2026-08-01), and the answer the example records is the previous revision, `ex:runbook-incident-triage-v2`. That a query can be executed says nothing about whether the retained history covers the instant asked about (**NC-16**, Section 14.3): the advisory `kee:historyCompleteness` value is not coverage evidence, and the shape says so at `sh:Info`.

**What checks it.** `kee:HistoricalBitemporalQueryingProfileShape` in `shacl/historical-bitemporal-querying-profile.ttl` requires exactly one pattern, exactly one time dimension and a profile declaration, at most one requested temporal target, and validates each `dcterms:source` against `kee:HistorySourceCoverageShape`, which requires the source to carry `dcterms:temporal` coverage.

```text
$ kee check examples/historical-bitemporal-querying.ttl --shapes shacl/historical-bitemporal-querying-profile.ttl
PASS examples/historical-bitemporal-querying.ttl (sh:Violation 0, sh:Warning 0, sh:Info 0, other 0; focus nodes 3)
[exit 0]
```

Move the requested instant to 2024-01-01 (line 77), a year before the retained history begins. The query is still well formed and the shape still passes; the shape checks that coverage is declared, not that it covers the instant:

```text
$ sed "77s|2026-06-01T00:00:00Z|2024-01-01T00:00:00Z|" examples/historical-bitemporal-querying.ttl \
    | kee check - --shapes shacl/historical-bitemporal-querying-profile.ttl
PASS - (sh:Violation 0, sh:Warning 0, sh:Info 0, other 0; focus nodes 3)
[exit 0]
```

Whether the history is sufficient is a question for the consumer, and it is answerable from the data the shape required to be present. This SPARQL `ASK` is true exactly when the requested instant lies inside the source's declared coverage:

```sparql
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX time:    <http://www.w3.org/2006/time#>
PREFIX xsd:     <http://www.w3.org/2001/XMLSchema#>
ASK {
  <https://example.org/kee/query-known-as-of-2026-06-01>
      dcterms:temporal/time:inXSDDateTimeStamp ?requested ;
      dcterms:source/dcterms:temporal ?coverage .
  ?coverage time:hasBeginning/time:inXSDDateTimeStamp ?start ;
            time:hasEnd/time:inXSDDateTimeStamp ?end .
  FILTER (xsd:dateTime(str(?start)) <= xsd:dateTime(str(?requested)) &&
          xsd:dateTime(str(?requested)) <= xsd:dateTime(str(?end)))
}
```

Run with rdflib 7.6.0 over the published file and over the edited one:

```text
original: True
instant moved to 2024-01-01: False
```

A conforming system reports the second case as history-insufficient, not as a complete historical answer (Section 14.3). The structural pass is the same in both runs; this is also the plainest demonstration that a structural pass is not full conformance (**NC-12**, Section 15.2).

**Where the chain bends.** The query reconstructs `ex:runbook-incident-triage-v2`, the revision before the one this page follows, which is the right answer for the date asked. The history source `ex:history-source-runbook` is described in this file and again in the retrieval example with the same bounds but a differently named interval resource (`ex:history-coverage-2025-through-2026` here, `ex:history-coverage-runbook` there); merged, the source carries two coverage intervals with identical bounds, which the shape accepts. Lines 54–63 of this file cross-reference the retrieval query of step 6 by its IRI.

## Step 6. A retrieval decision excludes a superseded version

`examples/ai-grounded-retrieval.ttl`, lines 27–34 and 75–89:

```turtle
ex:retrieval-query-escalation-threshold
    a kee:RetrievalQuery ;
    rdfs:label "Retrieval query: payment-latency escalation threshold"@en ;
    kee:profileConformance profile:AIGroundedRetrievalProfile ;
    kee:candidateResult ex:retrieval-result-runbook-v3, ex:retrieval-result-runbook-draft-2025 ;
    dcterms:references ex:historical-intent-active-at-2026-08-15 ;
    dcterms:description "What guidance was active for payment-latency alerts at the requested historical instant?"@en ;
    prov:generatedAtTime "2026-08-15T09:00:00Z"^^xsd:dateTime .

ex:retrieval-result-runbook-draft-2025
    a kee:RetrievalResult ;
    rdfs:label "Retrieval result: 2025 draft (superseded, historical only)"@en ;
    kee:retrievedArtifact ex:runbook-incident-triage-org-draft-2025 ;
    kee:eligibilityCategory ex:eligibility-historical-only ;
    kee:eligibilityBasis "supersession relation (replaced by the current org-wide standard)" ;
    kee:context ex:use-context-current-answer ;
    kee:profileConformance profile:AIGroundedRetrievalProfile ;
    kee:citationGranularity ex:citation-granularity-document-level ;
    kee:supersessionChainTarget ex:runbook-incident-triage-v3 ;
    kee:warningContent "Superseded draft retained for historical context only; do not use for current-answer grounding."@en ;
    kee:humanReviewRequired false ;
    kee:excludedFromCurrentAnswerGrounding true ;
    prov:wasGeneratedBy ex:eligibility-decision-draft ;
    prov:generatedAtTime "2026-08-15T09:00:02Z"^^xsd:dateTime .
```

and lines 94–95 and 100:

```turtle
ex:runbook-incident-triage-v3 a prov:Entity ; rdfs:label "Incident triage runbook v3"@en .
ex:runbook-incident-triage-org-draft-2025 a prov:Entity ; rdfs:label "Incident triage runbook org draft 2025"@en .
ex:retrieval-chunk-091 a kee:RetrievalChunk ; rdfs:label "Retrieval chunk 091"@en ; kee:mapsToArtifact ex:runbook-incident-triage-v3 .
```

**What is kept separate.** The query matched two results. Matching is a retrieval fact; whether a match may ground a current answer is a separate, recorded decision with its own basis, context, provenance and time (Section 14.5), so relevance is not validity (**NC-11**). The 2025 draft is excluded from current-answer grounding because it was superseded, and the exclusion is scoped to this consumer's use context: the draft's own triples, and the supersession history that `kee:supersessionChainTarget` summarizes but must not replace (Section 8.3), remain in the graph. Exclusion is not deletion (**NC-17**). The other result, the runbook this page follows (lines 60–73), is eligible only as contradictory evidence, with `kee:humanReviewRequired true` and a warning that both sides must be presented, because the contradiction of step 3 is still unresolved; promotion did not make it go away. The query's `prov:generatedAtTime` is when the retrieval ran, not the instant asked about; the historical intent is a separate point-in-time query it references (Section 14.4). The chunk at line 100 maps to the runbook by reference: what a chunk refers to is identity, and is not read from where the chunk came from (**NC-01**).

**What checks it.** `kee:RetrievalResultProfileShape` in `shacl/ai-grounded-retrieval-profile.ttl` requires the retrieved artifact, exactly one eligibility category, at least one eligibility basis, a consumer context, the decision activity and the decision time; it describes `kee:excludedFromCurrentAnswerGrounding` at `sh:Info` as "scoped to the current consumer/use decision" and says it "does not imply deletion or universal exclusion". `kee:RetrievalQueryProfileShape` requires the query's profile declaration and generation time.

```text
$ kee check examples/ai-grounded-retrieval.ttl --shapes shacl/ai-grounded-retrieval-profile.ttl
PASS examples/ai-grounded-retrieval.ttl (sh:Violation 0, sh:Warning 0, sh:Info 0, other 0; focus nodes 3)
[exit 0]
```

Delete the exclusion flag (line 87) and the file still passes: the flag is the consumer's decision, and the shape neither requires nor forbids it. What changes is the governed eligibility a consumer reads, and only that; the match set is untouched. The two readings can be seen side by side from the published file. This `SELECT` lists each matched result, its artifact, the exclusion flag if any, and how many triples the artifact itself carries:

```sparql
PREFIX kee: <https://w3id.org/kee#>
SELECT ?result ?artifact ?excluded (COUNT(?p) AS ?artifactTriples) WHERE {
  <https://example.org/kee/retrieval-query-escalation-threshold> kee:candidateResult ?result .
  ?result kee:retrievedArtifact ?artifact .
  OPTIONAL { ?result kee:excludedFromCurrentAnswerGrounding ?excluded }
  ?artifact ?p ?o .
} GROUP BY ?result ?artifact ?excluded ORDER BY ?result
```

```text
ex:retrieval-result-runbook-draft-2025 | ex:runbook-incident-triage-org-draft-2025 | true | 2
ex:retrieval-result-runbook-v3 | ex:runbook-incident-triage-v3 | None | 2
```

Both artifacts are present with their two triples each; one result is excluded. The consumer-side test named for NC-17 on the traceability page records the exclusion and then proves the artifact's triples and the graph size, less the one flag, are unchanged.

**Where the chain bends.** The retrieval query references a point-in-time query `ex:historical-intent-active-at-2026-08-15` carried in this file (lines 36–43). The historical example of step 5 carries an equivalent query under another IRI, `ex:query-active-at-2026-08-15`, which cross-references this retrieval query; the two files describe the same intent twice rather than sharing one resource.

## What this page does not show

Two of the seventeen rules are not demonstrated anywhere in the published material, and the specification says why. Section 18.5: "NC-03 (authority vs. responsibility) and NC-06 (confidence vs. trust) are not demonstrable at this baseline, and the reason is representational rather than epistemic. A non-collapse rule can be demonstrated only where both of its sides are represented, as Section 7.1's own preamble scopes them. KEE represents authority and it represents confidence. It represents neither accountability as a surface distinct from authority, nor trust as a surface distinct from confidence." Steps 2 and 3 show authority and contestation; neither they nor any shape carries an accountability or trust surface, and this page does not invent one.

Every `PASS` above is a structural result under the severity rule in `shacl/README.md`. The specification reports conformance in five dimensions (Section 15.2), and a structural pass settles only the first. Where a step shows the structural result staying the same while the consumer's reading changes (steps 5 and 6), that is the other four dimensions being exercised by something other than a shape. Which test or shape demonstrates each rule is tabulated in `docs/non-collapse-traceability.md`.
