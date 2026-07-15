# MindVault Engineering Guidelines

MindVault is a production-quality SaaS application for AI-powered personal knowledge management.

## Before Coding

1. Read `README.md` and all relevant documentation under `docs/`.
2. Read the assigned task specification in full.
3. Follow the approved architecture and existing engineering workflow.
4. Report missing or conflicting source-of-truth documentation before making assumptions.

## Scope and Design

- Implement only the assigned task; never add speculative or future-milestone features.
- Prefer simple, readable solutions over unnecessary abstractions.
- Keep business logic framework-independent whenever practical.
- Preserve boundaries between frameworks, databases, storage services, queues, and AI providers.
- Do not couple the application to a single LLM, embedding, storage, or transcription provider.
- Maintain production-quality, secure, and testable code.

## Implementation Standards

- Use Python 3.13 and type hints for all Python code.
- Follow the coding and testing standards under `docs/engineering/`.
- Write appropriate unit and integration tests for new functionality.
- Never commit secrets; use environment variables and document them in `.env.example`.
- Preserve existing work and avoid unrelated changes.

## Documentation and Decisions

- Keep documentation synchronized when architecture or behavior changes.
- Record significant architectural decisions as ADRs under `docs/adr/`.
- Do not redefine approved architecture within an implementation task.

## Completion

Run applicable linting, type checks, tests, and builds. Report files changed, validation results, assumptions, risks, and recommended follow-up work.
