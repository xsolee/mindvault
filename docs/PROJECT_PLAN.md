# Milestone 1 — Platform Foundation and Ingestion

## Objective

Build the production-ready application foundation required for:

* User accounts
* Personal workspaces
* Secure authentication
* Persistent PostgreSQL storage
* S3-compatible object storage
* Secure document uploads
* Asynchronous background processing
* Text extraction
* Audio transcription
* Document management
* Initial frontend workflows

Milestone 1 must produce a complete working application in which a user can register, log in, upload supported files, monitor processing, view extracted content or transcripts, and manage their documents.

## Out of Scope

Milestone 1 does not include:

* Grammar correction
* AI-generated summaries
* Structured AI notes
* Action item generation
* Project or topic detection
* Chunking
* Embeddings
* pgvector retrieval
* Semantic search
* Hybrid search
* RAG conversations
* Knowledge graphs
* Billing
* Kubernetes production deployment

These capabilities belong to later milestones.

---

## Milestone 1 Task Dashboard

| ID     | Task                                           | Status    | Depends On                     |
| ------ | ---------------------------------------------- | --------- | ------------------------------ |
| M1-001 | Project Bootstrap                              | Completed | None                           |
| M1-002 | FastAPI Application Foundation                 | Completed | M1-001                         |
| M1-003 | PostgreSQL Foundation                          | Approved  | M1-002                         |
| M1-004 | Docker Compose Development Environment         | Draft     | M1-002, M1-003                 |
| M1-005 | User and Workspace Domain                      | Draft     | M1-003                         |
| M1-006 | Authentication Foundation                      | Draft     | M1-005                         |
| M1-007 | Storage Foundation                             | Draft     | M1-004, M1-005                 |
| M1-008 | Document Domain                                | Draft     | M1-005, M1-007                 |
| M1-009 | Secure Document Upload                         | Draft     | M1-006, M1-007, M1-008         |
| M1-010 | Background Processing Foundation               | Draft     | M1-004, M1-008                 |
| M1-011 | Text Extraction Pipeline                       | Draft     | M1-009, M1-010                 |
| M1-012 | Audio Transcription Pipeline                   | Draft     | M1-009, M1-010                 |
| M1-013 | Document Management API                        | Draft     | M1-008, M1-009, M1-011, M1-012 |
| M1-014 | Frontend Application Foundation                | Draft     | M1-002                         |
| M1-015 | Authentication User Interface                  | Draft     | M1-006, M1-014                 |
| M1-016 | Document Upload and Management Interface       | Draft     | M1-013, M1-014, M1-015         |
| M1-017 | Milestone 1 Integration and Release Validation | Draft     | M1-001 through M1-016          |

Codex may only implement a task when:

1. The task status is `Approved`.
2. All dependencies are marked `Completed`.
3. The task specification exists and is approved.
4. No unresolved conflict exists with an ADR or architecture document.

---

## M1-001 — Project Bootstrap

* **Status:** Completed
* **Specification:** `docs/tasks/M1-001-project-bootstrap.md`
* **Depends On:** None

### Goal

Create the initial MindVault monorepo and its engineering governance foundation.

### Main Deliverables

* Root repository structure
* Backend, frontend, documentation, and infrastructure directories
* `AGENTS.md`
* `docs/engineering/codex-workflow.md`
* Root configuration placeholders
* Documentation structure
* License decision
* Git-based engineering workflow

---

## M1-002 — FastAPI Application Foundation

* **Status:** Completed
* **Specification:** `docs/tasks/M1-002-fastapi-application-foundation.md`
* **Depends On:** M1-001

### Goal

Create a production-ready FastAPI application foundation without database integration or business features.

### Main Deliverables

* FastAPI application factory
* Environment-based application settings
* API versioning
* Root metadata endpoint
* Liveness endpoint
* Readiness endpoint
* Logging foundation
* Consistent exception handling
* CORS configuration
* OpenAPI documentation
* Pytest configuration
* Ruff configuration
* MyPy configuration
* Backend Dockerfile
* Backend development documentation

### Completion Result

The backend starts successfully and exposes:

```text
GET /
GET /api/v1/health/live
GET /api/v1/health/ready
GET /docs
GET /redoc
GET /openapi.json
```

---

## M1-003 — PostgreSQL Foundation

* **Status:** Approved
* **Specification:** `docs/tasks/M1-003-postgresql-foundation.md`
* **Depends On:** M1-002

### Goal

Integrate PostgreSQL, SQLAlchemy 2, and Alembic into the FastAPI application.

### Planned Deliverables

* PostgreSQL configuration
* SQLAlchemy asynchronous engine
* Async session factory
* Request-scoped database dependency
* Declarative model base
* Shared model conventions
* Alembic initialization
* Migration workflow
* Database readiness check
* Integration-test database configuration
* Transaction-isolated test fixtures
* Database development documentation

### Out of Scope

* User model
* Workspace model
* Authentication
* Document model
* Redis
* pgvector

---

## M1-004 — Docker Compose Development Environment

* **Status:** Draft
* **Specification:** `docs/tasks/M1-004-docker-compose-development-environment.md`
* **Depends On:** M1-002 and M1-003

### Goal

Create a repeatable local development environment that starts the required platform infrastructure with one command.

### Planned Services

* FastAPI backend
* PostgreSQL
* Redis
* MinIO
* MinIO initialization service

### Planned Deliverables

* Docker Compose configuration
* Environment-variable integration
* Persistent development volumes
* Service health checks
* Internal service networking
* Startup dependency handling
* Development commands
* Troubleshooting documentation

### Out of Scope

* Production deployment
* Kubernetes
* Reverse proxy
* Monitoring platform
* Frontend production container

---

## M1-005 — User and Workspace Domain

* **Status:** Draft
* **Specification:** `docs/tasks/M1-005-user-workspace-domain.md`
* **Depends On:** M1-003

### Goal

Create the core user, workspace, membership, and tenancy data model.

### Planned Deliverables

* User database model
* Workspace database model
* Workspace membership model
* Workspace roles
* Personal workspace rules
* Common timestamp conventions
* Database migrations
* Domain constraints
* Tenant-ownership conventions
* Unit and integration tests

### Design Rule

Every tenant-owned resource introduced after this task must include or reliably derive a `workspace_id`.

---

## M1-006 — Authentication Foundation

* **Status:** Draft
* **Specification:** `docs/tasks/M1-006-authentication-foundation.md`
* **Depends On:** M1-005

### Goal

Implement secure registration, login, access-token issuance, refresh-token rotation, logout, and current-user retrieval.

### Planned Deliverables

* User registration
* Personal workspace creation during registration
* Argon2id password hashing
* Login endpoint
* JWT access tokens
* Refresh tokens
* Refresh-token hashing
* Refresh-token rotation
* Token revocation
* Logout
* Current-user endpoint
* Authentication dependencies
* Security-focused tests

### Out of Scope

* Social login
* Multi-factor authentication
* Password reset
* Email verification
* Organization invitations
* Subscription plans

---

## M1-007 — Storage Foundation

* **Status:** Draft
* **Specification:** `docs/tasks/M1-007-storage-foundation.md`
* **Depends On:** M1-004 and M1-005

### Goal

Create a provider-independent object-storage layer using S3-compatible APIs.

### Planned Deliverables

* Storage provider contract
* S3-compatible provider implementation
* MinIO development integration
* Object-key conventions
* Upload streaming
* Download streaming
* Signed download URLs
* Object existence checks
* Delete support
* Storage error mapping
* Integration tests

### Design Rules

* Original uploaded files are immutable.
* Storage keys must not expose user-provided paths.
* Business logic must not depend directly on MinIO or AWS SDK details.
* Derived artifacts must be stored separately from originals.

---

## M1-008 — Document Domain

* **Status:** Draft
* **Specification:** `docs/tasks/M1-008-document-domain.md`
* **Depends On:** M1-005 and M1-007

### Goal

Create the document metadata, artifact, and processing lifecycle domain.

### Planned Deliverables

* Document model
* Document artifact model
* Processing job model
* Processing attempt model
* Document status definitions
* Artifact type definitions
* Workspace ownership
* Uploaded-by relationship
* File metadata
* Storage references
* Content hash
* Soft-delete fields
* Database migrations
* Domain tests

### Initial Document Statuses

```text
UPLOADING
UPLOADED
QUEUED
PROCESSING
READY
FAILED
DELETED
```

---

## M1-009 — Secure Document Upload

* **Status:** Draft
* **Specification:** `docs/tasks/M1-009-secure-document-upload.md`
* **Depends On:** M1-006, M1-007, and M1-008

### Goal

Allow authenticated users to upload supported files safely.

### Initial Supported Formats

* TXT
* PDF
* DOCX
* Approved audio formats

### Planned Deliverables

* Authenticated upload endpoint
* Workspace authorization
* Streaming upload
* File-size validation
* Extension allowlist
* MIME-type validation
* Filename normalization
* Content hashing
* Duplicate handling policy
* Storage persistence
* Document metadata persistence
* Failure cleanup
* Upload API tests

### Security Requirements

* Never trust the client-provided MIME type alone.
* Never use the original filename as the storage key.
* Enforce upload limits before excessive resource use.
* Prevent cross-workspace access.
* Do not load large files entirely into memory.

---

## M1-010 — Background Processing Foundation

* **Status:** Draft
* **Specification:** `docs/tasks/M1-010-background-processing-foundation.md`
* **Depends On:** M1-004 and M1-008

### Goal

Integrate Redis and Dramatiq for asynchronous, observable, and retry-safe document processing.

### Planned Deliverables

* Redis broker configuration
* Dramatiq configuration
* Worker entry point
* Task enqueueing
* Processing job creation
* Job status updates
* Retry policy
* Backoff policy
* Failure recording
* Job attempt recording
* Idempotency conventions
* Worker tests
* Worker development documentation

### Design Rule

Every background task must be safe to execute more than once.

---

## M1-011 — Text Extraction Pipeline

* **Status:** Draft
* **Specification:** `docs/tasks/M1-011-text-extraction-pipeline.md`
* **Depends On:** M1-009 and M1-010

### Goal

Extract raw text and source metadata from TXT, PDF, and DOCX documents.

### Planned Deliverables

* Text-extractor contract
* TXT extractor
* PDF extractor
* DOCX extractor
* Raw-text artifact
* PDF page metadata
* DOCX paragraph or section metadata where available
* Extraction status updates
* Failure handling
* Retry-safe artifact generation
* Controlled test fixtures
* Extraction tests

### Out of Scope

* OCR
* Grammar correction
* Summaries
* Chunking
* Embeddings

---

## M1-012 — Audio Transcription Pipeline

* **Status:** Draft
* **Specification:** `docs/tasks/M1-012-audio-transcription-pipeline.md`
* **Depends On:** M1-009 and M1-010

### Goal

Transcribe uploaded audio through a replaceable speech-to-text provider.

### Planned Deliverables

* Speech-to-text provider contract
* Initial provider implementation
* Audio validation
* Raw transcript artifact
* Timestamped transcript segments
* Detected or selected language metadata
* Provider and model metadata
* Processing duration
* Usage metadata
* Cost metadata where available
* Retry-safe transcription
* Failure handling
* Contract tests

### Design Rule

The application must not depend directly on one transcription vendor.

---

## M1-013 — Document Management API

* **Status:** Draft
* **Specification:** `docs/tasks/M1-013-document-management-api.md`
* **Depends On:** M1-008, M1-009, M1-011, and M1-012

### Goal

Allow users to list, inspect, download, and remove documents and their derived artifacts.

### Planned Deliverables

* Paginated document listing
* Filtering by status
* Filtering by file type
* Document detail endpoint
* Artifact listing
* Artifact content retrieval
* Processing status retrieval
* Signed original-file download
* Soft-delete operation
* Workspace authorization
* API tests

---

## M1-014 — Frontend Application Foundation

* **Status:** Draft
* **Specification:** `docs/tasks/M1-014-frontend-application-foundation.md`
* **Depends On:** M1-002

### Goal

Create the production-ready React application shell.

### Planned Deliverables

* React
* TypeScript
* Vite
* Material UI theme
* TanStack Query provider
* React Router
* Application layout
* API client foundation
* Environment configuration
* Global error boundary
* Loading and error conventions
* ESLint or approved linting configuration
* Type checking
* Frontend tests
* Frontend Dockerfile
* Frontend development documentation

---

## M1-015 — Authentication User Interface

* **Status:** Draft
* **Specification:** `docs/tasks/M1-015-authentication-user-interface.md`
* **Depends On:** M1-006 and M1-014

### Goal

Implement registration, login, logout, session restoration, and protected frontend routes.

### Planned Deliverables

* Registration page
* Login page
* Form validation
* Authentication state
* Protected route handling
* Access-token handling
* Refresh-token workflow
* Session restoration
* Logout
* API error presentation
* Authentication UI tests

---

## M1-016 — Document Upload and Management Interface

* **Status:** Draft
* **Specification:** `docs/tasks/M1-016-document-upload-management-interface.md`
* **Depends On:** M1-013, M1-014, and M1-015

### Goal

Allow authenticated users to upload, browse, inspect, download, and delete documents through the frontend.

### Planned Deliverables

* File upload interface
* Supported-format guidance
* Client-side validation feedback
* Upload progress
* Document list
* Filtering and pagination
* Processing status display
* Document detail page
* Extracted text viewer
* Transcript viewer
* Original-file download
* Delete confirmation
* Status polling or controlled refresh
* UI tests

---

## M1-017 — Milestone 1 Integration and Release Validation

* **Status:** Draft
* **Specification:** `docs/tasks/M1-017-milestone-1-integration-validation.md`
* **Depends On:** M1-001 through M1-016

### Goal

Validate Milestone 1 as a complete integrated application.

### Planned Deliverables

* Full Docker Compose startup validation
* Registration and login validation
* Personal workspace validation
* TXT upload flow
* PDF upload flow
* DOCX upload flow
* Audio upload flow
* Text extraction validation
* Audio transcription validation
* Document-management validation
* Restart and persistence validation
* Workspace-isolation validation
* Failed-job and retry validation
* Security checklist
* Test-suite execution
* Documentation audit
* Known-limitations report
* Milestone completion report

---

# Milestone 1 Execution Order

The official implementation order is:

```text
M1-001 Project Bootstrap
    ↓
M1-002 FastAPI Application Foundation
    ↓
M1-003 PostgreSQL Foundation
    ↓
M1-004 Docker Compose Development Environment
    ↓
M1-005 User and Workspace Domain
    ↓
M1-006 Authentication Foundation
    ↓
M1-007 Storage Foundation
    ↓
M1-008 Document Domain
    ↓
M1-009 Secure Document Upload
    ↓
M1-010 Background Processing Foundation
    ↓
M1-011 Text Extraction Pipeline
    ↓
M1-012 Audio Transcription Pipeline
    ↓
M1-013 Document Management API
    ↓
M1-014 Frontend Application Foundation
    ↓
M1-015 Authentication User Interface
    ↓
M1-016 Document Upload and Management Interface
    ↓
M1-017 Integration and Release Validation
```

Some tasks may be implemented in parallel only when all dependencies are satisfied and the project owner explicitly approves parallel execution.

Codex must not independently reorder tasks.

---

# Current Project Status

## Completed

| ID     | Task              |
| ------ | ----------------- |
| M1-001 | Project Bootstrap |

## Approved and Ready for Implementation

| ID     | Task                           | Specification                                         |
| ------ | ------------------------------ | ----------------------------------------------------- |
| M1-002 | FastAPI Application Foundation | `docs/tasks/M1-002-fastapi-application-foundation.md` |

## Draft

| ID     | Task                                           |
| ------ | ---------------------------------------------- |
| M1-003 | PostgreSQL Foundation                          |
| M1-004 | Docker Compose Development Environment         |
| M1-005 | User and Workspace Domain                      |
| M1-006 | Authentication Foundation                      |
| M1-007 | Storage Foundation                             |
| M1-008 | Document Domain                                |
| M1-009 | Secure Document Upload                         |
| M1-010 | Background Processing Foundation               |
| M1-011 | Text Extraction Pipeline                       |
| M1-012 | Audio Transcription Pipeline                   |
| M1-013 | Document Management API                        |
| M1-014 | Frontend Application Foundation                |
| M1-015 | Authentication User Interface                  |
| M1-016 | Document Upload and Management Interface       |
| M1-017 | Milestone 1 Integration and Release Validation |

## Current Next Action

Implement:

```text
docs/tasks/M1-002-fastapi-application-foundation.md
```

using:

```text
docs/engineering/codex-workflow.md
```

Codex instruction:

```text
Follow the workflow in docs/engineering/codex-workflow.md.

Implement docs/tasks/M1-002-fastapi-application-foundation.md.
```

---

# Status Update Rules

When work begins on an approved task:

```text
Approved → Implementing
```

When Codex finishes implementation and validation:

```text
Implementing → Code Review
```

After architectural review, required fixes, and final validation:

```text
Code Review → Completed
```

Only after the current task is marked `Completed` may its direct successor be changed from:

```text
Draft → Approved
```

A status change must be committed to Git.

Example commits:

```text
docs: mark M1-002 as implementing
docs: move M1-002 to code review
docs: complete M1-002 FastAPI application foundation
docs: approve M1-003 PostgreSQL foundation
```

---

# Task Approval Rule

Before changing a task from `Draft` to `Approved`, confirm that:

1. Its complete specification exists.
2. Its dependencies are completed.
3. Relevant architectural decisions are documented.
4. Acceptance criteria are measurable.
5. Security requirements are defined.
6. Testing requirements are defined.
7. Out-of-scope boundaries are explicit.
8. The project plan and task specification agree.
