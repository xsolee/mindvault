# ADR-010: Tombstone, Purge, Export, and Backup Expiry

Status: Proposed

## Decision

Tombstone immediately, exhaustively purge source-derived artifacts asynchronously, expire encrypted backups within 30 days, replay an independent content-free deletion ledger before restored service access, and create versioned short-lived asynchronous ZIP exports containing originals, transcripts, notes and JSON metadata.

## Rationale

This reconciles immediate privacy behavior with operational recovery and portable exports.

## Consequences

Deletion races, backup lifecycle, restores, export snapshots and signed-download expiry require explicit workflows and tests.
