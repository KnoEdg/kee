# KEE / KnoEdg Trademark and Conformance-Claim Policy

> **Status:** Draft policy
> **Classification:** Informative, non-normative
> **Applies to:** the "KEE" name, the "KnoEdg" name, and any future project logo(s), independent of which license governs the underlying specification, vocabulary, or code

## 1. What this policy is, and is not

This policy governs use of the **names "KEE" and "KnoEdg"** and any conformance-claim language built on them. KEE is the specification and framework; KnoEdg is the stewarding project and organization. Both names are covered on the same terms below. This policy is separate from, and unaffected by, the license(s) that govern the specification, vocabulary, SHACL shapes, and reference implementation (see `LICENSE` and `NOTICE`). Those licenses grant broad rights to copy, modify, implement, and redistribute the licensed content, including for commercial purposes. This policy does not narrow those grants. It governs a different thing: who may use the *names* to describe what they built.

## 2. What is unrestricted

Anyone may, without asking permission:

- implement the KEE specification, in whole or in part, in any software, product, or service;
- fork, modify, and redistribute the specification, vocabulary, shapes, schemas, or reference implementation, under their respective licenses;
- build a commercial product or service on top of KEE-derived work;
- write, publish, and distribute their own documentation, tooling, or profiles composing KEE.

## 3. What requires permission

- Stating or implying that an implementation, fork, product, service, or organization **is** KEE or KnoEdg, **is the official** KEE or KnoEdg, or **is endorsed by, affiliated with, or certified by** the KEE project or KnoEdg, without such a relationship actually existing.
- Using "KEE," "KnoEdg," or a confusingly similar name as the primary name of a fork or derivative whose conformance behavior has diverged from the published specification baseline. A derivative that changes conformance behavior should choose its own name (see the OpenSearch/Elasticsearch precedent for why this matters in practice: a diverged fork sharing the original name creates real confusion about what "conforms" means).
- Using the phrase **"Conforms to KEE vX.Y.Z"**, **"KEE-Conformant"**, or an equivalent conformance badge/claim, for an implementation that has not been evaluated against the published conformance manifest and test suite (the `kee conformance` command and its manifest) for the cited version.

## 4. Conformance claims

A conformance claim under this policy must:

1. name the exact specification version claimed (e.g., "v0.10.0"), never an unqualified "KEE-conformant" claim with no version;
2. be evaluated against that version's published conformance manifest and test suite, not a self-declared subset;
3. distinguish structural (SHACL) conformance from profile-semantic, procedural, governance/policy, and interoperability conformance, per the specification's own conformance-dimension model (Section 15) — a structural PASS alone is not a general conformance claim.

No formal registration or certification program exists yet. Until one does, a conformance claim is self-asserted against the public test suite, and is expected to be accurate and falsifiable rather than pre-approved. A future formal conformance-testing/registration program, if one is established, would supersede this interim rule and would be recorded here as a policy update, not a silent change.

## 5. Why this exists as a separate instrument

The specification and reference implementation are licensed to be freely usable, including commercially, because that is what makes a specification a standard rather than a product. Trademark and conformance-claim control is the mechanism that protects the *meaning* of the names and the integrity of conformance claims without narrowing anyone's right to actually implement, fork, or commercialize the underlying work. The two questions -- "may you use this?" and "may you call it KEE or KnoEdg?" -- are independent by design, and the project's own governance process keeps them that way.

## 6. Contact

Questions about trademark use or conformance claims: see the repository's contact information (to be finalized alongside a formal conformance program, if one is established).

## 7. Status and review

This is a draft policy, published for transparency, not a finalized legal instrument. It has not received legal review. It will be revised as the project's conformance-testing infrastructure and commercial-licensing arrangements (see `COMMERCIAL-LICENSE.md`) mature.
