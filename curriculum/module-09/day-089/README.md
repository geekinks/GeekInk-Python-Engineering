# Day 089: Documentation and README Writing

## Learning Objectives

- Understand why documentation is a professional engineering requirement, not an afterthought.
- Write effective README files that help users and contributors get started quickly.
- Write Python docstrings following Google or NumPy style conventions.
- Generate documentation from code using pdoc.
- Document APIs with clear parameter descriptions and usage examples.

## Introduction

Code without documentation is a liability. No matter how well-written your code is, if no one can figure out how to install it, use it, or contribute to it, the code might as well not exist. Documentation is the bridge between your code and the people who need to use it --- including your future self.

The most important piece of documentation for any project is the README. It is the first thing a visitor sees on GitHub. A good README answers the essential questions in seconds: What does this project do? How do I install it? How do I use it? How do I contribute? A bad README (or no README) drives people away.

At the code level, docstrings document functions, classes, and modules. They explain what a piece of code does, what parameters it accepts, what it returns, and what exceptions it raises. When written consistently, docstrings can be used to auto-generate browsable HTML documentation.

## Concepts

### README Structure

A good README typically contains:

1. **Project title** and one-line description.
2. **Table of contents** (for longer READMEs).
3. **Installation** instructions.
4. **Usage** examples (the most important section).
5. **API reference** or link to full documentation.
6. **Contributing** guidelines.
7. **License** information.

### Docstring Styles

**Google style:**

```python
def calculate_gpa(scores, credit_hours):
    """Calculate weighted GPA from scores and credit hours.

    Args:
        scores: A list of numeric grade scores (0-100).
        credit_hours: A list of credit hours corresponding to each score.

    Returns:
        The weighted GPA as a float between 0.0 and 4.0.

    Raises:
        ValueError: If scores and credit_hours have different lengths.
        ValueError: If any score is outside the 0-100 range.
    """
```

**NumPy style:**

```python
def calculate_gpa(scores, credit_hours):
    """Calculate weighted GPA from scores and credit hours.

    Parameters
    ----------
    scores : list of float
        Grade scores between 0 and 100.
    credit_hours : list of int
        Credit hours for each corresponding score.

    Returns
    -------
    float
        The weighted GPA between 0.0 and 4.0.

    Raises
    ------
    ValueError
        If scores and credit_hours have different lengths.
    """
```

### Module-Level Docstrings

Every Python module (file) should have a docstring at the top:

```python
"""Student enrollment management.

This module provides functions for enrolling students in courses,
validating prerequisites, and managing waitlists.
"""
```

### Generating Documentation with pdoc

```bash
pip install pdoc

# Generate HTML docs
pdoc --html my_module.py

# Serve docs locally for preview
pdoc my_module.py
```

## Practical Examples

### Example: A complete project README

```markdown
# Student Grade Analyzer

A command-line tool for analyzing student performance data and
generating grade reports.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Installation

Requires Python 3.10 or later.

    git clone https://github.com/your-username/grade-analyzer.git
    cd grade-analyzer
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

## Usage

### Basic usage

    python analyze.py data/students.csv

### Generate a summary report

    python analyze.py data/students.csv --format summary --output report.txt

### Filter by department

    python analyze.py data/students.csv --department "Computer Science"

## Configuration

Create a `config.yaml` file in the project root:

    passing_grade: 50
    honors_threshold: 85
    output_format: csv

## Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Run tests: `pytest`
4. Submit a pull request.

See [CONTRIBUTING.md](../../../CONTRIBUTING.md) for detailed guidelines.

## License

MIT License. See [LICENSE](../../../LICENSE) for details.
```

### Example: Well-documented Python module

```python
"""Attendance tracking for educational institutions.

This module provides the AttendanceTracker class for recording and
analyzing student attendance. It supports daily check-ins, absence
tracking, and generating attendance reports.

Example:
    tracker = AttendanceTracker("CS101")
    tracker.record_attendance("STU001", "2024-01-15", present=True)
    report = tracker.get_report("STU001")
"""

from datetime import date


class AttendanceTracker:
    """Track student attendance for a specific course.

    Attributes:
        course_id: The course identifier string.
        records: A dictionary mapping student IDs to attendance records.
    """

    def __init__(self, course_id):
        """Initialize the tracker for a specific course.

        Args:
            course_id: A string identifying the course.
        """
        self.course_id = course_id
        self.records = {}

    def record_attendance(self, student_id, date_str, present=True):
        """Record a student's attendance for a given date.

        Args:
            student_id: The student's unique identifier.
            date_str: The date in YYYY-MM-DD format.
            present: Whether the student was present. Defaults to True.

        Raises:
            ValueError: If date_str is not in YYYY-MM-DD format.
        """
        try:
            date.fromisoformat(date_str)
        except ValueError:
            raise ValueError(f"Invalid date format: {date_str}. Use YYYY-MM-DD.")

        if student_id not in self.records:
            self.records[student_id] = []
        self.records[student_id].append({
            "date": date_str,
            "present": present,
        })

    def get_attendance_rate(self, student_id):
        """Calculate a student's attendance rate as a percentage.

        Args:
            student_id: The student's unique identifier.

        Returns:
            The attendance rate as a float between 0.0 and 100.0.
            Returns 0.0 if the student has no records.
        """
        if student_id not in self.records:
            return 0.0
        records = self.records[student_id]
        if not records:
            return 0.0
        present_count = sum(1 for r in records if r["present"])
        return (present_count / len(records)) * 100
```

## Guided Practice

1. Take the `InventoryManager` class from Day 086 (or create a simplified version).

2. It currently has minimal or no documentation. Add:
   - A module-level docstring with an example.
   - A class docstring describing the class.
   - Google-style docstrings for every public method.

3. Create a README for it as if it were a standalone project. Include installation, usage examples, and API reference.

4. Install pdoc (`pip install pdoc`) and generate HTML documentation from your module:

```bash
pdoc inventory_manager.py
```

5. Browse the generated documentation and verify it looks correct.

## Daily Challenge

You are given the following undocumented project. Your task is to add complete documentation.

```python
# task_manager.py

class Task:
    def __init__(self, title, description="", priority="medium"):
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = False
        self.subtasks = []

    def complete(self):
        self.completed = True
        for subtask in self.subtasks:
            subtask.complete()

    def add_subtask(self, title, description=""):
        subtask = Task(title, description, self.priority)
        self.subtasks.append(subtask)
        return subtask

    def progress(self):
        if not self.subtasks:
            return 100.0 if self.completed else 0.0
        completed = sum(1 for t in self.subtasks if t.completed)
        return (completed / len(self.subtasks)) * 100


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description="", priority="medium"):
        task = Task(title, description, priority)
        self.tasks.append(task)
        return task

    def get_tasks(self, priority=None, completed=None):
        results = self.tasks
        if priority is not None:
            results = [t for t in results if t.priority == priority]
        if completed is not None:
            results = [t for t in results if t.completed == completed]
        return results

    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.complete()
                return True
        return False

    def summary(self):
        total = len(self.tasks)
        done = sum(1 for t in self.tasks if t.completed)
        pending = total - done
        return {"total": total, "completed": done, "pending": pending}
```

Requirements:

1. Add a module-level docstring with a usage example.
2. Add Google-style docstrings to both classes and every method.
3. Create a `README.md` for this project with:
   - Title and description
   - Installation
   - Quick start example
   - Full API reference (every class and method)
   - Example output
4. Generate HTML docs with pdoc and confirm they render correctly.

## Expected Output

- A fully documented `task_manager.py` where `help(TaskManager)` in a Python shell shows clear, complete documentation.
- A `README.md` that a new developer could follow to use the task manager immediately.

## Assessment

1. What is the difference between a module docstring and a function docstring?
2. Why should a README include usage examples rather than just listing features?
3. What are the trade-offs between Google-style and NumPy-style docstrings?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-09/day-089/`

Include:
- `task_manager.py` (fully documented version)
- `README.md` (project README for the task manager)

## Additional Resources

- [PEP 257 -- Docstring Conventions](https://peps.python.org/pep-0257/)
- [Google Python Style Guide - Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
- [pdoc documentation](https://pdoc.dev/)

## Reflection

- Look at a project you built earlier in this course. Would a stranger be able to understand and use it based on its current documentation?
- How does writing documentation change the way you think about your code's public interface?
