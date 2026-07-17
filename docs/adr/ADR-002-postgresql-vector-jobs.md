# ADR-002: PostgreSQL for Records, Vectors, and Durable Jobs

Status: Proposed

## Decision

Use PostgreSQL with pgvector as the system of record, lexical/vector retrieval store, transactional outbox and MVP durable job queue.

## Rationale

This removes distributed commit gaps and an extra broker while launch throughput is modest.

## Consequences

Workers need leases, heartbeats, backoff, dead-lettering and reconciliation. Reassess a broker when measured queue load affects database SLOs.
