# SKOS concept schemes

Canonical SKOS concept schemes for the KEE controlled vocabularies. Each scheme
carries its own `dcterms:identifier`, description, and status.

Published schemes:

- `artifact-types.ttl` — controlled artifact classifications used with `dcterms:type`;
- `assertion-lifecycle.ttl`, `decision-lifecycle.ttl`, `organizational-memory-lifecycle.ttl`,
  `scientific-claim-lifecycle.ttl`, `software-engineering-lifecycle.ttl` — the five
  profile-specific lifecycle schemes;
- `contradiction-types.ttl` — the contradiction-cause scheme;
- `assertion-metadata-unit-kind.ttl` — managed assertion-unit kinds;
- `confidence-interpretation.ttl` — the confidence-interpretation sentinel;
- `confidence-status.ttl` — Informative / Non-Normative illustrative labels.

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
