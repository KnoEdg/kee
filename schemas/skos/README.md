# SKOS concept schemes

Canonical SKOS concept schemes for the KEE controlled vocabularies. Each scheme
carries its own `dcterms:identifier`, description, and status.

Published schemes:

- `artifact-types.ttl` — controlled artifact classifications used with `dcterms:type`;
- `assertion-lifecycle.ttl`, `decision-lifecycle.ttl`, `organizational-memory-lifecycle.ttl`,
  `scientific-claim-lifecycle.ttl`, `software-engineering-lifecycle.ttl` — the five
  profile-specific lifecycle schemes;
- `governance-record-lifecycle.ttl` — the governance-record review-status scheme: the
  review status of a record about governance (a transition record, a contradiction
  record, a contested authority claim, a crosswalk mapping) as a record, owned by the
  Governance Transition Profile and adopted by the other three; closed;
- `contradiction-types.ttl` — the contradiction-cause scheme;
- `assertion-metadata-unit-kind.ttl` — managed assertion-unit kinds;
- `confidence-interpretation.ttl` — the confidence-interpretation sentinel;
- `confidence-status.ttl` — Informative / Non-Normative illustrative labels;
- `query-time-dimension.ttl` — the time dimension a point-in-time query record
  declares (recorded versus valid time), for `kee:queryTimeDimension`;
- `retrieval-eligibility.ttl` — the retrieval-eligibility categories of a
  consumer-scoped retrieval decision, for `kee:eligibilityCategory`.

## Status

A scheme's own metadata is authoritative for its status, not this file. The
specification governs which schemes carry normative effect and which are
informative.

The lifecycle namespaces are compatibility-sensitive: profile-specific schemes
are authoritative for new writes, and the generic lifecycle namespace is
readable only under the published compatibility window.

## Extension

The contradiction-cause and assertion-unit-kind schemes are intentionally open.
A profile or domain may use its own vocabulary IRIs; validators must not close
these slots to the enumerations published here. A new shared KEE concept
requires the specification's KEE-owned-term admission test.

The governance-record review-status scheme is closed for the four classes that
adopt it: `shacl/governance-record-review-status-constraints.ttl` checks
membership, and a new concept needs a governed decision.

The query-time-dimension and retrieval-eligibility schemes are closed: the
owning profile shapes list their concepts with `sh:in`, so a new-write record
must use one of them, and a registered-legacy record carrying another value is
reported rather than rejected during the compatibility window. Adding a concept
to either is a governed decision and a MINOR release.
