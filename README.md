# MindVault

MindVault is a personal knowledge system for capturing ideas and preparation notes through voice, text, and uploaded documents. It connects related material and answers questions with traceable source citations.

The repository is being rebuilt from an approved product specification. Application implementation has not started.

## Approved baseline

- Backend: Python 3.13 and FastAPI
- Frontend: React and TypeScript
- Data: PostgreSQL with vector retrieval support
- AI: provider-independent transcription, embeddings, retrieval, and generation
- Runtime: Docker images for application components and Docker Compose for complete local and self-hosted production stacks
- Deployment goal: fully self-hostable with Docker while keeping the frontend, API, database, and storage compatible with managed alternatives such as Vercel and Supabase

Technology choices beyond this baseline require architecture review and, when consequential, an ADR.

## Documentation

- [Product brief](docs/product/product-brief.md)
- [MVP requirements](docs/product/mvp-requirements.md)
- [Open product questions](docs/product/open-questions.md)
- [Architecture principles](docs/architecture/principles.md)
- [System overview](docs/architecture/system-overview.md)
- [Quality and requirement traceability](docs/architecture/quality-and-traceability.md)
- [Delivery workflow](docs/engineering/delivery-workflow.md)

## Status

Product discovery and MVP requirements are approved. The complete architecture and ADR set are proposed for product-owner approval. Do not begin feature implementation until that gate is accepted.
