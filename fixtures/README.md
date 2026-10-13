# Conformance fixtures

These are the data files the reference validator's conformance suite runs against the shape graphs in `shacl/`. They are published so that anyone can reproduce the suite's results with their own SHACL engine and so that a shape change can be checked against the cases it is meant to accept and reject. The severity rule, the shape composition table, and the commands are in `shacl/README.md`.

Each directory proves one thing.

| Directory | What a file in it proves |
|---|---|
| `valid/` | One file per profile, written in the current canonical form. Each conforms to its profile's shape graph (composed as `shacl/README.md` describes): the report carries no `sh:Violation` result. A fixture here is the smallest data that satisfies every required constraint, not a worked example; the worked examples are in `examples/`. |
| `invalid/` | One file per required constraint. Each fails its profile's shape graph for the reason its name states, and that reason is pinned: the suite asserts that the named `sh:Violation` result (focus node, result path, constraint component) is present in the report, not merely that the file fails. A fixture that failed for some other reason would pass a weaker test and prove nothing about the constraint it is named for. |
| `warning/` | A file that conforms *only because of the severity policy*. It satisfies every `sh:Violation`-level constraint and omits something the profile recommends at `sh:Warning`, or writes a value a composed constraint reports at `sh:Warning`. Under the policy it conforms; under the SHACL default, where any result makes `sh:conforms` false, it does not. Run it both ways to see the policy do its work. `governance-transition-generic-review-status.ttl` is the staged case: its review status is a generic `lifecycle#` value, reported at `sh:Warning` in v0.11.0 and at `sh:Violation` from v0.12.0 by `governance-record-review-status-constraints.ttl`, composed with the governance transition shape. |

## Why the invalid fixtures fail

Several fixtures fail for more than one reason at once (a file missing its eligibility basis may also lack a context and a generation time). The named reason is the one the fixture exists to demonstrate; other results may accompany it. The shape column is the shape graph the suite loads for that fixture, with its composed dependencies; two authority and promotion fixtures are listed against `governance-transition-profile.ttl` because the constraint they demonstrate is inherited from it. `MinCount` means the required property is absent.

| Fixture | Shape graph | Named `sh:Violation` result |
|---|---|---|
| `ai-grounded-retrieval-eligibility-category-not-in-scheme.ttl` | `ai-grounded-retrieval-profile.ttl` | node-level `sh:or` on a new-write result (`dcterms:conformsTo`) whose `kee:eligibilityCategory` is outside the retrieval-eligibility scheme (specification Section 14.5; a tolerated warning at the v0.10.0 baseline, a `sh:Violation` since v0.11.0) |
| `ai-grounded-retrieval-missing-eligibility-basis.ttl` | `ai-grounded-retrieval-profile.ttl` | `kee:eligibilityBasis` (MinCount) |
| `ai-grounded-retrieval-missing-retrieved-artifact.ttl` | `ai-grounded-retrieval-profile.ttl` | `kee:retrievedArtifact` (MinCount) |
| `ai-grounded-retrieval-missing-timestamp.ttl` | `ai-grounded-retrieval-profile.ttl` | `prov:generatedAtTime` (MinCount) |
| `artifact-identity-granularity-blank-node-identity.ttl` | `artifact-identity-granularity-profile.ttl` | node-level `sh:NodeKind` on a blank-node focus: a managed artifact unit must be an IRI |
| `artifact-identity-granularity-missing-artifact-type.ttl` | `artifact-identity-granularity-profile.ttl` | `dcterms:type` or legacy `kee:artifactType` (MinCount) |
| `artifact-identity-granularity-missing-profile-conformance.ttl` | `artifact-identity-granularity-profile.ttl` | `dcterms:conformsTo` or legacy `kee:profileConformance` (MinCount) |
| `assertion-metadata-missing-lifecycle.ttl` | `assertion-metadata-profile.ttl` | `kee:lifecycleState` (MinCount) |
| `assertion-metadata-missing-managed-unit.ttl` | `assertion-metadata-profile.ttl` | `kee:managedAssertionUnit` (MinCount) |
| `assertion-metadata-missing-provenance.ttl` | `assertion-metadata-profile.ttl` | `prov:wasAttributedTo` (MinCount); `prov:generatedAtTime` (MinCount) |
| `assertion-missing-label.ttl` | `assertion-profile.ttl` | `rdfs:label` (MinCount); `skos:definition` (MinCount) |
| `assertion-missing-lifecycle.ttl` | `assertion-profile.ttl` | `kee:lifecycleState` (MinCount) |
| `assertion-missing-provenance.ttl` | `assertion-profile.ttl` | `prov:wasAttributedTo` (MinCount) |
| `authority-delegation-missing-governed-artifact.ttl` | `governance-transition-profile.ttl` | `kee:governedArtifact` (MinCount), inherited by the authority record through multi-typing |
| `authority-delegation-missing-granted-to.ttl` | `authority-delegation-profile.ttl` | `kee:grantedTo` (MinCount) |
| `authority-delegation-missing-second-claimant.ttl` | `authority-delegation-profile.ttl` | `kee:claimant` (MinCount): a contested claim needs two claimants |
| `authority-delegation-untyped-grantee-no-chain.ttl` | `authority-delegation-profile.ttl` | node-level `sh:or`: the grantee is typed only `prov:Agent` and resolves to no accountable person or organization (specification Section 12.3; a `sh:Violation` since v0.10.0) |
| `contradiction-records-missing-lifecycle.ttl` | `contradiction-records-profile.ttl` | `kee:lifecycleState` (MinCount) |
| `contradiction-records-missing-provenance.ttl` | `contradiction-records-profile.ttl` | `prov:wasGeneratedBy` (MinCount); `prov:wasAttributedTo` (MinCount); `prov:generatedAtTime` (MinCount) |
| `contradiction-records-missing-second-artifact.ttl` | `contradiction-records-profile.ttl` | `kee:conflictingArtifact` (MinCount): a contradiction needs two artifacts |
| `governance-transition-missing-governed-artifact.ttl` | `governance-transition-profile.ttl` | `kee:governedArtifact` (MinCount) |
| `governance-transition-missing-lifecycle.ttl` | `governance-transition-profile.ttl` | `kee:lifecycleState` (MinCount) |
| `governance-transition-missing-provenance.ttl` | `governance-transition-profile.ttl` | `prov:wasGeneratedBy` (MinCount); `prov:wasAttributedTo` (MinCount); `prov:generatedAtTime` (MinCount) |
| `historical-bitemporal-querying-missing-profile-conformance.ttl` | `historical-bitemporal-querying-profile.ttl` | `dcterms:conformsTo` or legacy `kee:profileConformance` (MinCount); node-level `sh:or` whose branches each require a conformance carrier |
| `historical-bitemporal-querying-missing-query-pattern.ttl` | `historical-bitemporal-querying-profile.ttl` | `kee:queryPattern` (MinCount) |
| `historical-bitemporal-querying-missing-time-dimension.ttl` | `historical-bitemporal-querying-profile.ttl` | `kee:queryTimeDimension` (MinCount) |
| `historical-bitemporal-querying-time-dimension-not-in-scheme.ttl` | `historical-bitemporal-querying-profile.ttl` | node-level `sh:or` on a new-write record (`dcterms:conformsTo`) whose `kee:queryTimeDimension` is outside the query-time-dimension scheme (specification Section 14.2; a tolerated warning at the v0.10.0 baseline, a `sh:Violation` since v0.11.0) |
| `lifecycle-crosswalk-missing-lifecycle.ttl` | `lifecycle-crosswalk-profile.ttl` | `kee:lifecycleState` (MinCount) |
| `lifecycle-crosswalk-missing-provenance.ttl` | `lifecycle-crosswalk-profile.ttl` | `prov:wasAttributedTo` (MinCount); `prov:generatedAtTime` (MinCount) |
| `lifecycle-crosswalk-missing-source-vocabulary.ttl` | `lifecycle-crosswalk-profile.ttl` | `kee:sourceVocabulary` (MinCount) |
| `promotion-missing-governed-artifact.ttl` | `governance-transition-profile.ttl` | `kee:governedArtifact` (MinCount), inherited by the promotion record through multi-typing |
| `promotion-missing-source-scope.ttl` | `promotion-profile.ttl` | `kee:sourceScope` (MinCount) |
| `scientific-claim-missing-label.ttl` | `scientific-claim-profile.ttl` | `rdfs:label` (MinCount); `skos:definition` (MinCount) |
| `scientific-claim-missing-lifecycle.ttl` | `scientific-claim-profile.ttl` | `kee:lifecycleState` (MinCount) |
| `scientific-claim-missing-provenance.ttl` | `scientific-claim-profile.ttl` | `prov:wasAttributedTo` (MinCount) |
| `software-engineering-missing-label.ttl` | `software-engineering-profile.ttl` | `rdfs:label` (MinCount); `skos:definition` (MinCount) |
| `software-engineering-missing-lifecycle.ttl` | `software-engineering-profile.ttl` | `kee:lifecycleState` (MinCount) |
| `software-engineering-missing-provenance.ttl` | `software-engineering-profile.ttl` | `prov:wasAttributedTo` (MinCount) |

## Why the warning fixtures are tolerated

Each file in `warning/` carries the results named here, all at `sh:Warning`, and no result at `sh:Violation`. One of them exercises a constraint that is staged: the governance-record review-status membership check reports at `sh:Warning` in v0.11.0 and at `sh:Violation` from v0.12.0, when that file becomes an expected-negative fixture under `invalid/`. The two query-classifier membership checks were staged the same way, at `sh:Warning` at the v0.10.0 baseline, and report at `sh:Violation` from v0.11.0; their two fixtures are listed under `invalid/` above.

| Fixture | Shape graph | Named `sh:Warning` result |
|---|---|---|
| `assertion-metadata-challenged-lifecycle.ttl` | `assertion-metadata-profile.ttl` with `lifecycle-status-constraints.ttl` | `kee:lifecycleState` written on the dispute axis (Section 9.3), and the legacy `kee:profileConformance` carrier |
| `assertion-without-source.ttl` | `assertion-profile.ttl` | `dcterms:source` (MinCount), the recommendation the profile states at `sh:Warning` |
| `governance-transition-generic-review-status.ttl` | `governance-transition-profile.ttl` with `governance-record-review-status-constraints.ttl` | `kee:lifecycleState` is the generic `lifecycle#Supported`, outside the governance-record review-status scheme (specification Section 9.2); `sh:Violation` from v0.12.0 |

## Reproducing a result

```bash
pip install pyshacl
pyshacl -s shacl/assertion-profile.ttl fixtures/valid/assertion.ttl -w --allow-infos        # Conforms: True
pyshacl -s shacl/assertion-profile.ttl fixtures/invalid/assertion-missing-lifecycle.ttl -w   # Conforms: False, kee:lifecycleState
pyshacl -s shacl/assertion-profile.ttl fixtures/warning/assertion-without-source.ttl -w      # Conforms: True
pyshacl -s shacl/assertion-profile.ttl fixtures/warning/assertion-without-source.ttl         # Conforms: False: the SHACL default
```

A fixture whose shape graph composes with another (the authority, promotion, assertion, assertion-metadata, scientific-claim, organizational-memory, governance-transition, contradiction-records and lifecycle-crosswalk profiles) needs every composed file loaded; `shacl/README.md` shows how.

The fixtures carry compatibility notes where they exercise registered legacy-readable carriers on purpose. Those notes describe what the file does, not what new data should do; the specification's Section 8 and Section 17 govern canonical new writes.
