# Northern Nigeria Data Analysis Dashboard

**Module:** 8 — Data Science and Visualization
**Day:** 80
**Difficulty:** Advanced

---

## Problem Statement

Data-driven decision making requires the ability to collect, clean, analyze, and visualize data effectively. This project challenges students to perform a complete data analysis on a dataset relevant to Northern Nigeria — covering education, agriculture, population, health, or economic indicators — and present findings through static and interactive visualizations.

## Objectives

- Load, clean, and transform real-world data with Pandas.
- Perform statistical analysis and derive insights.
- Create publication-quality static visualizations with Matplotlib and Seaborn.
- Build interactive charts with Plotly.
- Present findings in a Jupyter notebook with narrative explanations.
- Practice ethical data handling and sourcing.

## Requirements

### Dataset

Students should use a publicly available, ethically sourced dataset. Suggested sources:

- Nigeria National Bureau of Statistics (NBS)
- World Bank Open Data
- UNICEF Data
- Kaggle (Nigerian datasets)
- Generated or synthesized sample data (clearly labeled as such)

The dataset must have at least 100 rows and 5 meaningful columns.

### Functional Requirements

1. **Data loading and exploration:**
   - Load data from CSV.
   - Display shape, data types, summary statistics.
   - Identify and document data quality issues.

2. **Data cleaning:**
   - Handle missing values with documented strategy.
   - Remove duplicates.
   - Fix data types and formatting issues.
   - Handle outliers.

3. **Analysis:**
   - At least 3 analytical questions answered with data.
   - Group-by analysis with aggregations.
   - Correlation analysis where applicable.
   - Trend analysis (if time-series data).

4. **Visualizations (minimum 6):**
   - At least 2 static charts (Matplotlib or Seaborn).
   - At least 2 interactive charts (Plotly).
   - Charts must have titles, labels, and legends.
   - At least one chart comparing multiple categories.

5. **Narrative:**
   - Jupyter notebook with markdown cells explaining each step.
   - Key findings summarized at the end.
   - Data source attribution.

## Technologies

- Python 3.10+
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly

## Suggested Architecture

```
data-analysis-dashboard/
├── analysis.ipynb      — Main Jupyter notebook
├── data/
│   ├── raw/            — Original dataset(s)
│   └── cleaned/        — Cleaned dataset(s)
├── figures/            — Saved chart images
└── README.md           — Project overview and findings summary
```

## Implementation Milestones

| Milestone | Description |
| :--- | :--- |
| 1. Data acquisition | Find and load a suitable dataset |
| 2. Exploration | Initial exploration with .head(), .info(), .describe() |
| 3. Cleaning | Handle missing values, duplicates, type issues |
| 4. Analysis | Answer 3+ analytical questions |
| 5. Static visuals | Create Matplotlib/Seaborn charts |
| 6. Interactive visuals | Create Plotly charts |
| 7. Narrative | Add markdown explanations and summary |

## Testing Requirements

- Verify cleaned data has no missing values in critical columns.
- Verify statistical calculations by spot-checking against manual calculations.
- Verify all charts render correctly in the notebook.
- Verify interactive charts respond to hover and zoom.

## Expected Deliverables

1. `analysis.ipynb` — Complete Jupyter notebook.
2. `data/` directory with raw and cleaned datasets.
3. `figures/` directory with saved chart images.
4. `README.md` summarizing the project and key findings.

## Evaluation Criteria

| Criterion | Weight | Description |
| :--- | :--- | :--- |
| Data handling | 20% | Cleaning is thorough and well-documented |
| Analysis depth | 25% | Questions are meaningful, analysis is sound |
| Visualization quality | 25% | Charts are clear, labeled, and informative |
| Narrative | 15% | Explanations are clear and findings are summarized |
| Code quality | 15% | Clean, organized, reproducible notebook |
