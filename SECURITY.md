# Security policy

## Scope

This repository publishes a specification, term declarations, SHACL shape graphs, SKOS concept schemes, JSON Schemas, a JSON-LD context, examples, and conformance fixtures. It runs no service and ships no executable here. A security report about it is most likely one of:

- a published artifact that makes a consumer's tooling do something it should not when loaded (for example a context or schema that triggers a remote fetch, or a shape that is pathological for a validator);
- a persistent identifier under `https://w3id.org/kee` resolving somewhere it should not;
- a published file that carries private information or credentials.

## How to report

Do not open a public issue that contains exploit detail.

1. If GitHub's private vulnerability reporting is enabled on this repository, use **Report a vulnerability** under the repository's **Security** tab.
2. Otherwise, open an issue titled `Security: request for a private channel` with no detail beyond that sentence. A maintainer will reply with a private channel.

Include what you found, how to reproduce it, and which published file or identifier is affected.

## What to expect

- An acknowledgement within 14 days. This is a volunteer-maintained project with one primary maintainer, so acknowledgement is a commitment and resolution time is not.
- A fix that changes a published artifact ships as a release under the project's versioning rules, with a `CHANGELOG.md` entry that says what changed and why.
- Credit in the changelog if you want it; no bounty is offered.

## Out of scope

- Behaviour of third-party validators, RDF libraries, or resolvers that the published artifacts do not control.
- Content of data that someone else publishes as conforming to KEE. A conformance claim is theirs; see `TRADEMARK.md`.
