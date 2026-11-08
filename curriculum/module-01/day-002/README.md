# Day 002: Variables and Data Types

## Learning Objectives

- Understand what variables are and how they store data in memory.
- Follow Python naming conventions for variables.
- Identify and use the four basic data types: `int`, `float`, `str`, and `bool`.
- Use the `type()` function to inspect data types.
- Create meaningful variable names using snake_case.

## Introduction

In programming, we constantly need to store and work with data. A variable is a name that refers to a value stored in the computer's memory. Think of it as a labeled container: you put something inside and use the label to find it later.

Understanding data types is equally important. Python handles different kinds of data differently. A whole number like `25` behaves differently from the text `"25"` or the decimal `25.0`. Knowing the difference helps you avoid bugs and write correct programs.

Every program you will ever build depends on variables and data types. Today you lay the foundation for everything that follows.

## Concepts

### Variables

A variable is created the moment you assign a value to a name using the `=` sign. Python does not require you to declare the type of a variable. It figures out the type automatically based on the value you assign.

```python
age = 25          # Python knows this is an integer
name = "Musa"     # Python knows this is a string
```

### Naming Conventions

Python has rules and conventions for naming variables:

- Variable names must start with a letter or underscore (`_`), not a number.
- They can contain letters, numbers, and underscores.
- They are case-sensitive: `age`, `Age`, and `AGE` are three different variables.
- Use `snake_case` for variable names: `student_name`, `total_score`, `is_enrolled`.
- Avoid using Python reserved words like `print`, `if`, `for`, `class`, etc.

### Basic Data Types

| Type    | Description              | Example          |
| ------- | ------------------------ | ---------------- |
| `int`   | Whole numbers            | `42`, `-7`, `0`  |
| `float` | Decimal numbers          | `3.14`, `-0.5`   |
| `str`   | Text (strings)           | `"Hello"`, `'Hi'`|
| `bool`  | True or False            | `True`, `False`  |

### The `type()` Function

You can check the type of any value or variable using `type()`:

```python
print(type(42))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("Hello"))   # <class 'str'>
print(type(True))      # <class 'bool'>
```

## Practical Examples

```python
# Creating variables of different types
student_name = "Fatima Suleiman"
student_age = 19
gpa = 3.75
is_enrolled = True

# Printing variables
print(student_name)
print(student_age)
print(gpa)
print(is_enrolled)
```

```python
# Checking types
balance = 15000
interest_rate = 0.05
account_holder = "Ibrahim"
is_active = True

print(type(balance))        # <class 'int'>
print(type(interest_rate))  # <class 'float'>
print(type(account_holder)) # <class 'str'>
print(type(is_active))      # <class 'bool'>
```

```python
# Reassigning variables
score = 85
print(score)  # 85

score = 92
print(score)  # 92 — the old value is gone
```

```python
# Multiple assignment
x, y, z = 10, 20, 30
print(x, y, z)

# Same value to multiple variables
a = b = c = 0
print(a, b, c)
```

```python
# Using f-strings to include variables in text
city = "Kano"
population = 4_103_000  # Underscores for readability
print(f"The city of {city} has a population of about {population}")
```

## Guided Practice

Create a file called `student_profile.py` and follow these steps:

1. Create a variable `first_name` and assign it your first name.
2. Create a variable `last_name` with your last name.
3. Create a variable `age` with your age as an integer.
4. Create a variable `height_meters` with your height as a float.
5. Create a variable `is_student` and set it to `True`.
6. Print each variable along with its type:

```python
first_name = "Abubakar"
last_name = "Sadiq"
age = 21
height_meters = 1.75
is_student = True

print(f"First Name: {first_name} (type: {type(first_name).__name__})")
print(f"Last Name: {last_name} (type: {type(last_name).__name__})")
print(f"Age: {age} (type: {type(age).__name__})")
print(f"Height: {height_meters}m (type: {type(height_meters).__name__})")
print(f"Student: {is_student} (type: {type(is_student).__name__})")
```

7. Run the program and verify the output makes sense.

## Daily Challenge

Create a program called `profile_card.py` that stores the following information about a student using properly named variables:

- First name (string)
- Last name (string)
- Age (integer)
- Department (string)
- Level (integer, e.g., 100, 200, 300, 400)
- CGPA (float)
- Is a scholarship holder (boolean)

Print a formatted profile card like this:

```
========================================
         STUDENT PROFILE CARD
========================================
Name:        Halima Yusuf
Age:         20
Department:  Computer Science
Level:       300
CGPA:        4.25
Scholarship: Yes
========================================
```

Note: For the scholarship line, print "Yes" if the boolean is `True`, otherwise print "No". You can use a simple approach: `"Yes" if is_scholar else "No"`.

## Expected Output

A cleanly formatted profile card with all seven pieces of information displayed. The scholarship status should show "Yes" or "No" instead of `True` or `False`.

## Assessment

1. What is the difference between `int` and `float` in Python?
2. Why is `student_name` a better variable name than `sn` or `x`?
3. What does `type()` return when you pass it the value `True`?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-01/day-002/`

Your submission should include:
- `profile_card.py` containing your solution to the daily challenge.

## Additional Resources

- [Python Official Docs — Built-in Types](https://docs.python.org/3/library/stdtypes.html)
- [PEP 8 — Naming Conventions](https://peps.python.org/pep-0008/#naming-conventions)

## Reflection

- Why do you think Python uses different data types instead of treating everything the same?
- What naming convention will you use for your variables, and why does consistency matter?
