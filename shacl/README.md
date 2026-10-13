# SHACL shape graphs

This directory holds the shape graphs the KEE reference validator executes, published as the same bytes. There is one shape graph per profile and two cross-profile constraint files (`lifecycle-status-constraints.ttl` and `governance-record-review-status-constraints.ttl`). Which profiles are normative and which are draft is stated in the specification (Section 19) and in `docs/profiles/README.md`; a shape graph's existence says nothing about its profile's status.

Three things decide whether a validation result means what you think it means: the severity rule, which shape files must be loaded together, and whether the shapes targeted anything in your data at all.

## 1. The severity rule: what "conforms" means

**A file conforms to a KEE shape graph when the validation report carries no result at severity `sh:Violation`. Results at `sh:Warning` and `sh:Info` are reported but tolerated: they do not make the file non-conformant.**

This is a deliberate departure from the SHACL 1.0 default, under which a result at *any* severity makes `sh:conforms` false. KEE shapes state the specification's recommendations (SHOULD-level obligations, such as an assertion identifying its source) at `sh:Warning` or `sh:Info`, so that a missing recommendation is reported without making the data structurally invalid. A constraint whose breach is non-conformance is shaped at `sh:Violation`. The rule is applied by the validation engine, not by the shapes, so any SHACL engine reproduces it once it is told to tolerate warnings and infos.

The reference validator names the rule so a report can say which one produced its `conforms` value:

| Field | Value |
|---|---|
| policy id | `kee-violation-only-v1` |
| disallowed severities | `sh:Violation` |
| tolerated severities | `sh:Warning`, `sh:Info` |
| `conforms` is true when | the validation report carries no result at a disallowed severity |
| SHACL 1.2 successor | `sh:conformanceDisallows`, to which this maps as a rename |

Every `conforms` value the reference validator publishes (its conformance reports and evidence) is computed under this rule and carries the policy id. A `conforms` value from another engine with default settings is computed under a stricter rule and may be false for a file that conforms to KEE.

### Staged constraints

A constraint whose breach will be non-conformance from a named later version is shaped at `sh:Warning` until that version, so that data conforming today is reported before it is rejected. One such constraint is in force: the governance-record review-status membership check (`governance-record-review-status-constraints.ttl`, composed as the next section states) reports at `sh:Warning` in v0.11.0 and at `sh:Violation` from v0.12.0. The membership checks that close a new-write record's `kee:queryTimeDimension` (`historical-bitemporal-querying-profile.ttl`) and `kee:eligibilityCategory` (`ai-grounded-retrieval-profile.ttl`) to their concept schemes were staged the same way, at `sh:Warning` at the v0.10.0 baseline, and report at `sh:Violation` from v0.11.0. The registered-legacy branch of each (a record declaring only `kee:profileConformance`) stays at `sh:Warning` for as long as that carrier is readable. Each shape's message states its own schedule.

### With pyshacl

[pyshacl](https://github.com/RDFLib/pySHACL) is a SHACL engine with a command line. The flags that reproduce the rule are `-w` (results at Warning or Info do not invalidate) and `--allow-infos` (Info alone; implied by `-w` in current pyshacl, harmless to pass). No inference is applied: pyshacl's default of `-i none` matches the reference validator.

```bash
pip install pyshacl
pyshacl -s shacl/assertion-profile.ttl examples/assertion.ttl -w --allow-infos
```

The report's second line is `Conforms: True` for a conformant file. To see the rule do its work, run the warning fixture both ways:

```bash
pyshacl -s shacl/assertion-profile.ttl fixtures/warning/assertion-without-source.ttl -w   # Conforms: True
pyshacl -s shacl/assertion-profile.ttl fixtures/warning/assertion-without-source.ttl      # Conforms: False
```

The second run fails only because the file omits `dcterms:source`, which the Assertion profile recommends at `sh:Warning`.

## 2. Composition: which shape files load together

Some profile shapes are incomplete on their own. A promotion record *is* a governance transition record, so the governance transition shape's requirements (a governed artifact, a lifecycle state, provenance) apply to it; the promotion shape adds the promotion-specific ones and does not restate the inherited ones. The lifecycle-owning profiles compose with the cross-profile lifecycle-axis constraints (specification Section 9.3), which reject a value that mixes the lifecycle axis with another axis (dispute standing, evidence standing) on `kee:lifecycleState`. The four profiles whose records carry a review status of their own compose with the governance-record review-status constraints, which check that `kee:lifecycleState` on such a record is a concept of the shared review-status scheme (`schemas/skos/governance-record-lifecycle.ttl`): at `sh:Warning` in v0.11.0, the last dual-read version, and at `sh:Violation` from v0.12.0, the first rejecting version (Section 17.3).

| Shape graph | Load together with | Why |
|---|---|---|
| `promotion-profile.ttl` | `governance-transition-profile.ttl`, `governance-record-review-status-constraints.ttl` | A promotion record is a governance transition record; the inherited requirements and the owner's review-status scheme apply. The review-status constraints target `kee:PromotionRecord` directly, so a record typed only as a promotion record is reached without the parent type (Section 15.6); a record typed with both classes is reported once, by the governance transition shape. |
| `authority-delegation-profile.ttl` | `governance-transition-profile.ttl`, `governance-record-review-status-constraints.ttl` | An authority record is a governance transition record; the inherited requirements and the owner's review-status scheme apply, and the review-status constraints target `kee:AuthorityRecord` directly, so a record typed only as an authority record is reached without the parent type (Section 15.6); a record typed with both classes is reported once, by the governance transition shape. A contested authority claim adopts the same scheme. |
| `governance-transition-profile.ttl` | `governance-record-review-status-constraints.ttl` | Review-status membership on `kee:GovernanceTransitionRecord`; this profile owns the scheme. |
| `contradiction-records-profile.ttl` | `governance-record-review-status-constraints.ttl` | Review-status membership on `kee:ContradictionRecord`. The review status is not the contradiction's resolution (Section 13.1). |
| `lifecycle-crosswalk-profile.ttl` | `governance-record-review-status-constraints.ttl` | Review-status membership on `kee:LifecycleCrosswalkMapping`. The review status is not the mapping's strength (Section 9.4). |
| `assertion-profile.ttl` | `lifecycle-status-constraints.ttl` | Lifecycle-axis non-collapse (Section 9.3) on `kee:Assertion`. |
| `scientific-claim-profile.ttl` | `lifecycle-status-constraints.ttl` | Lifecycle-axis non-collapse (Section 9.3) on `kee:ScientificClaim`. |
| `organizational-memory-profile.ttl` | `lifecycle-status-constraints.ttl` | Lifecycle-axis non-collapse (Section 9.3) on `kee:OrganizationalMemoryArtifact`. |
| `assertion-metadata-profile.ttl` | `lifecycle-status-constraints.ttl` | Lifecycle-axis guard on `kee:AssertionMetadataRecord`, at `sh:Warning`: the slot carries the managed assertion unit's lifecycle, not a review status, and the review-status constraints are not composed with it. |
| `ai-grounded-retrieval-profile.ttl`, `artifact-identity-granularity-profile.ttl`, `decision-profile.ttl`, `historical-bitemporal-querying-profile.ttl`, `software-engineering-profile.ttl`, `lifecycle-status-constraints.ttl`, `governance-record-review-status-constraints.ttl` | nothing | Standalone. |

The reference validator's conformance runner composes these automatically when it loads a shape graph by name. A shape graph passed to an engine explicitly is validated alone, and a result from the composed dependency is then silently absent: `fixtures/invalid/promotion-missing-governed-artifact.ttl` fails for the inherited `kee:governedArtifact` only when the governance transition shape is loaded too.

pyshacl takes one shapes file, so compose by concatenation (Turtle permits a prefix to be declared more than once) or by parsing both files into one graph:

```bash
cat shacl/promotion-profile.ttl shacl/governance-transition-profile.ttl > promotion-composed.ttl
pyshacl -s promotion-composed.ttl examples/promotion.ttl -w --allow-infos
```

## 3. The focus-node caveat: a pass can be vacuous

A shape applies to the nodes of its `sh:targetClass`. A data file that contains no instance of that class produces an empty report and `Conforms: True`, because nothing was targeted. That pass means "nothing the shape targets was wrong", not "this file is a conformant instance of the profile". Validating assertion data against `decision-profile.ttl` passes for the wrong reason.

Before reading a pass as conformance, check that the target class occurs in your data:

| Shape graph | Target classes |
|---|---|
| `ai-grounded-retrieval-profile.ttl` | `kee:RetrievalQuery`, `kee:RetrievalResult` |
| `artifact-identity-granularity-profile.ttl` | `kee:ManagedArtifactUnit`, `kee:RetrievalChunk` |
| `assertion-metadata-profile.ttl` | `kee:AssertionMetadataRecord` |
| `assertion-profile.ttl` | `kee:Assertion` |
| `authority-delegation-profile.ttl` | `kee:AuthorityRecord`, `kee:ContestedAuthorityClaim` |
| `contradiction-records-profile.ttl` | `kee:ContradictionRecord` |
| `decision-profile.ttl` | `kee:Decision` |
| `governance-record-review-status-constraints.ttl` | `kee:GovernanceTransitionRecord`, `kee:PromotionRecord`, `kee:AuthorityRecord`, `kee:ContradictionRecord`, `kee:ContestedAuthorityClaim`, `kee:LifecycleCrosswalkMapping` |
| `governance-transition-profile.ttl` | `kee:GovernanceTransitionRecord` |
| `historical-bitemporal-querying-profile.ttl` | `kee:PointInTimeQuery` |
| `lifecycle-crosswalk-profile.ttl` | `kee:LifecycleCrosswalkMapping` |
| `lifecycle-status-constraints.ttl` | `kee:Assertion`, `kee:ScientificClaim`, `kee:OrganizationalMemoryArtifact`, `kee:AssertionMetadataRecord` |
| `organizational-memory-profile.ttl` | `kee:OrganizationalMemoryArtifact` |
| `promotion-profile.ttl` | `kee:PromotionRecord` |
| `scientific-claim-profile.ttl` | `kee:ScientificClaim` |
| `software-engineering-profile.ttl` | `kee:SoftwareEngineeringArtifact` |

A structural pass is also only structural. The specification distinguishes five conformance dimensions (Section 15.2); a clean SHACL report settles the first and says nothing about the others.

## Where the data is

- `examples/`: one worked example per profile, in Turtle, each registered in the reference validator's conformance manifest as expected-valid against its profile's shape graph.
- `fixtures/valid/`, `fixtures/invalid/`, `fixtures/warning/`: the conformance suite's own fixtures, with `fixtures/README.md` stating what each directory proves and the named reason every invalid fixture fails.
