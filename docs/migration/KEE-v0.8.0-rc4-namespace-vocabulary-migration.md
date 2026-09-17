# KEE v0.8.0-rc4 Namespace and Vocabulary Migration

**Status:** Release-candidate migration control  
**Scope:** KCHG-022 through KCHG-027  
**Normative owner:** `docs/specs/KEE-Specification-v0.8.0-rc4.md`

## Artifact classification

New writes use `dcterms:type` with values under `https://w3id.org/kee/artifact#`.

Historical `https://knoedg.org/vocab/*Artifact` values remain readable. `schemas/skos/artifact-types.ttl` publishes explicit SKOS mappings where reviewed. No class/category `owl:sameAs` is asserted.

## Lifecycle

New writes use the profile-specific lifecycle namespaces published in the corresponding SKOS files.

The generic `https://w3id.org/kee/lifecycle#` surface is legacy-read compatibility only. Migration MUST be profile-aware; labels such as Active, Accepted, Published, Stable, or Baselined are not automatically exact equivalents.

Historical `https://knoedg.org/vocab/` profile lifecycle concepts have explicit `skos:exactMatch` mappings to their canonical profile-specific RC4 identifiers where the definitions are carried forward unchanged.

## Contradiction causes

Canonical namespace: `https://w3id.org/kee/vocab/contradiction-cause#`.

The scheme is governed but open. `kee:causeType` may point to another profile/domain taxonomy when declared. The KEE scheme is a reusable local vocabulary, not a mandatory universal taxonomy.

## Assertion unit kinds

Canonical namespace: `https://w3id.org/kee/vocab/assertion-unit-kind#`.

The slot remains open. The initial seven concepts identify representation patterns and cite their representation prior art; they do not claim invention of RDF triples, reification, named graphs, nanopublications, or application claim objects.

## Confidence scheme

`schemas/skos/confidence-status.ttl` remains Informative / Non-Normative. `ProfileDefinedConfidence` is a sentinel, not a level. RC4 does not supply missing confidence semantics.

## Phantom namespaces

The JSON-LD context no longer declares `https://w3id.org/kee/governance#` or `https://w3id.org/kee/contradiction#` as if they were populated governed vocabularies. Canonical contradiction-cause terms use the explicit `vocab/contradiction-cause#` namespace.

## Compatibility policy

Migration is provenance-preserving. Implementations SHOULD retain the original IRI or migration provenance when rewriting stored data. Similar labels are insufficient for exact mapping. RC4 publishes no migration `owl:sameAs` assertions.

Retirement of legacy read support is outside RC4 and remains governed by KCHG-065/KCHG-066.
