# ADR-008: S3-Compatible Immutable Storage and Lifecycle

Status: Proposed

## Decision

Use private S3-compatible storage via an application port: Supabase Storage for managed launch and MinIO for self-hosting. Originals are immutable; access uses short-lived scoped authorization.

## Rationale

Both deployment profiles share storage semantics without storing binaries in containers or PostgreSQL.

## Consequences

Upload capabilities differ by provider, so completion verification, checksum and restart-safe client state remain application responsibilities.
