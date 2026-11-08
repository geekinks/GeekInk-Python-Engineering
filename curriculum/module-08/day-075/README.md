# Day 075: Data Cleaning

## Learning Objectives

- Identify common data quality problems: missing values, duplicates, incorrect types, inconsistent formatting.
- Handle missing values with `isna()`, `fillna()`, and `dropna()`.
- Remove duplicate rows and fix data type issues.
- Clean string data: strip whitespace, standardize case, fix formatting.

## Introduction

Real-world data is messy. Surveys have missing answers. Databases have duplicate entries. Spreadsheets mix text and numbers in the same column. Dates appear in five different formats. Names are spelled inconsistently. If you analyze messy data, you get wrong answers — sometimes dangerously wrong.

Data cleaning is the process of detecting and correcting these problems before analysis. It is often called the least glamorous but most important step in data science. Studies consistently show that data scientists spend 60-80% of their time cleaning data. The good news is that Pandas makes many cleaning operations straightforward once you know the patterns.

Today you will learn the core data cleaning operations and practice them on a deliberately messy dataset.

## Concepts

### Common Data Quality Problems

| Problem | Example | Solution |
|---------|---------|----------|
| Missing values | Empty cells, NaN | `fillna()`, `dropna()` |
| Duplicates | Same record entered twice | `drop_duplicates()` |
| Wrong data types | Age stored as string "25" | `astype()`, `pd.to_numeric()` |
| Inconsistent text | "Kano", "kano", " Kano " | `.str.strip()`, `.str.title()` |
| Outliers | Age = 999 | Filtering, capping |
| Inconsistent formats | Dates as "01/03/2024" and "2024-03-01" | `pd.to_datetime()` |

### Detecting Missing Values

```python
df.isna()           # Boolean DataFrame: True where value is missing
df.isna().sum()     # Count of missing values per column
df.isna().sum().sum()  # Total missing values
df.info()           # Shows non-null count per column
```

### Handling Missing Values

```python
# Drop rows with any missing value
df.dropna()

# Drop rows where specific columns are missing
df.dropna(subset=["name", "email"])

# Fill missing values with a constant
df["score"].fillna(0)

# Fill with column mean
df["score"].fillna(df["score"].mean())

# Fill with the previous value (forward fill)
df["temperature"].ffill()
```

### Removing Duplicates

```python
# Check for duplicates
df.duplicated().sum()

# Remove exact duplicate rows
df.drop_duplicates()

# Remove duplicates based on specific columns
df.drop_duplicates(subset=["name", "email"], keep="first")
```

### Fixing Data Types

```python
# Convert to numeric (errors='coerce' turns invalid values to NaN)
df["price"] = pd.to_numeric(df["price"], errors="coerce")

# Convert to datetime
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Convert to integer
df["quantity"] = df["quantity"].astype(int)
```

### Cleaning String Data

```python
# Strip whitespace
df["name"] = df["name"].str.strip()

# Standardize case
df["city"] = df["city"].str.title()

# Replace values
df["status"] = df["status"].replace({"Y": "Yes", "N": "No"})

# Remove unwanted characters
df["phone"] = df["phone"].str.replace("-", "").str.replace(" ", "")
```

### Renaming Columns

```python
df.rename(columns={"old_name": "new_name", "Qty": "quantity"})
df.columns = df.columns.str.lower().str.replace(" ", "_")
```

## Practical Examples

### Cleaning a Messy Dataset

```python
import pandas as pd
import numpy as np

# Create a deliberately messy dataset
messy_data = pd.DataFrame({
    "Name": ["Aisha ", " Ibrahim", "Fatima", "USMAN", "halima", "Aisha ", np.nan, "Musa"],
    "Age": ["22", "25", "twenty", "23", "21", "22", "24", "26"],
    "City": ["kano", "Lagos", "KANO", " lagos", "Kano", "kano", "Abuja", "kaduna"],
    "Score": [85, np.nan, 95, 60, 88, 85, np.nan, 65],
    "Email": ["aisha@mail.com", "ibrahim@mail.com", "fatima@mail.com",
              "usman@mail.com", "halima@mail.com", "aisha@mail.com", "musa@mail.com", np.nan],
})

print("BEFORE CLEANING:")
print(messy_data)
print(f"\nShape: {messy_data.shape}")
print(f"Missing values:\n{messy_data.isna().sum()}")
print(f"Duplicates: {messy_data.duplicated().sum()}")

# Step 1: Clean string columns
messy_data["Name"] = messy_data["Name"].str.strip().str.title()
messy_data["City"] = messy_data["City"].str.strip().str.title()

# Step 2: Fix data types
messy_data["Age"] = pd.to_numeric(messy_data["Age"], errors="coerce")

# Step 3: Handle missing values
messy_data["Score"] = messy_data["Score"].fillna(messy_data["Score"].mean().round(0))
messy_data["Age"] = messy_data["Age"].fillna(messy_data["Age"].median())
messy_data = messy_data.dropna(subset=["Name"])  # Name is required

# Step 4: Remove duplicates
messy_data = messy_data.drop_duplicates(subset=["Name", "Email"], keep="first")

# Step 5: Reset index after dropping rows
messy_data = messy_data.reset_index(drop=True)

print("\n\nAFTER CLEANING:")
print(messy_data)
print(f"\nShape: {messy_data.shape}")
print(f"Missing values:\n{messy_data.isna().sum()}")
```

### Cleaning a CSV File

```python
import pandas as pd

# Create a messy CSV
csv_content = """product,category,price,quantity,date_added
Rice (5kg),grain,2500,100,2024-01-15
Beans,grain,N/A,50,15/01/2024
Rice (5kg),grain,2500,100,2024-01-15
 Garri ,grain,1200,,-
Palm Oil,oil,4500,30,2024-02-01
Groundnut Oil,oil,three thousand,25,2024-02-10
Sugar,,1800,45,2024-01-20
Salt,seasoning,500,200,
"""

with open("messy_products.csv", "w") as f:
    f.write(csv_content)

# Read and clean
df = pd.read_csv("messy_products.csv", na_values=["N/A", "-", ""])

print("Raw data:")
print(df)
print(f"\nInfo:")
df.info()

# Clean product names
df["product"] = df["product"].str.strip()

# Fix price column
df["price"] = pd.to_numeric(df["price"], errors="coerce")

# Fill missing category
df["category"] = df["category"].fillna("uncategorized")

# Fill missing quantity with 0
df["quantity"] = df["quantity"].fillna(0).astype(int)

# Parse dates
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce", dayfirst=True)

# Remove duplicates
df = df.drop_duplicates()

print("\nCleaned data:")
print(df)
```

## Guided Practice

**Step 1:** Create a messy student dataset.

```python
import pandas as pd
import numpy as np

data = {
    "student_name": [" Ali Musa", "Binta Yusuf", "ali musa", "Chidi Eze  ", np.nan,
                     "Danladi  Garba", "Esther Obi", "Faruk Ibrahim", "Binta Yusuf"],
    "registration_id": ["STU001", "STU002", "STU001", "STU003", "STU004",
                        "STU005", "STU006", "STU007", "STU002"],
    "department": ["CS", "cs", "CS", "Engineering", "Math", "CS", "engineering", "Math", "CS"],
    "gpa": [3.5, "3.8", 3.5, 2.9, np.nan, 3.2, 3.7, "N/A", 3.8],
    "year": [2, 1, 2, 3, 1, 4, 2, 3, 1],
}

df = pd.DataFrame(data)
print("Messy data:")
print(df)
```

**Step 2:** Clean it following the standard process.

```python
# Strip and standardize names
df["student_name"] = df["student_name"].str.strip().str.title()
df["department"] = df["department"].str.strip().str.title()

# Fix GPA
df["gpa"] = pd.to_numeric(df["gpa"], errors="coerce")
df["gpa"] = df["gpa"].fillna(df["gpa"].mean().round(2))

# Drop rows with missing name
df = df.dropna(subset=["student_name"])

# Remove duplicates by registration_id
df = df.drop_duplicates(subset=["registration_id"], keep="first")

df = df.reset_index(drop=True)
print("\nCleaned data:")
print(df)
```

## Daily Challenge

Create a file `data_cleaning.py` that:

1. Creates a messy DataFrame with at least 15 rows and 6 columns including:
   - At least 5 missing values spread across different columns.
   - At least 3 duplicate rows.
   - At least one column with mixed types (e.g., numbers and text in a numeric column).
   - Inconsistent string formatting (mixed case, extra whitespace).
   - At least one date column with inconsistent formats.

2. Prints a data quality report before cleaning:
   - Total rows and columns
   - Missing values per column
   - Duplicate count
   - Data types

3. Cleans the data step by step, printing a description of each step.

4. Prints the data quality report after cleaning showing all issues are resolved.

5. Saves the cleaned data to `cleaned_data.csv`.

## Expected Output

A clear before-and-after comparison showing the data quality improvement. Each cleaning step is described with what was fixed and how many rows/values were affected.

## Assessment

1. What is the difference between `dropna()` and `fillna()`? When would you use each?
2. Why is it important to handle missing values before performing calculations?
3. What does `errors="coerce"` do in `pd.to_numeric()`?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-08/day-075/`

Include your `data_cleaning.py` file and the generated `cleaned_data.csv`.

## Additional Resources

- [Pandas: Working with Missing Data](https://pandas.pydata.org/docs/user_guide/missing_data.html)
- [Pandas: Duplicated](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.duplicated.html)

## Reflection

- Why do you think data cleaning takes such a large portion of a data scientist's time?
- What strategies could you use to prevent messy data from being entered in the first place?
