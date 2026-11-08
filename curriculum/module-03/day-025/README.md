# Day 025: Lambda Functions and Higher-Order Functions

## Learning Objectives

- Write lambda (anonymous) functions for short, one-expression operations.
- Use `map()` to transform every element in a sequence.
- Use `filter()` to select elements that meet a condition.
- Use `sorted()` with a `key` function to customize sort order.
- Understand what higher-order functions are and why they matter.

## Introduction

Not every function needs a name. Sometimes you need a tiny function that you will use only once — to sort a list by a specific field, to filter out invalid entries, or to transform data in a pipeline. Python provides lambda functions for exactly this purpose. A lambda is a small anonymous function defined in a single expression.

Lambda functions become especially powerful when combined with higher-order functions — functions that take other functions as arguments. Python's built-in `map()`, `filter()`, and `sorted()` are higher-order functions. They let you process entire collections of data in a clean, readable way without writing explicit loops. This style of programming is common in data processing, and you will use it frequently as you advance.

## Concepts

### Lambda Functions

A lambda function is defined with the `lambda` keyword, followed by parameters, a colon, and a single expression. It returns the result of that expression automatically.

```python
# Regular function
def square(x):
    return x ** 2

# Equivalent lambda
square = lambda x: x ** 2
```

Lambdas are best used inline, as arguments to other functions, not as named replacements for `def`.

### Higher-Order Functions

A higher-order function is a function that takes another function as an argument or returns a function. Python's `map()`, `filter()`, and `sorted()` are all higher-order functions.

### `map(function, iterable)`

Applies the function to every element and returns an iterator of results.

### `filter(function, iterable)`

Returns an iterator of elements for which the function returns `True`.

### `sorted(iterable, key=function)`

Returns a new sorted list. The `key` function determines the sort criterion.

## Practical Examples

```python
# Lambda basics
double = lambda x: x * 2
print(double(5))    # 10

full_name = lambda first, last: f"{first} {last}"
print(full_name("Amina", "Bello"))    # Amina Bello


# map() — transform every element
prices_usd = [10, 25, 50, 100]
prices_ngn = list(map(lambda p: p * 1600, prices_usd))
print(prices_ngn)    # [16000, 40000, 80000, 160000]


# map() with a named function
def to_uppercase(text):
    return text.upper()

names = ["amina", "musa", "fatima"]
upper_names = list(map(to_uppercase, names))
print(upper_names)    # ['AMINA', 'MUSA', 'FATIMA']


# filter() — select elements
scores = [45, 82, 67, 38, 91, 55, 73]
passing = list(filter(lambda s: s >= 50, scores))
print(passing)    # [82, 67, 91, 55, 73]


# filter() to remove empty strings
entries = ["Amina", "", "Musa", "", "Fatima", ""]
clean = list(filter(None, entries))
print(clean)    # ['Amina', 'Musa', 'Fatima']


# sorted() with a key function
students = [
    {"name": "Zainab", "score": 88},
    {"name": "Amina", "score": 95},
    {"name": "Ibrahim", "score": 72},
]

by_score = sorted(students, key=lambda s: s["score"], reverse=True)
for s in by_score:
    print(f"{s['name']}: {s['score']}")
# Amina: 95
# Zainab: 88
# Ibrahim: 72


# Chaining map and filter
numbers = range(1, 21)
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(result)    # [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
```

## Guided Practice

Process a list of student records using lambda, map, filter, and sorted.

```python
students = [
    {"name": "Halima", "score": 82, "department": "CS"},
    {"name": "Yusuf", "score": 45, "department": "EE"},
    {"name": "Aisha", "score": 91, "department": "CS"},
    {"name": "Musa", "score": 67, "department": "ME"},
    {"name": "Fatima", "score": 38, "department": "CS"},
    {"name": "Ibrahim", "score": 73, "department": "EE"},
]

# Step 1: Filter students who passed (score >= 50)
passed = list(filter(lambda s: s["score"] >= 50, students))
print("Passed:")
for s in passed:
    print(f"  {s['name']}: {s['score']}")

# Step 2: Get just the names of passing students
passed_names = list(map(lambda s: s["name"], passed))
print(f"\nPassing names: {passed_names}")

# Step 3: Sort all students by score (highest first)
ranked = sorted(students, key=lambda s: s["score"], reverse=True)
print("\nRanked:")
for i, s in enumerate(ranked, 1):
    print(f"  {i}. {s['name']} — {s['score']}")

# Step 4: Filter CS students and calculate their average
cs_students = list(filter(lambda s: s["department"] == "CS", students))
cs_avg = sum(map(lambda s: s["score"], cs_students)) / len(cs_students)
print(f"\nCS average: {cs_avg:.1f}")
```

## Daily Challenge

Create a file called `student_processor.py` that works with the following list of student records:

```python
students = [
    {"name": "Amina", "score": 85, "age": 20, "department": "CS"},
    {"name": "Musa", "score": 42, "age": 22, "department": "EE"},
    {"name": "Fatima", "score": 91, "age": 19, "department": "CS"},
    {"name": "Ibrahim", "score": 67, "age": 21, "department": "ME"},
    {"name": "Halima", "score": 38, "age": 23, "department": "CS"},
    {"name": "Yusuf", "score": 73, "age": 20, "department": "EE"},
    {"name": "Zainab", "score": 55, "age": 22, "department": "ME"},
    {"name": "Hassan", "score": 89, "age": 21, "department": "CS"},
]
```

Using only `map()`, `filter()`, `sorted()`, and `lambda` (no explicit for-loops for the processing), produce the following outputs:

1. A list of names of students who passed (score >= 50).
2. A list of names of students who failed (score < 50).
3. All students sorted by score from highest to lowest — print rank, name, and score.
4. The average score of all students.
5. A list of student names from the CS department, sorted alphabetically.
6. A list of students aged 21 or older, showing name and age.

Print each result clearly with a label.

## Expected Output

```
Passed: ['Amina', 'Fatima', 'Ibrahim', 'Yusuf', 'Zainab', 'Hassan']
Failed: ['Musa', 'Halima']

Ranked by Score:
  1. Fatima — 91
  2. Hassan — 89
  3. Amina — 85
  4. Yusuf — 73
  5. Ibrahim — 67
  6. Zainab — 55
  7. Musa — 42
  8. Halima — 38

Average score: 67.5

CS students (alphabetical): ['Amina', 'Fatima', 'Halima', 'Hassan']

Students aged 21+:
  Musa — 22
  Ibrahim — 21
  Halima — 23
  Zainab — 22
  Hassan — 21
```

## Assessment

1. When should you use a lambda function instead of a regular `def` function?
2. What does `map()` return, and why do you often wrap it in `list()`?
3. Explain the difference between `filter()` and a list comprehension with an `if` clause. When might you prefer one over the other?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-03/day-025/`

Include your `student_processor.py` file.

## Additional Resources

- [Python Docs: Lambda Expressions](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)
- [Python Docs: Built-in Functions — map, filter, sorted](https://docs.python.org/3/library/functions.html)

## Reflection

- In what situations would a named function be clearer than a lambda, even if the lambda works?
- How does thinking in terms of "transform" (map) and "select" (filter) change the way you approach data processing?
