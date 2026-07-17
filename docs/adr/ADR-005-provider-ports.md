# ADR-005: Application-Owned Provider Ports

Status: Proposed

## Decision

Isolate storage, transcription, normalization, embeddings, reranking, generation, grounding and email behind application-owned interfaces.

## Rationale

Cost, capability, region and privacy change; core behavior must remain portable.

## Consequences

Adapters must declare capabilities/version and pass conformance tests. Portability does not imply lowest-common-denominator silent fallback.
