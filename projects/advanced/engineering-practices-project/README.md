# Build, Test, Document and Deploy a Python Application

**Module:** 9 — Software Engineering Practices
**Day:** 90
**Difficulty:** Advanced

---

## Problem Statement

Writing code is only part of software engineering. Professional developers must also test their code, document it, manage versions, and prepare it for deployment. This project requires students to take a previous project (or build a small new one) and apply the full suite of engineering practices learned in Module 9.

## Objectives

- Write clean, PEP 8 compliant Python code.
- Implement comprehensive unit and integration tests.
- Add structured logging throughout the application.
- Write professional documentation (README, docstrings, API docs).
- Use Git with a proper branching workflow.
- Create a Dockerfile for containerized deployment.
- Set up a basic CI/CD pipeline with GitHub Actions.

## Requirements

### Base Application

Choose one of the following as the base application to work on:

1. **Personal Expense Tracker** (from Module 3) — add tests, logging, docs, Docker.
2. **Student Management API** (from Module 6) — add tests, logging, docs, Docker.
3. **A new small application** — a CLI tool or API of your design.

The base application must have at least 3 modules and meaningful functionality.

### Engineering Practices to Apply

1. **Code quality:**
   - All code follows PEP 8 (verify with `pylint` or `flake8`).
   - Type hints on all function signatures.
   - No unused imports or variables.

2. **Testing:**
   - At least 10 unit tests with `pytest`.
   - At least 3 integration tests.
   - Test coverage of at least 70%.
   - Tests must pass: `pytest --tb=short`

3. **Logging:**
   - Replace all `print()` debugging with `logging` module.
   - Use appropriate log levels (DEBUG, INFO, WARNING, ERROR).
   - Configure logging to write to both console and file.

4. **Documentation:**
   - README with project description, setup, usage, and testing instructions.
   - Google-style docstrings on all public functions and classes.
   - At least one architecture or flow diagram (text-based is fine).

5. **Git workflow:**
   - At least 5 meaningful commits with descriptive messages.
   - Use a feature branch for development.
   - Create a pull request with description.

6. **Docker (stretch goal):**
   - Create a `Dockerfile` that builds and runs the application.
   - Create a `docker-compose.yml` if the app uses a database.
   - Document Docker commands in the README.

7. **CI/CD (stretch goal):**
   - Create a `.github/workflows/ci.yml` that runs tests on push.
   - The pipeline should: install dependencies, lint, run tests.

## Technologies

- Python 3.10+
- pytest
- pylint or flake8
- logging (standard library)
- Docker
- GitHub Actions

## Implementation Milestones

| Milestone | Description |
| :--- | :--- |
| 1. Select base app | Choose and set up the project |
| 2. Clean code | Refactor to PEP 8, add type hints |
| 3. Tests | Write unit and integration tests |
| 4. Logging | Add structured logging |
| 5. Documentation | Write README, docstrings, architecture notes |
| 6. Docker | Create Dockerfile and test |
| 7. CI/CD | Create GitHub Actions workflow |

## Testing Requirements

- All tests must pass: `pytest`
- Linting must pass: `pylint src/` or `flake8 src/`
- Docker build must succeed: `docker build -t myapp .`

## Expected Deliverables

1. Complete source code with applied engineering practices.
2. Test suite with passing tests.
3. Logging configuration and log output samples.
4. Professional README.
5. Dockerfile (stretch).
6. GitHub Actions workflow file (stretch).
7. Git log showing meaningful commit history.

## Evaluation Criteria

| Criterion | Weight | Description |
| :--- | :--- | :--- |
| Code quality | 20% | PEP 8, type hints, clean structure |
| Testing | 25% | Coverage, test quality, all tests pass |
| Documentation | 20% | README, docstrings, architecture docs |
| Logging | 10% | Appropriate levels, file and console output |
| Git workflow | 10% | Meaningful commits, branching, PR |
| Docker/CI (stretch) | 15% | Dockerfile works, CI pipeline runs |
