# M1-002: FastAPI Application Foundation

Task specification placeholder. Scope must be approved before implementation.
# MindVault — M1-002 FastAPI Application Foundation

## Document Information

* **Task ID:** M1-002
* **Task Name:** FastAPI Application Foundation
* **Milestone:** Milestone 1 — Platform Foundation and Ingestion
* **Status:** Approved
* **Depends On:** M1-001 — Project Bootstrap
* **Version:** 1.0

---

## Objective

Create the initial production-ready FastAPI application foundation for MindVault.

This task establishes:

* Backend runtime
* Application configuration
* API versioning
* Health endpoints
* Logging
* Error handling
* CORS
* Python dependency management
* Automated tests
* Backend Docker image
* Backend development documentation

This task must not implement database integration or business features.

---

## Business Context

MindVault will eventually support:

* User authentication
* Workspaces
* Document uploads
* Object storage
* Background processing
* Audio transcription
* AI-generated notes
* Hybrid retrieval
* RAG conversations

These capabilities require a reliable backend application foundation.

This task creates that foundation without prematurely introducing future infrastructure or business logic.

---

## Expected Outcome

After this task is complete, a developer must be able to:

1. Install the backend dependencies.
2. Start the FastAPI application locally.
3. Open the generated OpenAPI documentation.
4. Call versioned health endpoints.
5. Configure the application using environment variables.
6. Run tests, linting, formatting checks, and type checking.
7. Build and run the backend Docker image.

---

## Architecture Constraints

The MindVault backend is a modular monolith.

The implementation must support future domains without introducing unnecessary abstraction.

Use:

* Python 3.13
* FastAPI
* Pydantic v2
* `pydantic-settings`
* Uvicorn
* Pytest
* HTTPX
* Ruff
* MyPy

Do not introduce:

* A third-party dependency injection framework
* Repository interfaces
* Service abstractions
* Event buses
* Provider factories
* Database abstractions
* Framework-independent domain layers without an actual business requirement

FastAPI dependency injection may be used where appropriate.

Prefer simple functions and modules over speculative design patterns.

---

## Scope

Implement:

* Python project configuration
* FastAPI application factory
* Environment-based settings
* API versioning
* Root metadata endpoint
* Liveness endpoint
* Readiness endpoint
* Pydantic response schemas
* Logging configuration
* Application exception foundation
* Consistent API error responses
* CORS configuration
* Backend Dockerfile
* Automated tests
* Backend development documentation

---

## Out of Scope

Do not implement:

* PostgreSQL
* SQLAlchemy
* Alembic
* Database models
* User registration
* Authentication
* JWT tokens
* Refresh tokens
* RBAC
* Redis
* Dramatiq
* MinIO
* S3 storage
* Document uploads
* File processing
* Audio transcription
* AI providers
* Embeddings
* Semantic search
* RAG
* Billing
* Kubernetes
* Nginx
* Metrics
* Distributed tracing
* External logging platforms

Do not modify unrelated frontend or infrastructure files.

Do not implement future tasks.

---

## Required Backend Structure

Use the existing repository structure where possible.

The relevant backend structure should be:

```text
backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── router.py
│   │       └── endpoints/
│   │           ├── __init__.py
│   │           └── health.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── exceptions.py
│   │   └── logging.py
│   │
│   └── schemas/
│       ├── __init__.py
│       ├── error.py
│       └── health.py
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── api/
│       ├── __init__.py
│       └── test_health.py
│
├── .dockerignore
├── Dockerfile
├── pyproject.toml
└── README.md
```

Requirements:

* Preserve existing directories created by M1-001.
* Do not delete folders reserved for future modules.
* Do not create duplicate test directories.
* Use `backend/tests/` as the canonical backend test location.
* Do not overwrite unrelated existing files.
* Modify existing placeholder files only when required by this task.

---

## Application Factory

Create an application factory:

```python
def create_application() -> FastAPI:
    ...
```

Expose the module-level ASGI application:

```python
app = create_application()
```

The application must start using:

```bash
uvicorn app.main:app
```

### Why

An application factory improves:

* Testability
* Configuration control
* Router registration
* Middleware registration
* Future application lifespan management

Do not create factory hierarchies or plugin systems.

---

## Application Configuration

Implement settings using `pydantic-settings`.

Settings must load from environment variables.

Required settings:

| Environment variable | Purpose                  | Default                 |
| -------------------- | ------------------------ | ----------------------- |
| `APP_NAME`           | Public API name          | `MindVault API`         |
| `APP_VERSION`        | Application version      | `0.1.0`                 |
| `APP_ENV`            | Runtime environment      | `development`           |
| `APP_DEBUG`          | Debug mode               | `false`                 |
| `API_V1_PREFIX`      | Versioned API prefix     | `/api/v1`               |
| `APP_HOST`           | Server host              | `0.0.0.0`               |
| `APP_PORT`           | Server port              | `8000`                  |
| `LOG_LEVEL`          | Logging level            | `INFO`                  |
| `CORS_ORIGINS`       | Allowed frontend origins | `http://localhost:5173` |

Supported environment values:

* `development`
* `test`
* `staging`
* `production`

Requirements:

* Use an enum or constrained type for `APP_ENV`.
* Debug mode must default to `false`.
* Settings must not contain secrets.
* Do not print the complete settings object in logs.
* Update the root `.env.example` with these values when necessary.
* Do not create a separate backend `.env` containing real values.

---

## CORS Configuration

Configure FastAPI CORS middleware using application settings.

Requirements:

* Origins must be configuration-driven.
* The local React development origin may be enabled by default.
* Production must not allow every origin by default.
* Do not use `"*"` as the production origin configuration.
* Credentials may only be enabled when appropriate for the configured origins.
* CORS origin parsing must support a practical environment-variable format.

A comma-separated format is acceptable:

```text
CORS_ORIGINS=http://localhost:5173,http://localhost:3000
```

---

## API Versioning

All business-facing API endpoints must eventually live under:

```text
/api/v1
```

For this task, register the health router under the configured API v1 prefix.

Do not hardcode the prefix in multiple files.

---

## Root Endpoint

Implement:

```http
GET /
```

Expected response:

```json
{
  "name": "MindVault API",
  "version": "0.1.0",
  "environment": "development",
  "docs_url": "/docs"
}
```

Requirements:

* Return HTTP 200.
* Use a Pydantic response model or an explicitly typed response.
* Do not expose secrets.
* Do not expose filesystem paths.
* Do not expose installed dependency versions.
* Do not expose internal infrastructure details.

---

## Liveness Endpoint

Implement:

```http
GET /api/v1/health/live
```

Expected response:

```json
{
  "status": "ok"
}
```

Purpose:

Confirms that the FastAPI application process is running.

Requirements:

* Return HTTP 200.
* Do not check PostgreSQL, Redis, or storage.
* Use a Pydantic response model.

---

## Readiness Endpoint

Implement:

```http
GET /api/v1/health/ready
```

Expected response for this task:

```json
{
  "status": "ready",
  "checks": {}
}
```

Purpose:

Provides a future location for dependency readiness checks.

Requirements:

* Return HTTP 200.
* Do not add fake database, Redis, or storage checks.
* Use a Pydantic response model.
* Keep the checks structure extensible but simple.

---

## OpenAPI Configuration

Configure FastAPI-generated OpenAPI documentation.

Required routes:

* Swagger UI: `/docs`
* ReDoc: `/redoc`
* OpenAPI schema: `/openapi.json`

Configure:

* Application title
* Application description
* Application version
* Contact or license metadata only when accurate and approved

Do not manually create an OpenAPI YAML file in this task.

---

## Logging

Implement a small logging configuration using Python’s standard `logging` module.

Requirements:

* Log level comes from settings.
* Use a consistent human-readable format.
* Avoid duplicate handlers during tests or application reloads.
* Application startup should emit a concise log message.
* Unexpected application errors must be logged.
* Do not log secrets.
* Do not log full environment variables.
* Do not log authorization headers.
* Do not add external logging dependencies.

Do not introduce:

* Loguru
* Structlog
* OpenTelemetry
* External log aggregation
* Distributed tracing

These may be considered in a later observability task.

---

## Exception Handling

Create a minimal application exception foundation.

Implement:

* A base `MindVaultException`
* A machine-readable error code
* A public error message
* An HTTP status code
* A handler for known MindVault exceptions
* A generic handler for unexpected exceptions
* A consistent error response schema

Expected error shape:

```json
{
  "error": {
    "code": "internal_server_error",
    "message": "An unexpected error occurred."
  }
}
```

Requirements:

* Known application errors must use their defined status code.
* Unexpected errors must return HTTP 500.
* Unexpected errors must be logged.
* Production responses must not expose stack traces.
* Production responses must not expose raw exception messages.
* Do not create a large exception hierarchy.
* Do not add business-specific exceptions.

---

## Middleware

Required middleware:

* CORS middleware

A lightweight request ID middleware may only be introduced if:

* It remains small.
* It has automated tests.
* It does not add unnecessary dependencies.
* It is useful for correlating error logs.

Do not add:

* Authentication middleware
* Rate-limiting middleware
* Metrics middleware
* Database-session middleware
* Distributed tracing middleware

---

## Dependency Management

Use `backend/pyproject.toml` as the source of truth for Python dependencies and tooling.

### Runtime dependencies

Include only dependencies required by this task, such as:

* FastAPI
* Uvicorn
* Pydantic
* `pydantic-settings`

### Development dependencies

Include only development tools required by this task, such as:

* Pytest
* HTTPX
* Ruff
* MyPy

Add async testing support only when required by the chosen test approach.

Do not add:

* SQLAlchemy
* Alembic
* Asyncpg
* Redis
* Dramatiq
* Boto3
* MinIO SDK
* JWT libraries
* Password-hashing libraries
* AI SDKs
* pgvector

Configure:

* Pytest
* Ruff
* MyPy

Use reasonable strictness.

Do not configure checks that cannot pass against the implemented code.

---

## Dockerfile

Create `backend/Dockerfile`.

Requirements:

* Use an official Python 3.13 slim image.
* Set a clear working directory.
* Avoid unnecessary operating-system packages.
* Install backend dependencies from the project configuration.
* Copy the application source.
* Use a non-root runtime user.
* Expose port `8000`.
* Start Uvicorn using `app.main:app`.
* Do not use `--reload` in the Docker command.
* Do not include frontend assets.
* Do not include PostgreSQL, Redis, or MinIO setup.
* Do not copy secrets into the image.

A multi-stage build is optional.

Prefer clarity and reproducibility over premature optimization.

---

## Docker Ignore

Create `backend/.dockerignore`.

Exclude at minimum:

* Python cache files
* Test caches
* Virtual environments
* Git metadata
* Local environment files
* IDE configuration
* Coverage output
* Build artifacts

Do not exclude required application source.

---

## Backend README

Update `backend/README.md`.

Include:

* Backend purpose
* Technology stack
* Prerequisites
* Environment setup
* Dependency installation
* Local development server command
* Test command
* Ruff lint command
* Ruff formatting command
* MyPy command
* Docker build command
* Docker run command
* Available endpoints
* Current scope limitations

All commands must reflect the actual implementation.

Do not document unverified commands.

---

## Testing Requirements

Write automated tests for the following.

### Application creation

Verify:

* The FastAPI application can be created.
* Application title is configured.
* Application version is configured.
* Required routers are registered.

### Root endpoint

Verify:

* Returns HTTP 200.
* Returns the application name.
* Returns the application version.
* Returns the environment.
* Returns the docs URL.
* Does not expose sensitive fields.

### Liveness endpoint

Verify:

* Returns HTTP 200.
* Returns:

```json
{
  "status": "ok"
}
```

### Readiness endpoint

Verify:

* Returns HTTP 200.
* Returns:

```json
{
  "status": "ready",
  "checks": {}
}
```

### Configuration

Test useful configuration behavior:

* Default environment value
* Supported environment parsing
* Default API prefix
* CORS origin parsing
* Debug mode default

Do not test Pydantic internals.

### Error handling

Verify:

* A known MindVault exception returns the expected status code.
* A known MindVault exception returns the standard error shape.
* An unexpected exception returns HTTP 500.
* Unexpected exceptions do not expose raw exception messages.

A test-only route may be registered on a test application when necessary.

Do not add public production routes solely for testing exceptions.

### Test isolation

Tests must not require:

* PostgreSQL
* Redis
* S3
* MinIO
* External APIs
* Internet access

---

## Validation Commands

The project must support commands equivalent to:

```bash
pytest
ruff check .
ruff format --check .
mypy app
```

Run these commands from the `backend/` directory unless the project configuration specifies otherwise.

Also verify application import:

```bash
python -c "from app.main import app; print(app.title)"
```

Where Docker is available, verify:

```bash
docker build -t mindvault-backend ./backend
```

If Docker is unavailable:

* Report that it was not executed.
* Do not claim that the image build passed.

---

## Security Requirements

* No secrets in source control.
* Debug mode defaults to disabled.
* Production CORS must not allow all origins by default.
* Unexpected errors must not expose stack traces.
* Unexpected errors must not expose raw exception messages.
* Health endpoints must not expose sensitive infrastructure details.
* Docker must run as a non-root user.
* Environment-specific behavior must be explicit.
* Dependency versions should use reasonable constraints.
* Do not add development-only behavior to the production Docker command.

---

## Documentation Requirements

Update only documentation directly affected by this task.

Required updates:

* `backend/README.md`
* Root `.env.example`, when needed
* `docs/PROJECT_PLAN.md` task status only when instructed by the project workflow

Do not invent missing architecture documents.

Do not change approved architectural decisions.

If the implementation conflicts with an approved ADR or architecture document, stop and report the conflict.

---

## Acceptance Criteria

M1-002 is complete when:

1. `backend/pyproject.toml` contains the required runtime dependencies.
2. `backend/pyproject.toml` contains the required development tooling.
3. The application starts using:

```bash
uvicorn app.main:app
```

4. `GET /` returns HTTP 200 and public application metadata.
5. `GET /api/v1/health/live` returns HTTP 200.
6. `GET /api/v1/health/ready` returns HTTP 200.
7. Swagger documentation is available at `/docs`.
8. ReDoc documentation is available at `/redoc`.
9. OpenAPI JSON is available at `/openapi.json`.
10. Settings load from environment variables.
11. CORS origins are configuration-driven.
12. Debug mode defaults to disabled.
13. Logging is configured without duplicate handlers.
14. Known application exceptions use the standard error response.
15. Unexpected exceptions return a safe HTTP 500 response.
16. Tests pass.
17. Ruff linting passes.
18. Ruff formatting validation passes.
19. MyPy validation passes.
20. Application import succeeds.
21. The backend Docker image builds when Docker is available.
22. The Docker container runs as a non-root user.
23. Backend documentation matches the actual commands.
24. No database or business features are introduced.
25. No unrelated files are overwritten or deleted.

---

## Definition of Done

This task is complete only when:

* All acceptance criteria are satisfied.
* Implementation remains within scope.
* Automated tests pass.
* Linting passes.
* Formatting validation passes.
* Type checking passes.
* Application import succeeds.
* Docker validation is completed when available.
* Documentation matches the implementation.
* A completion report is provided.
* Unavailable validation steps are reported honestly.
* No future milestone functionality is implemented.

---

## Completion Report Requirements

At completion, provide the following.

### Summary

Describe the backend foundation implemented.

### Files Created

List every newly created file.

### Files Modified

List every modified file.

### Files Removed

List removed files, or explicitly state that none were removed.

### Architecture Notes

Explain significant implementation decisions and tradeoffs.

### Validation Results

Report the actual results of:

* Pytest
* Ruff linting
* Ruff formatting check
* MyPy
* Application import
* Docker build, when available
* Docker runtime verification, when available

### Assumptions

List assumptions made during implementation.

### Risks

List unresolved risks.

### Follow-Up Recommendations

List recommended future work without implementing it.

---

## Codex Execution Instruction

Codex must follow:

```text
docs/engineering/codex-workflow.md
```

Codex must also read:

```text
AGENTS.md
docs/PROJECT_PLAN.md
```

before implementation.

Codex must implement only this approved task.
