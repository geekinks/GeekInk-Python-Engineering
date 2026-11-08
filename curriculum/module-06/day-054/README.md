# Day 054: SQLite with Python

## Learning Objectives

- Use Python's `sqlite3` module to connect to and manage SQLite databases.
- Perform all CRUD (Create, Read, Update, Delete) operations from Python code.
- Write parameterized queries to prevent SQL injection attacks.
- Use context managers for safe database connection handling.
- Build a CLI task manager backed by SQLite.

## Introduction

You have been writing SQL queries directly over the last two days. Now you will learn to integrate SQLite deeply into Python applications. The `sqlite3` module is part of Python's standard library, meaning you can use it without installing anything.

The most important practice you will learn today is **parameterized queries**. When your application takes input from users (a search term, a name, a filter), that input must never be inserted directly into a SQL string. Direct string formatting is how SQL injection attacks happen -- one of the most common and dangerous security vulnerabilities in software. Parameterized queries solve this completely.

You will also learn to use context managers (`with` statements) to ensure database connections are always closed properly, even when errors occur.

## Concepts

### Connection and Cursor

```python
import sqlite3

conn = sqlite3.connect("myapp.db")  # Open or create database file
cursor = conn.cursor()               # Create a cursor to execute queries
# ... do work ...
conn.commit()                        # Save changes
conn.close()                         # Close the connection
```

### Context Managers

```python
with sqlite3.connect("myapp.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    # conn.commit() is called automatically on success
    # conn.rollback() is called on exception
```

### Parameterized Queries (Preventing SQL Injection)

**DANGEROUS -- never do this:**
```python
name = input("Enter name: ")
cursor.execute(f"SELECT * FROM users WHERE name = '{name}'")
# If the user types: ' OR '1'='1
# The query becomes: SELECT * FROM users WHERE name = '' OR '1'='1'
# This returns ALL users!
```

**SAFE -- always do this:**
```python
name = input("Enter name: ")
cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
```

### Row Factory

By default, `fetchall()` returns tuples. You can configure it to return dictionaries:

```python
conn.row_factory = sqlite3.Row
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
row = cursor.fetchone()
print(row["name"])  # Access by column name
```

## Practical Examples

```python
import sqlite3


def create_database():
    """Create the tasks database and table."""
    with sqlite3.connect("tasks.db") as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT DEFAULT '',
                priority TEXT DEFAULT 'medium' CHECK(priority IN ('low', 'medium', 'high')),
                completed INTEGER DEFAULT 0,
                created_at TEXT DEFAULT (datetime('now', 'localtime'))
            )
        """)
    print("Database ready.")


def add_task(title, description="", priority="medium"):
    """Add a new task using parameterized queries."""
    with sqlite3.connect("tasks.db") as conn:
        cursor = conn.execute(
            "INSERT INTO tasks (title, description, priority) VALUES (?, ?, ?)",
            (title, description, priority)
        )
        print(f"Task added with ID: {cursor.lastrowid}")
        return cursor.lastrowid


def list_tasks(show_completed=False):
    """List tasks, optionally including completed ones."""
    with sqlite3.connect("tasks.db") as conn:
        conn.row_factory = sqlite3.Row
        if show_completed:
            rows = conn.execute("SELECT * FROM tasks ORDER BY priority, created_at").fetchall()
        else:
            rows = conn.execute(
                "SELECT * FROM tasks WHERE completed = 0 ORDER BY priority, created_at"
            ).fetchall()
    
    if not rows:
        print("  No tasks found.")
        return
    
    print(f"  {'ID':<4} {'Title':<30} {'Priority':<10} {'Status':<10} {'Created'}")
    print(f"  {'-'*4} {'-'*30} {'-'*10} {'-'*10} {'-'*19}")
    for row in rows:
        status = "Done" if row["completed"] else "Pending"
        print(f"  {row['id']:<4} {row['title']:<30} {row['priority']:<10} {status:<10} {row['created_at']}")


def complete_task(task_id):
    """Mark a task as completed."""
    with sqlite3.connect("tasks.db") as conn:
        cursor = conn.execute(
            "UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,)
        )
        if cursor.rowcount == 0:
            print(f"  Task {task_id} not found.")
        else:
            print(f"  Task {task_id} marked as completed.")


def delete_task(task_id):
    """Delete a task by ID."""
    with sqlite3.connect("tasks.db") as conn:
        cursor = conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        if cursor.rowcount == 0:
            print(f"  Task {task_id} not found.")
        else:
            print(f"  Task {task_id} deleted.")


# Demo usage
create_database()

add_task("Learn SQLite with Python", "Day 054 of the bootcamp", "high")
add_task("Complete daily challenge", priority="high")
add_task("Review Module 5 notes", priority="low")
add_task("Read PEP 8 style guide", "Prepare for Module 9", "medium")

print("\nActive tasks:")
list_tasks()

complete_task(1)

print("\nAll tasks (including completed):")
list_tasks(show_completed=True)
```

```python
import sqlite3


def search_tasks(keyword):
    """Search tasks by keyword using parameterized LIKE query."""
    with sqlite3.connect("tasks.db") as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            "SELECT * FROM tasks WHERE title LIKE ? OR description LIKE ?",
            (f"%{keyword}%", f"%{keyword}%")
        ).fetchall()
    
    print(f"Search results for '{keyword}':")
    for row in rows:
        print(f"  [{row['id']}] {row['title']}")
    
    if not rows:
        print("  No matching tasks.")


def get_task_stats():
    """Get task statistics using aggregate queries."""
    with sqlite3.connect("tasks.db") as conn:
        total = conn.execute("SELECT COUNT(*) FROM tasks").fetchone()[0]
        completed = conn.execute("SELECT COUNT(*) FROM tasks WHERE completed = 1").fetchone()[0]
        pending = total - completed
        
        by_priority = conn.execute(
            "SELECT priority, COUNT(*) FROM tasks GROUP BY priority ORDER BY priority"
        ).fetchall()
    
    print("Task Statistics:")
    print(f"  Total: {total}")
    print(f"  Completed: {completed}")
    print(f"  Pending: {pending}")
    print(f"  By priority:")
    for priority, count in by_priority:
        print(f"    {priority}: {count}")


search_tasks("Module")
print()
get_task_stats()
```

## Guided Practice

Build a reusable database helper class that wraps common operations.

```python
import sqlite3
from contextlib import contextmanager


class Database:
    """A simple database helper that manages connections safely."""
    
    def __init__(self, db_path):
        self.db_path = db_path
    
    @contextmanager
    def get_connection(self):
        """Context manager for database connections."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        try:
            yield conn
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            conn.close()
    
    def execute(self, query, params=()):
        """Execute a single query and return the cursor."""
        with self.get_connection() as conn:
            return conn.execute(query, params).fetchall()
    
    def execute_write(self, query, params=()):
        """Execute a write query and return the number of affected rows."""
        with self.get_connection() as conn:
            cursor = conn.execute(query, params)
            return cursor.lastrowid if "INSERT" in query.upper() else cursor.rowcount


# Usage
db = Database("helper_demo.db")

# Create table
db.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT,
        created_at TEXT DEFAULT (datetime('now', 'localtime'))
    )
""")

# Insert
note_id = db.execute_write(
    "INSERT INTO notes (title, content) VALUES (?, ?)",
    ("First Note", "This is a test note.")
)
print(f"Created note with ID: {note_id}")

# Query
notes = db.execute("SELECT * FROM notes")
for note in notes:
    print(f"  [{note['id']}] {note['title']}: {note['content']}")
```

## Daily Challenge

**Build a CLI Task Manager**

Write a complete command-line task manager called `task_manager.py` that:

1. Uses SQLite to store tasks persistently.
2. Supports these commands:
   - `add <title>` -- add a new task (prompt for description and priority).
   - `list` -- show all pending tasks.
   - `all` -- show all tasks including completed.
   - `done <id>` -- mark a task as completed.
   - `delete <id>` -- remove a task.
   - `search <keyword>` -- search tasks by title or description.
   - `stats` -- show task statistics.
   - `edit <id>` -- update a task's title or description.
   - `quit` -- exit the program.
3. Uses parameterized queries for all database operations.
4. Validates input (numeric IDs, valid priority values).
5. Handles errors gracefully (task not found, invalid input).

Requirements:
- Use context managers for all database connections.
- Use `sqlite3.Row` for readable result access.
- Prevent SQL injection on all user inputs.
- Format output in clean, aligned tables.
- Create the database and table on first run.

## Expected Output

```
=== Task Manager ===
Commands: add, list, all, done, delete, search, stats, edit, quit

> add Learn Python databases
Description: Complete Day 054 exercises
Priority (low/medium/high): high
Task #1 added.

> add Review SQL syntax
Description:
Priority (low/medium/high): medium
Task #2 added.

> list
Pending Tasks:
  ID  Title                          Priority   Created
  1   Learn Python databases         high       2025-03-15 10:30
  2   Review SQL syntax              medium     2025-03-15 10:31

> done 1
Task #1 marked as completed.

> stats
Task Statistics:
  Total: 2 | Completed: 1 | Pending: 1
  By priority: high(1) medium(1)

> quit
Goodbye!
```

## Assessment

1. What is SQL injection, and how do parameterized queries prevent it?
2. What is the difference between `conn.commit()` and `conn.rollback()`?
3. Why should you use `conn.row_factory = sqlite3.Row` instead of accessing tuple indices?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-06/day-054/`

Include `task_manager.py` and a `README.md`. Do not include the `.db` file.

## Additional Resources

- [sqlite3 module documentation](https://docs.python.org/3/library/sqlite3.html)
- [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)

## Reflection

- How does using a database change the way you think about data persistence compared to file-based storage?
- What would need to change in your task manager if you switched from SQLite to PostgreSQL?
