# Day 076: Data Transformation

## Learning Objectives

- Use GroupBy operations to aggregate data by categories.
- Apply aggregation functions: sum, mean, count, min, max.
- Merge and join DataFrames from multiple sources.
- Create pivot tables for multi-dimensional summaries.
- Use apply() and map() to transform column values.

## Introduction

Raw data rarely comes in the format you need for analysis. Data transformation is the process of reshaping, combining, and summarizing data into the form that answers your questions. If data cleaning fixes errors, data transformation restructures the data to reveal insights.

GroupBy is the single most important transformation operation. It splits data into groups based on a column's values, applies an aggregation function to each group, and combines the results. Merge and join operations combine data from multiple tables — essential when your data is spread across several files or database tables.

Today you will learn the transformation operations that take you from "I have clean data" to "I have answers."

## Concepts

### GroupBy

```python
# Group by one column and aggregate
df.groupby("category")["revenue"].sum()

# Group by multiple columns
df.groupby(["state", "category"])["revenue"].mean()

# Multiple aggregations
df.groupby("category").agg(
    total_revenue=("revenue", "sum"),
    avg_price=("price", "mean"),
    num_products=("product", "count"),
)
```

### Merging DataFrames

```python
# Inner join (only matching rows)
merged = pd.merge(orders, customers, on="customer_id")

# Left join (all rows from left, matching from right)
merged = pd.merge(orders, customers, on="customer_id", how="left")

# Join on different column names
merged = pd.merge(df1, df2, left_on="emp_id", right_on="employee_id")
```

### Pivot Tables

```python
# Rows = state, Columns = category, Values = revenue (sum)
pivot = df.pivot_table(values="revenue", index="state", columns="category", aggfunc="sum")
```

### apply() and map()

```python
# Apply a function to each row
df["grade"] = df["score"].apply(lambda x: "Pass" if x >= 50 else "Fail")

# Map values using a dictionary
df["level"] = df["year"].map({1: "Freshman", 2: "Sophomore", 3: "Junior", 4: "Senior"})

# Apply a function to each row (using axis=1)
df["full_name"] = df.apply(lambda row: f"{row['first']} {row['last']}", axis=1)
```

### Value Counts

```python
# Count occurrences of each unique value
df["category"].value_counts()

# As percentages
df["category"].value_counts(normalize=True)
```

## Practical Examples

### Sales Analysis with GroupBy

```python
import pandas as pd

sales = pd.DataFrame({
    "product": ["Rice", "Beans", "Rice", "Oil", "Beans", "Rice", "Oil", "Rice", "Beans", "Oil"],
    "region": ["North", "North", "South", "South", "South", "North", "North", "South", "North", "South"],
    "month": ["Jan", "Jan", "Jan", "Jan", "Feb", "Feb", "Feb", "Feb", "Mar", "Mar"],
    "units": [150, 80, 200, 60, 95, 180, 70, 210, 100, 75],
    "unit_price": [2500, 3500, 2500, 4500, 3500, 2500, 4500, 2500, 3500, 4500],
})

sales["revenue"] = sales["units"] * sales["unit_price"]

# Total revenue by product
print("Revenue by Product:")
print(sales.groupby("product")["revenue"].sum().sort_values(ascending=False))

# Average units sold by region
print("\nAvg Units by Region:")
print(sales.groupby("region")["units"].mean().round(0))

# Revenue by product and region
print("\nRevenue by Product and Region:")
print(sales.groupby(["product", "region"])["revenue"].sum())

# Multiple aggregations
summary = sales.groupby("product").agg(
    total_units=("units", "sum"),
    avg_price=("unit_price", "mean"),
    total_revenue=("revenue", "sum"),
    num_transactions=("units", "count"),
)
print("\nProduct Summary:")
print(summary)
```

### Merging Data from Multiple Sources

```python
import pandas as pd

# Students table
students = pd.DataFrame({
    "student_id": [1, 2, 3, 4, 5],
    "name": ["Aisha", "Ibrahim", "Fatima", "Usman", "Halima"],
    "department_id": [101, 102, 101, 103, 102],
})

# Departments table
departments = pd.DataFrame({
    "dept_id": [101, 102, 103, 104],
    "dept_name": ["Computer Science", "Engineering", "Mathematics", "Physics"],
})

# Scores table
scores = pd.DataFrame({
    "student_id": [1, 1, 2, 2, 3, 3, 4, 5, 5],
    "subject": ["Math", "English", "Math", "English", "Math", "English", "Math", "Math", "English"],
    "score": [85, 78, 72, 88, 95, 91, 60, 88, 82],
})

# Merge students with departments
student_dept = pd.merge(students, departments,
                         left_on="department_id", right_on="dept_id")
print("Students with Departments:")
print(student_dept[["name", "dept_name"]])

# Merge with scores
full_data = pd.merge(student_dept, scores, on="student_id")
print("\nFull Data:")
print(full_data[["name", "dept_name", "subject", "score"]])

# Average score per department
dept_avg = full_data.groupby("dept_name")["score"].mean().round(1)
print("\nAverage Score per Department:")
print(dept_avg)
```

### Pivot Tables

```python
import pandas as pd

sales = pd.DataFrame({
    "product": ["Rice", "Beans", "Oil"] * 4,
    "region": ["North"] * 3 + ["South"] * 3 + ["North"] * 3 + ["South"] * 3,
    "quarter": ["Q1"] * 6 + ["Q2"] * 6,
    "revenue": [375000, 280000, 270000, 500000, 332500, 337500,
                450000, 350000, 315000, 525000, 350000, 337500],
})

# Revenue by product and region
pivot = sales.pivot_table(values="revenue", index="product",
                           columns="region", aggfunc="sum")
print("Revenue Pivot (Product x Region):")
print(pivot)

# Add margins (totals)
pivot_with_totals = sales.pivot_table(values="revenue", index="product",
                                       columns="region", aggfunc="sum", margins=True)
print("\nWith Totals:")
print(pivot_with_totals)
```

## Guided Practice

**Step 1:** Create a dataset of employee records.

```python
import pandas as pd

employees = pd.DataFrame({
    "name": ["Ali", "Binta", "Chidi", "Danladi", "Esther", "Faruk",
             "Gambo", "Hauwa", "Isa", "Jamila"],
    "department": ["Engineering", "Marketing", "Engineering", "Sales",
                   "Marketing", "Engineering", "Sales", "Marketing",
                   "Engineering", "Sales"],
    "salary": [85000, 72000, 92000, 68000, 78000, 95000, 71000, 81000, 88000, 75000],
    "years": [5, 3, 8, 2, 6, 10, 4, 7, 6, 3],
})
```

**Step 2:** Group by department and calculate aggregates.

```python
dept_summary = employees.groupby("department").agg(
    headcount=("name", "count"),
    avg_salary=("salary", "mean"),
    total_salary=("salary", "sum"),
    avg_years=("years", "mean"),
)
print(dept_summary.round(0))
```

**Step 3:** Add a seniority level using apply.

```python
def get_seniority(years):
    if years <= 2:
        return "Junior"
    elif years <= 5:
        return "Mid"
    else:
        return "Senior"

employees["seniority"] = employees["years"].apply(get_seniority)
print(employees[["name", "years", "seniority"]])
```

**Step 4:** Create a pivot table of average salary by department and seniority.

```python
pivot = employees.pivot_table(values="salary", index="department",
                               columns="seniority", aggfunc="mean")
print(pivot.round(0))
```

## Daily Challenge

Create a script `data_transformation.py` that:

1. Creates two DataFrames:
   - `orders`: order_id, customer_id, product, quantity, unit_price, order_date
   - `customers`: customer_id, name, city, membership_level (Bronze/Silver/Gold)
   - Use at least 20 orders across 8 customers.

2. Merges the two DataFrames on customer_id.

3. Adds a "total_price" column (quantity * unit_price).

4. Performs and prints:
   - Total revenue per city.
   - Average order value per membership level.
   - Top 3 products by total revenue.
   - Number of orders per customer.
   - A pivot table showing total revenue by city and membership level.

5. Adds a "value_category" column using apply: orders above 10000 are "High", 5000-10000 are "Medium", below 5000 are "Low".

6. Shows the count of orders in each value category.

## Expected Output

Clear, labeled output for each analysis step. The pivot table should be formatted as a readable table.

## Assessment

1. What does `groupby()` do conceptually? Describe it in terms of split-apply-combine.
2. What is the difference between `pd.merge()` with `how="inner"` and `how="left"`?
3. When would you use a pivot table instead of a simple groupby?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-08/day-076/`

Include your `data_transformation.py` file.

## Additional Resources

- [Pandas GroupBy Guide](https://pandas.pydata.org/docs/user_guide/groupby.html)
- [Pandas Merge and Join](https://pandas.pydata.org/docs/user_guide/merging.html)

## Reflection

- Think of a real-world scenario where you would need to merge data from two different sources. What would the common key be?
- How do GroupBy operations relate to SQL's GROUP BY clause?
