# MindVault Project Plan

## Document Information

* **Project:** MindVault
* **Version:** 1.0
* **Status:** Active
* **Last Updated:** July 15, 2026

## Purpose

This document is the source of truth for MindVault milestones, task order, dependencies, and task statuses.

Detailed implementation requirements are stored in `docs/tasks/`.

## Task Statuses

* `Draft` — Not ready for implementation
* `Approved` — Ready for implementation
* `Implementing` — Work in progress
* `Code Review` — Implementation completed and awaiting review
* `Completed` — Validated and finished
* `Blocked` — Waiting on a dependency or decision
* `Superseded` — Replaced by another task
* `Cancelled` — No longer planned

Codex may only implement tasks marked `Approved` whose dependencies are `Completed`.

# Milestone 1 — Platform Foundation and Ingestion

## Objective

Build the application foundation required for authentication, workspaces, document storage, uploads, background processing, text extraction, and audio transcription.

RAG, embeddings, semantic search, AI note generation, and knowledge graphs are outside Milestone 1.

## M1-001 — Project Bootstrap

* **Status:** Completed
* **Specification:** `docs/tasks/M1-001-project-bootstrap.md`
* **Depends On:** None

### Goal

Create the initial repository structure, project instructions, engineering workflow, documentation directories, and bootstrap configuration.

## M1-002 — FastAPI Application Foundation

* **Status:** Approved
* **Specification:** `docs/tasks/M1-002-fastapi-application-foundation.md`
* **Depends On:** M1-001 — Project Bootstrap

### Goal

Create the production-ready FastAPI application foundation without database integration or business functionality.

### Deliverables

* FastAPI application factory
* Environment-based settings
* API versioning
* Root metadata endpoint
* Liveness endpoint
* Readiness endpoint
* Logging foundation
* Error-handling foundation
* CORS configuration
* Python project configuration
* Automated tests
* Backend Dockerfile
* Backend development documentation

## M1-003 — PostgreSQL Foundation

* **Status:** Draft
* **Specification:** `docs/tasks/M1-003-postgresql-foundation.md`
* **Depends On:** M1-002

### Goal

Integrate PostgreSQL, SQLAlchemy 2, Alembic, database sessions, and readiness checks.

## Current Project Status

### Completed

* M1-001 — Project Bootstrap

### Approved and Ready

* M1-002 — FastAPI Application Foundation

### Next Action

Implement:

```text
docs/tasks/M1-002-fastapi-application-foundation.md
```

using:

```text
docs/engineering/codex-workflow.md
```

## Task Execution Rule

Before implementing a task:

1. Confirm the task is marked `Approved`.
2. Confirm every dependency is marked `Completed`.
3. Read `AGENTS.md`.
4. Read this project plan.
5. Follow `docs/engineering/codex-workflow.md`.
6. Read the assigned task specification.
7. Inspect the repository.
8. Implement only the approved scope.
9. Run all applicable validation.
10. Provide a completion report.

## Source-of-Truth Priority

When documents conflict, use this order:

1. Approved ADRs
2. Approved architecture and security documentation
3. `docs/PROJECT_PLAN.md`
4. Approved task specification
5. `docs/engineering/codex-workflow.md`
6. Existing implementation
7. Chat history
