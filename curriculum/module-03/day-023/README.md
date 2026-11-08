# Day 023: Keyword Arguments and Default Parameters

## Learning Objectives

- Use keyword arguments to make function calls more readable.
- Define default parameter values to make functions more flexible.
- Understand the difference between positional and keyword arguments.
- Use `*args` to accept a variable number of positional arguments.
- Use `**kwargs` to accept a variable number of keyword arguments.

## Introduction

So far you have called functions by passing arguments in order. This works well for functions with one or two parameters, but when a function has many parameters, positional arguments become confusing. Which number is the width? Which is the height? Keyword arguments solve this by letting you name each argument when you call the function.

Default parameters take this further. They let you define sensible default values so that callers only need to provide arguments that differ from the norm. Combined with `*args` and `**kwargs`, you can write functions that are both flexible and easy to use. Python's built-in functions like `print()` and `sorted()` use these features extensively, and now you will too.

## Concepts

### Keyword Arguments

When calling a function, you can specify which parameter each argument belongs to by name:

```python
def create_profile(name, age, city):
    print(f"{name}, {age}, from {city}")

create_profile(name="Halima", age=22, city="Kano")
```

This makes the call self-documenting. The order does not matter when all arguments are keyword arguments.

### Default Parameter Values

You can give parameters default values. If the caller does not provide that argument, the default is used:

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Musa")              # Uses default: "Hello, Musa!"
greet("Musa", "Salam")     # Overrides: "Salam, Musa!"
```

Parameters with defaults must come after parameters without defaults.

### `*args` — Variable Positional Arguments

The `*args` syntax lets a function accept any number of positional arguments. Inside the function, `args` is a tuple.

```python
def total(*args):
    return sum(args)

print(total(10, 20, 30))   # 60
```

### `**kwargs` — Variable Keyword Arguments

The `**kwargs` syntax lets a function accept any number of keyword arguments. Inside the function, `kwargs` is a dictionary.

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Aisha", role="Student", level="Beginner")
```

## Practical Examples

```python
# Default parameters in action
def generate_email(username, domain="geekink.com"):
    return f"{username}@{domain}"


print(generate_email("amina"))
# Output: amina@geekink.com

print(generate_email("musa", "gmail.com"))
# Output: musa@gmail.com


# Mixing positional and keyword arguments
def register_student(name, course, level="beginner", active=True):
    status = "Active" if active else "Inactive"
    print(f"Registered: {name} | {course} | {level} | {status}")


register_student("Ibrahim", "Python Engineering")
register_student("Fatima", "Data Science", level="intermediate")
register_student("Hassan", "Web Dev", active=False)


# Using *args to handle variable inputs
def calculate_average(*scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)


print(calculate_average(80, 90, 70))       # 80.0
print(calculate_average(95, 88, 76, 91))   # 87.5


# Using **kwargs to build a flexible function
def build_student_record(student_id, name, **details):
    record = {"id": student_id, "name": name}
    record.update(details)
    return record


student = build_student_record(
    101,
    "Zainab",
    department="Computer Science",
    gpa=3.8,
    year=2
)
print(student)
# {'id': 101, 'name': 'Zainab', 'department': 'Computer Science', 'gpa': 3.8, 'year': 2}


# Combining *args and **kwargs
def log_event(event_type, *tags, **metadata):
    print(f"Event: {event_type}")
    print(f"Tags: {', '.join(tags)}")
    for key, value in metadata.items():
        print(f"  {key}: {value}")


log_event("login", "security", "user-action", user="amina", ip="192.168.1.1")
```

## Guided Practice

Build a flexible report generator.

**Step 1:** Create a function with default formatting options.

```python
def generate_report(title, data, separator="=", width=40):
    print(separator * width)
    print(title.center(width))
    print(separator * width)
    for key, value in data.items():
        print(f"  {key}: {value}")
    print(separator * width)
```

**Step 2:** Call it with defaults and with custom options.

```python
grades = {"Math": 85, "English": 92, "Science": 78}

generate_report("Student Grades", grades)

print()

generate_report("Student Grades", grades, separator="-", width=50)
```

**Step 3:** Add `**kwargs` for extra footer notes.

```python
def generate_report(title, data, separator="=", width=40, **footer):
    print(separator * width)
    print(title.center(width))
    print(separator * width)
    for key, value in data.items():
        print(f"  {key}: {value}")
    print(separator * width)
    for key, value in footer.items():
        label = key.replace("_", " ").title()
        print(f"  {label}: {value}")


grades = {"Math": 85, "English": 92, "Science": 78}
generate_report(
    "Student Grades",
    grades,
    generated_by="GeekInk System",
    date="2024-11-08"
)
```

## Daily Challenge

Create a file called `report_generator.py` with a function called `generate_report` that accepts:

- `title` (required) — The report title.
- `*items` — A variable number of strings representing report line items.
- `author` (keyword, default `"Anonymous"`) — The report author.
- `date` (keyword, default `None`) — The report date. If not provided, use today's date.
- `width` (keyword, default `50`) — The width of the separator lines.

The function should:
1. Print a header with the title centered within a line of `=` characters.
2. Print each item as a numbered line.
3. Print a footer showing the author and date.

Example call:

```python
generate_report(
    "Weekly Progress",
    "Completed Module 3 exercises",
    "Submitted Day 22 challenge",
    "Started reading about file handling",
    author="Amina Bello",
    width=45
)
```

Expected output:

```
=============================================
            Weekly Progress
=============================================
  1. Completed Module 3 exercises
  2. Submitted Day 22 challenge
  3. Started reading about file handling
=============================================
  Author: Amina Bello
  Date: 2024-11-08
=============================================
```

## Expected Output

A working program that produces formatted reports with customizable title, items, author, date, and width. The function must use `*args` for items and keyword arguments with defaults.

## Assessment

1. What is the difference between a positional argument and a keyword argument?
2. Why must parameters with default values come after parameters without defaults in a function definition?
3. When would you use `**kwargs` instead of named keyword parameters?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-03/day-023/`

Include your `report_generator.py` file.

## Additional Resources

- [Python Docs: Keyword Arguments](https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments)
- [Python Docs: Arbitrary Argument Lists](https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists)

## Reflection

- How do default parameters improve the usability of a function?
- Think of a real-world form or application that has required and optional fields. How does that relate to required and default parameters?
