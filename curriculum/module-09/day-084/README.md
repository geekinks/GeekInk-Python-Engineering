# Day 084: Testing with pytest

## Learning Objectives

- Understand the advantages of pytest over unittest for most Python projects.
- Write tests using plain `assert` statements and pytest conventions.
- Use fixtures to set up and tear down test state.
- Apply `@pytest.mark.parametrize` to test multiple inputs with a single test function.
- Organize tests using markers and run specific subsets of tests.

## Introduction

Yesterday you learned `unittest`, Python's built-in testing framework. It works well, but it requires you to write classes, use special assertion methods like `assertEqual`, and follow a somewhat verbose pattern. `pytest` is a third-party framework that has become the de facto standard in the Python community because it lets you write simpler, more readable tests.

With pytest, a test is just a function whose name starts with `test_`. You use plain Python `assert` statements instead of special methods. When a test fails, pytest shows you exactly what values were compared, making debugging faster. pytest also provides fixtures --- reusable setup functions that are injected into tests automatically --- and parametrize, which lets you run the same test logic against many different inputs with a single function.

If you understand unittest, learning pytest is straightforward. The concepts are the same; the syntax is cleaner.

## Concepts

### pytest Basics

```python
# No class needed. Just a function.
def test_addition():
    assert 2 + 3 == 5

def test_string_upper():
    assert "hello".upper() == "HELLO"
```

### Fixtures

A fixture is a function decorated with `@pytest.fixture` that provides test data or setup. Tests that need the fixture declare it as a parameter.

```python
import pytest

@pytest.fixture
def sample_list():
    return [1, 2, 3, 4, 5]

def test_sum(sample_list):
    assert sum(sample_list) == 15

def test_length(sample_list):
    assert len(sample_list) == 5
```

### Parametrize

Run the same test with different inputs:

```python
import pytest

@pytest.mark.parametrize("input_val, expected", [
    (1, 1),
    (2, 4),
    (3, 9),
    (4, 16),
    (-2, 4),
])
def test_square(input_val, expected):
    assert input_val ** 2 == expected
```

### Markers

Tag tests to run specific subsets:

```python
import pytest

@pytest.mark.slow
def test_large_computation():
    result = sum(range(10_000_000))
    assert result == 49999995000000
```

Run only slow tests: `pytest -m slow`
Skip slow tests: `pytest -m "not slow"`

### Testing Exceptions

```python
import pytest

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_value_error_message():
    with pytest.raises(ValueError, match="cannot be empty"):
        raise ValueError("Input cannot be empty")
```

## Practical Examples

### Source code (same calculator from Day 083)

```python
# calculator.py

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def average(numbers):
    if not numbers:
        raise ValueError("Cannot average an empty list")
    return sum(numbers) / len(numbers)
```

### pytest version of the tests

```python
# test_calculator_pytest.py

import pytest
from calculator import add, divide, average


# --- Fixtures ---

@pytest.fixture
def sample_scores():
    return [80, 90, 70, 85, 95]


# --- Tests for add ---

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, -1, -2),
    (-1, 1, 0),
    (0, 0, 0),
    (100, 200, 300),
])
def test_add(a, b, expected):
    assert add(a, b) == expected


def test_add_floats():
    assert add(0.1, 0.2) == pytest.approx(0.3)


# --- Tests for divide ---

def test_divide_basic():
    assert divide(10, 2) == 5

def test_divide_float_result():
    assert divide(1, 3) == pytest.approx(0.3333333)

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


# --- Tests for average ---

def test_average(sample_scores):
    assert average(sample_scores) == 84.0

def test_average_single():
    assert average([100]) == 100

def test_average_empty():
    with pytest.raises(ValueError):
        average([])
```

### Running pytest

```bash
# Install pytest
pip install pytest

# Run all tests
pytest

# Verbose output
pytest -v

# Run a specific file
pytest test_calculator_pytest.py

# Run tests matching a name pattern
pytest -k "divide"

# Show print output
pytest -s

# Stop at first failure
pytest -x
```

## Guided Practice

1. Take your `string_utils.py` from Day 083 and rewrite its test suite using pytest.

2. Replace the `TestCase` class with plain functions.

3. Replace `self.assertEqual` with `assert`.

4. Create a fixture for reusable test data.

5. Use `@pytest.mark.parametrize` for `is_palindrome` with at least 6 test cases:

```python
@pytest.mark.parametrize("text, expected", [
    ("racecar", True),
    ("hello", False),
    ("A man a plan a canal Panama", True),
    ("", True),
    ("a", True),
    ("ab", False),
])
def test_is_palindrome(text, expected):
    assert is_palindrome(text) == expected
```

6. Run with `pytest -v` and confirm all tests pass.

## Daily Challenge

Rewrite the Day 083 `Calculator` class test suite using pytest. Then extend it.

Requirements:

1. Convert all 15+ unittest tests to pytest functions (no classes required, but you may use them).

2. Create a `calculator` fixture that returns a fresh `Calculator()` instance.

3. Use `@pytest.mark.parametrize` for arithmetic operations. Test at least 5 input combinations per operation.

4. Add a `@pytest.fixture` called `calculator_with_history` that creates a calculator and performs 3 operations before returning it. Use it to test `get_last_operation` and history-related behavior.

5. Add a custom marker `@pytest.mark.edge_case` and apply it to tests that cover boundary conditions (division by zero, empty history, very large numbers).

6. Create a `conftest.py` file that registers the custom marker:

```python
# conftest.py

def pytest_configure(config):
    config.addinivalue_line(
        "markers", "edge_case: marks tests for edge case scenarios"
    )
```

7. Demonstrate running only edge case tests with `pytest -m edge_case -v`.

Your test file should have at least 20 test cases.

## Expected Output

```
$ pytest -v test_calculator_pytest.py
test_calculator_pytest.py::test_add[2-3-5] PASSED
test_calculator_pytest.py::test_add[neg1-neg1-neg2] PASSED
test_calculator_pytest.py::test_divide_by_zero PASSED
...
========================= 20 passed in 0.05s =========================
```

## Assessment

1. What are two advantages of pytest over unittest?
2. How does `@pytest.mark.parametrize` reduce code duplication in tests?
3. What is a fixture, and how does pytest inject it into a test function?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-09/day-084/`

Include:
- `calculator_oop.py` (the Calculator class, same as Day 083)
- `test_calculator_pytest.py`
- `conftest.py`
- `test_string_utils_pytest.py` (from Guided Practice)

## Additional Resources

- [pytest documentation](https://docs.pytest.org/)
- [pytest fixtures documentation](https://docs.pytest.org/en/stable/how-to/fixtures.html)

## Reflection

- Compare your unittest tests from yesterday with today's pytest versions. Which do you find more readable?
- When would you choose unittest over pytest, or does pytest replace it entirely for your projects?
