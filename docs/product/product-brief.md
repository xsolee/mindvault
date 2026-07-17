# Product Brief

Status: Approved

## Problem

People often have useful ideas, commitments, and preparation notes when writing is inconvenient or unsafe, including while driving. Those notes later become difficult to find or connect with supporting documents.

## Product vision

MindVault provides a private memory workspace where users capture voice or text, upload documents, and later ask questions across all captured material. Answers must identify their supporting sources so users can verify where information came from.

## Initial users

The initial audience is professionals who need to capture ideas and retrieve preparation material for stand-ups, meetings, and presentations. The SaaS supports multiple user accounts, with each user's knowledge isolated by default. Shared workspaces are not approved for MVP.

## Core outcomes

A user can:

1. Record a voice note through a mobile application, including during temporary network loss and while the screen is locked when the operating system permits it.
2. Add a text note through mobile or web.
3. Upload PDF, DOCX, TXT, and Markdown documents.
4. Process content into searchable text while preserving the original source.
5. Ask a question across voice transcripts, notes, and documents.
6. Receive a grounded answer with citations to every supporting source.
7. Open citations as original files, extracted passages, and audio timestamps when the source supports them.
8. Delete owned content and its derived data.
9. Export owned data as a ZIP containing original sources, transcripts, notes, and machine-readable JSON metadata.

## Retrieval behavior

MindVault relates information without requiring users to create tags. It combines:

- exact identifiers and lexical search, such as matching `JIRA-100`
- structured source metadata
- semantic vector retrieval
- relevant conversation context from the current conversation

Conversation history may help interpret a follow-up question, but retrieved source evidence remains required. If sufficient evidence is unavailable, MindVault refuses to invent an answer and explains that it lacks supporting information.

## Language behavior

MVP supports spoken and written English and Filipino. Preserve original source text and transcripts for provenance. Also produce an English normalized representation for cross-language retrieval; never replace or discard the original wording.

## Content integrity

Users cannot edit transcripts, extracted document text, or generated answers in MVP. Corrections require a new source or reprocessing workflow. System-generated metadata must remain distinguishable from original content.

## Safety constraint

Driving capture must minimize interaction. The product must not encourage reading, editing, or navigating while driving. Recording should use a hands-free, low-interaction flow and defer review until the user is no longer driving.

## Application surfaces

- React web application for desktop and mobile browsers
- Expo/React Native mobile application for reliable mobile recording capabilities
- Shared TypeScript packages for API contracts, validation, and reusable non-UI logic

The applications share a monorepo and as much safe code as practical, but platform-specific UI and recording integrations are permitted.

## Approved technical baseline

- Python 3.13 and FastAPI backend
- React, React Native with Expo, and strict TypeScript clients
- PostgreSQL as the system of record
- Vector-assisted retrieval and retrieval-augmented generation
- Provider boundaries for transcription, embeddings, language models, and storage
- Docker-based development and production-ready container images
- Docker Compose environments for complete local and self-hosted production stacks
- Optional managed deployment using compatible frontend, API, PostgreSQL, and object-storage services
- Philippine users and applicable privacy obligations as the initial operational context

## MVP limits

- Voice recording: 30 minutes per recording
- Upload size: 25 MB per document
- Processing: asynchronous, with visible status and retry behavior

These limits must be configurable without code changes. They are product guardrails, not permanent architectural limits.

## Retention and deletion

Deletion removes content from active use and schedules its derived data for deletion. Encrypted backups may retain deleted data for no more than 30 days, after which it must be permanently removed through the backup lifecycle. User-facing behavior must clearly distinguish immediate active-system deletion from backup expiration.

## Launch and deployment

- Android is the initial native mobile launch target; iOS is deferred.
- The first production target is managed cloud infrastructure in a region appropriate for Philippine users. Singapore is acceptable.
- Complete self-hosted Docker deployment remains supported.

## Commercial model

MindVault will offer a Free Trial, Starter subscription, and Pro subscription. Exact prices and included transcription, storage, ingestion, and question allowances require provider selection and unit-economics approval before billing implementation.

## Explicit MVP exclusions

- Shared or collaborative workspaces
- Manual tags
- Editing source-derived text or generated answers
- Billing implementation before pricing and unit economics are approved
- iOS native application
