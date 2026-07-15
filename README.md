# MindVault

## Project Overview

MindVault is a production-quality SaaS application for AI-powered personal knowledge management. This repository currently contains the engineering foundation only; product functionality will be delivered in later milestone tasks.

## Vision

MindVault will help people capture, organize, process, and retrieve knowledge across their documents while retaining clear ownership and control of their data.

## Technology Stack

- Backend: Python 3.13, FastAPI, Pydantic 2, SQLAlchemy 2, PostgreSQL, and Dramatiq
- Frontend: React, TypeScript, Material UI, TanStack Query, and Vite
- Storage: S3-compatible object storage
- Delivery: Docker-based local and production environments

The architecture documents define the approved boundaries and are the source of truth as implementation progresses.

## Repository Structure

```text
backend/         Python application and worker foundation
frontend/        React and TypeScript application foundation
docs/            Product, architecture, API, database, and engineering guidance
infrastructure/  Deployment, proxy, monitoring, and operations assets
.github/         Repository automation definitions
```

## Local Development

Local setup instructions will be added with the backend and frontend foundation tasks. This bootstrap intentionally installs no dependencies and starts no services.

## Milestones

Milestone scope and sequencing are maintained in `docs/product/milestones.md` and the task specifications under `docs/tasks/`.

## License

Copyright (c) 2026 MindVault. All rights reserved. See `LICENSE` for details.
