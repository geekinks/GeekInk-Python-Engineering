# Day 079: Interactive Visualizations with Plotly

## Learning Objectives

- Understand the difference between static and interactive charts.
- Create interactive charts using Plotly Express.
- Add hover data, custom tooltips, and click interactions.
- Build multi-chart layouts with Plotly subplots.

## Introduction

Static charts (Matplotlib, Seaborn) are images — once generated, you cannot interact with them. Interactive charts let users hover over data points to see details, zoom into regions of interest, pan across large datasets, and toggle series visibility. They are especially useful for dashboards and presentations where the audience wants to explore the data themselves.

Plotly is the leading interactive visualization library for Python. Plotly Express provides a high-level interface that creates professional interactive charts in one or two lines of code, while Plotly Graph Objects gives fine-grained control when you need it.

Plotly charts render in the browser (as HTML and JavaScript), so they work in Jupyter Notebooks, can be saved as HTML files for sharing, and can be embedded in web applications.

## Concepts

### Plotly Express vs Graph Objects

**Plotly Express** (quick, high-level):
```python
import plotly.express as px
fig = px.scatter(df, x="hours", y="score", color="department")
fig.show()
```

**Plotly Graph Objects** (detailed control):
```python
import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Scatter(x=df["hours"], y=df["score"], mode="markers"))
fig.show()
```

### Common Plotly Express Charts

```python
import plotly.express as px

px.line(df, x="date", y="value")             # Line chart
px.bar(df, x="category", y="value")           # Bar chart
px.scatter(df, x="x", y="y")                  # Scatter plot
px.histogram(df, x="score")                   # Histogram
px.box(df, x="group", y="value")              # Box plot
px.pie(df, values="revenue", names="product") # Pie chart
px.sunburst(df, path=["region", "city"], values="pop")  # Sunburst
px.treemap(df, path=["region", "city"], values="pop")   # Treemap
```

### Hover and Tooltips

```python
fig = px.scatter(df, x="hours", y="score",
                  hover_data=["name", "department"],
                  hover_name="name")
```

### Updating Layout

```python
fig.update_layout(
    title="Chart Title",
    xaxis_title="X Axis",
    yaxis_title="Y Axis",
    template="plotly_white",  # Clean white theme
    height=500,
    width=800,
)
```

### Saving Charts

```python
# As interactive HTML
fig.write_html("chart.html")

# As static image (requires kaleido)
fig.write_image("chart.png")
```

## Practical Examples

### Interactive Scatter Plot

```python
import plotly.express as px
import pandas as pd
import numpy as np

np.random.seed(42)

df = pd.DataFrame({
    "student": [f"Student {i}" for i in range(1, 51)],
    "hours_studied": np.random.uniform(2, 12, 50).round(1),
    "score": np.random.normal(70, 12, 50).clip(20, 100).round(0),
    "department": np.random.choice(["CS", "Engineering", "Math", "Physics"], 50),
    "attendance": np.random.uniform(60, 100, 50).round(0),
})

fig = px.scatter(df, x="hours_studied", y="score",
                  color="department", size="attendance",
                  hover_name="student",
                  hover_data={"attendance": ":.0f", "hours_studied": ":.1f"},
                  title="Study Hours vs Exam Score",
                  labels={"hours_studied": "Hours Studied per Week",
                          "score": "Exam Score",
                          "attendance": "Attendance %"},
                  template="plotly_white")

fig.update_layout(height=500)
fig.show()
```

### Interactive Bar Chart with Grouping

```python
import plotly.express as px
import pandas as pd

data = {
    "state": ["Kano", "Lagos", "Abuja", "Kaduna", "Kano", "Lagos", "Abuja", "Kaduna"],
    "semester": ["First", "First", "First", "First", "Second", "Second", "Second", "Second"],
    "enrollment": [450, 380, 290, 310, 480, 420, 315, 340],
}
df = pd.DataFrame(data)

fig = px.bar(df, x="state", y="enrollment", color="semester",
              barmode="group", title="Student Enrollment by State and Semester",
              labels={"enrollment": "Number of Students"},
              template="plotly_white",
              color_discrete_sequence=["#3498db", "#2ecc71"])

fig.update_layout(height=450)
fig.show()
```

### Animated Chart

```python
import plotly.express as px
import pandas as pd
import numpy as np

np.random.seed(42)

records = []
for year in range(2020, 2025):
    for dept in ["CS", "Engineering", "Math"]:
        base = {"CS": 200, "Engineering": 150, "Math": 100}[dept]
        growth = (year - 2020) * np.random.randint(10, 30)
        records.append({"year": year, "department": dept, "enrollment": base + growth})

df = pd.DataFrame(records)

fig = px.bar(df, x="department", y="enrollment", color="department",
              animation_frame="year", range_y=[0, 400],
              title="Department Growth Over Time",
              template="plotly_white")
fig.show()
```

### Subplots with Plotly

```python
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

fig = make_subplots(rows=2, cols=2,
                     subplot_titles=("Temperature", "Rainfall",
                                     "Humidity", "Wind Speed"))

fig.add_trace(go.Scatter(x=months, y=[25, 28, 33, 37, 38, 34, 30, 28, 30, 33, 29, 26],
                          mode="lines+markers", name="Temp"),
              row=1, col=1)

fig.add_trace(go.Bar(x=months, y=[0, 0, 2, 15, 65, 120, 210, 280, 180, 40, 0, 0],
                      name="Rain", marker_color="#3498db"),
              row=1, col=2)

fig.add_trace(go.Scatter(x=months, y=[20, 18, 22, 35, 55, 70, 80, 85, 75, 45, 25, 20],
                          fill="tozeroy", name="Humidity"),
              row=2, col=1)

np.random.seed(42)
fig.add_trace(go.Scatter(x=months, y=np.random.uniform(5, 25, 12).round(1),
                          mode="lines+markers", name="Wind"),
              row=2, col=2)

fig.update_layout(height=600, title_text="Weather Dashboard", template="plotly_white")
fig.show()
```

### Saving as HTML

```python
# Any Plotly figure can be saved as a standalone HTML file
fig.write_html("weather_dashboard.html")
# Open the file in any browser to interact with the charts
```

## Guided Practice

**Step 1:** Create a DataFrame of monthly sales for 3 products over 12 months.

```python
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

np.random.seed(42)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

records = []
for month in months:
    for product in ["Rice", "Beans", "Oil"]:
        base = {"Rice": 1500, "Beans": 800, "Oil": 600}[product]
        units = base + np.random.randint(-200, 300)
        price = {"Rice": 2500, "Beans": 3500, "Oil": 4500}[product]
        records.append({"month": month, "product": product,
                        "units": units, "revenue": units * price})

df = pd.DataFrame(records)
```

**Step 2:** Create an interactive line chart of monthly units sold by product.

**Step 3:** Create a grouped bar chart of revenue by product and month.

**Step 4:** Save both charts to an HTML file.

## Daily Challenge

Create a script `plotly_dashboard.py` that builds an interactive dashboard:

1. Create or use a dataset with at least 50 rows and 5 columns (mix of numeric and categorical).
2. Build 4 interactive charts:
   - A scatter plot with color-coded categories and hover details.
   - A line chart showing a trend over time.
   - A bar chart comparing categories with grouped or stacked bars.
   - A pie or sunburst chart showing proportions.
3. Combine them into a single layout using `make_subplots`.
4. Apply a consistent theme (`template="plotly_white"`).
5. Save the dashboard as `interactive_dashboard.html`.

The HTML file should be shareable — anyone can open it in a browser and interact with the charts without installing Python.

## Expected Output

An `interactive_dashboard.html` file that opens in a browser showing four interactive charts. Users can hover for details, zoom, pan, and toggle series.

## Assessment

1. What advantage do interactive charts have over static charts?
2. How does Plotly Express differ from Plotly Graph Objects?
3. Why is saving a chart as HTML useful for sharing with non-technical stakeholders?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-08/day-079/`

Include your `plotly_dashboard.py` and `interactive_dashboard.html`.

## Additional Resources

- [Plotly Express Documentation](https://plotly.com/python/plotly-express/)
- [Plotly Subplots](https://plotly.com/python/subplots/)

## Reflection

- When would you choose Plotly over Matplotlib or Seaborn?
- How does interactivity change the way people engage with data?
