# ADR-003: Immutable, Versioned Provenance

Status: Proposed

## Decision

Preserve immutable originals and versioned representations/segments. Citations reference immutable segments aligned to original evidence.

## Rationale

Grounded answers, multilingual normalization, reprocessing and audits require stable lineage.

## Consequences

Storage grows across versions until garbage collection; schema and jobs must maintain lineage and atomic active-version cutover.
