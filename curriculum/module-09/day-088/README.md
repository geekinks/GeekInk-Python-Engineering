# Day 088: Pull Requests and Code Review

## Learning Objectives

- Create well-structured pull requests with clear titles and descriptions.
- Review code effectively, focusing on correctness, readability, and maintainability.
- Provide constructive, specific, and actionable feedback.
- Use GitHub features like issues, labels, and project boards for project management.
- Understand the purpose of code review beyond catching bugs.

## Introduction

A pull request (PR) is a proposal to merge your changes into a shared codebase. It is not just a mechanism for moving code --- it is the primary place where knowledge transfer, quality assurance, and team communication happen in professional software development. When you open a PR, you are asking your teammates to review your work, suggest improvements, and approve it for production.

Code review serves multiple purposes. It catches bugs that the author missed. It ensures code follows team conventions. It spreads knowledge of the codebase across the team so that no single person is the only one who understands a given module. It also mentors junior developers by showing them how experienced engineers think about code.

Writing a good PR description is just as important as writing good code. A reviewer who understands the context, motivation, and approach can provide much better feedback than one who has to guess what the code is trying to accomplish.

## Concepts

### Anatomy of a Good Pull Request

**Title**: Short, descriptive, present tense.
- Good: "Add student enrollment validation"
- Bad: "Changes" or "fix stuff"

**Description** should answer:
1. **What** does this PR do?
2. **Why** is this change needed?
3. **How** does it work (briefly)?
4. **How to test** --- steps a reviewer can follow to verify.

### PR Template

```markdown
## Summary
Brief description of what this PR does and why.

## Changes
- Added enrollment validation to StudentRegistry
- Added unit tests for validation logic
- Updated README with new API documentation

## How to Test
1. Run `pytest test_enrollment.py -v`
2. Try enrolling a student in a full course
3. Verify the error message is clear

## Checklist
- [ ] Tests pass
- [ ] Code follows PEP 8
- [ ] Documentation updated
- [ ] No print() statements left in code
```

### Code Review Best Practices

**As a reviewer:**
- Read the PR description first to understand the context.
- Focus on logic, correctness, and edge cases, not just style.
- Be specific: "This loop could raise IndexError if the list is empty" is better than "This might break."
- Suggest alternatives, do not just criticize: "Consider using a dict lookup instead of chained if/elif for readability."
- Distinguish between blocking issues and suggestions. Use labels like "nit:" for minor style preferences.
- Acknowledge what is done well.

**As an author:**
- Keep PRs small and focused. One PR per feature or fix.
- Respond to every comment, even if just to acknowledge it.
- Do not take feedback personally. Reviews improve the code, not judge you.

### GitHub Features for Project Management

- **Issues**: Track bugs, feature requests, and tasks.
- **Labels**: Categorize issues (bug, enhancement, documentation, good first issue).
- **Milestones**: Group issues into release targets.
- **Projects**: Kanban-style boards for tracking work (To Do, In Progress, Done).

## Practical Examples

### Example: A well-written PR description

```markdown
## Summary
Add input validation to the student enrollment system to prevent
enrolling students in courses that are already at maximum capacity.

## Motivation
Currently, the system silently allows enrollment beyond the course
capacity limit, which causes issues when generating class lists.
This was reported in issue #42.

## Changes
- Added `is_full()` method to `Course` class
- Added capacity check in `StudentRegistry.enroll()`
- `enroll()` now raises `CourseFullError` when capacity is exceeded
- Added 4 unit tests covering normal enrollment, full course,
  boundary (exactly at capacity), and error message content

## How to Test
```bash
pytest tests/test_enrollment.py -v
```

## Checklist
- [x] All existing tests pass
- [x] New tests added for new behavior
- [x] Follows PEP 8
- [x] Docstrings updated
```

### Example: Good vs bad review comments

**Bad:**
> "This is wrong."

**Good:**
> "This comparison `if count = 5` uses assignment instead of equality. Should be `if count == 5`."

**Bad:**
> "Why did you do it this way?"

**Good:**
> "This works, but using `dict.get(key, default)` instead of the try/except block would simplify this from 5 lines to 1. What do you think?"

**Acknowledging good work:**
> "Nice use of a context manager here --- keeps the resource cleanup clean."

## Guided Practice

1. Review the following code as if it were submitted in a pull request. Write at least 5 review comments, categorized as "blocking" or "suggestion":

```python
import json

def load_students(filepath):
    f = open(filepath, 'r')
    data = json.load(f)
    return data

def calculate_class_average(students):
    total = 0
    for s in students:
        total += s['grade']
    avg = total / len(students)
    return avg

def get_top_students(students, n):
    sorted_students = sorted(students, key=lambda x: x['grade'], reverse=True)
    return sorted_students[:n]

def save_report(filepath, report):
    f = open(filepath, 'w')
    json.dump(report, f)
    print(f"Report saved to {filepath}")

class GradeProcessor:
    def __init__(self, filepath):
        self.students = load_students(filepath)
    
    def process(self):
        avg = calculate_class_average(self.students)
        top = get_top_students(self.students, 5)
        report = {
            'average': avg,
            'top_students': top,
            'total': len(self.students)
        }
        save_report('report.json', report)
        return report
```

2. Write your review comments in a file called `code_review.md`, formatted as:

```markdown
### Line X: [blocking/suggestion]
Comment text here.
```

3. After writing your review, rewrite the code to address all your own feedback.

## Daily Challenge

### Part 1: Write a PR Description

You have made the following changes to a student management system. Write a complete PR description using the template above.

Changes made:
- Added a `search_students(query)` method that searches by name or student ID.
- Added case-insensitive search.
- Added pagination with `limit` and `offset` parameters.
- Added 8 unit tests.
- Fixed a bug where `get_student()` returned a mutable reference (now returns a copy).

Write this as `pr_description.md`.

### Part 2: Review a Pull Request

Review the following code submission. Write detailed review comments (at least 8) covering correctness, style, security, and best practices.

```python
import sqlite3
import os

DB_NAME = "school.db"

def get_db():
    return sqlite3.connect(DB_NAME)

def init_db():
    db = get_db()
    db.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT)")
    db.commit()

def add_student(name, email, password):
    db = get_db()
    db.execute(f"INSERT INTO students (name, email, password) VALUES ('{name}', '{email}', '{password}')")
    db.commit()

def find_student(name):
    db = get_db()
    cursor = db.execute(f"SELECT * FROM students WHERE name = '{name}'")
    return cursor.fetchone()

def delete_student(id):
    db = get_db()
    db.execute(f"DELETE FROM students WHERE id = {id}")
    db.commit()
    print(f"Student {id} deleted")

def update_email(id, new_email):
    db = get_db()
    db.execute(f"UPDATE students SET email = '{new_email}' WHERE id = {id}")
    db.commit()

def list_all():
    db = get_db()
    cursor = db.execute("SELECT * FROM students")
    students = cursor.fetchall()
    for s in students:
        print(s)
    return students
```

Write your review as `code_review_challenge.md`.

### Part 3: Fix the Code

Rewrite the reviewed code to address all the issues you identified. Save as `school_db_fixed.py`.

## Expected Output

Three files:
- `pr_description.md` --- A well-structured PR description.
- `code_review_challenge.md` --- At least 8 specific, categorized review comments.
- `school_db_fixed.py` --- The corrected code addressing all review findings.

## Assessment

1. What are the key elements of a good pull request description?
2. Why is it important to distinguish between blocking issues and suggestions in a code review?
3. What is the most critical security issue in the code you reviewed today?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-09/day-088/`

Include:
- `pr_description.md`
- `code_review.md` (from Guided Practice)
- `code_review_challenge.md`
- `school_db_fixed.py`

## Additional Resources

- [GitHub Pull Request documentation](https://docs.github.com/en/pull-requests)
- [Google's Code Review Developer Guide](https://google.github.io/eng-practices/review/)

## Reflection

- How does reviewing someone else's code help you become a better programmer?
- Think about feedback you have received on your own work. What made it helpful or unhelpful?
