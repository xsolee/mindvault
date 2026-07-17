# ADR-009: Managed-First and Self-Hosted Docker Profiles

Status: Proposed

## Decision

Launch managed in Singapore using Vercel, Render and Supabase while maintaining a complete Docker Compose profile with equivalent application semantics.

## Rationale

Managed operations accelerate launch; Docker preserves portability and local/self-hosted use.

## Consequences

CI must validate both profiles. The Android artifact is built separately and is not containerized.
