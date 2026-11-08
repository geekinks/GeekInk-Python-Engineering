# Day 026: Modules and Packages

## Learning Objectives

- Import and use Python's built-in modules.
- Create your own modules and import them into other files.
- Understand the difference between `import`, `from...import`, and `import...as`.
- Use `if __name__ == "__main__"` to control script execution.
- Know what Python's standard library offers and where to find documentation.

## Introduction

As your programs grow, putting everything in a single file becomes unmanageable. Modules let you split your code into separate files, each focused on a specific responsibility. A module is simply a Python file that contains functions, classes, and variables that other files can import and use.

Python also ships with a rich standard library — hundreds of modules ready to use without installing anything. Need to work with dates? Import `datetime`. Need random numbers? Import `random`. Need to interact with the operating system? Import `os`. Before writing a function from scratch, check whether the standard library already provides it. Professional engineers leverage existing, tested code instead of reinventing it.

## Concepts

### Importing Modules

```python
import math
print(math.sqrt(16))    # 4.0

from math import pi, sqrt
print(pi)               # 3.141592653589793
print(sqrt(25))         # 5.0

import datetime as dt
today = dt.date.today()
```

### Creating Your Own Module

Any `.py` file is a module. If you have a file called `helpers.py`, you can import it from another file in the same directory:

```python
# helpers.py
def greet(name):
    return f"Hello, {name}!"
```

```python
# main.py
import helpers
print(helpers.greet("Amina"))
```

### `if __name__ == "__main__"`

When Python runs a file directly, it sets `__name__` to `"__main__"`. When the file is imported as a module, `__name__` is set to the module's name. This lets you include test code that only runs when the file is executed directly.

```python
# helpers.py
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("Test"))
```

### Packages

A package is a directory containing an `__init__.py` file and one or more modules. Packages organize related modules into a hierarchy.

### The Standard Library

Key modules you should know about:

| Module | Purpose |
|--------|---------|
| `math` | Mathematical functions |
| `random` | Random number generation |
| `datetime` | Date and time handling |
| `os` | Operating system interface |
| `sys` | System-specific parameters |
| `json` | JSON encoding/decoding |
| `csv` | CSV file handling |
| `pathlib` | Object-oriented file paths |
| `collections` | Specialized container types |
| `string` | String constants and utilities |

## Practical Examples

```python
# Using the math module
import math

print(math.ceil(4.3))      # 5
print(math.floor(4.7))     # 4
print(math.factorial(5))   # 120
print(math.gcd(12, 8))     # 4


# Using the random module
import random

print(random.randint(1, 100))
print(random.choice(["Amina", "Musa", "Fatima"]))
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)


# Using the datetime module
from datetime import date, timedelta

today = date.today()
print(f"Today: {today}")
print(f"Day of week: {today.strftime('%A')}")

future = today + timedelta(days=100)
print(f"100 days from now: {future}")


# Using os and pathlib
import os
from pathlib import Path

print(f"Current directory: {os.getcwd()}")
print(f"Home directory: {Path.home()}")


# Creating and using a custom module
# Imagine this is in a file called string_utils.py:
"""
def reverse(text):
    return text[::-1]

def count_words(text):
    return len(text.split())

def title_case(text):
    return text.title()
"""
# Then in main.py:
# from string_utils import reverse, count_words
# print(reverse("hello"))      # olleh
# print(count_words("Hello world from GeekInk"))  # 4
```

## Guided Practice

Create a small project with two files.

**Step 1:** Create `math_utils.py`:

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

if __name__ == "__main__":
    print("Testing math_utils:")
    print(f"add(3, 5) = {add(3, 5)}")
    print(f"divide(10, 3) = {divide(10, 3)}")
    print(f"average([80, 90, 70]) = {average([80, 90, 70])}")
```

**Step 2:** Create `main.py` that imports and uses the module:

```python
from math_utils import add, subtract, multiply, divide, average

print("Calculator")
print(f"10 + 5 = {add(10, 5)}")
print(f"10 - 5 = {subtract(10, 5)}")
print(f"10 * 5 = {multiply(10, 5)}")
print(f"10 / 5 = {divide(10, 5)}")

grades = [85, 92, 78, 90, 88]
print(f"Average grade: {average(grades)}")
```

**Step 3:** Run `math_utils.py` directly to see the tests, then run `main.py` to see the calculator.

## Daily Challenge

Create a project with the following structure:

```
day-026/
    math_utils.py
    string_utils.py
    main.py
```

**`math_utils.py`** must contain:
- `factorial(n)` — Returns the factorial of n (without using `math.factorial`).
- `is_prime(n)` — Returns `True` if n is prime.
- `fibonacci(n)` — Returns a list of the first n Fibonacci numbers.

**`string_utils.py`** must contain:
- `is_palindrome(text)` — Returns `True` if the text reads the same forwards and backwards (case-insensitive, ignoring spaces).
- `word_frequency(text)` — Returns a dictionary mapping each word (lowercase) to its count.
- `truncate(text, max_length)` — Returns the text truncated to `max_length` characters, adding `"..."` if truncated.

**`main.py`** must:
- Import functions from both modules.
- Demonstrate each function with example calls and printed results.
- Use `if __name__ == "__main__"` properly.

Both module files must include their own `if __name__ == "__main__"` test sections.

## Expected Output

When running `main.py`:

```
=== Math Utils ===
factorial(5) = 120
is_prime(17) = True
is_prime(15) = False
fibonacci(8) = [0, 1, 1, 2, 3, 5, 8, 13]

=== String Utils ===
is_palindrome("racecar") = True
is_palindrome("hello") = False
word_frequency("the cat and the dog") = {'the': 2, 'cat': 1, 'and': 1, 'dog': 1}
truncate("Hello World from GeekInk", 15) = Hello World fro...
```

## Assessment

1. What is the difference between `import math` and `from math import sqrt`?
2. What happens when you run a Python file directly versus importing it as a module? How does `__name__` differ?
3. Name three modules from Python's standard library and describe what each one does.

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-03/day-026/`

Include `math_utils.py`, `string_utils.py`, and `main.py`.

## Additional Resources

- [Python Docs: Modules](https://docs.python.org/3/tutorial/modules.html)
- [Python Standard Library Index](https://docs.python.org/3/library/index.html)

## Reflection

- How does splitting code into modules make a project easier to work on as a team?
- Before writing a function, how would you check whether Python's standard library already has what you need?
