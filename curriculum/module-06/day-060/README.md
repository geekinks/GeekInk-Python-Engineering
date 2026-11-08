# Day 060: Module 6 Project -- Student Management REST API

## Learning Objectives

- Design and build a complete REST API from requirements to implementation.
- Integrate FastAPI with SQLAlchemy for persistent data storage.
- Implement authentication, CRUD operations, and data validation in one application.
- Apply proper error handling, status codes, and API design conventions.
- Document your API with clear endpoint descriptions.

## Introduction

Over the past ten days, you have learned relational databases, SQL, SQLAlchemy ORM, FastAPI, REST API design, and authentication. Today you bring all of these skills together to build a complete Student Management REST API.

This project extends the Student Management System you built in Module 4 (OOP) by adding a web API layer on top of a persistent database. Instead of a CLI interface, users interact with your system through HTTP endpoints. This is how real-world applications are built: a database stores the data, an ORM maps it to Python objects, and a web framework exposes it to the world.

This is a significant project. Plan your architecture before writing code. Think about your database schema, your API endpoints, your Pydantic models, and how authentication fits into the picture.

## Project Requirements

### Core Features

1. **Student Management**: CRUD operations for students (name, email, department, level, GPA).
2. **Course Management**: CRUD operations for courses (title, code, credits, department).
3. **Enrollment System**: enroll students in courses, drop courses, view enrollments.
4. **User Authentication**: register, login, JWT-protected endpoints.
5. **Data Persistence**: SQLAlchemy with SQLite.

### API Endpoints

```
Authentication:
  POST   /api/register          Register a new user
  POST   /api/login             Login and get access token

Students:
  GET    /api/students           List all students (filterable)
  POST   /api/students           Create a student (auth required)
  GET    /api/students/{id}      Get student details
  PUT    /api/students/{id}      Update a student (auth required)
  DELETE /api/students/{id}      Delete a student (auth required)

Courses:
  GET    /api/courses            List all courses
  POST   /api/courses            Create a course (auth required)
  GET    /api/courses/{id}       Get course details with enrolled students
  PUT    /api/courses/{id}       Update a course (auth required)
  DELETE /api/courses/{id}       Delete a course (auth required)

Enrollments:
  POST   /api/enrollments        Enroll a student in a course (auth required)
  DELETE /api/enrollments        Drop a student from a course (auth required)
  GET    /api/students/{id}/courses    List courses a student is enrolled in
  GET    /api/courses/{id}/students    List students enrolled in a course

Statistics:
  GET    /api/stats              Summary statistics (total students, courses, enrollments)
```

### Technical Requirements

- FastAPI for the web framework.
- SQLAlchemy ORM for database models.
- SQLite as the database.
- Pydantic models for request/response validation.
- JWT-based authentication with password hashing.
- Proper HTTP status codes.
- Query parameter filtering and pagination.
- Error handling for all edge cases.

## Project Architecture

```
student_api/
    main.py              # FastAPI app entry point
    config.py            # Configuration (secret key, database URL)
    database.py          # SQLAlchemy engine and session setup
    models.py            # SQLAlchemy ORM models
    schemas.py           # Pydantic request/response models
    auth.py              # Authentication utilities (hashing, JWT)
    routers/
        students.py      # Student endpoints
        courses.py       # Course endpoints
        enrollments.py   # Enrollment endpoints
        auth.py          # Auth endpoints
    README.md
```

## Starter Scaffold

### database.py

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./student_management.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


def get_db():
    """Dependency that provides a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### models.py

```python
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

# Many-to-many association table
enrollments = Table(
    "enrollments",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id"), primary_key=True),
    Column("course_id", Integer, ForeignKey("courses.id"), primary_key=True),
)


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)


class Student(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    department = Column(String, nullable=False)
    level = Column(Integer, default=100)
    gpa = Column(Float, default=0.0)
    
    courses = relationship("Course", secondary=enrollments, back_populates="students")


class Course(Base):
    __tablename__ = "courses"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String, unique=True, nullable=False)
    title = Column(String, nullable=False)
    credits = Column(Integer, nullable=False)
    department = Column(String, nullable=False)
    
    students = relationship("Student", secondary=enrollments, back_populates="courses")
```

### schemas.py

```python
from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class StudentCreate(BaseModel):
    first_name: str = Field(min_length=1)
    last_name: str = Field(min_length=1)
    email: str
    department: str
    level: int = Field(default=100, ge=100, le=400)
    gpa: float = Field(default=0.0, ge=0.0, le=4.0)


class StudentResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    department: str
    level: int
    gpa: float
    
    class Config:
        from_attributes = True


class CourseCreate(BaseModel):
    code: str = Field(min_length=2)
    title: str = Field(min_length=1)
    credits: int = Field(ge=1, le=6)
    department: str


class CourseResponse(BaseModel):
    id: int
    code: str
    title: str
    credits: int
    department: str
    
    class Config:
        from_attributes = True


class EnrollmentRequest(BaseModel):
    student_id: int
    course_id: int


class UserRegister(BaseModel):
    username: str = Field(min_length=3)
    password: str = Field(min_length=6)


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
```

### main.py

```python
from fastapi import FastAPI
from database import engine, Base

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="GeekInk Student Management API",
    description="A complete REST API for managing students, courses, and enrollments.",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "title": "GeekInk Student Management API",
        "version": "1.0.0",
        "docs": "/docs",
    }


# TODO: Include routers
# from routers import students, courses, enrollments, auth
# app.include_router(auth.router, prefix="/api", tags=["Authentication"])
# app.include_router(students.router, prefix="/api", tags=["Students"])
# app.include_router(courses.router, prefix="/api", tags=["Courses"])
# app.include_router(enrollments.router, prefix="/api", tags=["Enrollments"])
```

## Evaluation Criteria

| Criterion | Weight | Description |
|-----------|--------|-------------|
| API completeness | 25% | All required endpoints implemented and working |
| Database design | 15% | Proper schema, relationships, and constraints |
| Authentication | 15% | Secure password hashing, JWT, endpoint protection |
| Code quality | 15% | Clean, organized, follows project structure |
| Error handling | 10% | Proper status codes, validation, edge cases |
| Data validation | 10% | Pydantic models validate all input |
| Documentation | 10% | README, endpoint descriptions, setup instructions |

## Testing Your API

After implementing, test with:

1. FastAPI auto-docs: `http://127.0.0.1:8000/docs`
2. A test script using `requests`
3. curl commands from the terminal

Example test flow:

```bash
# Register
curl -X POST http://127.0.0.1:8000/api/register \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'

# Login
curl -X POST http://127.0.0.1:8000/api/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "admin123"}'

# Create a student (use the token from login)
curl -X POST http://127.0.0.1:8000/api/students \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -d '{"first_name": "Amina", "last_name": "Ibrahim", "email": "amina@uni.edu.ng", "department": "Computer Science"}'
```

## Assessment

1. How does separating your application into models, schemas, routers, and auth modules improve maintainability?
2. What is the role of the SQLAlchemy `Session` in the request lifecycle?
3. How would you modify this API to support role-based access control (e.g., admin vs. student)?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-06/day-060/`

Include your complete project directory, a `README.md` with setup and usage instructions, and do not include the `.db` file or any secret keys.

## Additional Resources

- [FastAPI larger applications guide](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
- [SQLAlchemy relationships](https://docs.sqlalchemy.org/en/20/orm/relationships.html)
- [FastAPI + SQLAlchemy tutorial](https://fastapi.tiangolo.com/tutorial/sql-databases/)

## Reflection

- How does building a REST API change the way you think about application architecture?
- What was the most challenging part of integrating authentication with database-backed CRUD operations?
- How would this API need to change to be production-ready?
