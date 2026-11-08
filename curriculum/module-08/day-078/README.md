# Day 078: Seaborn for Statistical Visualization

## Learning Objectives

- Understand how Seaborn builds on Matplotlib with a higher-level interface.
- Create distribution plots, categorical plots, and heatmaps.
- Use pair plots to explore relationships between multiple variables.
- Apply Seaborn styling and color palettes for professional charts.

## Introduction

Seaborn is a statistical visualization library built on top of Matplotlib. While Matplotlib gives you control over every pixel, Seaborn gives you charts that are statistically informative and visually polished with minimal code. A single Seaborn function call can produce a chart that would take 15-20 lines of Matplotlib.

Seaborn excels at showing distributions, relationships between variables, and comparisons across categories. It works seamlessly with Pandas DataFrames — you pass column names instead of raw arrays, and Seaborn handles the rest.

When you need to quickly explore a dataset and understand its statistical properties, Seaborn is the tool to reach for. When you need pixel-perfect customization, you drop down to Matplotlib.

## Concepts

### Seaborn vs Matplotlib

| Feature | Matplotlib | Seaborn |
|---------|-----------|---------|
| Level | Low-level | High-level |
| Input | Arrays | DataFrames (column names) |
| Defaults | Basic | Polished |
| Stat support | Manual | Built-in (regression, distributions) |
| Chart types | General | Statistical |

### Setting Style

```python
import seaborn as sns

sns.set_theme(style="whitegrid")  # Options: darkgrid, whitegrid, dark, white, ticks
sns.set_palette("husl")          # Color palette
```

### Distribution Plots

```python
# Histogram with KDE
sns.histplot(data=df, x="score", kde=True)

# KDE (Kernel Density Estimation) only
sns.kdeplot(data=df, x="score", hue="department")

# Box plot
sns.boxplot(data=df, x="department", y="score")

# Violin plot
sns.violinplot(data=df, x="department", y="score")
```

### Categorical Plots

```python
# Count plot (like a bar chart of value_counts)
sns.countplot(data=df, x="category")

# Bar plot with statistical estimation
sns.barplot(data=df, x="department", y="score", estimator="mean")

# Strip plot (individual points)
sns.stripplot(data=df, x="department", y="score", jitter=True)
```

### Relationship Plots

```python
# Scatter with regression line
sns.regplot(data=df, x="hours", y="score")

# Scatter colored by category
sns.scatterplot(data=df, x="hours", y="score", hue="department")

# Pair plot (all pairwise relationships)
sns.pairplot(df, hue="category")
```

### Heatmap

```python
# Correlation matrix
corr = df[["math", "english", "science"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", center=0)
```

## Practical Examples

### Distribution Analysis

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.seed(42)

df = pd.DataFrame({
    "department": np.random.choice(["CS", "Engineering", "Math"], 100),
    "score": np.random.normal(70, 12, 100).clip(20, 100).round(0),
    "hours_studied": np.random.uniform(2, 12, 100).round(1),
    "attendance": np.random.uniform(60, 100, 100).round(0),
})

sns.set_theme(style="whitegrid")

fig, axes = plt.subplots(2, 2, figsize=(12, 9))

# Histogram with KDE
sns.histplot(data=df, x="score", kde=True, bins=15, ax=axes[0, 0], color="#3498db")
axes[0, 0].set_title("Score Distribution")

# Box plot by department
sns.boxplot(data=df, x="department", y="score", ax=axes[0, 1], palette="Set2")
axes[0, 1].set_title("Scores by Department")

# Violin plot
sns.violinplot(data=df, x="department", y="hours_studied", ax=axes[1, 0], palette="muted")
axes[1, 0].set_title("Study Hours by Department")

# KDE by department
sns.kdeplot(data=df, x="score", hue="department", ax=axes[1, 1], fill=True, alpha=0.4)
axes[1, 1].set_title("Score Density by Department")

fig.suptitle("Student Performance Analysis", fontsize=14)
fig.tight_layout()
plt.show()
```

### Correlation Heatmap

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.seed(42)

df = pd.DataFrame({
    "math": np.random.normal(72, 10, 50),
    "english": np.random.normal(75, 12, 50),
    "science": np.random.normal(68, 11, 50),
    "attendance": np.random.uniform(60, 100, 50),
    "hours_studied": np.random.uniform(2, 10, 50),
})

# Add some realistic correlations
df["science"] = df["science"] + 0.5 * (df["math"] - 72)
df["english"] = df["english"] + 0.3 * (df["hours_studied"] - 6) * 3

corr = df.corr()

fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", center=0,
            square=True, linewidths=1, ax=ax)
ax.set_title("Variable Correlation Matrix", fontsize=14, pad=15)
fig.tight_layout()
plt.show()
```

### Pair Plot for Exploration

```python
import seaborn as sns
import pandas as pd
import numpy as np

np.random.seed(42)

df = pd.DataFrame({
    "math": np.random.normal(72, 10, 60),
    "english": np.random.normal(75, 12, 60),
    "science": np.random.normal(68, 11, 60),
    "level": np.random.choice(["100L", "200L", "300L"], 60),
})

g = sns.pairplot(df, hue="level", palette="Set2", diag_kind="kde",
                  plot_kws={"alpha": 0.6, "s": 40})
g.fig.suptitle("Pairwise Score Relationships", y=1.02)
plt.show()
```

### Categorical Comparison

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.seed(42)

data = []
for dept in ["CS", "Engineering", "Mathematics"]:
    for semester in ["First", "Second"]:
        n = 20
        scores = np.random.normal(70 + (5 if semester == "Second" else 0), 10, n)
        for s in scores:
            data.append({"department": dept, "semester": semester, "score": round(s)})

df = pd.DataFrame(data)

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

sns.barplot(data=df, x="department", y="score", hue="semester", ax=axes[0], palette="Set2")
axes[0].set_title("Average Score by Department")

sns.boxplot(data=df, x="department", y="score", hue="semester", ax=axes[1], palette="Set2")
axes[1].set_title("Score Distribution")

sns.stripplot(data=df, x="department", y="score", hue="semester", dodge=True,
              ax=axes[2], palette="Set2", alpha=0.6, size=4)
axes[2].set_title("Individual Scores")

fig.suptitle("Semester Performance Comparison", fontsize=14)
fig.tight_layout()
plt.show()
```

## Guided Practice

Create a statistical report using Seaborn.

**Step 1:** Create a DataFrame with 80 student records: name, department (4 departments), gpa, study_hours, attendance_pct.

**Step 2:** Create a histogram with KDE of GPA distribution.

**Step 3:** Create a box plot comparing GPA across departments.

**Step 4:** Create a scatter plot of study_hours vs gpa with a regression line.

**Step 5:** Create a correlation heatmap of the numeric columns.

**Step 6:** Arrange all four in a 2x2 grid and save as `student_report.png`.

## Daily Challenge

Create a script `seaborn_analysis.py` that produces a statistical visualization report:

1. Create or load a DataFrame with at least 100 rows and 5+ columns including both numeric and categorical data.
2. Create a figure with 6 subplots (2x3 or 3x2):
   - A histogram with KDE showing a distribution.
   - A box plot comparing a numeric variable across categories.
   - A violin plot for the same comparison.
   - A scatter plot with regression line showing a relationship.
   - A heatmap of correlations between numeric variables.
   - A count plot or bar plot showing category frequencies.
3. Apply a consistent Seaborn theme and color palette.
4. All charts must have titles and clean labels.
5. Save the figure as `statistical_report.png`.

## Expected Output

A saved PNG file with 6 professional statistical charts that together tell a story about the dataset.

## Assessment

1. What advantage does Seaborn's `hue` parameter provide?
2. When would you use a violin plot instead of a box plot?
3. What does a pair plot show and when is it most useful?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-08/day-078/`

Include your `seaborn_analysis.py` and `statistical_report.png`.

## Additional Resources

- [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)
- [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html)

## Reflection

- How does Seaborn's higher-level interface change your workflow compared to Matplotlib?
- Which chart type was most effective at revealing patterns in your data?
