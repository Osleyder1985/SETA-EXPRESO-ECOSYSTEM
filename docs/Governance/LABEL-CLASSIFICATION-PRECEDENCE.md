# Label Classification Precedence

## Purpose

Define deterministic rules for future automation of GitHub label classification.

## Classification order

1. Explicit Issue classification.
2. Declared change type.
3. Affected artifacts.
4. Domain validation against Label-Catalog.yml.
5. Work type validation against Label-Catalog.yml.
6. Human review when ambiguity exists.

## Conflict resolution

Priority order:

Issue declaration > Artifact evidence > Automatic inference.

If classification cannot be determined safely, validation must fail and request human classification.

## Automation rules

Automation may validate and suggest classifications, but must not:

- invent new labels;
- create taxonomy categories;
- replace architectural decisions;
- bypass human review for ambiguous cases.

## Separation of concepts

Labels identify domain and work type.

They do not represent:

- project phase;
- priority;
- status;
- approval state.
