# ADR-006: Separate Web and Android Apps in One Monorepo

Status: Proposed

## Decision

Use pnpm workspaces with React web and Expo/React Native Android apps sharing generated contracts and non-UI packages, not a forced universal UI.

## Rationale

Native background recording needs platform integration while web needs independent static/Vercel deployment.

## Consequences

Some UI duplication is accepted. Android uses native development builds and a durable SQLite upload outbox.
