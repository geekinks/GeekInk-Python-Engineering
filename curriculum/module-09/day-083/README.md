# Day 083: Unit Testing with unittest

## Learning Objectives

- Understand why automated testing is essential in professional software development.
- Write unit tests using Python's built-in `unittest` module.
- Use `TestCase`, `setUp`, `tearDown`, and common assertion methods.
- Organize tests alongside source code and run them from the command line.
- Test both expected behavior and expected failures (exception handling).

## Introduction

Imagine you build a student grading system. It works perfectly today. Next week you add a new feature and suddenly grades are calculated wrong. Without tests, you might not notice until a student complains. With tests, the failure is caught the moment you run them.

Unit testing means writing small, focused tests that verify individual functions or methods work correctly in isolation. Each test checks one specific behavior: given these inputs, the function should produce this output. When you change your code, you run all your tests. If they pass, you have confidence your change did not break anything. If they fail, you know exactly what broke and where.

Python includes `unittest` in its standard library. It follows the xUnit testing pattern used across many languages: you create a test class, write test methods, and use assertion methods to check results. This makes your test suite a living specification of how your code is supposed to behave.

## Concepts

### The unittest Framework

A test class inherits from `unittest.TestCase`. Each method whose name starts with `test_` is discovered and run automatically. The framework provides assertion methods to compare actual results against expected results.

### Common Assertion Methods

| Method | Checks |
|--------|--------|
| `assertEqual(a, b)` | `a == b` |
| `assertNotEqual(a, b)` | `a != b` |
| `assertTrue(x)` | `bool(x) is True` |
| `assertFalse(x)` | `bool(x) is False` |
| `assertIs(a, b)` | `a is b` |
| `assertIsNone(x)` | `x is None` |
| `assertIn(a, b)` | `a in b` |
| `assertRaises(exc)` | A specific exception is raised |
| `assertAlmostEqual(a, b)` | `round(a-b, 7) == 0` |

### setUp and tearDown

`setUp()` runs before every test method. Use it to create objects or state that multiple tests need. `tearDown()` runs after every test method, even if the test fails. Use it for cleanup.

## Practical Examples

### The code to test

```python
# calculator.py

def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def divide(a, b):
    """Return a divided by b. Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def average(numbers):
    """Return the arithmetic mean of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot average an empty list")
    return sum(numbers) / len(numbers)
```

### The test file

```python
# test_calculator.py

import unittest
from calculator import add, divide, average


class TestAdd(unittest.TestCase):
    """Tests for the add function."""

    def test_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

    def test_mixed_numbers(self):
        self.assertEqual(add(-1, 1), 0)

    def test_floats(self):
        self.assertAlmostEqual(add(0.1, 0.2), 0.3)


class TestDivide(unittest.TestCase):
    """Tests for the divide function."""

    def test_basic_division(self):
        self.assertEqual(divide(10, 2), 5)

    def test_float_result(self):
        self.assertAlmostEqual(divide(1, 3), 0.3333333)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)


class TestAverage(unittest.TestCase):
    """Tests for the average function."""

    def setUp(self):
        self.scores = [80, 90, 70, 85, 95]

    def test_average_of_scores(self):
        self.assertEqual(average(self.scores), 84.0)

    def test_single_value(self):
        self.assertEqual(average([100]), 100)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            average([])


if __name__ == "__main__":
    unittest.main()
```

### Running the tests

```bash
# Run all tests in a file
python -m unittest test_calculator.py

# Run with verbose output
python -m unittest -v test_calculator.py

# Discover and run all test files in a directory
python -m unittest discover -s tests -p "test_*.py"
```

## Guided Practice

1. Create a file `string_utils.py`:

```python
def reverse_string(s):
    """Return the reversed version of a string."""
    return s[::-1]


def count_vowels(s):
    """Count the number of vowels (a, e, i, o, u) in a string."""
    return sum(1 for char in s.lower() if char in "aeiou")


def is_palindrome(s):
    """Check if a string reads the same forwards and backwards (case-insensitive)."""
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def truncate(s, max_length, suffix="..."):
    """Truncate a string to max_length characters, adding suffix if truncated."""
    if len(s) <= max_length:
        return s
    return s[:max_length - len(suffix)] + suffix
```

2. Create `test_string_utils.py` with a test class for each function. Include:
   - At least 3 test methods per function.
   - Tests for normal cases, edge cases (empty string, single character), and boundary conditions.
   - Use `setUp` to define reusable test data.

3. Run your tests with verbose output and confirm they all pass.

## Daily Challenge

Write a `Calculator` class and a complete test suite for it.

### The Calculator class (create `calculator_oop.py`)

```python
class Calculator:
    """A calculator that maintains a running history of operations."""

    def __init__(self):
        self.history = []

    def add(self, a, b):
        """Add two numbers and record the operation."""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        """Subtract b from a and record the operation."""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        """Multiply two numbers and record the operation."""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        """Divide a by b. Raises ValueError if b is zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def get_last_operation(self):
        """Return the most recent operation string, or None if no history."""
        if not self.history:
            return None
        return self.history[-1]

    def clear_history(self):
        """Clear all operation history."""
        self.history.clear()
```

Write `test_calculator_oop.py` with:

- A `setUp` method that creates a fresh `Calculator` instance for each test.
- Tests for each arithmetic method with positive, negative, and float inputs.
- A test that `divide(x, 0)` raises `ValueError`.
- Tests for `get_last_operation` returning the correct string after an operation.
- A test that `get_last_operation` returns `None` on a fresh calculator.
- A test that `clear_history` empties the history list.
- At least 15 test methods total.

## Expected Output

```
$ python -m unittest -v test_calculator_oop.py
test_add_positive ... ok
test_add_negative ... ok
test_add_floats ... ok
test_subtract_basic ... ok
...
----------------------------------------------------------------------
Ran 15 tests in 0.002s

OK
```

## Assessment

1. Why should each test method test only one specific behavior?
2. What is the purpose of `setUp` and when would you use `tearDown`?
3. How does `assertRaises` work, and why is it better than wrapping code in a try/except inside your test?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-09/day-083/`

Include:
- `calculator_oop.py`
- `test_calculator_oop.py`
- `string_utils.py` and `test_string_utils.py` (from Guided Practice)

## Additional Resources

- [unittest documentation](https://docs.python.org/3/library/unittest.html)
- [Python Testing Best Practices](https://docs.python.org/3/library/unittest.html#organizing-test-code)

## Reflection

- How does writing tests change the way you think about designing your functions?
- If you had to explain to a teammate why they should write tests, what argument would be most convincing?
