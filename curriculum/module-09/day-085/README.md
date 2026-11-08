# Day 085: Integration Testing

## Learning Objectives

- Distinguish between unit tests and integration tests.
- Write integration tests that verify components work together correctly.
- Test database operations using temporary databases.
- Test HTTP APIs using FastAPI's TestClient.
- Understand test isolation and why each test should start with a clean state.

## Introduction

Unit tests verify that individual functions and methods work in isolation. Integration tests verify that multiple components work together correctly. A unit test might confirm that your `add_student()` function inserts a record into a dictionary. An integration test would verify that calling `add_student()` actually stores the record in a database and that `get_student()` retrieves it back correctly.

In real applications, bugs frequently live at the boundaries between components: the format a function returns does not match what the next function expects, or a database query returns rows in a different order than the code assumes. Integration tests catch these boundary bugs that unit tests miss.

The challenge of integration testing is managing state. If one test writes to a database, it must not affect the next test. This is called test isolation. Common strategies include using a fresh temporary database for each test, wrapping each test in a database transaction that rolls back, or using fixtures that clean up after themselves.

## Concepts

### Unit Tests vs Integration Tests

| Aspect | Unit Test | Integration Test |
|--------|-----------|------------------|
| Scope | Single function/method | Multiple components together |
| Speed | Very fast (milliseconds) | Slower (may involve I/O) |
| Dependencies | None (isolated) | Database, API, file system |
| Failure reason | Logic error in one function | Incompatible interfaces |

### Testing with Databases

Use SQLite in-memory databases for fast, isolated database tests:

```python
import sqlite3

def get_test_db():
    conn = sqlite3.connect(":memory:")
    conn.execute("""
        CREATE TABLE students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            grade REAL
        )
    """)
    return conn
```

### Testing APIs with FastAPI TestClient

FastAPI provides a `TestClient` that lets you send HTTP requests to your app without running a server:

```python
from fastapi.testclient import TestClient
from myapp import app

client = TestClient(app)
response = client.get("/students")
assert response.status_code == 200
```

## Practical Examples

### Example: Database integration test

```python
# student_db.py

import sqlite3


def create_tables(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            gpa REAL DEFAULT 0.0
        )
    """)
    conn.commit()


def add_student(conn, name, email, gpa=0.0):
    conn.execute(
        "INSERT INTO students (name, email, gpa) VALUES (?, ?, ?)",
        (name, email, gpa),
    )
    conn.commit()


def get_student_by_email(conn, email):
    cursor = conn.execute(
        "SELECT id, name, email, gpa FROM students WHERE email = ?",
        (email,),
    )
    row = cursor.fetchone()
    if row is None:
        return None
    return {"id": row[0], "name": row[1], "email": row[2], "gpa": row[3]}


def get_all_students(conn):
    cursor = conn.execute("SELECT id, name, email, gpa FROM students")
    return [
        {"id": r[0], "name": r[1], "email": r[2], "gpa": r[3]}
        for r in cursor.fetchall()
    ]


def update_gpa(conn, email, new_gpa):
    conn.execute(
        "UPDATE students SET gpa = ? WHERE email = ?",
        (new_gpa, email),
    )
    conn.commit()


def delete_student(conn, email):
    conn.execute("DELETE FROM students WHERE email = ?", (email,))
    conn.commit()
```

### Integration tests for the database module

```python
# test_student_db.py

import sqlite3
import pytest
from student_db import (
    create_tables, add_student, get_student_by_email,
    get_all_students, update_gpa, delete_student,
)


@pytest.fixture
def db():
    """Create a fresh in-memory database for each test."""
    conn = sqlite3.connect(":memory:")
    create_tables(conn)
    yield conn
    conn.close()


def test_add_and_retrieve_student(db):
    add_student(db, "Amina Yusuf", "amina@example.com", 3.8)
    student = get_student_by_email(db, "amina@example.com")
    assert student is not None
    assert student["name"] == "Amina Yusuf"
    assert student["gpa"] == 3.8


def test_get_nonexistent_student(db):
    student = get_student_by_email(db, "nobody@example.com")
    assert student is None


def test_add_multiple_students(db):
    add_student(db, "Amina", "amina@example.com")
    add_student(db, "Ibrahim", "ibrahim@example.com")
    all_students = get_all_students(db)
    assert len(all_students) == 2


def test_unique_email_constraint(db):
    add_student(db, "Amina", "amina@example.com")
    with pytest.raises(sqlite3.IntegrityError):
        add_student(db, "Another Amina", "amina@example.com")


def test_update_gpa(db):
    add_student(db, "Amina", "amina@example.com", 3.0)
    update_gpa(db, "amina@example.com", 3.9)
    student = get_student_by_email(db, "amina@example.com")
    assert student["gpa"] == 3.9


def test_delete_student(db):
    add_student(db, "Amina", "amina@example.com")
    delete_student(db, "amina@example.com")
    student = get_student_by_email(db, "amina@example.com")
    assert student is None
```

### Example: API integration test

```python
# app.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

students = {}


class StudentCreate(BaseModel):
    name: str
    email: str
    gpa: float = 0.0


@app.post("/students", status_code=201)
def create_student(student: StudentCreate):
    if student.email in students:
        raise HTTPException(status_code=400, detail="Email already exists")
    students[student.email] = {
        "name": student.name,
        "email": student.email,
        "gpa": student.gpa,
    }
    return students[student.email]


@app.get("/students/{email}")
def get_student(email: str):
    if email not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return students[email]


@app.get("/students")
def list_students():
    return list(students.values())
```

```python
# test_app.py

import pytest
from fastapi.testclient import TestClient
from app import app, students


@pytest.fixture(autouse=True)
def clear_students():
    """Ensure each test starts with an empty student store."""
    students.clear()
    yield
    students.clear()


client = TestClient(app)


def test_create_student():
    response = client.post("/students", json={
        "name": "Amina",
        "email": "amina@example.com",
        "gpa": 3.5,
    })
    assert response.status_code == 201
    assert response.json()["name"] == "Amina"


def test_get_student():
    client.post("/students", json={
        "name": "Amina",
        "email": "amina@example.com",
    })
    response = client.get("/students/amina@example.com")
    assert response.status_code == 200
    assert response.json()["name"] == "Amina"


def test_get_nonexistent_student():
    response = client.get("/students/nobody@example.com")
    assert response.status_code == 404


def test_duplicate_email():
    client.post("/students", json={
        "name": "Amina",
        "email": "amina@example.com",
    })
    response = client.post("/students", json={
        "name": "Other",
        "email": "amina@example.com",
    })
    assert response.status_code == 400


def test_list_students():
    client.post("/students", json={"name": "A", "email": "a@test.com"})
    client.post("/students", json={"name": "B", "email": "b@test.com"})
    response = client.get("/students")
    assert response.status_code == 200
    assert len(response.json()) == 2
```

## Guided Practice

1. Copy the `student_db.py` and `test_student_db.py` files above.

2. Run the tests with `pytest -v test_student_db.py` and confirm they pass.

3. Add a new function `get_honor_students(conn, min_gpa=3.5)` that returns students with GPA >= min_gpa.

4. Write integration tests for your new function that:
   - Add 5 students with different GPAs.
   - Call `get_honor_students()` and verify the correct students are returned.
   - Test with a custom `min_gpa` threshold.

## Daily Challenge

Build a simple Task Management API with FastAPI and write integration tests for it.

### API Requirements

Create `task_app.py` with these endpoints:

- `POST /tasks` --- Create a task with `title` (required), `description` (optional), `priority` (low/medium/high, default medium).
- `GET /tasks` --- List all tasks. Support query parameter `?priority=high` to filter.
- `GET /tasks/{task_id}` --- Get a specific task by ID.
- `PUT /tasks/{task_id}` --- Update a task's title, description, or priority.
- `DELETE /tasks/{task_id}` --- Delete a task. Return 404 if not found.
- `POST /tasks/{task_id}/complete` --- Mark a task as completed.

### Test Requirements

Write `test_task_app.py` with at least 12 integration tests covering:

- Creating a task and verifying the response.
- Getting a task by ID.
- Getting a nonexistent task (404).
- Listing all tasks.
- Filtering tasks by priority.
- Updating a task.
- Deleting a task.
- Deleting a nonexistent task (404).
- Completing a task.
- The full lifecycle: create, update, complete, verify, delete.

Use a fixture to clear state between tests.

## Expected Output

```
$ pytest -v test_task_app.py
test_task_app.py::test_create_task PASSED
test_task_app.py::test_get_task PASSED
test_task_app.py::test_get_nonexistent PASSED
...
========================= 12 passed in 0.3s =========================
```

## Assessment

1. What is the key difference between a unit test and an integration test?
2. Why is test isolation important, and what happens when tests share state?
3. How does FastAPI's TestClient allow you to test HTTP endpoints without running a server?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-09/day-085/`

Include:
- `task_app.py`
- `test_task_app.py`
- `student_db.py` and `test_student_db.py` (with your additions from Guided Practice)

## Additional Resources

- [FastAPI Testing documentation](https://fastapi.tiangolo.com/tutorial/testing/)
- [pytest fixtures documentation](https://docs.pytest.org/en/stable/how-to/fixtures.html)

## Reflection

- Why can a project have passing unit tests but still have bugs that only integration tests catch?
- When would you choose to write an integration test instead of a unit test?
