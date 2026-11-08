# Day 074: Pandas Series and DataFrames

## Learning Objectives

- Understand the two core Pandas data structures: Series and DataFrame.
- Create DataFrames from dictionaries, lists, and CSV files.
- Explore a dataset using `.head()`, `.info()`, `.describe()`, and `.shape`.
- Select columns and filter rows using conditions.

## Introduction

Pandas is the most important library in the Python data science ecosystem. While NumPy works with raw numerical arrays, Pandas adds labeled rows and columns, making data manipulation intuitive and expressive. If NumPy is the engine, Pandas is the steering wheel.

A DataFrame is a table — rows and columns with labels, like a spreadsheet or a SQL table. Almost everything you do in data science starts with loading data into a DataFrame and then filtering, transforming, and summarizing it. The operations that took 10-15 lines of code with Python lists and dictionaries take one or two lines with Pandas.

Today you will learn to create DataFrames, explore their structure, and perform basic selection and filtering — the skills you will use in every data analysis from here on.

## Concepts

### Series

A one-dimensional labeled array. Think of it as a single column of data with an index:

```python
import pandas as pd

# From a list
scores = pd.Series([85, 72, 95, 60, 88], name="Math")

# From a dictionary (keys become the index)
populations = pd.Series({"Kano": 4_103_000, "Lagos": 9_113_000, "Abuja": 3_464_000})
```

### DataFrame

A two-dimensional labeled data structure — a table with rows and columns:

```python
# From a dictionary of lists
df = pd.DataFrame({
    "Name": ["Aisha", "Ibrahim", "Fatima"],
    "Age": [22, 25, 20],
    "Score": [88, 75, 92],
})
```

### Reading CSV Files

```python
df = pd.read_csv("data.csv")

# Common parameters
df = pd.read_csv("data.csv",
                  sep=",",          # delimiter (default comma)
                  header=0,         # which row is the header (0 = first)
                  index_col="id",   # use this column as row index
                  na_values=["N/A", "missing"])  # treat these as NaN
```

### Exploring a DataFrame

```python
df.head()       # First 5 rows
df.tail(3)      # Last 3 rows
df.shape        # (rows, columns)
df.columns      # Column names
df.dtypes       # Data type of each column
df.info()       # Summary: column names, types, non-null counts
df.describe()   # Statistics for numeric columns
```

### Selecting Columns

```python
# Single column (returns a Series)
names = df["Name"]

# Multiple columns (returns a DataFrame)
subset = df[["Name", "Score"]]
```

### Filtering Rows

```python
# Boolean condition
high_scorers = df[df["Score"] > 80]

# Multiple conditions (use & for AND, | for OR, wrap each in parentheses)
young_high = df[(df["Age"] < 25) & (df["Score"] > 80)]

# Using .query() for readability
result = df.query("Age < 25 and Score > 80")
```

### Sorting

```python
df.sort_values("Score", ascending=False)
df.sort_values(["Age", "Score"], ascending=[True, False])
```

## Practical Examples

### Creating and Exploring a DataFrame

```python
import pandas as pd

students = pd.DataFrame({
    "Name": ["Aisha", "Ibrahim", "Fatima", "Usman", "Halima",
             "Musa", "Zainab", "Yusuf", "Amina", "Suleiman"],
    "Age": [22, 25, 20, 23, 21, 24, 22, 26, 20, 23],
    "State": ["Kano", "Lagos", "Kano", "Kaduna", "Kano",
              "Lagos", "Abuja", "Kaduna", "Lagos", "Kano"],
    "Math": [85, 72, 95, 60, 88, 78, 91, 65, 82, 70],
    "English": [78, 88, 91, 55, 82, 75, 85, 70, 90, 68],
    "Science": [92, 65, 88, 70, 79, 82, 87, 75, 85, 72],
})

print(students.head())
print(f"\nShape: {students.shape}")
print(f"\nColumn types:\n{students.dtypes}")
print(f"\nStatistics:\n{students.describe()}")
```

### Column Operations

```python
# Add a new column
students["Total"] = students["Math"] + students["English"] + students["Science"]
students["Average"] = students["Total"] / 3

# Round values
students["Average"] = students["Average"].round(1)

print(students[["Name", "Total", "Average"]].head())
```

### Filtering and Sorting

```python
# Students from Kano
kano_students = students[students["State"] == "Kano"]
print(f"Students from Kano: {len(kano_students)}")

# Top 3 students by average
top_3 = students.sort_values("Average", ascending=False).head(3)
print("\nTop 3 students:")
print(top_3[["Name", "Average"]])

# Students who passed all subjects (>= 50) but failed at least one (< 70)
borderline = students[
    (students[["Math", "English", "Science"]].min(axis=1) >= 50) &
    (students[["Math", "English", "Science"]].min(axis=1) < 70)
]
print(f"\nBorderline students: {len(borderline)}")
```

### Reading from CSV

```python
# Create a sample CSV first
sample_data = """name,department,salary,years
Ali,Engineering,85000,5
Binta,Marketing,72000,3
Chidi,Engineering,92000,8
Danladi,Sales,68000,2
Esther,Marketing,78000,6
Faruk,Engineering,95000,10
Gambo,Sales,71000,4
Hauwa,Marketing,81000,7
"""

with open("employees.csv", "w") as f:
    f.write(sample_data)

# Read it back
emp = pd.read_csv("employees.csv")
print(emp.info())
print(emp.describe())
print(f"\nEngineering avg salary: {emp[emp['department'] == 'Engineering']['salary'].mean():,.0f}")
```

## Guided Practice

**Step 1:** Create a DataFrame of 8 Nigerian states with columns: state, population, area_km2, capital.

```python
import pandas as pd

states = pd.DataFrame({
    "state": ["Kano", "Lagos", "Kaduna", "Katsina", "Borno", "Sokoto", "Abuja", "Rivers"],
    "population": [13_999_000, 12_551_000, 8_252_000, 7_831_000, 5_860_000, 4_975_000, 3_464_000, 7_304_000],
    "area_km2": [20_131, 3_345, 46_053, 24_192, 69_435, 28_232, 7_315, 11_077],
    "capital": ["Kano", "Ikeja", "Kaduna", "Katsina", "Maiduguri", "Sokoto", "Abuja", "Port Harcourt"],
})
```

**Step 2:** Explore the DataFrame.

```python
print(states.head())
print(states.info())
print(states.describe())
```

**Step 3:** Add a population density column.

```python
states["density"] = (states["population"] / states["area_km2"]).round(0)
```

**Step 4:** Find the most and least dense states.

```python
most_dense = states.sort_values("density", ascending=False).iloc[0]
print(f"Most dense: {most_dense['state']} ({most_dense['density']:.0f} people/km2)")
```

**Step 5:** Filter states with population above 7 million.

```python
large_states = states[states["population"] > 7_000_000]
print(f"\nStates above 7M population: {len(large_states)}")
print(large_states[["state", "population"]])
```

## Daily Challenge

Create a script `pandas_exploration.py` that:

1. Creates a DataFrame of at least 12 products with columns: product_name, category, price, units_sold, rating (1-5).
2. Displays the first 5 rows and the DataFrame info.
3. Adds a "revenue" column (price * units_sold).
4. Finds and prints:
   - The most expensive product.
   - The product with the highest revenue.
   - The average rating per category.
   - Products with rating >= 4 and revenue > 10000.
5. Sorts by revenue (descending) and displays the top 5.
6. Saves the DataFrame to a CSV file called `products_analysis.csv`.

## Expected Output

A clear printout of each analysis step with labeled sections. The CSV file should be readable and well-formatted.

## Assessment

1. What is the difference between a Pandas Series and a DataFrame?
2. How do you filter rows where two conditions must both be true?
3. What does `df.describe()` show and why is it useful?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-08/day-074/`

Include your `pandas_exploration.py` file and the generated `products_analysis.csv`.

## Additional Resources

- [Pandas Getting Started](https://pandas.pydata.org/docs/getting_started/index.html)
- [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)

## Reflection

- How does working with Pandas compare to the dictionary-based analysis you did on Day 071?
- What operations that were complex with raw Python become simple with Pandas?
