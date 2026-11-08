# Day 017: List and Dictionary Comprehensions

## Learning Objectives

- Write list comprehensions to create lists concisely.
- Add conditions to comprehensions for filtering.
- Write dictionary comprehensions.
- Understand when comprehensions improve readability versus when they do not.
- Transform and filter datasets using comprehensions.

## Introduction

List comprehensions are a compact, Pythonic way to create lists. Instead of writing a multi-line for loop that appends to a list, you express the same logic in a single line. They are one of Python's most distinctive features, and experienced Python developers use them constantly.

Dictionary comprehensions work the same way but produce dictionaries. Both are powerful tools for transforming and filtering data.

## Concepts

### Basic List Comprehension

```python
# Traditional loop
squares = []
for x in range(1, 6):
    squares.append(x ** 2)

# Comprehension — same result
squares = [x ** 2 for x in range(1, 6)]
# [1, 4, 9, 16, 25]
```

### Comprehension with Condition

```python
# Only include even numbers
evens = [x for x in range(1, 21) if x % 2 == 0]
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

### Comprehension with If/Else

```python
labels = ["even" if x % 2 == 0 else "odd" for x in range(1, 6)]
# ["odd", "even", "odd", "even", "odd"]
```

### Dictionary Comprehension

```python
# Square lookup table
squares = {x: x ** 2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### When Not to Use Comprehensions

If the logic is complex enough to hurt readability, use a regular loop. A comprehension should be understandable at a glance. Avoid nested comprehensions with multiple conditions.

## Practical Examples

```python
# Extracting data from a list of dicts
students = [
    {"name": "Amina", "score": 85},
    {"name": "Bashir", "score": 62},
    {"name": "Chioma", "score": 91},
    {"name": "Danjuma", "score": 45},
]

# Names of students who passed (score >= 50)
passed = [s["name"] for s in students if s["score"] >= 50]
print(passed)  # ["Amina", "Bashir", "Chioma"]
```

```python
# Transforming a list of prices from Naira to USD
prices_naira = [5000, 12000, 800, 35000, 2500]
rate = 1550
prices_usd = [round(p / rate, 2) for p in prices_naira]
print(prices_usd)  # [3.23, 7.74, 0.52, 22.58, 1.61]
```

```python
# Cleaning data: strip whitespace and lowercase
raw_names = ["  Amina ", "BASHIR", "  chioma  ", "Danjuma"]
clean_names = [name.strip().title() for name in raw_names]
print(clean_names)  # ["Amina", "Bashir", "Chioma", "Danjuma"]
```

```python
# Dictionary comprehension: word lengths
words = ["python", "engineering", "code", "build"]
lengths = {word: len(word) for word in words}
print(lengths)  # {"python": 6, "engineering": 11, "code": 4, "build": 5}
```

```python
# Inverting a dictionary
grades = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0}
inverted = {v: k for k, v in grades.items()}
print(inverted)  # {4.0: "A", 3.0: "B", 2.0: "C", 1.0: "D"}
```

```python
# Filtering a dictionary
inventory = {"rice": 50, "beans": 0, "oil": 12, "sugar": 0, "salt": 30}
in_stock = {item: qty for item, qty in inventory.items() if qty > 0}
print(in_stock)  # {"rice": 50, "oil": 12, "salt": 30}
```

## Guided Practice

Create a file called `data_transformer.py`:

1. Start with this list of student records:

```python
students = [
    {"name": "Hauwa", "math": 80, "english": 65, "science": 72},
    {"name": "Ibrahim", "math": 55, "english": 88, "science": 60},
    {"name": "Jummai", "math": 92, "english": 78, "science": 85},
    {"name": "Kabir", "math": 40, "english": 45, "science": 38},
    {"name": "Laraba", "math": 70, "english": 72, "science": 68},
]
```

2. Use comprehensions to:
   - Calculate each student's average: `[{**s, "average": ...} for s in students]`
   - Get names of students with average above 60.
   - Create a dictionary mapping names to their averages.
   - Find students who failed any subject (below 50).

## Daily Challenge

Build a program called `data_processor.py` that processes a dataset of products:

```python
products = [
    {"name": "Laptop", "price": 450000, "category": "Electronics", "stock": 5},
    {"name": "Phone", "price": 180000, "category": "Electronics", "stock": 0},
    {"name": "Shirt", "price": 5500, "category": "Clothing", "stock": 25},
    {"name": "Shoes", "price": 15000, "category": "Clothing", "stock": 8},
    {"name": "Rice 50kg", "price": 45000, "category": "Food", "stock": 100},
    {"name": "Headphones", "price": 12000, "category": "Electronics", "stock": 15},
    {"name": "Trousers", "price": 8000, "category": "Clothing", "stock": 0},
    {"name": "Cooking Oil", "price": 8500, "category": "Food", "stock": 60},
]
```

Use comprehensions to generate and display:

1. All product names in uppercase.
2. Products that are in stock (stock > 0).
3. Products grouped by category (a dictionary: `{category: [product_names]}`).
4. The most expensive product in each category.
5. Products with prices converted to USD (rate: 1550).
6. A discount price list: 20% off all electronics, 10% off clothing, no discount on food.

Display each result clearly with labels.

## Expected Output

Six labeled sections, each showing the result of a comprehension-based transformation on the product dataset.

## Assessment

1. Convert this loop to a list comprehension: `result = []; for x in range(10): if x % 3 == 0: result.append(x * 2)`
2. What is the difference between `[x for x in items if condition]` and `[x if condition else y for x in items]`?
3. When should you avoid using a comprehension?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-02/day-017/`

Your submission should include:
- `data_processor.py` containing your solution to the daily challenge.

## Additional Resources

- [Python Official Docs — List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [PEP 274 — Dict Comprehensions](https://peps.python.org/pep-0274/)

## Reflection

- How do comprehensions change the way you think about transforming data?
- Write a rule of thumb for when to use a comprehension versus a regular loop.
