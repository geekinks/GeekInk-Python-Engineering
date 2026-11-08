# Day 056: SQLAlchemy ORM Fundamentals

## Learning Objectives

- Understand what an ORM is and why it is useful.
- Define database models as Python classes using SQLAlchemy.
- Perform CRUD operations using SQLAlchemy's session API.
- Query data using SQLAlchemy's query interface instead of raw SQL.
- Rebuild the task manager from Day 054 using SQLAlchemy.

## Introduction

Writing raw SQL works well for simple applications, but as your application grows, managing SQL strings becomes error-prone and repetitive. An ORM (Object-Relational Mapper) lets you work with database tables as if they were Python classes and with rows as if they were Python objects.

SQLAlchemy is Python's most popular and powerful ORM. It maps your Python classes to database tables and translates method calls into SQL queries. Instead of writing `INSERT INTO tasks (title, priority) VALUES ('Learn ORM', 'high')`, you write `task = Task(title="Learn ORM", priority="high")` and add it to a session.

The key advantage is that your application code speaks Python, not SQL. You get type safety, autocompletion in your editor, and a cleaner separation between your business logic and your database layer.

## Concepts

### ORM Core Ideas

- **Model**: a Python class that represents a database table.
- **Session**: a workspace that tracks changes and synchronizes them with the database.
- **Engine**: the connection to the database.

### Defining Models

```python
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    department = Column(String, default="Undeclared")
    gpa = Column(Float, default=0.0)
```

### Engine and Session

```python
engine = create_engine("sqlite:///school.db", echo=False)
Base.metadata.create_all(engine)

with Session(engine) as session:
    # Work with the database
    pass
```

### CRUD with SQLAlchemy

- **Create**: `session.add(obj)` then `session.commit()`
- **Read**: `session.query(Model).filter(...).all()`
- **Update**: modify object attributes then `session.commit()`
- **Delete**: `session.delete(obj)` then `session.commit()`

## Practical Examples

```python
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, DateTime
from sqlalchemy.orm import declarative_base, Session
from datetime import datetime

Base = declarative_base()


class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    description = Column(String(500), default="")
    priority = Column(String(10), default="medium")
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)
    
    def __repr__(self):
        status = "Done" if self.completed else "Pending"
        return f"Task(id={self.id}, title='{self.title}', priority='{self.priority}', status={status})"


# Create the database and tables
engine = create_engine("sqlite:///tasks_orm.db", echo=False)
Base.metadata.create_all(engine)
print("Database and tables created.")
```

```python
# CREATE -- adding new records
with Session(engine) as session:
    tasks = [
        Task(title="Learn SQLAlchemy", description="Day 056 lesson", priority="high"),
        Task(title="Build task manager with ORM", priority="high"),
        Task(title="Review database design", priority="medium"),
        Task(title="Read SQLAlchemy docs", priority="low"),
    ]
    session.add_all(tasks)
    session.commit()
    
    for task in tasks:
        print(f"  Created: {task}")
```

```python
# READ -- querying records
with Session(engine) as session:
    # Get all tasks
    print("All tasks:")
    all_tasks = session.query(Task).all()
    for t in all_tasks:
        print(f"  {t}")
    
    # Filter by priority
    print("\nHigh-priority tasks:")
    high = session.query(Task).filter(Task.priority == "high").all()
    for t in high:
        print(f"  {t}")
    
    # Filter with multiple conditions
    print("\nPending medium/high tasks:")
    filtered = session.query(Task).filter(
        Task.completed == False,
        Task.priority.in_(["medium", "high"])
    ).order_by(Task.priority).all()
    for t in filtered:
        print(f"  {t}")
    
    # Search by keyword
    print("\nTasks containing 'ORM':")
    search = session.query(Task).filter(Task.title.contains("ORM")).all()
    for t in search:
        print(f"  {t}")
```

```python
# UPDATE -- modifying records
with Session(engine) as session:
    task = session.query(Task).filter(Task.id == 1).first()
    if task:
        print(f"Before: {task}")
        task.completed = True
        session.commit()
        print(f"After:  {task}")
```

```python
# DELETE -- removing records
with Session(engine) as session:
    task = session.query(Task).filter(Task.id == 4).first()
    if task:
        print(f"Deleting: {task}")
        session.delete(task)
        session.commit()
        print("Deleted.")
    
    remaining = session.query(Task).count()
    print(f"Remaining tasks: {remaining}")
```

## Guided Practice

Build a student database using SQLAlchemy with relationships.

```python
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, Session, relationship

Base = declarative_base()


class Department(Base):
    __tablename__ = "departments"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)
    
    students = relationship("Student", back_populates="department")
    
    def __repr__(self):
        return f"Department(name='{self.name}')"


class Student(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    level = Column(Integer, default=100)
    gpa = Column(Float, default=0.0)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=False)
    
    department = relationship("Department", back_populates="students")
    
    def __repr__(self):
        return f"Student(name='{self.name}', level={self.level}, gpa={self.gpa})"


# Setup
engine = create_engine("sqlite:///students_orm.db", echo=False)
Base.metadata.create_all(engine)

# Populate
with Session(engine) as session:
    cs = Department(name="Computer Science")
    se = Department(name="Software Engineering")
    
    session.add_all([
        Student(name="Amina Ibrahim", email="amina@uni.edu.ng", level=200, gpa=3.8, department=cs),
        Student(name="Usman Bello", email="usman@uni.edu.ng", level=300, gpa=3.5, department=se),
        Student(name="Fatima Abubakar", email="fatima@uni.edu.ng", level=100, gpa=3.9, department=cs),
    ])
    session.commit()

# Query using relationships
with Session(engine) as session:
    print("Students by department:")
    departments = session.query(Department).all()
    for dept in departments:
        print(f"\n  {dept.name}:")
        for student in dept.students:
            print(f"    {student.name} - Level {student.level}, GPA: {student.gpa}")
```

## Daily Challenge

**Rebuild the Task Manager Using SQLAlchemy**

Take the CLI task manager you built on Day 054 and rebuild it using SQLAlchemy instead of raw `sqlite3`.

Write a script called `task_manager_orm.py` that:

1. Defines a `Task` model class with SQLAlchemy.
2. Supports the same commands: add, list, all, done, delete, search, stats, quit.
3. Uses SQLAlchemy's session and query API instead of raw SQL.
4. Adds a `Category` model with a one-to-many relationship (each task belongs to a category).
5. Supports assigning and filtering by category.

Requirements:
- Use `declarative_base()` for model definition.
- Use `Session` context managers.
- Use SQLAlchemy query methods (`.filter()`, `.order_by()`, `.count()`, etc.).
- Define a relationship between Task and Category.
- Format output cleanly.

## Expected Output

```
=== Task Manager (SQLAlchemy) ===
Commands: add, list, all, done, delete, search, stats, categories, quit

> add Learn SQLAlchemy ORM
Description: Complete Day 056 exercises
Priority (low/medium/high): high
Category (or 'new' to create): new
Category name: Learning
Task #1 added (Category: Learning).

> categories
Categories:
  Learning: 1 task(s)

> list
Pending Tasks:
  ID  Title                     Priority  Category    Created
  1   Learn SQLAlchemy ORM      high      Learning    2025-03-15

> quit
Goodbye!
```

## Assessment

1. What is an ORM, and what problem does it solve compared to writing raw SQL?
2. How does SQLAlchemy's `relationship()` function simplify working with related tables?
3. What is the purpose of `session.commit()`? What happens if you forget to call it?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-06/day-056/`

Include `task_manager_orm.py` and a `README.md`. Do not include `.db` files.

## Additional Resources

- [SQLAlchemy ORM tutorial](https://docs.sqlalchemy.org/en/20/tutorial/)
- [SQLAlchemy Column types](https://docs.sqlalchemy.org/en/20/core/types.html)

## Reflection

- What advantages did SQLAlchemy give you compared to raw sqlite3?
- Were there any operations that felt more natural in raw SQL than through the ORM?
