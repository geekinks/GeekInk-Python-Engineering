# Day 071: Introduction to Data Science

## Learning Objectives

- Understand what data science is and how it differs from software engineering.
- Learn the data science workflow: collect, clean, analyze, visualize, communicate.
- Survey Python's data science ecosystem: NumPy, Pandas, Matplotlib, Scikit-learn.
- Identify real-world data science applications and the data they use.

## Introduction

Data science is the practice of extracting knowledge and insights from data. While software engineering focuses on building systems, data science focuses on understanding what the data those systems produce actually means. The two disciplines complement each other — engineers build the pipelines, data scientists interpret the results.

As a Python engineer, data science skills make you significantly more valuable. You can analyze user behavior, monitor system performance, build dashboards for stakeholders, and make data-driven decisions about what to build next. Companies in every industry — agriculture, healthcare, finance, education, logistics — need people who can turn raw data into actionable insights.

Python has become the dominant language for data science because of its ecosystem. Libraries like NumPy, Pandas, Matplotlib, and Scikit-learn provide powerful tools that would take thousands of lines to build from scratch. Over the next ten days, you will learn to use these tools to analyze real-world data.

## Concepts

### What Data Scientists Do

Data scientists answer questions with data. The questions can be descriptive ("What happened?"), diagnostic ("Why did it happen?"), predictive ("What will happen?"), or prescriptive ("What should we do?").

Examples:
- A school administrator asks: "Which subjects have the lowest pass rates this semester?"
- A business owner asks: "Which products sell best during Ramadan?"
- A health worker asks: "Which communities have the highest malaria incidence?"

### The Data Science Workflow

```
1. Define the Question
       |
2. Collect Data (databases, APIs, files, surveys)
       |
3. Clean Data (fix errors, handle missing values, standardize formats)
       |
4. Explore and Analyze (statistics, patterns, relationships)
       |
5. Visualize (charts, dashboards, reports)
       |
6. Communicate Findings (present to stakeholders)
```

Each step builds on the previous one. Skipping data cleaning leads to incorrect analysis. Poor visualization makes correct analysis unpersuasive.

### Python's Data Science Ecosystem

| Library | Purpose | You Will Learn |
|---------|---------|----------------|
| **NumPy** | Numerical computing with arrays | Day 073 |
| **Pandas** | Data manipulation and analysis | Days 074-076 |
| **Matplotlib** | Static charts and plots | Day 077 |
| **Seaborn** | Statistical visualizations | Day 078 |
| **Plotly** | Interactive charts | Day 079 |
| **Jupyter** | Interactive notebooks for analysis | Day 072 |
| **Scikit-learn** | Machine learning | Module 10 |

### Types of Data

- **Structured data**: Rows and columns (CSV files, database tables, spreadsheets).
- **Unstructured data**: Text, images, audio, video.
- **Time series data**: Data points indexed by time (stock prices, weather readings, sensor data).

Most data science begins with structured data in tabular form.

### Basic Statistics Review

| Measure | What It Tells You |
|---------|-------------------|
| **Mean** | The average value |
| **Median** | The middle value (less affected by outliers) |
| **Mode** | The most frequent value |
| **Standard deviation** | How spread out values are |
| **Min / Max** | The range of values |

```python
import statistics

scores = [78, 85, 92, 65, 88, 73, 95, 80, 70, 82]

print(f"Mean: {statistics.mean(scores)}")
print(f"Median: {statistics.median(scores)}")
print(f"Std Dev: {statistics.stdev(scores):.2f}")
print(f"Min: {min(scores)}, Max: {max(scores)}")
```

## Practical Examples

### Analyzing Data with Pure Python

Before learning specialized libraries, understand what they replace:

```python
# Student exam results
students = [
    {"name": "Aisha", "math": 85, "english": 78, "science": 92},
    {"name": "Ibrahim", "math": 72, "english": 88, "science": 65},
    {"name": "Fatima", "math": 95, "english": 91, "science": 88},
    {"name": "Usman", "math": 60, "english": 55, "science": 70},
    {"name": "Halima", "math": 88, "english": 82, "science": 79},
]

# Calculate average score per student
for s in students:
    avg = (s["math"] + s["english"] + s["science"]) / 3
    print(f"{s['name']}: {avg:.1f}")

# Find the highest scorer in math
best_math = max(students, key=lambda s: s["math"])
print(f"\nBest in Math: {best_math['name']} ({best_math['math']})")

# Calculate class average per subject
subjects = ["math", "english", "science"]
for subject in subjects:
    avg = sum(s[subject] for s in students) / len(students)
    print(f"Class avg {subject}: {avg:.1f}")
```

### Reading and Analyzing a CSV File

```python
import csv

# Assume we have a file: sales_data.csv
# product,category,units_sold,unit_price
# Rice,Grain,150,2500
# Beans,Grain,80,3500
# ...

def analyze_sales(filepath):
    with open(filepath, "r") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # Total revenue
    total_revenue = sum(int(r["units_sold"]) * float(r["unit_price"]) for r in rows)
    print(f"Total Revenue: N{total_revenue:,.0f}")

    # Revenue by category
    categories = {}
    for r in rows:
        cat = r["category"]
        revenue = int(r["units_sold"]) * float(r["unit_price"])
        categories[cat] = categories.get(cat, 0) + revenue

    print("\nRevenue by Category:")
    for cat, rev in sorted(categories.items(), key=lambda x: -x[1]):
        print(f"  {cat}: N{rev:,.0f}")

    # Best selling product
    best = max(rows, key=lambda r: int(r["units_sold"]))
    print(f"\nBest seller: {best['product']} ({best['units_sold']} units)")
```

### Simple Data Visualization with Built-in Tools

```python
# A text-based bar chart (before we learn Matplotlib)
data = {"Kano": 45, "Lagos": 38, "Abuja": 52, "Kaduna": 31, "Sokoto": 28}

max_val = max(data.values())
print("Enrollment by State")
print("-" * 40)
for state, count in sorted(data.items(), key=lambda x: -x[1]):
    bar = "#" * int(count / max_val * 30)
    print(f"{state:>8} | {bar} {count}")
```

## Guided Practice

Perform a simple analysis using only Python's standard library.

**Step 1:** Create a file called `weather_data.py`. Define a dataset:

```python
weather = [
    {"month": "Jan", "avg_temp": 25, "rainfall_mm": 0},
    {"month": "Feb", "avg_temp": 28, "rainfall_mm": 0},
    {"month": "Mar", "avg_temp": 33, "rainfall_mm": 2},
    {"month": "Apr", "avg_temp": 37, "rainfall_mm": 15},
    {"month": "May", "avg_temp": 38, "rainfall_mm": 65},
    {"month": "Jun", "avg_temp": 34, "rainfall_mm": 120},
    {"month": "Jul", "avg_temp": 30, "rainfall_mm": 210},
    {"month": "Aug", "avg_temp": 28, "rainfall_mm": 280},
    {"month": "Sep", "avg_temp": 30, "rainfall_mm": 180},
    {"month": "Oct", "avg_temp": 33, "rainfall_mm": 40},
    {"month": "Nov", "avg_temp": 29, "rainfall_mm": 0},
    {"month": "Dec", "avg_temp": 26, "rainfall_mm": 0},
]
```

**Step 2:** Calculate the average annual temperature.

**Step 3:** Find the hottest and coldest months.

**Step 4:** Calculate total annual rainfall.

**Step 5:** Identify the rainy season (months with rainfall > 50mm).

**Step 6:** Print a text-based chart of monthly rainfall.

## Daily Challenge

Write a Python script (`data_science_intro.py`) that:

1. Defines a dataset of at least 10 students with these fields: name, age, state, math_score, english_score, science_score.
2. Calculates and prints:
   - The overall class average across all subjects.
   - The highest and lowest scoring students (by total score).
   - The subject with the highest class average.
   - The number of students who scored above 75 in all three subjects.
3. Groups students by state and shows the average total score per state.
4. Prints a text-based horizontal bar chart of the average score per state.

Use only the Python standard library (no NumPy or Pandas yet).

## Expected Output

A terminal printout showing calculated statistics, grouped data, and a text-based visualization. The analysis should be clear and the output well-formatted.

## Assessment

1. What are the five stages of the data science workflow?
2. Name three Python libraries used in data science and describe what each does.
3. Why is data cleaning an important step before analysis?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-08/day-071/`

Include your `data_science_intro.py` file.

## Additional Resources

- [Python statistics Module](https://docs.python.org/3/library/statistics.html)
- [Python csv Module](https://docs.python.org/3/library/csv.html)

## Reflection

- Think of a problem in your community that could be better understood with data. What data would you need, and what questions would you ask?
- After doing analysis with pure Python, what operations felt tedious or repetitive? (This will motivate learning Pandas.)
