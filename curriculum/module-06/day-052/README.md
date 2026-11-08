# Day 052: SQL Fundamentals

## Learning Objectives

- Write SQL statements to create tables with appropriate data types and constraints.
- Insert data into tables using INSERT statements.
- Query data using SELECT with WHERE, ORDER BY, and LIMIT clauses.
- Use SQLite as a lightweight database for practice and development.
- Build and query a students database from scratch.

## Introduction

SQL (Structured Query Language) is the standard language for communicating with relational databases. Whether you are using SQLite, PostgreSQL, MySQL, or any other relational database, the core SQL syntax is the same. Learning SQL gives you a skill that transfers across all of these systems.

Today you will learn the foundational SQL commands: CREATE TABLE to define your data structure, INSERT to add records, and SELECT to retrieve data. These three operations are the starting point for everything you will do with databases.

We will use SQLite for practice because it requires no server setup -- it stores the entire database in a single file, and Python includes built-in support for it through the `sqlite3` module.

## Concepts

### Data Types in SQLite

SQLite uses a simplified type system:

| Type    | Description                    | Examples           |
|---------|--------------------------------|--------------------|
| INTEGER | Whole numbers                  | 1, 42, -100       |
| REAL    | Floating-point numbers         | 3.14, -0.5        |
| TEXT    | Character strings              | 'Amina', 'Kano'   |
| BLOB    | Binary data                    | Images, files      |
| NULL    | Missing or unknown value       | NULL               |

### CREATE TABLE

```sql
CREATE TABLE table_name (
    column1 TYPE CONSTRAINTS,
    column2 TYPE CONSTRAINTS,
    ...
);
```

Common constraints:
- `PRIMARY KEY` -- uniquely identifies each row.
- `NOT NULL` -- column cannot be empty.
- `UNIQUE` -- no duplicate values allowed.
- `DEFAULT value` -- default value if none is provided.

### INSERT

```sql
INSERT INTO table_name (column1, column2) VALUES (value1, value2);
```

### SELECT

```sql
SELECT column1, column2 FROM table_name;
SELECT * FROM table_name WHERE condition;
SELECT * FROM table_name ORDER BY column ASC;
SELECT * FROM table_name LIMIT 10;
```

## Practical Examples

```python
import sqlite3

# Create a database and a table
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        department TEXT DEFAULT 'Undeclared',
        level INTEGER DEFAULT 100,
        gpa REAL DEFAULT 0.0
    )
""")

conn.commit()
print("Table 'students' created successfully.")
conn.close()
```

```python
import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Insert individual records
cursor.execute("""
    INSERT INTO students (first_name, last_name, email, department, level, gpa)
    VALUES ('Amina', 'Ibrahim', 'amina@example.com', 'Computer Science', 200, 3.8)
""")

# Insert multiple records at once
students_data = [
    ('Usman', 'Bello', 'usman@example.com', 'Software Engineering', 300, 3.5),
    ('Fatima', 'Abubakar', 'fatima@example.com', 'Computer Science', 100, 3.9),
    ('Hassan', 'Musa', 'hassan@example.com', 'Information Technology', 200, 3.2),
    ('Salma', 'Mohammed', 'salma@example.com', 'Computer Science', 400, 3.7),
    ('Yusuf', 'Danjuma', 'yusuf@example.com', 'Software Engineering', 100, 2.8),
]

cursor.executemany("""
    INSERT INTO students (first_name, last_name, email, department, level, gpa)
    VALUES (?, ?, ?, ?, ?, ?)
""", students_data)

conn.commit()
print(f"Inserted {cursor.rowcount} records.")
conn.close()
```

```python
import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Select all students
print("All Students:")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(f"  {row}")

# Select specific columns with a condition
print("\nComputer Science students:")
cursor.execute("""
    SELECT first_name, last_name, level, gpa
    FROM students
    WHERE department = 'Computer Science'
""")
for row in cursor.fetchall():
    print(f"  {row[0]} {row[1]} - Level {row[2]}, GPA: {row[3]}")

# Ordering results
print("\nStudents ordered by GPA (highest first):")
cursor.execute("""
    SELECT first_name, last_name, gpa
    FROM students
    ORDER BY gpa DESC
""")
for row in cursor.fetchall():
    print(f"  {row[0]} {row[1]}: {row[2]}")

# Limiting results
print("\nTop 3 students by GPA:")
cursor.execute("""
    SELECT first_name, last_name, gpa
    FROM students
    ORDER BY gpa DESC
    LIMIT 3
""")
for row in cursor.fetchall():
    print(f"  {row[0]} {row[1]}: {row[2]}")

conn.close()
```

```python
import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Using comparison operators
print("Students with GPA above 3.5:")
cursor.execute("SELECT first_name, gpa FROM students WHERE gpa > 3.5")
for row in cursor.fetchall():
    print(f"  {row[0]}: {row[1]}")

# Using LIKE for pattern matching
print("\nStudents whose name starts with 'A':")
cursor.execute("SELECT first_name, last_name FROM students WHERE first_name LIKE 'A%'")
for row in cursor.fetchall():
    print(f"  {row[0]} {row[1]}")

# Using AND/OR
print("\nCS students at level 200 or above:")
cursor.execute("""
    SELECT first_name, last_name, level
    FROM students
    WHERE department = 'Computer Science' AND level >= 200
""")
for row in cursor.fetchall():
    print(f"  {row[0]} {row[1]} - Level {row[2]}")

conn.close()
```

## Guided Practice

Build a complete student database from scratch and run various queries.

```python
import sqlite3
import os

# Start fresh
db_path = "practice_school.db"
if os.path.exists(db_path):
    os.remove(db_path)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Step 1: Create the table
cursor.execute("""
    CREATE TABLE students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        department TEXT NOT NULL,
        level INTEGER NOT NULL CHECK(level IN (100, 200, 300, 400)),
        gpa REAL DEFAULT 0.0 CHECK(gpa >= 0.0 AND gpa <= 4.0)
    )
""")

# Step 2: Insert sample data
data = [
    ('Amina', 'Ibrahim', 'amina@uni.edu.ng', 'Computer Science', 200, 3.8),
    ('Usman', 'Bello', 'usman@uni.edu.ng', 'Software Engineering', 300, 3.5),
    ('Fatima', 'Abubakar', 'fatima@uni.edu.ng', 'Computer Science', 100, 3.9),
    ('Hassan', 'Musa', 'hassan@uni.edu.ng', 'Information Technology', 200, 3.2),
    ('Salma', 'Mohammed', 'salma@uni.edu.ng', 'Computer Science', 400, 3.7),
    ('Yusuf', 'Danjuma', 'yusuf@uni.edu.ng', 'Software Engineering', 100, 2.8),
    ('Aisha', 'Abdullahi', 'aisha@uni.edu.ng', 'Computer Science', 300, 3.6),
    ('Ibrahim', 'Sani', 'ibrahim@uni.edu.ng', 'Information Technology', 400, 3.1),
]

cursor.executemany(
    "INSERT INTO students (first_name, last_name, email, department, level, gpa) VALUES (?, ?, ?, ?, ?, ?)",
    data
)
conn.commit()

# Step 3: Run queries
print("=== Student Database Queries ===\n")

print("1. All students:")
cursor.execute("SELECT id, first_name, last_name, department, level, gpa FROM students")
print(f"   {'ID':<4} {'Name':<20} {'Department':<25} {'Level':<6} {'GPA':<4}")
print(f"   {'-'*4} {'-'*20} {'-'*25} {'-'*6} {'-'*4}")
for row in cursor.fetchall():
    print(f"   {row[0]:<4} {row[1]+' '+row[2]:<20} {row[3]:<25} {row[4]:<6} {row[5]:<4}")

print(f"\n2. Student count by department:")
cursor.execute("SELECT department, COUNT(*) FROM students GROUP BY department")
for dept, count in cursor.fetchall():
    print(f"   {dept}: {count}")

print(f"\n3. Average GPA by department:")
cursor.execute("SELECT department, ROUND(AVG(gpa), 2) FROM students GROUP BY department")
for dept, avg in cursor.fetchall():
    print(f"   {dept}: {avg}")

conn.close()
print(f"\nDatabase saved to: {db_path}")
```

## Daily Challenge

**Build a Student Records Database**

Write a script called `student_db.py` that:

1. Creates a SQLite database called `students.db`.
2. Creates a `students` table with columns: id, first_name, last_name, email, department, level, gpa.
3. Inserts at least 10 student records with varied data.
4. Runs and displays results for the following queries:
   - All students sorted alphabetically by last name.
   - Students in the "Computer Science" department.
   - Students with GPA above 3.5, ordered by GPA descending.
   - The number of students at each level.
   - The student with the highest GPA.
   - Students whose email contains "uni.edu".
5. Implements a simple command-line interface that lets the user choose which query to run.

Requirements:
- Use parameterized queries (the `?` placeholder) for any user input to prevent SQL injection.
- Use `CREATE TABLE IF NOT EXISTS` to make the script safe to run multiple times.
- Format output as aligned tables.

## Expected Output

```
=== Student Records Database ===

Choose a query:
  1. All students (alphabetical)
  2. Computer Science students
  3. High GPA students (> 3.5)
  4. Students per level
  5. Top student
  6. Search by email
  0. Exit

Enter choice: 3

Students with GPA > 3.5:
  ID  Name                 Department              GPA
  --  ----                 ----------              ---
   3  Fatima Abubakar      Computer Science        3.9
   1  Amina Ibrahim        Computer Science        3.8
   5  Salma Mohammed       Computer Science        3.7
   7  Aisha Abdullahi      Computer Science        3.6

Enter choice: 0
Goodbye!
```

## Assessment

1. What is the purpose of `AUTOINCREMENT` on a primary key column?
2. Why is it important to use `?` placeholders instead of string formatting when building SQL queries?
3. What does `CREATE TABLE IF NOT EXISTS` do, and why is it useful?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-06/day-052/`

Include `student_db.py` and a `README.md`.

## Additional Resources

- [SQLite SQL documentation](https://www.sqlite.org/lang.html)
- [Python sqlite3 module](https://docs.python.org/3/library/sqlite3.html)

## Reflection

- How does querying data with SQL compare to filtering lists and dictionaries in Python?
- What advantages does a database provide as your dataset grows larger?
