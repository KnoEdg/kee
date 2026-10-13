<!-- Read CONTRIBUTING.md first: it says which changes a pull request can make directly and which go through the governed change process. -->

## What this changes

<!-- One paragraph. If it touches a published artifact (specification, shape graph, concept scheme, schema, context, vocabulary, example, or fixture), name it and say whether any conformance result changes. -->

## Why

<!-- The observation or report that motivated it. Link the issue if there is one. -->

## Checklist

- [ ] The commit messages follow Conventional Commits (`type(scope)?: subject`).
- [ ] No commit, file, or this description carries a co-author trailer, a "generated with" line, or a session link for a software tool. CI rejects them.
- [ ] The branch name describes the work (`fix/<subject>`, `docs/<subject>`), not a tool or a session.
- [ ] A change to a shape, example, or fixture was validated (`shacl/README.md` has the commands), and a fixture that is meant to fail still fails for its named reason (`fixtures/README.md`).
- [ ] A change that alters normative meaning is marked as such, so it can be routed through the governed process rather than merged as an editorial fix.
