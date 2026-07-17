# ADR-007: Application-Owned Authentication and Rotating Sessions

Status: Proposed

## Decision

Use email/password accounts with Argon2id, short access tokens, one-time rotating hashed refresh sessions, secure web cookies and Android secure storage.

## Rationale

This keeps managed and self-hosted deployments behaviorally equivalent without a mandatory identity platform.

## Consequences

MindVault owns a security-sensitive subsystem and must test recovery, rotation, replay detection, CSRF, revocation and rate limiting thoroughly.
