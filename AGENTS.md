# AGENTS.md

Project guidance for AI coding agents working in this repository.

## graphify

For any question about this repo's architecture, structure, components, or how to add/modify/find
code, your first action should be `graphify query "<question>"` when `graphify-out/graph.json`
exists. Use `graphify path "<A>" "<B>"` for relationship questions and `graphify explain "<concept>"`
for focused-concept questions. These return a scoped subgraph, usually much smaller than the full
report or raw grep output.

Triggers: "how do I…", "where is…", "what does … do", "add/modify a <component>",
"explain the architecture", or anything that depends on how files or classes relate.

If `graphify-out/wiki/index.md` exists, use it for broad navigation. Read `graphify-out/GRAPH_REPORT.md`
only for broad architecture review or when query/path/explain do not surface enough context. Only read
source files when (a) modifying/debugging specific code, (b) the graph lacks the needed detail, or
(c) the graph is missing or stale.

Type `/graphify` in Copilot Chat to build or update the graph.

## Scope And Priorities

- Prioritize `docker/servicio1` (authentication/authorization service) unless asked otherwise.
- Keep solutions simple, academic, and demonstrable. Avoid unnecessary enterprise complexity.
- Optimize for CI repeatability: code should be easy to test, containerize, and run in Jenkins.

## Current Project Context

- Two FastAPI microservices run with Docker Compose.
- Existing orchestration is defined in [docker-compose.yml](docker-compose.yml).
- Base project usage and delivery milestones are documented in [README.md](README.md).
- Documentation folder exists at [docs/entrega1](docs/entrega1), but detailed architecture docs are still pending.

## Expected Stack For Servicio1

- Python 3.11+
- FastAPI + Uvicorn
- SQLAlchemy
- Pydantic
- Pytest
- HTTPX or FastAPI TestClient
- Docker and Docker Compose
- Jenkins (local CI/CD)

## Target Structure For Servicio1

When refactoring from a single-file app, move toward this layout:

```text
docker/servicio1/
  app/
    main.py
    api/
    models/
    schemas/
    services/
    db/
  tests/
```

Use incremental changes to preserve a working state after each step.

## Coding Conventions

- Separate concerns clearly: routes, business logic, data models, schemas, persistence.
- Use environment variables for configuration and secrets. Do not hardcode credentials.
- Keep naming consistent across endpoints, schemas, and services.
- Return explicit HTTP errors with appropriate status codes.
- Design auth logic so it can evolve to JWT + roles/permissions.

## Endpoint Baseline For Servicio1

Implement and maintain these first:

- `GET /health`
- `POST /auth/register`
- `POST /auth/login`
- `GET /auth/me`
- `GET /users/{id}`

All request/response contracts must use Pydantic schemas.

## Testing Expectations

- Create unit tests first, then integration tests.
- Prefer isolated, deterministic tests (no external dependencies unless required).
- Use descriptive test names that validate observable behavior.
- Keep tests runnable locally and in CI with a single command.

Suggested standard commands (once tests exist):

```bash
pytest -q
```

## Docker Expectations

- Keep Dockerfiles readable and minimal.
- Expose the correct service port.
- Use a clear startup command.
- Ensure Compose is suitable for local execution and CI validation steps.

Note: current service Dockerfiles use `uvicorn ... --reload`; avoid `--reload` in CI-oriented runs.

## Jenkins Expectations

When adding `Jenkinsfile`, keep stages explicit and in this order:

1. `checkout`
2. `install`
3. `test`
4. `build`
5. `deploy` (local with Docker or Docker Compose)

Pipeline commands must run in a local Linux/Jenkins environment without manual steps.

## Agent Workflow In This Repo

- Before writing large code blocks, propose folder/file structure first.
- Split big changes into small, verifiable steps.
- If a change impacts tests, Docker, or Jenkins, call that out explicitly.
- Prefer linking to existing project docs instead of duplicating content.

## Incremental Delivery Sequence (Servicio1)

Use this order unless the user requests a different sequence:

1. Create or validate local virtual environment with venv.
2. Install servicio1 dependencies.
3. Confirm development branch exists for feature work.
4. Implement endpoints.
5. Validate manually in Swagger.
6. Add unit tests.
7. Add integration tests.
8. Update Dockerfile if needed.
9. Update docker-compose orchestration if needed.
10. Add or update Jenkinsfile with test/build/deploy-local stages.

Keep each step independently runnable so Jenkins can repeat validation reliably.

## Practical References

- Setup and run commands: [README.md](README.md)
- Local orchestration details: [docker-compose.yml](docker-compose.yml)
- Current servicio1 entrypoint: [docker/servicio1/main.py](docker/servicio1/main.py)
- Current servicio2 entrypoint: [docker/servicio2/main.py](docker/servicio2/main.py)