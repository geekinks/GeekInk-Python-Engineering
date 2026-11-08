# Day 080: Module 8 Project -- Northern Nigeria Data Analysis Dashboard

## Learning Objectives

- Apply the full data science workflow to a real-world dataset.
- Perform data cleaning, transformation, and statistical analysis using Pandas.
- Create both static and interactive visualizations.
- Present findings in a Jupyter Notebook with narrative documentation.

## Introduction

This is the culminating project for Module 8. You will build a complete data analysis project focused on Northern Nigeria — using data related to education, agriculture, population, climate, or another topic relevant to the region.

This project brings together everything from the past ten days: data exploration, cleaning, transformation, Matplotlib and Seaborn static charts, and Plotly interactive visualizations. The deliverable is a Jupyter Notebook that serves as both the analysis and the report.

A strong project is not just technically correct — it tells a story. Start with a question, walk through the data, build toward insight, and end with a clear conclusion.

## Project Requirements

### Dataset

Choose one of these themes or propose your own:

1. **Education**: Student enrollment, exam performance, school distribution across states.
2. **Agriculture**: Crop production, rainfall patterns, farming seasons.
3. **Population**: State populations, growth rates, urbanization.
4. **Health**: Disease incidence, healthcare facility distribution.
5. **Economy**: Market prices, trade volumes, employment.

You may use publicly available data or create a realistic synthetic dataset. If creating synthetic data, it must be realistic — use reasonable ranges, correlations, and patterns that reflect actual conditions.

### Sample Dataset (Education Theme)

Create a CSV file `northern_nigeria_education.csv` with these columns:

- `state` (7 Northern states)
- `lga` (Local Government Area)
- `school_name`
- `school_type` (Primary / Secondary)
- `enrollment_male`
- `enrollment_female`
- `num_teachers`
- `num_classrooms`
- `pass_rate` (percentage)
- `year` (2020-2024)

Generate at least 100 rows of realistic data.

### Analysis Requirements

Your notebook must include:

1. **Introduction** (Markdown): What question are you investigating? Why does it matter?

2. **Data Loading and Exploration**:
   - Load the dataset.
   - Display the first rows, shape, info, and describe.
   - Identify data quality issues.

3. **Data Cleaning**:
   - Handle missing values.
   - Fix data types.
   - Address any inconsistencies.

4. **Data Transformation**:
   - Create derived columns (e.g., total enrollment, student-teacher ratio).
   - Group and aggregate data meaningfully.
   - Create at least one pivot table.

5. **Statistical Analysis**:
   - Summary statistics for key variables.
   - Correlation analysis between relevant variables.
   - At least one comparison across groups (states, years, school types).

6. **Visualization** (minimum 6 charts):
   - At least 2 static charts (Matplotlib or Seaborn).
   - At least 2 interactive charts (Plotly).
   - A correlation heatmap.
   - A distribution plot.
   - Each chart must have a title, labels, and a caption explaining what it shows.

7. **Findings** (Markdown): What patterns did you discover? What are the key insights?

8. **Conclusions and Recommendations** (Markdown): Based on your analysis, what actions would you recommend?

## Starter Code

### Generating a Synthetic Dataset

```python
import pandas as pd
import numpy as np

np.random.seed(42)

states = ["Kano", "Kaduna", "Katsina", "Sokoto", "Borno", "Bauchi", "Jigawa"]
school_types = ["Primary", "Secondary"]
years = [2020, 2021, 2022, 2023, 2024]

records = []
for state in states:
    num_lgas = np.random.randint(8, 15)
    for lga_num in range(num_lgas):
        lga_name = f"{state}_LGA_{lga_num + 1}"
        num_schools = np.random.randint(3, 8)
        for school_num in range(num_schools):
            school_type = np.random.choice(school_types, p=[0.6, 0.4])
            school_name = f"{lga_name}_{school_type[:3]}_{school_num + 1}"
            for year in years:
                base_male = np.random.randint(80, 400) if school_type == "Primary" else np.random.randint(60, 300)
                base_female = int(base_male * np.random.uniform(0.6, 1.0))
                growth = (year - 2020) * np.random.randint(0, 15)

                records.append({
                    "state": state,
                    "lga": lga_name,
                    "school_name": school_name,
                    "school_type": school_type,
                    "enrollment_male": base_male + growth,
                    "enrollment_female": base_female + growth,
                    "num_teachers": np.random.randint(5, 30),
                    "num_classrooms": np.random.randint(4, 20),
                    "pass_rate": np.random.uniform(35, 95).round(1),
                    "year": year,
                })

# Introduce some missing values for cleaning practice
df = pd.DataFrame(records)
mask = np.random.random(len(df)) < 0.05
df.loc[mask, "pass_rate"] = np.nan
mask2 = np.random.random(len(df)) < 0.03
df.loc[mask2, "num_teachers"] = np.nan

df.to_csv("northern_nigeria_education.csv", index=False)
print(f"Dataset created: {len(df)} rows, {len(df.columns)} columns")
print(df.head())
```

### Notebook Starter

Start your `analysis.ipynb` notebook with:

```markdown
# Northern Nigeria Education Data Analysis

## Introduction

[Your introduction here: What question are you investigating?]

## Setup
```

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

sns.set_theme(style="whitegrid")

df = pd.read_csv("northern_nigeria_education.csv")
print(f"Dataset: {df.shape[0]} rows, {df.shape[1]} columns")
df.head()
```

## Implementation Milestones

1. **Dataset creation**: Generate and save the CSV. Verify it loads correctly.
2. **Exploration**: Display head, info, describe. Identify issues.
3. **Cleaning**: Handle missing values. Verify no issues remain.
4. **Feature engineering**: Create total_enrollment, student_teacher_ratio, gender_parity_index.
5. **Analysis**: Group by state, year, school_type. Create pivot tables. Calculate correlations.
6. **Static visualizations**: Create Matplotlib/Seaborn charts with clear titles.
7. **Interactive visualizations**: Create Plotly charts with hover details.
8. **Narrative**: Write clear Markdown cells explaining each step and each finding.
9. **Conclusions**: Summarize findings and recommendations.

## Evaluation Criteria

| Criteria | Weight | Description |
|----------|--------|-------------|
| Data handling | 25% | Cleaning, transformation, feature engineering |
| Analysis depth | 25% | Statistical rigor, meaningful aggregations |
| Visualizations | 25% | Quality, variety, informativeness of charts |
| Narrative | 15% | Clear explanation, logical flow, actionable conclusions |
| Code quality | 10% | Clean, readable, well-organized code |

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-08/day-080/`

Include:
- `generate_data.py` (dataset generation script)
- `northern_nigeria_education.csv` (the dataset)
- `analysis.ipynb` (your Jupyter Notebook)

## Additional Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Plotly for Python](https://plotly.com/python/)
- [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html)

## Reflection

- What surprised you most about the data you analyzed?
- How could this kind of analysis be used to improve education policy in Northern Nigeria?
- What additional data would make this analysis more powerful?
