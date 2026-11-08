# Student Management REST API

**Module:** 6 — Database and Backend Engineering
**Day:** 60
**Difficulty:** Intermediate

---

## Problem Statement

Modern applications rely on backend APIs to manage data. This project builds a RESTful API for student management using FastAPI, SQLAlchemy, and SQLite — combining database design, ORM usage, API development, and authentication into a production-style backend service.

## Objectives

- Design a relational database schema with proper relationships.
- Implement an ORM layer with SQLAlchemy.
- Build RESTful API endpoints with FastAPI.
- Implement request validation with Pydantic models.
- Add basic authentication (JWT-based).
- Write API documentation with proper status codes and error responses.

## Requirements

### Data Model

1. **Student** — id, name, email, enrollment_date, department.
2. **Course** — id, name, code, credits, department.
3. **Enrollment** — student_id, course_id, enrollment_date, grade (nullable).
4. **User** — id, username, hashed_password, role (admin/instructor).

### API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| POST | /auth/register | Register a new user |
| POST | /auth/login | Login and receive JWT token |
| GET | /students | List all students (paginated) |
| POST | /students | Create a new student |
| GET | /students/{id} | Get student details |
| PUT | /students/{id} | Update student information |
| DELETE | /students/{id} | Delete a student |
| GET | /courses | List all courses |
| POST | /courses | Create a new course |
| POST | /enrollments | Enroll a student in a course |
| GET | /students/{id}/courses | List courses for a student |
| PUT | /enrollments/{id} | Update enrollment grade |

### Non-Functional Requirements

- Passwords must be hashed (never stored in plaintext).
- API must return appropriate HTTP status codes.
- Input validation must reject invalid data with clear error messages.
- SQL injection must be prevented (use parameterized queries / ORM).

## Technologies

- Python 3.10+
- FastAPI
- SQLAlchemy 2.0+
- SQLite
- Pydantic
- python-jose (JWT)
- passlib (password hashing)
- uvicorn (ASGI server)

## Suggested Architecture

```
student-management-api/
├── main.py           — FastAPI application entry point
├── database.py       — Database connection and session
├── models.py         — SQLAlchemy ORM models
├── schemas.py        — Pydantic request/response schemas
├── routers/
│   ├── auth.py       — Authentication endpoints
│   ├── students.py   — Student CRUD endpoints
│   ├── courses.py    — Course endpoints
│   └── enrollments.py — Enrollment endpoints
├── auth.py           — JWT and password utilities
└── requirements.txt
```

## Implementation Milestones

| Milestone | Description |
| :--- | :--- |
| 1. Database setup | Create SQLAlchemy models and database connection |
| 2. Student CRUD | Implement student endpoints with Pydantic validation |
| 3. Course CRUD | Implement course endpoints |
| 4. Enrollments | Implement enrollment logic with relationships |
| 5. Authentication | Add user registration, login, and JWT protection |
| 6. Testing | Test endpoints manually with the FastAPI docs UI |

## Testing Requirements

- Use FastAPI's interactive docs (`/docs`) to test all endpoints manually.
- Verify CRUD operations persist to the database.
- Test authentication flow: register, login, access protected endpoint.
- Test validation: submit invalid data and verify error responses.

## Expected Deliverables

1. Complete API source code with the directory structure above.
2. `requirements.txt` listing all dependencies.
3. A README documenting how to run the API and use each endpoint.
4. Screenshots of the FastAPI docs page showing available endpoints.

## Evaluation Criteria

| Criterion | Weight | Description |
| :--- | :--- | :--- |
| API design | 20% | RESTful conventions, proper status codes |
| Database modeling | 20% | Proper schema design with relationships |
| Functionality | 25% | All endpoints working correctly |
| Authentication | 15% | Secure password handling, JWT working |
| Code organization | 10% | Clean project structure, separation of concerns |
| Documentation | 10% | Clear README, API documented |
