# Backend Architecture

Status: Proposed for approval

## Processes and layers

The API and worker use the same Python package and composition root.

```text
domain/          Entities, value objects, policies, state transitions
application/     Use cases, ports, commands, queries, orchestration
adapters/        PostgreSQL, object storage, AI, email, document parsers
entrypoints/     FastAPI routes, worker runner, operational commands
```

FastAPI, SQLAlchemy, provider SDKs, and storage clients stay outside domain code. Application DTOs do not expose provider types.

## Modules

| Module | Owns |
| --- | --- |
| identity_access | Accounts, password credentials, sessions, recovery, ownership policy |
| sources | Source aggregate, source objects, lifecycle, limits |
| uploads | Idempotent upload sessions and completion verification |
| ingestion | Processing workflows, attempts, publication and reprocessing |
| content_processing | Extraction, transcription, language detection and normalization |
| knowledge | Representations, segments, identifiers, embeddings and provenance |
| retrieval | Query interpretation, retrieval channels, fusion, reranking, evidence bundles |
| conversations | Current-conversation messages and context |
| answers | Generation, claim validation, refusal and persistence |
| citations | Claim mapping and authorized source resolution |
| exports | Export snapshots, ZIP manifests and artifacts |
| usage_plans | Entitlements, reservations and consumption; no payment collection |
| operations | Jobs, audit events, health, reconciliation and observability |

Modules may call one another only through application interfaces. Database tables do not define module APIs.

## HTTP conventions

- Prefix: `/api/v1`
- JSON uses stable machine-readable error codes and RFC 9457 problem details.
- Mutations accept an `Idempotency-Key` where duplicate client delivery is plausible.
- Long operations return `202 Accepted` plus a status resource.
- Collections use cursor pagination.
- Each response carries a request/correlation ID.
- OpenAPI is the canonical wire contract; generated TypeScript clients fail CI on drift.

## API groups

```text
/auth/register, /auth/login, /auth/refresh, /auth/logout, /auth/recovery
/account, /account/sessions
/uploads, /uploads/{id}/complete
/sources, /sources/notes, /sources/{id}/status|retry|original
/conversations, /conversations/{id}/messages
/answers/{id}, /citations/{id}
/exports, /exports/{id}/download
/usage
/health/live, /health/ready
```

## Authentication decision

Use application-owned email/password accounts for MVP:

- Argon2id password hashing with versioned parameters.
- Short-lived access tokens and rotating, one-time refresh sessions stored hashed in PostgreSQL.
- Web receives Secure, HttpOnly, SameSite cookies plus CSRF protection.
- Android stores refresh credentials only in OS secure storage.
- Recovery uses single-use, hashed, expiring tokens through an email-provider port.
- Session revocation and account-wide logout are supported.

This avoids making self-hosting depend on a proprietary identity service. Social login and passkeys are deferred.

## Provider ports

`ObjectStore`, `Transcriber`, `LanguageNormalizer`, `EmbeddingProvider`, `Reranker`, `AnswerGenerator`, `GroundingEvaluator`, `DocumentExtractor`, `EmailSender`, `ArchiveBuilder`, `Clock`, and `IdGenerator` are application-owned interfaces. Adapters declare capabilities, model/version, region, retention behavior, and health.

## Background execution

Use a PostgreSQL durable job/outbox table for MVP. API transactions atomically change business state and insert a job. Workers lease jobs using `FOR UPDATE SKIP LOCKED`, lease expiry, heartbeat, bounded exponential backoff with jitter, and dead-letter state. Stage handlers are idempotent.

This avoids Redis and cross-system commit gaps initially. Reassess a dedicated broker only when measured queue throughput or scheduling needs exceed PostgreSQL capacity.

## Authorization invariant

Every repository method takes an authenticated `account_id`; every owned row carries `account_id`; every query includes it. PostgreSQL row-level security is defense in depth for managed production, not a substitute for application checks. Workers re-authorize ownership and active state when executing jobs.
