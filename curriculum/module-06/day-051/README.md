# Day 051: Introduction to Databases

## Learning Objectives

- Understand what databases are and why they are essential in software engineering.
- Distinguish between relational and non-relational databases.
- Learn core relational database concepts: tables, rows, columns, and primary keys.
- Recognize when a database is the right tool for data storage.
- Design a simple database schema for a real-world scenario.

## Introduction

So far in this course, you have stored data in variables, files, CSV, and JSON. These approaches work for small-scale applications, but they break down when data grows large, multiple users need simultaneous access, or you need to enforce rules about data integrity.

A database is a structured system for storing, organizing, and retrieving data. It provides guarantees that flat files cannot: data consistency (every record follows the same structure), data integrity (rules prevent invalid data), concurrency (multiple programs can read and write safely at the same time), and efficient querying (find any record in milliseconds, even among millions).

Relational databases organize data into tables with rows and columns, connected by relationships. They are the backbone of most business applications, from banking systems to social networks to the student management system you built in Module 4.

## Concepts

### Relational Database Fundamentals

A **relational database** stores data in **tables** (also called relations):

| student_id | first_name | last_name | email              | enrollment_year |
|------------|------------|-----------|--------------------| --------------- |
| 1          | Amina      | Ibrahim   | amina@example.com  | 2025            |
| 2          | Usman      | Bello     | usman@example.com  | 2025            |
| 3          | Fatima     | Abubakar  | fatima@example.com | 2024            |

Key terms:
- **Table**: a collection of related data organized in rows and columns.
- **Row** (record): one entry in the table (e.g., one student).
- **Column** (field): one attribute of the data (e.g., `first_name`).
- **Primary key**: a column (or set of columns) that uniquely identifies each row. No two rows can share the same primary key.
- **Foreign key**: a column that references the primary key of another table, creating a relationship.

### Relational vs Non-Relational

| Feature | Relational (SQL) | Non-Relational (NoSQL) |
|---------|-------------------|------------------------|
| Structure | Fixed schema (tables) | Flexible schema (documents, key-value) |
| Query language | SQL | Varies by database |
| Relationships | Enforced via foreign keys | Typically embedded |
| Examples | SQLite, PostgreSQL, MySQL | MongoDB, Redis, Firebase |
| Best for | Structured, relational data | Unstructured or rapidly changing data |

For this course, we focus on relational databases because they are the most widely used in professional software engineering.

### Common Relational Databases

- **SQLite**: serverless, file-based, built into Python. Perfect for learning and small applications.
- **PostgreSQL**: powerful, open-source, production-grade. Used by large-scale applications.
- **MySQL/MariaDB**: widely used in web applications.

### When to Use a Database

Use a database when:
- You need to store more than a trivial amount of structured data.
- Multiple users or processes need to access the data concurrently.
- You need to search, filter, or aggregate data efficiently.
- Data integrity is important (no duplicate records, no invalid references).
- You need data to persist reliably across application restarts.

A flat file (CSV, JSON) is fine when:
- The data is small and read-only.
- Only one process accesses it at a time.
- You do not need complex queries.

## Practical Examples

```python
# Thinking about data as tables (no database yet -- just Python)

# A "students" table as a list of dictionaries
students = [
    {"id": 1, "name": "Amina Ibrahim", "department": "Computer Science", "level": 200},
    {"id": 2, "name": "Usman Bello", "department": "Software Engineering", "level": 300},
    {"id": 3, "name": "Fatima Abubakar", "department": "Computer Science", "level": 100},
]

# A "courses" table
courses = [
    {"id": 101, "title": "Introduction to Programming", "department": "Computer Science", "credits": 3},
    {"id": 102, "title": "Data Structures", "department": "Computer Science", "credits": 4},
    {"id": 103, "title": "Software Engineering", "department": "Software Engineering", "credits": 3},
]

# An "enrollments" table (relationship between students and courses)
enrollments = [
    {"student_id": 1, "course_id": 101},
    {"student_id": 1, "course_id": 102},
    {"student_id": 2, "course_id": 103},
    {"student_id": 3, "course_id": 101},
]

# Simulating a query: "Which courses is Amina enrolled in?"
amina_id = 1
amina_course_ids = [e["course_id"] for e in enrollments if e["student_id"] == amina_id]
amina_courses = [c["title"] for c in courses if c["id"] in amina_course_ids]
print(f"Amina's courses: {amina_courses}")
# This is tedious with lists -- SQL makes it a single query.
```

```python
# Quick SQLite demo -- connecting to a database is this simple
import sqlite3

# Create an in-memory database
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# Create a table
cursor.execute("""
    CREATE TABLE students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        department TEXT,
        level INTEGER
    )
""")

# Insert data
cursor.execute("INSERT INTO students VALUES (1, 'Amina Ibrahim', 'Computer Science', 200)")
cursor.execute("INSERT INTO students VALUES (2, 'Usman Bello', 'Software Engineering', 300)")

# Query data
cursor.execute("SELECT name, department FROM students")
for row in cursor.fetchall():
    print(f"  {row[0]} - {row[1]}")

conn.close()
```

## Guided Practice

Design a database schema on paper (or in a Markdown file) for a school system.

Think through the following questions:
1. What entities exist? (Students, Courses, Instructors, Departments)
2. What attributes does each entity have?
3. What relationships exist between entities?
4. What should the primary key be for each table?

```markdown
# School Database Schema

## Tables

### departments
| Column        | Type    | Constraints    |
|---------------|---------|----------------|
| id            | INTEGER | PRIMARY KEY    |
| name          | TEXT    | NOT NULL       |
| building      | TEXT    |                |

### students
| Column          | Type    | Constraints                     |
|-----------------|---------|----------------------------------|
| id              | INTEGER | PRIMARY KEY                     |
| first_name      | TEXT    | NOT NULL                        |
| last_name       | TEXT    | NOT NULL                        |
| email           | TEXT    | UNIQUE, NOT NULL                |
| department_id   | INTEGER | FOREIGN KEY -> departments(id)  |
| enrollment_year | INTEGER |                                 |

### courses
| Column        | Type    | Constraints                     |
|---------------|---------|----------------------------------|
| id            | INTEGER | PRIMARY KEY                     |
| title         | TEXT    | NOT NULL                        |
| credits       | INTEGER | NOT NULL                        |
| department_id | INTEGER | FOREIGN KEY -> departments(id)  |

### enrollments
| Column     | Type    | Constraints                    |
|------------|---------|--------------------------------|
| id         | INTEGER | PRIMARY KEY                    |
| student_id | INTEGER | FOREIGN KEY -> students(id)    |
| course_id  | INTEGER | FOREIGN KEY -> courses(id)     |
| semester   | TEXT    | NOT NULL                       |
| grade      | TEXT    |                                |
```

## Daily Challenge

**Design a Library Database Schema**

Create a Markdown file called `library_schema.md` that designs a complete database schema for a library management system.

Your schema must include tables for:

1. **books** -- ISBN, title, author, genre, publication year, total copies, available copies.
2. **members** -- member ID, name, email, phone, membership date, membership type (student/staff/public).
3. **loans** -- which member borrowed which book, loan date, due date, return date.
4. **authors** -- author ID, name, nationality (a book may have multiple authors).
5. **book_authors** -- junction table linking books to authors (many-to-many).

For each table, specify:
- Column names and data types.
- Primary keys.
- Foreign keys and the relationships they represent.
- NOT NULL and UNIQUE constraints where appropriate.

Then answer these questions in your file:
1. Why is `book_authors` needed? Why not just put the author name in the `books` table?
2. What would happen if you tried to delete a member who has outstanding loans?
3. How would you find all books currently on loan using this schema?

## Expected Output

A well-structured Markdown file with clear table definitions, proper relationships, and thoughtful answers to the design questions.

## Assessment

1. What is the difference between a primary key and a foreign key?
2. Why would you choose a relational database over storing data in a JSON file?
3. What is a junction table, and when do you need one?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-06/day-051/`

Include `library_schema.md` and a `README.md`.

## Additional Resources

- [SQLite documentation](https://www.sqlite.org/docs.html)
- [PostgreSQL documentation](https://www.postgresql.org/docs/)
- [Database normalization explained](https://docs.microsoft.com/en-us/office/troubleshoot/access/database-normalization-description)

## Reflection

- How does thinking about data in terms of tables and relationships change how you design applications?
- What are the trade-offs of using a database versus flat files for a small personal project?
