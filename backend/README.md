# MindVault Backend

The MindVault backend is a Python 3.13 FastAPI application. This foundation provides
environment-based configuration, versioned health endpoints, logging, consistent error
responses, CORS, and generated OpenAPI documentation. It intentionally has no database or
business-domain integration yet.

## Technology

- Python 3.13
- FastAPI and Pydantic 2
- Pydantic Settings
- Uvicorn
- Pytest, HTTPX, Ruff, and MyPy for development

## Local development

Prerequisites are Python 3.13 and `pip`. From the `backend/` directory, create and activate a
virtual environment, then install the application and development tools:

```bash
python -m venv .venv
```

PowerShell activation:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Configuration is loaded from environment variables. The supported variables and development
defaults are documented in the root `.env.example`. Copy it to a root `.env` for local overrides,
or export individual variables in the shell. Never commit a populated `.env` file.

Start the development server from `backend/`:

```bash
uvicorn app.main:app --reload
```

Open <http://localhost:8000/docs> for Swagger UI.

## Quality checks

Run these commands from `backend/`:

```bash
pytest
ruff check .
ruff format --check .
mypy app
```

Apply Ruff formatting with:

```bash
ruff format .
```

## Docker

From the repository root, build and run the non-root backend image:

```bash
docker build -t mindvault-backend ./backend
docker run --rm -p 8000:8000 --env-file .env mindvault-backend
```

Omit `--env-file .env` to use application defaults.

## Endpoints

| Method | Path | Purpose |
| --- | --- | --- |
| `GET` | `/` | Public application metadata |
| `GET` | `/api/v1/health/live` | Process liveness |
| `GET` | `/api/v1/health/ready` | Dependency-free readiness |
| `GET` | `/docs` | Swagger UI |
| `GET` | `/redoc` | ReDoc |
| `GET` | `/openapi.json` | Generated OpenAPI schema |

## Current limitations

This milestone does not include persistence, authentication, workspaces, document processing,
queues, object storage, or AI providers. Those capabilities belong to later approved tasks.
