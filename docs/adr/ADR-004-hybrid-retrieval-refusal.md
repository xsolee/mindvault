# ADR-004: Hybrid Retrieval and Evidence-Gated Answers

Status: Proposed

## Decision

Fuse exact identifiers, full text, metadata and vectors; rerank; generate structured claims; validate every claim/citation; refuse when the versioned evidence policy fails.

## Rationale

Vectors alone are unreliable for exact references and do not prove claim support.

## Consequences

A multilingual golden corpus, measurable thresholds and persisted retrieval telemetry are mandatory.
