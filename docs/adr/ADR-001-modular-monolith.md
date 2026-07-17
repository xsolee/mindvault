# ADR-001: Modular Monolith with API and Worker Processes

Status: Proposed

## Decision

Use one Python modular-monolith codebase and image, run as independently scalable API and worker processes.

## Rationale

It preserves transactional consistency and simple operations while isolating slow ingestion from requests. Module interfaces provide future extraction seams.

## Consequences

Module ownership and dependency rules require tests. Independent services are deferred until measured scaling or organizational needs justify them.
