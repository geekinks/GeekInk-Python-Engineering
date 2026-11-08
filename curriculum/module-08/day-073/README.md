# Day 073: NumPy Fundamentals

## Learning Objectives

- Understand the difference between Python lists and NumPy arrays.
- Create arrays using various methods.
- Perform element-wise operations and basic linear algebra.
- Use indexing, slicing, and reshaping.
- Calculate basic statistics with NumPy functions.

## Introduction

NumPy (Numerical Python) is the foundation of Python's data science stack. Every major data science library — Pandas, Matplotlib, Scikit-learn — is built on top of NumPy. Its core contribution is the `ndarray` (n-dimensional array), a data structure that stores numbers far more efficiently than Python lists and supports fast mathematical operations on entire arrays at once.

Why does this matter? When you write `[x * 2 for x in my_list]`, Python loops through each element one at a time. When you write `my_array * 2`, NumPy applies the operation to all elements simultaneously using optimized C code. For datasets with millions of rows, this difference is the difference between seconds and minutes.

Learning NumPy gives you the vocabulary and mental model for working with numerical data. The concepts you learn today — arrays, broadcasting, vectorized operations — appear everywhere in data science and machine learning.

## Concepts

### Arrays vs Lists

| Feature | Python List | NumPy Array |
|---------|------------|-------------|
| Data types | Mixed (`[1, "two", 3.0]`) | Homogeneous (all same type) |
| Speed | Slow for math | Fast (C-optimized) |
| Operations | Element-by-element loop | Vectorized (whole-array) |
| Memory | Higher overhead per element | Compact storage |
| Dimensions | Nested lists for 2D | True multi-dimensional |

### Creating Arrays

```python
import numpy as np

# From a list
a = np.array([1, 2, 3, 4, 5])

# 2D array from nested lists
matrix = np.array([[1, 2, 3], [4, 5, 6]])

# Zeros and ones
zeros = np.zeros((3, 4))       # 3 rows, 4 columns of zeros
ones = np.ones((2, 3))         # 2 rows, 3 columns of ones

# Range of numbers
sequence = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]

# Evenly spaced numbers
linear = np.linspace(0, 1, 5)   # [0.0, 0.25, 0.5, 0.75, 1.0]

# Random numbers
random_arr = np.random.rand(3, 3)      # 3x3 uniform random [0,1)
random_int = np.random.randint(1, 100, size=10)  # 10 random ints
```

### Array Properties

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

arr.shape    # (2, 3) — 2 rows, 3 columns
arr.ndim     # 2 — number of dimensions
arr.size     # 6 — total elements
arr.dtype    # int64 — data type
```

### Vectorized Operations

```python
a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

a + b     # [11, 22, 33, 44]
a * b     # [10, 40, 90, 160]
a ** 2    # [100, 400, 900, 1600]
a > 25    # [False, False, True, True]
```

### Indexing and Slicing

```python
arr = np.array([10, 20, 30, 40, 50])

arr[0]        # 10
arr[-1]       # 50
arr[1:4]      # [20, 30, 40]
arr[arr > 25] # [30, 40, 50] — boolean indexing

# 2D indexing
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix[0, 1]    # 2 (row 0, column 1)
matrix[:, 0]    # [1, 4, 7] — all rows, column 0
matrix[1, :]    # [4, 5, 6] — row 1, all columns
```

### Reshaping

```python
arr = np.arange(12)          # [0, 1, 2, ..., 11]
matrix = arr.reshape(3, 4)   # 3 rows, 4 columns
flat = matrix.flatten()       # Back to 1D
transposed = matrix.T         # Swap rows and columns
```

## Practical Examples

### Student Exam Score Analysis

```python
import numpy as np

# 10 students, 3 subjects (Math, English, Science)
scores = np.array([
    [85, 78, 92],
    [72, 88, 65],
    [95, 91, 88],
    [60, 55, 70],
    [88, 82, 79],
    [78, 75, 82],
    [91, 85, 87],
    [65, 70, 75],
    [82, 90, 85],
    [70, 68, 72],
])

subjects = ["Math", "English", "Science"]

# Average per subject (column-wise)
subject_avgs = scores.mean(axis=0)
for subject, avg in zip(subjects, subject_avgs):
    print(f"{subject}: {avg:.1f}")

# Average per student (row-wise)
student_avgs = scores.mean(axis=1)
print(f"\nHighest student avg: {student_avgs.max():.1f}")
print(f"Lowest student avg: {student_avgs.min():.1f}")

# Students scoring above 80 in all subjects
all_above_80 = np.all(scores > 80, axis=1)
print(f"\nStudents above 80 in all subjects: {all_above_80.sum()}")

# Standard deviation per subject
for subject, std in zip(subjects, scores.std(axis=0)):
    print(f"{subject} std dev: {std:.2f}")
```

### Working with Random Data

```python
import numpy as np

np.random.seed(42)

# Simulate daily temperatures for 30 days (Celsius)
temperatures = np.random.normal(loc=32, scale=4, size=30)

print(f"Mean temperature: {temperatures.mean():.1f}C")
print(f"Max: {temperatures.max():.1f}C, Min: {temperatures.min():.1f}C")
print(f"Days above 35C: {(temperatures > 35).sum()}")
print(f"Days below 28C: {(temperatures < 28).sum()}")

# 7-day moving average
moving_avg = np.convolve(temperatures, np.ones(7)/7, mode="valid")
print(f"\n7-day moving averages (first 5): {moving_avg[:5].round(1)}")
```

### Matrix Operations

```python
import numpy as np

# Sales data: 4 products, 3 months
sales = np.array([
    [150, 200, 180],  # Product A
    [80, 95, 110],    # Product B
    [220, 190, 250],  # Product C
    [60, 70, 55],     # Product D
])

prices = np.array([2500, 3500, 1800, 5000])

# Revenue per product per month
revenue = sales * prices.reshape(-1, 1)  # Broadcasting
print("Revenue matrix:")
print(revenue)

# Total revenue per month
monthly_total = revenue.sum(axis=0)
print(f"\nMonthly totals: {monthly_total}")

# Total revenue per product
product_total = revenue.sum(axis=1)
print(f"Product totals: {product_total}")
```

## Guided Practice

**Step 1:** Create an array of 20 random exam scores between 40 and 100.

```python
import numpy as np
np.random.seed(7)
scores = np.random.randint(40, 101, size=20)
print("Scores:", scores)
```

**Step 2:** Calculate the mean, median, standard deviation, min, and max.

```python
print(f"Mean: {scores.mean():.1f}")
print(f"Median: {np.median(scores):.1f}")
print(f"Std Dev: {scores.std():.1f}")
print(f"Min: {scores.min()}, Max: {scores.max()}")
```

**Step 3:** Find how many students passed (score >= 50) and how many scored an A (>= 80).

```python
passed = (scores >= 50).sum()
grade_a = (scores >= 80).sum()
print(f"Passed: {passed}/{len(scores)}")
print(f"Grade A: {grade_a}/{len(scores)}")
```

**Step 4:** Replace all failing scores (< 50) with 50 (minimum passing mark).

```python
adjusted = scores.copy()
adjusted[adjusted < 50] = 50
print(f"Adjusted scores: {adjusted}")
print(f"New mean: {adjusted.mean():.1f}")
```

## Daily Challenge

Write a Python script `numpy_analysis.py` that uses NumPy to analyze student exam scores:

1. Create a 2D NumPy array representing 15 students and 4 subjects (Math, English, Science, Hausa). Use random scores between 30 and 100.
2. Calculate and print:
   - The class average for each subject.
   - The overall average across all subjects.
   - The student with the highest total score (print their index and total).
   - The subject with the widest spread of scores (highest standard deviation).
3. Create a boolean array showing which students passed all subjects (>= 50).
4. Calculate the percentage of students who passed all subjects.
5. Find the correlation between Math and Science scores using `np.corrcoef()`.
6. Reshape the array into a different valid shape and print both shapes.

## Expected Output

Terminal output showing all calculated statistics with clear labels. The analysis should demonstrate proficiency with array operations, boolean indexing, and statistical functions.

## Assessment

1. Why are NumPy arrays faster than Python lists for numerical computations?
2. What does `axis=0` mean in `array.mean(axis=0)` for a 2D array?
3. How does boolean indexing work? Give an example of filtering an array.

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-08/day-073/`

Include your `numpy_analysis.py` file.

## Additional Resources

- [NumPy User Guide](https://numpy.org/doc/stable/user/index.html)
- [NumPy Quickstart Tutorial](https://numpy.org/doc/stable/user/quickstart.html)

## Reflection

- How does thinking in terms of array operations (vectorized) differ from thinking in terms of loops?
- Where else in your programming experience could NumPy arrays replace manual loops?
