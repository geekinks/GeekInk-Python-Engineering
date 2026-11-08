# Day 012: Tuples and Sets

## Learning Objectives

- Create and use tuples as immutable sequences.
- Understand when to use tuples instead of lists.
- Unpack tuples into individual variables.
- Create sets and perform set operations: union, intersection, difference.
- Understand the unique, unordered nature of sets.

## Introduction

Lists are flexible, but sometimes you need data that should not change after creation. Tuples serve that purpose: they are immutable sequences, meaning once created, their contents cannot be modified. This makes them useful for representing fixed data like coordinates, RGB colors, or database records.

Sets, on the other hand, are unordered collections of unique items. They are powerful tools for removing duplicates, checking membership quickly, and performing mathematical set operations like union and intersection.

## Concepts

### Tuples

A tuple is an ordered, immutable sequence:

```python
coordinates = (9.0579, 7.4951)   # Abuja coordinates
rgb_color = (255, 128, 0)
student_record = ("Halima", 300, 3.85)
```

Tuples use parentheses `()` but it is actually the commas that make a tuple:

```python
single_item = (42,)   # Note the trailing comma
not_a_tuple = (42)     # This is just the integer 42
```

### Tuple Unpacking

You can assign each element of a tuple to a separate variable:

```python
name, level, gpa = ("Halima", 300, 3.85)
print(name)   # Halima
print(level)  # 300
print(gpa)    # 3.85
```

### When to Use Tuples vs Lists

| Use a Tuple when...                    | Use a List when...                    |
| --------------------------------------- | -------------------------------------- |
| Data should not change (coordinates)    | Data will be modified (shopping list)  |
| Returning multiple values from function | Building a collection over time        |
| Dictionary keys (tuples are hashable)   | Need sorting, appending, removing      |

### Sets

A set is an unordered collection of unique elements:

```python
fruits = {"mango", "banana", "orange", "mango"}
print(fruits)  # {"mango", "banana", "orange"} — duplicates removed
```

### Set Operations

| Operation            | Method                 | Operator |
| -------------------- | ---------------------- | -------- |
| Union                | `a.union(b)`           | `a \| b` |
| Intersection         | `a.intersection(b)`    | `a & b`  |
| Difference           | `a.difference(b)`      | `a - b`  |
| Symmetric Difference | `a.symmetric_difference(b)` | `a ^ b` |

## Practical Examples

```python
# Tuple basics
states = ("Kano", "Lagos", "Rivers", "Kaduna", "Borno")
print(states[0])      # Kano
print(states[-1])     # Borno
print(len(states))    # 5
print("Lagos" in states)  # True

# Cannot modify
# states[0] = "Abuja"  # TypeError!
```

```python
# Tuple unpacking
student = ("Ibrahim Musa", "Computer Science", 3.92)
name, department, gpa = student
print(f"{name} studies {department} with a {gpa} GPA")

# Swap variables using tuple unpacking
a = 10
b = 20
a, b = b, a
print(a, b)  # 20, 10
```

```python
# Sets and uniqueness
raw_scores = [85, 92, 85, 78, 92, 90, 78, 85]
unique_scores = set(raw_scores)
print(unique_scores)        # {85, 78, 90, 92}
print(len(unique_scores))   # 4 unique scores
```

```python
# Set operations
frontend = {"HTML", "CSS", "JavaScript", "Python"}
backend = {"Python", "Java", "SQL", "Go"}

print(f"All skills: {frontend | backend}")
print(f"Shared: {frontend & backend}")           # {"Python"}
print(f"Frontend only: {frontend - backend}")     # {"HTML", "CSS", "JavaScript"}
print(f"Backend only: {backend - frontend}")      # {"Java", "SQL", "Go"}
print(f"Exclusive: {frontend ^ backend}")         # All except "Python"
```

```python
# Adding and removing from sets
skills = {"Python", "Git"}
skills.add("SQL")
skills.add("Python")  # No effect, already exists
print(skills)          # {"Python", "Git", "SQL"}

skills.discard("Git")
print(skills)          # {"Python", "SQL"}
```

## Guided Practice

Create a file called `student_courses.py`:

1. Create a tuple representing a student: `(name, matric_number, department)`.
2. Unpack the tuple and print each value.
3. Create two sets: courses the student registered for, and courses available this semester.
4. Find and print:
   - Courses the student is taking that are available.
   - Available courses the student has not registered for.
   - All unique courses mentioned.

```python
student = ("Zainab Abdullahi", "CSC/2023/045", "Computer Science")
name, matric, dept = student
print(f"Student: {name}")
print(f"Matric: {matric}")
print(f"Department: {dept}")

registered = {"CSC301", "CSC305", "MTH201", "GST301", "CSC311"}
available = {"CSC301", "CSC305", "CSC307", "CSC311", "CSC315", "MTH201", "GST301"}

taking = registered & available
print(f"\nRegistered and available: {taking}")

not_registered = available - registered
print(f"Available but not registered: {not_registered}")

all_courses = registered | available
print(f"All courses mentioned: {all_courses}")
```

## Daily Challenge

Build a program called `duplicate_finder.py` that:

1. Asks the user to enter items one at a time (press Enter with no input to stop).
2. Stores all items in a list.
3. Uses a set to find:
   - All unique items.
   - Items that appear more than once (duplicates).
   - How many times each duplicate appears.
4. Displays a report:

```
Enter items (empty line to stop):
> mango
> banana
> mango
> orange
> banana
> mango
> guava

===== DUPLICATE REPORT =====
Total items entered: 7
Unique items: 4

Duplicates found:
  mango    — appeared 3 times
  banana   — appeared 2 times

Items with no duplicates:
  orange
  guava
=============================
```

Hint: Use a combination of a list (to preserve all entries and count occurrences) and a set (to find unique items).

## Expected Output

A formatted report showing total items, unique count, duplicates with their counts, and items that appeared only once.

## Assessment

1. What happens if you try to modify a tuple after creating it?
2. If you add the same item to a set twice, how many copies does the set contain?
3. What is the result of `{1, 2, 3} & {2, 3, 4}`?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-02/day-012/`

Your submission should include:
- `duplicate_finder.py` containing your solution to the daily challenge.

## Additional Resources

- [Python Official Docs — Tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
- [Python Official Docs — Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)

## Reflection

- When would you use a tuple instead of a list in your own projects?
- How could set operations be useful when working with real data, such as comparing two class rosters?
