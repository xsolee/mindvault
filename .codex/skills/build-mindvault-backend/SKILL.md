---
name: build-mindvault-backend
description: Design, implement, review, or test an approved MindVault backend task using Python 3.13 and FastAPI. Use for API, domain logic, PostgreSQL, ingestion, transcription, document processing, retrieval, RAG, provider adapters, background work, security, or backend deployment changes with an approved specification.
---

# Build MindVault Backend

1. Read `AGENTS.md`, the assigned task, relevant architecture and ADRs, and any approved API or data contracts.
2. Report missing or conflicting sources of truth before coding. Do not choose an unresolved provider or infrastructure service implicitly.
3. Keep domain rules separate from FastAPI, persistence, queues, storage, transcription, embeddings, and LLM SDKs.
4. Preserve source provenance and ownership authorization across ingestion, retrieval, and citation paths.
5. Prefer exact identifier and metadata retrieval alongside semantic retrieval when the task involves knowledge search.
6. Make ingestion and background operations idempotent, retry-aware, and observable as required by the task.
7. Use Python 3.13 type hints. Add proportionate unit and integration tests, including failure and authorization cases.
8. Modify only assigned files. Coordinate contract changes with the frontend owner through the main agent.
9. Run specified formatting, linting, typing, tests, and builds. Report actual results and residual risks.

Do not expand scope, approve architecture changes, or claim end-to-end completion independently.
