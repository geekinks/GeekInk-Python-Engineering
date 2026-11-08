# Day 072: Jupyter Notebooks

## Learning Objectives

- Understand what Jupyter Notebooks are and why they are used in data science.
- Install and launch Jupyter Notebook.
- Work with code cells and markdown cells.
- Document an analysis using a mixture of code, output, and explanatory text.

## Introduction

Jupyter Notebooks are interactive documents that combine code, output, and narrative text in a single file. Unlike a `.py` script where you write everything, run it, and see the output in a terminal, a Jupyter Notebook lets you run code in small chunks (cells) and see the output immediately below each chunk.

This format is ideal for data science because data exploration is iterative. You load a dataset, look at the first few rows, decide to filter it, visualize a column, notice something interesting, and investigate further. Each step builds on the last, and seeing the output inline keeps the flow natural.

Notebooks are also excellent for communication. A notebook that mixes code with markdown explanations, charts, and conclusions can serve as both the analysis and the report — your stakeholders can read the narrative and see the evidence alongside it.

## Concepts

### What Is a Jupyter Notebook?

A `.ipynb` file (IPython Notebook) containing an ordered list of cells. Each cell is either:

- **Code cell**: Contains Python code. When you run it, the output appears directly below.
- **Markdown cell**: Contains formatted text using Markdown syntax (headings, lists, bold, links, images).
- **Raw cell**: Unformatted text (rarely used).

### Installing Jupyter

```bash
pip install jupyter
```

Or with the project requirements:

```bash
pip install -r requirements.txt  # jupyter is listed
```

### Launching Jupyter

```bash
jupyter notebook
```

This starts a local server and opens your browser. Navigate to a folder and click "New > Python 3" to create a notebook.

Alternatively, VS Code has built-in Jupyter support — open a `.ipynb` file and VS Code provides the notebook interface.

### Essential Keyboard Shortcuts

In **command mode** (press `Esc` to enter):

| Shortcut | Action |
|----------|--------|
| `A`      | Insert cell above |
| `B`      | Insert cell below |
| `D D`    | Delete current cell |
| `M`      | Convert cell to Markdown |
| `Y`      | Convert cell to code |
| `Enter`  | Enter edit mode |

In **edit mode** (press `Enter` to enter):

| Shortcut | Action |
|----------|--------|
| `Shift+Enter` | Run cell and move to next |
| `Ctrl+Enter`  | Run cell and stay |
| `Tab`          | Code completion |
| `Shift+Tab`    | Show documentation |

### Markdown in Notebooks

```markdown
# Heading 1
## Heading 2
### Heading 3

**Bold text** and *italic text*

- Bullet list item
- Another item

1. Numbered list
2. Second item

`inline code`

[Link text](https://example.com)

| Column A | Column B |
|----------|----------|
| Value 1  | Value 2  |
```

## Practical Examples

### A Data Exploration Notebook

Create a notebook with the following cells (each code block represents a separate cell):

**Cell 1 (Markdown):**
```markdown
# Student Performance Analysis
Analyzing exam scores for 10 students across three subjects.
```

**Cell 2 (Code):**
```python
# Define the dataset
students = {
    "Name": ["Aisha", "Ibrahim", "Fatima", "Usman", "Halima",
             "Musa", "Zainab", "Yusuf", "Amina", "Suleiman"],
    "Math": [85, 72, 95, 60, 88, 78, 91, 65, 82, 70],
    "English": [78, 88, 91, 55, 82, 75, 85, 70, 90, 68],
    "Science": [92, 65, 88, 70, 79, 82, 87, 75, 85, 72],
}
print(f"Number of students: {len(students['Name'])}")
```

**Cell 3 (Code):**
```python
# Calculate averages
for i, name in enumerate(students["Name"]):
    avg = (students["Math"][i] + students["English"][i] + students["Science"][i]) / 3
    print(f"{name}: {avg:.1f}")
```

**Cell 4 (Markdown):**
```markdown
## Subject Averages
Let's see which subject the class performed best in.
```

**Cell 5 (Code):**
```python
for subject in ["Math", "English", "Science"]:
    avg = sum(students[subject]) / len(students[subject])
    print(f"{subject}: {avg:.1f}")
```

**Cell 6 (Markdown):**
```markdown
## Findings
- Science has the highest average
- The range of math scores is the widest, suggesting uneven preparation
```

### Using Magic Commands

Jupyter provides special commands prefixed with `%` or `%%`:

```python
# Time how long a cell takes to run
%timeit sum(range(1000000))

# Show all variables in the current namespace
%who

# Run an external Python script
%run my_script.py

# Write cell contents to a file
%%writefile output.py
print("This was written from a notebook cell")
```

### Rich Output

Notebooks can display more than just text:

```python
# Display an image (if PIL/Pillow is installed)
from IPython.display import Image, display, HTML

# Display formatted HTML
display(HTML("<h3 style='color: green;'>Analysis Complete</h3>"))

# Display a formatted table using HTML
html_table = """
<table>
<tr><th>Subject</th><th>Average</th></tr>
<tr><td>Math</td><td>78.6</td></tr>
<tr><td>English</td><td>78.2</td></tr>
<tr><td>Science</td><td>79.5</td></tr>
</table>
"""
display(HTML(html_table))
```

## Guided Practice

Create a Jupyter Notebook called `exploration.ipynb` that tells a story with data.

**Step 1:** Create a new notebook. Add a Markdown cell with a title and description of what you are analyzing.

**Step 2:** In a code cell, define a dataset about 5 cities (name, population, area_km2, number_of_schools).

**Step 3:** In a Markdown cell, write a question: "Which city has the highest population density?"

**Step 4:** In a code cell, calculate population density for each city and print the results.

**Step 5:** In a Markdown cell, write your finding.

**Step 6:** In a code cell, calculate the student-to-school ratio for each city.

**Step 7:** In a Markdown cell, summarize your conclusions.

## Daily Challenge

Create a Jupyter Notebook called `market_analysis.ipynb` that analyzes a market dataset.

1. Define a dataset of at least 8 products with: name, category, price, units_sold, supplier.
2. Use Markdown cells to structure the analysis with headings and explanatory text.
3. Calculate:
   - Total revenue per product.
   - Average price per category.
   - Best and worst selling products.
   - Total revenue and profit margin (assume cost is 60% of price).
4. Include at least 4 Markdown cells that explain what each analysis step does and what you found.
5. End with a "Conclusions" section summarizing the key findings.

The notebook should read like a report — someone who opens it should understand the analysis without running the code.

## Expected Output

A `.ipynb` file that alternates between Markdown narrative and code cells with output. The analysis progresses logically from data definition to findings to conclusions.

## Assessment

1. What is the difference between a code cell and a Markdown cell?
2. Why are Jupyter Notebooks preferred over plain Python scripts for data exploration?
3. What keyboard shortcut runs a cell and moves to the next one?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-08/day-072/`

Include your `market_analysis.ipynb` notebook file.

## Additional Resources

- [Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/en/stable/)
- [Markdown Guide](https://www.markdownguide.org/cheat-sheet/)

## Reflection

- How does the notebook format change the way you think about writing code compared to a `.py` file?
- In what situations would a notebook be better than a script, and vice versa?
