# MindVault Engineering Guidelines

MindVault is a production-quality SaaS application for personal knowledge capture and retrieval.

## Source of truth

Before changing code or documentation, read `README.md`, the relevant documents under `docs/`, and the assigned task specification in full. Report missing, contradictory, or unapproved requirements before implementation.

Priority order:

1. Explicit user decision
2. Approved task specification and acceptance criteria
3. Accepted ADRs and architecture documents
4. Product documentation
5. Engineering guidelines

Do not convert an example, deployment preference, or open question into an approved requirement.

## Delivery rules

- Work on one approved task at a time.
- Implement only the assigned scope; do not add future features.
- Prefer simple, readable designs and framework-independent business rules.
- Preserve boundaries around databases, storage, queues, transcription, embeddings, and LLM providers.
- Use Python 3.13 with type hints and strict TypeScript.
- Add proportionate unit, integration, and end-to-end tests.
- Never commit secrets. Document configuration in `.env.example`.
- Keep behavior and architecture documentation synchronized.
- Record consequential decisions under `docs/adr/`.

## Roles and delegation

The main agent is the technical lead and integrator. It owns requirement clarification, architecture coherence, task assignment, integration, and completion reporting.

Use the repository skills for bounded specialist work:

- `$manage-mindvault-project`: planning, scope, acceptance criteria, dependencies, and status
- `$build-mindvault-backend`: approved backend design and implementation
- `$build-mindvault-frontend`: approved frontend design and implementation
- `$verify-mindvault-quality`: independent verification and defect reporting

Subagents may be used when the user explicitly requests delegation or parallel work. Give each agent non-overlapping file ownership and a bounded deliverable. The main agent must review and integrate all results. Specialist agents cannot approve product scope or architecture changes.

## Completion

Run applicable formatting, linting, type checks, tests, and builds. Report changed files, actual validation results, assumptions, risks, and recommended follow-up work.
