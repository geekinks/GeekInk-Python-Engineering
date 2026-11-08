# Day 057: Introduction to FastAPI

## Learning Objectives

- Understand what a web framework is and why FastAPI is a modern choice.
- Create a FastAPI application with multiple endpoints.
- Use path parameters and query parameters to accept input.
- Define request and response models using Pydantic for automatic validation.
- Run a development server and test your API.

## Introduction

A web framework is a toolkit that helps you build web applications and APIs. So far in this course, you have built Python programs that run in the terminal. Starting today, you will build programs that run on the web -- receiving HTTP requests and returning structured responses.

FastAPI is a modern Python web framework designed for building APIs. It stands out for three reasons: it is extremely fast (one of the fastest Python frameworks), it generates interactive documentation automatically, and it uses Python type hints for request validation.

When you define an endpoint in FastAPI and declare that a parameter should be an integer, FastAPI will automatically validate incoming requests and return helpful error messages if the data is wrong. This eliminates a huge class of bugs and reduces the code you need to write.

## Concepts

### What is an API?

An API (Application Programming Interface) is a set of endpoints that other programs can call to read or write data. When you used the weather API on Day 044, you were the client. Now you are building the server.

### FastAPI Basics

Install with: `pip install fastapi uvicorn`

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, World"}
```

Run with: `uvicorn main:app --reload`

### Path Parameters

```python
@app.get("/students/{student_id}")
def get_student(student_id: int):
    return {"student_id": student_id}
```

The `{student_id}` in the path becomes a function parameter. The type hint `int` tells FastAPI to validate and convert it.

### Query Parameters

```python
@app.get("/students")
def list_students(department: str = None, limit: int = 10):
    return {"department": department, "limit": limit}
# URL: /students?department=CS&limit=5
```

### Pydantic Models

Pydantic models define the shape of request and response data:

```python
from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    email: str
    department: str = "Undeclared"
    level: int = 100
```

### Automatic Documentation

FastAPI generates interactive API docs at:
- `/docs` -- Swagger UI (try endpoints from the browser)
- `/redoc` -- ReDoc (clean documentation)

## Practical Examples

```python
# main.py
from fastapi import FastAPI

app = FastAPI(
    title="GeekInk Student API",
    description="A simple student management API",
    version="1.0.0",
)


@app.get("/")
def root():
    """Welcome endpoint."""
    return {
        "message": "Welcome to the GeekInk Student API",
        "docs": "/docs",
    }


@app.get("/hello/{name}")
def greet(name: str):
    """Greet a user by name."""
    return {"greeting": f"Hello, {name}! Welcome to GeekInk."}


@app.get("/add/{a}/{b}")
def add_numbers(a: int, b: int):
    """Add two numbers."""
    return {"a": a, "b": b, "sum": a + b}
```

```python
# Using Pydantic models for request validation
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

app = FastAPI(title="Student API v2")

# In-memory storage (will be replaced by a database later)
students_db = {}
next_id = 1


class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: str
    department: str = "Undeclared"
    level: int = Field(default=100, ge=100, le=400)


class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    department: str
    level: int


@app.post("/students", response_model=StudentResponse, status_code=201)
def create_student(student: StudentCreate):
    """Create a new student."""
    global next_id
    
    # Check for duplicate email
    for s in students_db.values():
        if s["email"] == student.email:
            raise HTTPException(status_code=400, detail="Email already registered.")
    
    student_dict = student.model_dump()
    student_dict["id"] = next_id
    students_db[next_id] = student_dict
    next_id += 1
    
    return student_dict


@app.get("/students", response_model=list[StudentResponse])
def list_students(department: Optional[str] = None, limit: int = 10):
    """List all students, optionally filtered by department."""
    results = list(students_db.values())
    
    if department:
        results = [s for s in results if s["department"].lower() == department.lower()]
    
    return results[:limit]


@app.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: int):
    """Get a student by ID."""
    if student_id not in students_db:
        raise HTTPException(status_code=404, detail="Student not found.")
    return students_db[student_id]
```

```python
# Query parameters with validation
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/search")
def search(
    q: str = Query(min_length=2, description="Search query"),
    page: int = Query(default=1, ge=1, description="Page number"),
    per_page: int = Query(default=10, ge=1, le=100, description="Results per page"),
):
    """Search endpoint with validated query parameters."""
    return {
        "query": q,
        "page": page,
        "per_page": per_page,
        "results": f"Showing results for '{q}' (page {page})",
    }
```

## Guided Practice

Build and test a simple API step by step.

Create `main.py`:

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="GeekInk Course API")

# In-memory data store
courses = {
    1: {"id": 1, "title": "Python Foundations", "credits": 3, "instructor": "Dr. Ahmed"},
    2: {"id": 2, "title": "Data Structures", "credits": 4, "instructor": "Prof. Musa"},
    3: {"id": 3, "title": "Web Development", "credits": 3, "instructor": "Dr. Fatima"},
}
next_id = 4


class CourseCreate(BaseModel):
    title: str
    credits: int
    instructor: str


class CourseResponse(BaseModel):
    id: int
    title: str
    credits: int
    instructor: str


@app.get("/")
def root():
    return {"message": "GeekInk Course API", "total_courses": len(courses)}


@app.get("/courses", response_model=list[CourseResponse])
def list_courses(instructor: Optional[str] = None):
    result = list(courses.values())
    if instructor:
        result = [c for c in result if instructor.lower() in c["instructor"].lower()]
    return result


@app.get("/courses/{course_id}", response_model=CourseResponse)
def get_course(course_id: int):
    if course_id not in courses:
        raise HTTPException(status_code=404, detail="Course not found")
    return courses[course_id]


@app.post("/courses", response_model=CourseResponse, status_code=201)
def create_course(course: CourseCreate):
    global next_id
    course_dict = course.model_dump()
    course_dict["id"] = next_id
    courses[next_id] = course_dict
    next_id += 1
    return course_dict
```

Run it:
```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```

Test it:
- Open `http://127.0.0.1:8000/docs` in your browser.
- Try each endpoint using the interactive documentation.
- Or use `curl` from the terminal:

```bash
curl http://127.0.0.1:8000/
curl http://127.0.0.1:8000/courses
curl http://127.0.0.1:8000/courses/1
curl -X POST http://127.0.0.1:8000/courses \
  -H "Content-Type: application/json" \
  -d '{"title": "Machine Learning", "credits": 4, "instructor": "Dr. Usman"}'
```

## Daily Challenge

**Build a "Hello" API with Multiple Endpoints**

Write a FastAPI application called `hello_api.py` that provides:

1. `GET /` -- returns a welcome message with API version and available endpoints.
2. `GET /greet/{name}` -- greets the user by name. Optional query parameter `language` (en, ha, yo) changes the greeting:
   - en: "Hello, {name}!"
   - ha: "Sannu, {name}!"
   - yo: "Bawo, {name}!"
3. `GET /time` -- returns the current date and time.
4. `POST /calculate` -- accepts a JSON body with `a` (float), `b` (float), and `operation` (add/subtract/multiply/divide). Returns the result. Handle division by zero.
5. `GET /courses` -- returns a list of sample courses.
6. `POST /courses` -- adds a new course to the in-memory list.
7. `GET /courses/{course_id}` -- returns a single course by ID.

Requirements:
- Use Pydantic models for request/response bodies.
- Use appropriate HTTP status codes.
- Raise `HTTPException` for errors.
- Include docstrings on all endpoints (they appear in `/docs`).
- Test all endpoints using the auto-generated `/docs` page or curl.

## Expected Output

```json
// GET /
{"message": "Welcome to the GeekInk Hello API", "version": "1.0.0"}

// GET /greet/Amina?language=ha
{"greeting": "Sannu, Amina!", "language": "ha"}

// POST /calculate with {"a": 10, "b": 3, "operation": "multiply"}
{"a": 10.0, "b": 3.0, "operation": "multiply", "result": 30.0}
```

## Assessment

1. What is the difference between path parameters and query parameters in FastAPI?
2. How does Pydantic help with API development? What happens if a client sends invalid data?
3. What is the purpose of `response_model` in a FastAPI endpoint?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-06/day-057/`

Include `hello_api.py` and a `README.md` with instructions to run and test.

## Additional Resources

- [FastAPI documentation](https://fastapi.tiangolo.com/)
- [Pydantic documentation](https://docs.pydantic.dev/)
- [uvicorn documentation](https://www.uvicorn.org/)

## Reflection

- How does building an API differ from building a CLI application?
- What advantages does automatic documentation provide during development and collaboration?
