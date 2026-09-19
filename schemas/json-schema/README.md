# JSON Schema

JSON Schema artifacts for KEE metadata and profile declarations.

Published schemas:

- `profile-metadata.schema.json` — profile metadata;
- `lifecycle-state.schema.json` — lifecycle state definitions;
- `governance-metadata.schema.json` — governance metadata;
- `provenance-metadata.schema.json` — provenance metadata;
- `profile-conformance.schema.json` — profile conformance declarations;
- `v0.9-profile-declaration.schema.json` — the JSON profile declaration, an
  optional candidate surface. An implementation that ignores it remains
  conforming.

## Status

Each schema's own `title` and `description` state what it covers. The
specification governs which of these surfaces carry normative effect; a schema
file existing here does not by itself create one.

Structural validity against any of these schemas is a statement about structure
only. It establishes nothing about the other four conformance dimensions.
