# Day 016: Nested Loops and Patterns

## Learning Objectives

- Write nested for loops and understand their execution order.
- Use nested loops to work with two-dimensional data.
- Generate text-based patterns using nested loops.
- Understand the relationship between outer and inner loop variables.
- Analyze the number of iterations in nested loop structures.

## Introduction

Sometimes a single loop is not enough. When you need to process rows and columns, compare every item in one list with every item in another, or generate structured patterns, you use nested loops — a loop inside a loop. The outer loop controls one dimension (rows), and the inner loop controls another (columns).

Nested loops are the foundation for working with grids, tables, matrices, and any two-dimensional structure.

## Concepts

### How Nested Loops Execute

For each iteration of the outer loop, the inner loop runs completely:

```python
for i in range(3):        # Outer: runs 3 times
    for j in range(4):    # Inner: runs 4 times per outer iteration
        print(f"({i},{j})", end=" ")
    print()  # New line after each row
```

This produces 3 rows of 4 items each (3 x 4 = 12 total iterations).

### Iteration Count

If the outer loop runs `m` times and the inner loop runs `n` times, the inner block executes `m * n` times total. Be aware that deeply nested loops with large ranges can be slow.

## Practical Examples

```python
# Right triangle
n = 5
for row in range(1, n + 1):
    print("* " * row)
```

Output:
```
*
* *
* * *
* * * *
* * * * *
```

```python
# Inverted triangle
n = 5
for row in range(n, 0, -1):
    print("* " * row)
```

```python
# Number pyramid
for row in range(1, 6):
    for col in range(1, row + 1):
        print(col, end=" ")
    print()
```

Output:
```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

```python
# Processing a 2D table
scores = [
    ["Amina", 85, 92, 78],
    ["Bashir", 90, 88, 95],
    ["Chioma", 72, 80, 85],
]

print(f"{'Name':<10} {'Math':>5} {'Eng':>5} {'Sci':>5} {'Avg':>6}")
print("-" * 35)

for row in scores:
    name = row[0]
    grades = row[1:]
    avg = sum(grades) / len(grades)
    print(f"{name:<10} {grades[0]:>5} {grades[1]:>5} {grades[2]:>5} {avg:>6.1f}")
```

```python
# Diamond pattern
n = 5
# Upper half
for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "* " * i
    print(spaces + stars)
# Lower half
for i in range(n - 1, 0, -1):
    spaces = " " * (n - i)
    stars = "* " * i
    print(spaces + stars)
```

## Guided Practice

Create a file called `grid_practice.py`:

1. Create a 5x5 grid of numbers where each cell contains `row * column`.
2. Print it as a formatted table with headers.

```python
size = 5

# Header row
print("    ", end="")
for col in range(1, size + 1):
    print(f"{col:>4}", end="")
print()
print("    " + "----" * size)

# Data rows
for row in range(1, size + 1):
    print(f"{row:>3} |", end="")
    for col in range(1, size + 1):
        print(f"{row * col:>4}", end="")
    print()
```

Output:
```
       1   2   3   4   5
    --------------------
  1 |   1   2   3   4   5
  2 |   2   4   6   8  10
  3 |   3   6   9  12  15
  4 |   4   8  12  16  20
  5 |   5  10  15  20  25
```

## Daily Challenge

Build a program called `pattern_printer.py` that:

1. Displays a menu of patterns:
   - 1: Right triangle
   - 2: Inverted triangle
   - 3: Centered pyramid
   - 4: Diamond
   - 5: Hollow rectangle
   - 6: Exit

2. Asks the user for the size (number of rows).

3. Prints the chosen pattern using `*` characters.

4. Loops back to the menu until the user chooses to exit.

Expected patterns for size 5:

**Right triangle:**
```
*
* *
* * *
* * * *
* * * * *
```

**Centered pyramid:**
```
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
```

**Diamond:**
```
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
```

**Hollow rectangle:**
```
* * * * *
*       *
*       *
*       *
* * * * *
```

## Expected Output

An interactive pattern printer that generates five different patterns at user-specified sizes, with a loop-back menu.

## Assessment

1. If an outer loop runs 10 times and an inner loop runs 10 times, how many times does the inner block execute?
2. How do you print output on the same line inside a loop?
3. What is the purpose of `print()` (with no arguments) after an inner loop?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-02/day-016/`

Your submission should include:
- `pattern_printer.py` containing your solution to the daily challenge.

## Additional Resources

- [Python Official Docs — for Statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [Python Official Docs — print()](https://docs.python.org/3/library/functions.html#print)

## Reflection

- What was the trickiest pattern to generate, and how did you figure out the logic?
- How do you determine the correct number of spaces and stars for each row in a centered pattern?
