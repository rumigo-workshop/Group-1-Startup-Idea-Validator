# Startup Idea Validator

Startup Idea Validator helps founders turn an early product idea into a structured validation report. The project is being built as a team exercise and brings together a FastAPI service, a React frontend, and supporting tests and container tooling.

## What it aims to answer

Given a founder's idea, the product will help surface:

- Potential competitors and market context
- Customer complaints, trends, and risks
- An overall validation score
- A clear report that can guide the next research step

## Project structure

```text
.
├── packages/
│   ├── api/       FastAPI service
│   ├── tests/     API and integration tests
│   └── web/       React + TypeScript + Vite frontend
├── contribution.md
├── Dockerfile
└── compose.yaml
```

> Some branches may not yet contain every directory. Work from the branch assigned to your issue and keep changes scoped to your area.

## Prerequisites

- Python 3.11+
- Node.js 20+
- npm

## Run the frontend

The web application uses React, TypeScript, and Vite.

```powershell
cd packages\web
npm install
npm run dev
```

Vite prints the local address, usually `http://localhost:5173`.

### Build and lint

```powershell
npm run build
npm run lint
```

### Authors and Books interface

The frontend includes a responsive Authors and Books management screen with:

- Author and book forms
- Author selection for each book
- Loading, empty, and error states
- A built-in mock-data mode for UI testing without an API
- A live API mode for FastAPI integration

Mock mode is enabled by default. To use a live API, create `packages/web/.env.local` locally (never commit it):

```env
VITE_API_URL=http://localhost:8000
```

The frontend live mode expects this API contract:

| Method | Endpoint | Request body |
| --- | --- | --- |
| `GET` | `/authors` | — |
| `POST` | `/authors` | `{ "name": "string", "bio": "string" }` |
| `DELETE` | `/authors/{id}` | — |
| `GET` | `/books` | — |
| `POST` | `/books` | `{ "title": "string", "author_id": 1 }` |
| `DELETE` | `/books/{id}` | — |

## Run the API

From the repository root:

```powershell
cd packages\api
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

Once running, FastAPI's interactive documentation is available at `http://localhost:8000/docs`.

## Containers

When the branch includes the container configuration, start the project with:

```powershell
docker compose up --build
```

## Team workflow

- Read [contribution.md](contribution.md) before starting work.
- Use focused branches named `feat/<issue-number>-short-name`.
- Do not commit `.env` files, tokens, or other secrets.
- Keep commits small and scoped to one issue.
- Open a pull request and request an independent review before merging.

## Current integration note

The Authors and Books frontend uses the API contract above. The backend team should confirm that its response shapes and endpoints match it before live mode is used; mock mode remains available while that integration is completed.
