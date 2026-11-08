# Day 077: Matplotlib Fundamentals

## Learning Objectives

- Understand the Matplotlib Figure/Axes architecture.
- Create line plots, bar charts, scatter plots, and histograms.
- Customize charts with titles, labels, legends, colors, and grid lines.
- Save figures to image files.

## Introduction

Data visualization turns numbers into pictures that tell stories. A table of 1000 rows is hard to interpret, but a chart built from that same data can reveal trends, outliers, and patterns in seconds. Visualization is how data scientists communicate their findings to stakeholders who may not understand code or statistics.

Matplotlib is the foundational plotting library in Python. While newer libraries like Seaborn and Plotly offer higher-level interfaces, Matplotlib gives you full control over every element of a chart. Understanding Matplotlib is essential because Seaborn and Pandas plotting are built on top of it.

Today you will learn to create the four most common chart types and customize them to look professional and informative.

## Concepts

### Figure and Axes

Every Matplotlib chart has a Figure (the canvas) and one or more Axes (the individual plots):

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()          # One plot
fig, axes = plt.subplots(1, 2)    # Two plots side by side
fig, axes = plt.subplots(2, 2)    # Four plots in a grid
```

### The Two Plotting Interfaces

**pyplot interface** (quick plots):
```python
plt.plot(x, y)
plt.title("My Chart")
plt.show()
```

**Object-oriented interface** (recommended for anything beyond a quick plot):
```python
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("My Chart")
plt.show()
```

### Common Customization Options

```python
ax.set_title("Chart Title", fontsize=14)
ax.set_xlabel("X Axis Label")
ax.set_ylabel("Y Axis Label")
ax.legend()
ax.grid(True, linestyle="--", alpha=0.7)
fig.tight_layout()  # Prevent label overlap
```

### Saving Figures

```python
fig.savefig("chart.png", dpi=150, bbox_inches="tight")
```

## Practical Examples

### Line Plot

```python
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
temperatures = [25, 28, 33, 37, 38, 34, 30, 28, 30, 33, 29, 26]
rainfall = [0, 0, 2, 15, 65, 120, 210, 280, 180, 40, 0, 0]

fig, ax1 = plt.subplots(figsize=(10, 5))

ax1.plot(months, temperatures, color="#e74c3c", marker="o", linewidth=2, label="Temperature (C)")
ax1.set_xlabel("Month")
ax1.set_ylabel("Temperature (C)", color="#e74c3c")
ax1.tick_params(axis="y", labelcolor="#e74c3c")

ax2 = ax1.twinx()
ax2.bar(months, rainfall, alpha=0.3, color="#3498db", label="Rainfall (mm)")
ax2.set_ylabel("Rainfall (mm)", color="#3498db")
ax2.tick_params(axis="y", labelcolor="#3498db")

fig.suptitle("Monthly Weather Data - Northern Nigeria", fontsize=14)
fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.9))
fig.tight_layout()
plt.show()
```

### Bar Chart

```python
import matplotlib.pyplot as plt

departments = ["Computer Science", "Engineering", "Mathematics", "Physics", "Chemistry"]
enrollment = [245, 180, 120, 95, 110]
colors = ["#2ecc71", "#3498db", "#e74c3c", "#f39c12", "#9b59b6"]

fig, ax = plt.subplots(figsize=(8, 5))

bars = ax.bar(departments, enrollment, color=colors, edgecolor="white", linewidth=1.5)

for bar, value in zip(bars, enrollment):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5,
            str(value), ha="center", fontsize=11)

ax.set_title("Department Enrollment", fontsize=14, pad=15)
ax.set_ylabel("Number of Students")
ax.set_ylim(0, max(enrollment) + 30)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.xticks(rotation=15)
fig.tight_layout()
plt.show()
```

### Scatter Plot

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
hours_studied = np.random.uniform(1, 10, 30)
exam_scores = 40 + 5 * hours_studied + np.random.normal(0, 5, 30)
exam_scores = np.clip(exam_scores, 0, 100)

fig, ax = plt.subplots(figsize=(8, 5))

ax.scatter(hours_studied, exam_scores, c="#3498db", alpha=0.7, s=60, edgecolors="white")

z = np.polyfit(hours_studied, exam_scores, 1)
p = np.poly1d(z)
x_line = np.linspace(1, 10, 100)
ax.plot(x_line, p(x_line), "--", color="#e74c3c", linewidth=2, label="Trend line")

ax.set_title("Study Hours vs Exam Score", fontsize=14)
ax.set_xlabel("Hours Studied per Week")
ax.set_ylabel("Exam Score")
ax.legend()
ax.grid(True, linestyle="--", alpha=0.3)
fig.tight_layout()
plt.show()
```

### Histogram

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(7)
scores = np.random.normal(loc=65, scale=12, size=200)
scores = np.clip(scores, 0, 100)

fig, ax = plt.subplots(figsize=(8, 5))

n, bins, patches = ax.hist(scores, bins=15, color="#3498db", edgecolor="white",
                            alpha=0.8)

ax.axvline(scores.mean(), color="#e74c3c", linestyle="--", linewidth=2,
           label=f"Mean: {scores.mean():.1f}")
ax.axvline(np.median(scores), color="#2ecc71", linestyle="--", linewidth=2,
           label=f"Median: {np.median(scores):.1f}")

ax.set_title("Distribution of Exam Scores", fontsize=14)
ax.set_xlabel("Score")
ax.set_ylabel("Number of Students")
ax.legend()
fig.tight_layout()
plt.show()
```

### Multiple Subplots

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
categories = ["Rice", "Beans", "Oil", "Flour", "Sugar"]
values = [45000, 32000, 28000, 22000, 18000]
monthly_sales = np.random.randint(500, 2000, (12, 5))
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

fig, axes = plt.subplots(2, 2, figsize=(12, 9))

# Top left: Bar chart
axes[0, 0].bar(categories, values, color="#3498db")
axes[0, 0].set_title("Annual Revenue by Product")
axes[0, 0].set_ylabel("Revenue (Naira)")

# Top right: Line chart
for i, cat in enumerate(categories):
    axes[0, 1].plot(months, monthly_sales[:, i], marker=".", label=cat)
axes[0, 1].set_title("Monthly Sales Trend")
axes[0, 1].legend(fontsize=8)
axes[0, 1].tick_params(axis="x", rotation=45)

# Bottom left: Pie chart
axes[1, 0].pie(values, labels=categories, autopct="%1.0f%%", startangle=90)
axes[1, 0].set_title("Revenue Share")

# Bottom right: Histogram
all_sales = monthly_sales.flatten()
axes[1, 1].hist(all_sales, bins=12, color="#2ecc71", edgecolor="white")
axes[1, 1].set_title("Sales Distribution")
axes[1, 1].set_xlabel("Units Sold")

fig.suptitle("Sales Dashboard", fontsize=16, y=1.02)
fig.tight_layout()
plt.show()
```

## Guided Practice

Create a multi-chart analysis of student performance.

**Step 1:** Generate the data.

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)
subjects = ["Math", "English", "Science", "Hausa", "Social Studies"]
class_averages = [72, 78, 68, 82, 75]
student_scores = np.random.normal(loc=70, scale=12, size=50).clip(20, 100)
```

**Step 2:** Create a bar chart of class averages.

**Step 3:** Create a histogram of overall score distribution.

**Step 4:** Create a scatter plot comparing Math vs Science scores for 30 students.

**Step 5:** Arrange all three in a single figure with `subplots(1, 3)`.

**Step 6:** Save the figure as `student_analysis.png`.

## Daily Challenge

Create a script `matplotlib_charts.py` that produces a single figure with four charts from a dataset of your choice (e.g., sales data, weather data, school data):

1. A **line plot** showing a trend over time (at least 12 data points).
2. A **bar chart** comparing categories (at least 5 categories).
3. A **scatter plot** showing the relationship between two variables (at least 20 data points).
4. A **histogram** showing the distribution of a numeric variable (at least 50 data points).

Requirements:
- All charts must have titles, axis labels, and appropriate colors.
- At least one chart must have a legend.
- Use `subplots(2, 2)` for the layout.
- Add a main title with `suptitle()`.
- Save the figure as `dashboard.png` at 150 DPI.

## Expected Output

A saved PNG file (`dashboard.png`) containing four professional-looking charts arranged in a 2x2 grid. The charts should be readable, well-labeled, and visually consistent.

## Assessment

1. What is the difference between a Figure and an Axes in Matplotlib?
2. When would you use a histogram instead of a bar chart?
3. How do you add a trend line to a scatter plot?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-08/day-077/`

Include your `matplotlib_charts.py` file and the generated `dashboard.png`.

## Additional Resources

- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)

## Reflection

- Which chart type was most effective at communicating information from your dataset?
- How does the choice of chart type affect the story your data tells?
