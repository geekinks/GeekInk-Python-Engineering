# Day 053: Advanced SQL

## Learning Objectives

- Update and delete records safely using UPDATE and DELETE statements.
- Join tables using INNER JOIN and LEFT JOIN to combine related data.
- Use aggregate functions (COUNT, SUM, AVG, MIN, MAX) with GROUP BY and HAVING.
- Write complex queries that answer real business questions.
- Build queries for a multi-table school database.

## Introduction

Yesterday you learned to create tables, insert records, and write basic SELECT queries. Today you will learn the SQL operations that make relational databases truly powerful: updating and deleting data, joining tables to combine information from multiple sources, and aggregating data to produce summaries and reports.

JOINs are perhaps the most important concept in SQL. They let you combine rows from two or more tables based on related columns. When your student data is in one table and their course enrollments are in another, a JOIN lets you answer questions like "What courses is Amina taking?" with a single query.

Aggregate functions let you summarize data: count how many students are in each department, calculate average GPAs, find the highest score. Combined with GROUP BY, these functions turn raw data into meaningful insights.

## Concepts

### UPDATE

Modify existing records. Always include a WHERE clause, or you will update every row.

```sql
UPDATE students SET gpa = 3.9 WHERE id = 1;
UPDATE students SET level = 300 WHERE department = 'Computer Science' AND level = 200;
```

### DELETE

Remove records. Always include a WHERE clause.

```sql
DELETE FROM students WHERE id = 5;
DELETE FROM enrollments WHERE semester = '2023-Fall';
```

### JOIN Types

**INNER JOIN**: returns only rows that have matching values in both tables.

```sql
SELECT students.name, courses.title
FROM students
INNER JOIN enrollments ON students.id = enrollments.student_id
INNER JOIN courses ON enrollments.course_id = courses.id;
```

**LEFT JOIN**: returns all rows from the left table, with matching rows from the right table (NULL where there is no match).

```sql
SELECT students.name, enrollments.course_id
FROM students
LEFT JOIN enrollments ON students.id = enrollments.student_id;
```

### Aggregate Functions

| Function | Purpose                   |
|----------|---------------------------|
| COUNT()  | Count the number of rows  |
| SUM()    | Add up numeric values     |
| AVG()    | Calculate the average     |
| MIN()    | Find the minimum value    |
| MAX()    | Find the maximum value    |

### GROUP BY and HAVING

```sql
-- Count students per department
SELECT department, COUNT(*) as student_count
FROM students
GROUP BY department;

-- Only departments with more than 5 students
SELECT department, COUNT(*) as student_count
FROM students
GROUP BY department
HAVING COUNT(*) > 5;
```

## Practical Examples

```python
import sqlite3
import os

# Set up a multi-table database
db_path = "school_advanced.db"
if os.path.exists(db_path):
    os.remove(db_path)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create tables
cursor.executescript("""
    CREATE TABLE departments (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
    );

    CREATE TABLE students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        department_id INTEGER NOT NULL,
        level INTEGER NOT NULL,
        gpa REAL DEFAULT 0.0,
        FOREIGN KEY (department_id) REFERENCES departments(id)
    );

    CREATE TABLE courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        department_id INTEGER NOT NULL,
        credits INTEGER NOT NULL,
        FOREIGN KEY (department_id) REFERENCES departments(id)
    );

    CREATE TABLE enrollments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        course_id INTEGER NOT NULL,
        semester TEXT NOT NULL,
        grade TEXT,
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (course_id) REFERENCES courses(id)
    );
""")

# Insert data
cursor.executemany("INSERT INTO departments VALUES (?, ?)", [
    (1, "Computer Science"), (2, "Software Engineering"), (3, "Information Technology"),
])

cursor.executemany("INSERT INTO students (name, department_id, level, gpa) VALUES (?, ?, ?, ?)", [
    ("Amina Ibrahim", 1, 200, 3.8), ("Usman Bello", 2, 300, 3.5),
    ("Fatima Abubakar", 1, 100, 3.9), ("Hassan Musa", 3, 200, 3.2),
    ("Salma Mohammed", 1, 400, 3.7), ("Yusuf Danjuma", 2, 100, 2.8),
    ("Aisha Abdullahi", 1, 300, 3.6), ("Ibrahim Sani", 3, 400, 3.1),
])

cursor.executemany("INSERT INTO courses (title, department_id, credits) VALUES (?, ?, ?)", [
    ("Intro to Programming", 1, 3), ("Data Structures", 1, 4),
    ("Software Design", 2, 3), ("Database Systems", 1, 3),
    ("Networking", 3, 3), ("Web Development", 2, 4),
])

cursor.executemany("INSERT INTO enrollments (student_id, course_id, semester, grade) VALUES (?, ?, ?, ?)", [
    (1, 1, "2025-Spring", "A"), (1, 2, "2025-Spring", "A"),
    (2, 3, "2025-Spring", "B+"), (2, 6, "2025-Spring", "A"),
    (3, 1, "2025-Spring", "A"), (4, 5, "2025-Spring", "B"),
    (5, 2, "2025-Spring", "A"), (5, 4, "2025-Spring", "B+"),
    (6, 3, "2025-Spring", None), (7, 2, "2025-Spring", "A"),
])

conn.commit()
print("Database setup complete.\n")
```

```python
# UPDATE examples
print("=== UPDATE ===")
print("Before update:")
cursor.execute("SELECT name, gpa FROM students WHERE id = 4")
print(f"  {cursor.fetchone()}")

cursor.execute("UPDATE students SET gpa = 3.4 WHERE id = 4")
conn.commit()

print("After update:")
cursor.execute("SELECT name, gpa FROM students WHERE id = 4")
print(f"  {cursor.fetchone()}")
```

```python
# JOIN examples
print("\n=== INNER JOIN: Students with their departments ===")
cursor.execute("""
    SELECT s.name, d.name as department, s.level, s.gpa
    FROM students s
    INNER JOIN departments d ON s.department_id = d.id
    ORDER BY d.name, s.name
""")
print(f"  {'Name':<20} {'Department':<25} {'Level':<6} {'GPA'}")
print(f"  {'-'*20} {'-'*25} {'-'*6} {'-'*4}")
for row in cursor.fetchall():
    print(f"  {row[0]:<20} {row[1]:<25} {row[2]:<6} {row[3]}")
```

```python
# Multi-table JOIN
print("\n=== Students and their enrolled courses ===")
cursor.execute("""
    SELECT s.name, c.title, e.grade
    FROM enrollments e
    INNER JOIN students s ON e.student_id = s.id
    INNER JOIN courses c ON e.course_id = c.id
    ORDER BY s.name
""")
for row in cursor.fetchall():
    grade = row[2] if row[2] else "Not graded"
    print(f"  {row[0]:<20} {row[1]:<25} {grade}")
```

```python
# LEFT JOIN -- shows students even if they have no enrollments
print("\n=== LEFT JOIN: All students, with enrollments ===")
cursor.execute("""
    SELECT s.name, COALESCE(c.title, 'No courses') as course
    FROM students s
    LEFT JOIN enrollments e ON s.id = e.student_id
    LEFT JOIN courses c ON e.course_id = c.id
    ORDER BY s.name
""")
for row in cursor.fetchall():
    print(f"  {row[0]:<20} {row[1]}")
```

```python
# Aggregate functions with GROUP BY
print("\n=== Aggregate Queries ===")

print("\nStudents per department:")
cursor.execute("""
    SELECT d.name, COUNT(s.id) as count
    FROM departments d
    LEFT JOIN students s ON d.id = s.department_id
    GROUP BY d.name
""")
for row in cursor.fetchall():
    print(f"  {row[0]}: {row[1]}")

print("\nAverage GPA per department:")
cursor.execute("""
    SELECT d.name, ROUND(AVG(s.gpa), 2) as avg_gpa
    FROM departments d
    INNER JOIN students s ON d.id = s.department_id
    GROUP BY d.name
""")
for row in cursor.fetchall():
    print(f"  {row[0]}: {row[1]}")

print("\nDepartments with average GPA above 3.5 (HAVING):")
cursor.execute("""
    SELECT d.name, ROUND(AVG(s.gpa), 2) as avg_gpa
    FROM departments d
    INNER JOIN students s ON d.id = s.department_id
    GROUP BY d.name
    HAVING AVG(s.gpa) > 3.5
""")
for row in cursor.fetchall():
    print(f"  {row[0]}: {row[1]}")

conn.close()
```

## Guided Practice

Using the database created above, write and run the following queries:

1. Find the total number of credits each student is enrolled in.
2. Find courses with no enrollments.
3. Find the student enrolled in the most courses.

```python
import sqlite3

conn = sqlite3.connect("school_advanced.db")
cursor = conn.cursor()

# 1. Total credits per student
print("Total credits per student:")
cursor.execute("""
    SELECT s.name, SUM(c.credits) as total_credits
    FROM students s
    INNER JOIN enrollments e ON s.id = e.student_id
    INNER JOIN courses c ON e.course_id = c.id
    GROUP BY s.id
    ORDER BY total_credits DESC
""")
for row in cursor.fetchall():
    print(f"  {row[0]:<20} {row[1]} credits")

# 2. Courses with no enrollments
print("\nCourses with no enrollments:")
cursor.execute("""
    SELECT c.title
    FROM courses c
    LEFT JOIN enrollments e ON c.id = e.course_id
    WHERE e.id IS NULL
""")
results = cursor.fetchall()
if results:
    for row in results:
        print(f"  {row[0]}")
else:
    print("  All courses have enrollments.")

# 3. Student with most courses
print("\nStudent with most courses:")
cursor.execute("""
    SELECT s.name, COUNT(e.id) as course_count
    FROM students s
    INNER JOIN enrollments e ON s.id = e.student_id
    GROUP BY s.id
    ORDER BY course_count DESC
    LIMIT 1
""")
row = cursor.fetchone()
print(f"  {row[0]}: {row[1]} courses")

conn.close()
```

## Daily Challenge

**Write Queries for a Multi-Table School Database**

Using the `school_advanced.db` database from the examples above, write a script called `school_queries.py` that answers these questions:

1. List all students with their department name and number of enrolled courses.
2. Find the average GPA of students who are enrolled in "Data Structures".
3. List departments ranked by their total number of enrollments.
4. Find students who are enrolled in more than one course.
5. Show the grade distribution (count of each grade) across all enrollments.
6. Find the course with the most enrolled students.
7. List students who are NOT enrolled in any courses.
8. Update all students in level 100 to level 200, then verify the change.

Requirements:
- Each query should print a descriptive header.
- Format output in aligned columns.
- Use appropriate JOINs and aggregate functions.
- After the UPDATE query, print the before and after state.

## Expected Output

```
=== School Database Queries ===

1. Students with departments and enrollment counts:
   Name                 Department              Courses
   Amina Ibrahim        Computer Science        2
   Usman Bello          Software Engineering    2
   ...

2. Average GPA of students in "Data Structures": 3.77

3. Departments by total enrollments:
   Computer Science: 6
   Software Engineering: 3
   Information Technology: 1

...
```

## Assessment

1. What is the difference between INNER JOIN and LEFT JOIN? When would you use each?
2. What is the difference between WHERE and HAVING in a SQL query?
3. Why should you always include a WHERE clause with UPDATE and DELETE statements?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-06/day-053/`

Include `school_queries.py` and a `README.md`.

## Additional Resources

- [SQL JOINs visual explanation](https://www.w3schools.com/sql/sql_join.asp)
- [SQLite aggregate functions](https://www.sqlite.org/lang_aggfunc.html)

## Reflection

- How do JOINs change the way you think about organizing data across tables?
- What is the most complex query you wrote today, and how did you break it down into parts?
