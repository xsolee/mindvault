# Architecture Principles

Status: Approved principles; detailed architecture pending

1. PostgreSQL is the system of record. Vector search is a retrieval capability, not a separate source of truth.
2. Preserve provenance from original source through extraction, chunking, retrieval, and citation.
3. Treat voice, text, and uploaded files as source variants feeding a common knowledge-ingestion model.
4. Combine exact identifiers, metadata filters, and semantic retrieval; do not rely only on embeddings.
5. Keep transcription, embedding, generation, object storage, and background execution behind application-owned boundaries.
6. Make asynchronous processing idempotent and observable because uploads and transcription can be slow or fail.
7. Authorize every source and retrieval operation by owner before returning content to an LLM or user.
8. Prefer a modular monolith until measured requirements justify distributed services.
9. Keep frontend hosting, API hosting, database, and object storage independently deployable.
10. Record provider and infrastructure selections as ADRs after requirements and operational constraints are known.
11. Package deployable application processes as production-ready Docker images and support complete local and self-hosted production stacks through Docker Compose.
12. Keep containers stateless where practical; persist durable data in PostgreSQL and object storage rather than container filesystems.
13. Keep managed services optional. A deployment may replace containerized frontend hosting, PostgreSQL, or object storage with compatible managed services without changing core business logic.
14. Preserve both original-language content and an English normalized representation; derived translations never replace source evidence.
15. Support separate web and native-mobile clients in one monorepo, sharing contracts and non-UI logic while permitting platform-specific capture implementations.
16. Default to strict per-user data isolation. Every query, retrieval candidate, source, and generated citation must be authorized for the requesting user.
