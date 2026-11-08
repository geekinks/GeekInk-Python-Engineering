# Day 014: For Loops

## Learning Objectives

- Use `for` loops to iterate over lists, strings, tuples, and dictionaries.
- Use `range()` to generate numeric sequences.
- Use `enumerate()` to track index positions while iterating.
- Use `zip()` to iterate over multiple sequences in parallel.
- Apply for loops to solve repetitive computation problems.

## Introduction

Loops let your program repeat actions. Instead of writing the same code ten times, you write it once inside a loop and let Python run it as many times as needed. The `for` loop is Python's primary tool for iterating over sequences — lists, strings, ranges of numbers, dictionary items, and more.

Nearly every real program uses loops. Processing student records, generating reports, reading file lines, building menus — all of these require iteration. Mastering the `for` loop is essential.

## Concepts

### Basic For Loop

```python
for item in sequence:
    # Do something with item
```

Python takes each item from the sequence, one at a time, and executes the indented block.

### `range()` Function

`range()` generates a sequence of numbers:

```python
range(5)         # 0, 1, 2, 3, 4
range(1, 6)      # 1, 2, 3, 4, 5
range(0, 10, 2)  # 0, 2, 4, 6, 8
range(10, 0, -1) # 10, 9, 8, ..., 1
```

### `enumerate()` Function

Gives you both the index and the value:

```python
for index, item in enumerate(sequence):
    print(f"{index}: {item}")
```

### `zip()` Function

Iterates over two or more sequences in parallel:

```python
for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

## Practical Examples

```python
# Iterating over a list
cities = ["Kano", "Lagos", "Abuja", "Port Harcourt"]
for city in cities:
    print(f"Welcome to {city}!")
```

```python
# Using range for counting
for i in range(1, 6):
    print(f"Iteration {i}")
```

```python
# Summing a list of prices
prices = [2500, 1800, 3200, 950, 4100]
total = 0
for price in prices:
    total += price
print(f"Total: {total:,} Naira")  # Total: 12,550 Naira
```

```python
# enumerate for numbered output
students = ["Amina", "Bashir", "Chidinma", "Danjuma"]
for i, name in enumerate(students, start=1):
    print(f"{i}. {name}")
```

```python
# zip to combine parallel data
subjects = ["Math", "English", "Science"]
scores = [88, 72, 95]

for subject, score in zip(subjects, scores):
    grade = "A" if score >= 70 else "B" if score >= 60 else "C"
    print(f"{subject}: {score} ({grade})")
```

```python
# Iterating over a string
word = "Python"
for i, char in enumerate(word):
    print(f"Position {i}: '{char}'")
```

## Guided Practice

Create a file called `statistics.py`:

1. Create a list of 10 test scores.
2. Use a for loop to calculate:
   - The sum of all scores
   - The highest score
   - The lowest score
   - The average
   - How many scores are above average
3. Print a summary report.

```python
scores = [78, 92, 65, 88, 73, 95, 81, 70, 86, 90]

total = 0
highest = scores[0]
lowest = scores[0]

for score in scores:
    total += score
    if score > highest:
        highest = score
    if score < lowest:
        lowest = score

average = total / len(scores)

above_average = 0
for score in scores:
    if score > average:
        above_average += 1

print(f"Scores: {scores}")
print(f"Total:  {total}")
print(f"Average: {average:.1f}")
print(f"Highest: {highest}")
print(f"Lowest:  {lowest}")
print(f"Above average: {above_average} out of {len(scores)}")
```

## Daily Challenge

Build a program called `multiplication_table.py` that:

1. Asks the user for a number `n`.
2. Generates and displays the multiplication table for that number (1 through 12).
3. Then asks if they want a full multiplication grid (1-10 x 1-10).
4. If yes, display a formatted multiplication grid:

```
Enter a number: 7

Multiplication Table for 7:
  7 x  1 =   7
  7 x  2 =  14
  7 x  3 =  21
  ...
  7 x 12 =  84

Show full grid? (yes/no): yes

     1    2    3    4    5    6    7    8    9   10
  +-------------------------------------------------
1 |  1    2    3    4    5    6    7    8    9   10
2 |  2    4    6    8   10   12   14   16   18   20
3 |  3    6    9   12   15   18   21   24   27   30
...
```

Use nested formatting to align the grid columns.

## Expected Output

A single-number multiplication table (1-12) followed by an optional full 10x10 multiplication grid with aligned columns.

## Assessment

1. What is the difference between `range(5)` and `range(1, 6)`?
2. What does `enumerate()` return that a plain for loop does not?
3. What happens when you `zip()` two lists of different lengths?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-02/day-014/`

Your submission should include:
- `multiplication_table.py` containing your solution to the daily challenge.

## Additional Resources

- [Python Official Docs — for Statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements)
- [Python Official Docs — range()](https://docs.python.org/3/library/stdtypes.html#range)

## Reflection

- How do for loops reduce code repetition in your programs?
- When would you use `enumerate()` instead of a plain for loop?
