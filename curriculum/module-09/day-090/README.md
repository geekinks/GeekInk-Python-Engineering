# Day 090: Module 9 Project --- Build, Test, Document and Deploy

## Learning Objectives

- Apply all software engineering practices learned in Module 9 to a complete project.
- Write clean, PEP 8-compliant code with type hints and docstrings.
- Build a comprehensive test suite with pytest.
- Add structured logging throughout the application.
- Use Git workflows with meaningful commits.
- Write professional documentation.
- Understand Docker basics and CI/CD concepts.

## Introduction

This is the capstone day for Module 9. Over the past nine days you have learned individual engineering practices: clean code, debugging, testing, logging, Git workflows, code review, and documentation. Today you bring them all together in a single project.

The goal is not to build something complex. The goal is to build something complete. A small, well-engineered application with tests, logging, documentation, and a proper Git history is worth far more than a large application with none of those things. This is the difference between writing code and engineering software.

You will also get an introduction to Docker and GitHub Actions. These tools are part of the modern deployment pipeline. Docker packages your application so it runs identically on any machine. GitHub Actions automates your tests so they run every time you push code.

## Project: Contact Book API

Build a Contact Book REST API using FastAPI with SQLite as the database.

### Requirements

**Functional requirements:**

1. Create a contact (name, email, phone, category).
2. List all contacts with optional filtering by category.
3. Get a single contact by ID.
4. Update a contact.
5. Delete a contact.
6. Search contacts by name (partial match, case-insensitive).

**Engineering requirements:**

1. **Clean code**: PEP 8 compliant, type hints on all functions, Google-style docstrings.
2. **Project structure**:
   ```
   contact-book/
   ├── README.md
   ├── requirements.txt
   ├── app/
   │   ├── __init__.py
   │   ├── main.py          # FastAPI app and routes
   │   ├── database.py       # Database setup and connection
   │   ├── models.py         # Pydantic models
   │   └── crud.py           # Database operations
   ├── tests/
   │   ├── __init__.py
   │   ├── conftest.py       # Shared fixtures
   │   ├── test_crud.py      # Unit tests for CRUD operations
   │   └── test_api.py       # Integration tests for API endpoints
   ├── Dockerfile
   └── .github/
       └── workflows/
           └── test.yml
   ```

3. **Testing**: At least 15 tests covering:
   - All CRUD operations (unit tests against the database).
   - All API endpoints (integration tests with TestClient).
   - Edge cases (duplicate emails, nonexistent contacts, empty search).

4. **Logging**: Log every API request, database operation, and error. Use INFO for normal operations, WARNING for edge cases, ERROR for failures.

5. **Git workflow**: Make at least 8 meaningful commits as you build. Suggested progression:
   - Initial project setup and database schema
   - CRUD operations
   - API endpoints
   - Unit tests
   - Integration tests
   - Logging
   - Documentation
   - Docker and CI configuration

6. **Documentation**: Complete README with installation, usage, API reference, and testing instructions.

### Starter Code

**database.py:**

```python
"""Database configuration and connection management."""

import sqlite3
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

DB_PATH = Path("contacts.db")


def get_connection(db_path: str = str(DB_PATH)) -> sqlite3.Connection:
    """Create and return a database connection.

    Args:
        db_path: Path to the SQLite database file.
            Use ':memory:' for testing.

    Returns:
        A sqlite3.Connection object with row_factory set to sqlite3.Row.
    """
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    logger.debug("Database connection established: %s", db_path)
    return conn


def init_db(conn: sqlite3.Connection) -> None:
    """Create database tables if they do not exist.

    Args:
        conn: An active database connection.
    """
    conn.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT,
            category TEXT DEFAULT 'general',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    logger.info("Database initialized successfully")
```

### Docker Basics

Create a `Dockerfile`:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build and run:

```bash
docker build -t contact-book .
docker run -p 8000:8000 contact-book
```

### GitHub Actions CI

Create `.github/workflows/test.yml`:

```yaml
name: Tests

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests
        run: pytest -v
```

## Guided Practice

Follow this sequence to build the project:

1. Create the project directory and initialize Git.
2. Set up `database.py` (provided above) and `models.py`.
3. Build `crud.py` with all database operations.
4. Write unit tests for CRUD operations (`test_crud.py`).
5. Build the FastAPI app in `main.py` with all endpoints.
6. Write integration tests (`test_api.py`).
7. Add logging throughout.
8. Write the README.
9. Add the Dockerfile and GitHub Actions workflow.
10. Make a final commit with all work complete.

## Daily Challenge

Complete the Contact Book API project as described above. This is the Module 9 milestone project.

Additional stretch goals (optional):
- Add pagination to the list endpoint.
- Add input validation (valid email format, non-empty name).
- Add a `PUT /contacts/{id}/favorite` endpoint to mark a contact as favorite.
- Add a CSV export endpoint: `GET /contacts/export`.

## Expected Output

A complete, working project that:

```bash
# Tests pass
$ pytest -v
========================= 15 passed in 0.5s =========================

# Application runs
$ uvicorn app.main:app
INFO:     Uvicorn running on http://127.0.0.1:8000

# API works
$ curl -X POST http://localhost:8000/contacts \
    -H "Content-Type: application/json" \
    -d '{"name": "Amina", "email": "amina@example.com", "phone": "08012345678"}'
{"id": 1, "name": "Amina", "email": "amina@example.com", ...}

# Docker builds
$ docker build -t contact-book .
Successfully built contact-book
```

## Assessment

### Module 9 Assessment Criteria

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Clean Code | 15% | PEP 8, type hints, docstrings, consistent style |
| Testing | 25% | Test coverage, test quality, edge cases |
| Logging | 10% | Appropriate log levels, useful messages |
| Git History | 10% | Meaningful commits, logical progression |
| Documentation | 15% | README quality, API documentation |
| Functionality | 20% | All endpoints work correctly |
| Docker/CI | 5% | Dockerfile exists and builds, CI config present |

### Knowledge Check

1. Describe the complete lifecycle of a feature from creation to deployment using the practices learned in Module 9.
2. Why is it valuable to have automated tests run on every push via CI?
3. How does Docker solve the "it works on my machine" problem?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-09/day-090/`

Include:
- The complete project directory with all files listed in the project structure.
- A screenshot or copy of your `pytest -v` output.
- Your Git log (`git log --oneline`).

## Additional Resources

- [FastAPI documentation](https://fastapi.tiangolo.com/)
- [Docker Getting Started](https://docs.docker.com/get-started/)
- [GitHub Actions documentation](https://docs.github.com/en/actions)

## Reflection

- Look at the first Python code you wrote in Day 1 of this course. How does it compare to what you are building now in terms of engineering quality?
- Which of the Module 9 practices (clean code, testing, logging, Git, documentation, Docker) do you think will have the biggest impact on your career? Why?
