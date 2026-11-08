# Day 081: Writing Clean Python

## Learning Objectives

- Understand the purpose and key rules of PEP 8, Python's official style guide.
- Apply consistent naming conventions for variables, functions, classes, and constants.
- Use type hints to document expected argument and return types.
- Format code automatically with tools like `black`, `isort`, and `pylint`.
- Recognize and fix common style violations in existing code.

## Introduction

Clean code is code that other engineers can read, understand, and modify without confusion. In a professional environment you rarely work alone; your teammates, future maintainers, and even your future self will need to navigate what you wrote months ago. Code that follows a consistent style removes unnecessary friction from that process.

Python has an official style guide called PEP 8. It covers indentation, line length, import ordering, naming conventions, whitespace, and more. Following PEP 8 is not about being pedantic; it is about making Python code look familiar to every Python developer regardless of company or project. When every file follows the same rules, code reviews focus on logic rather than formatting.

Beyond manual discipline, the Python ecosystem provides powerful automated tools. `black` reformats your code deterministically, `isort` sorts your imports, and `pylint` checks for style violations and potential bugs. Together, these tools enforce consistency without requiring you to memorize every rule.

## Concepts

### PEP 8 Naming Conventions

| Element | Convention | Example |
|---------|-----------|---------|
| Variable | snake_case | `student_count` |
| Function | snake_case | `calculate_average()` |
| Class | PascalCase | `StudentRecord` |
| Constant | UPPER_SNAKE_CASE | `MAX_RETRIES` |
| Module | short, lowercase | `utils.py` |
| Private attribute | leading underscore | `_internal_cache` |

### Indentation and Line Length

Use 4 spaces per indentation level. Never mix tabs and spaces. Keep lines under 79 characters for code and 72 for docstrings and comments. If a line is too long, break it using parentheses or backslash continuation.

### Imports

Imports should be at the top of the file, grouped in this order, separated by a blank line:

1. Standard library imports
2. Third-party imports
3. Local application imports

### Type Hints

Type hints document what types a function expects and returns. They do not enforce anything at runtime by default, but they help editors, linters, and other developers understand your code.

```python
def calculate_average(scores: list[float]) -> float:
    return sum(scores) / len(scores)
```

### Docstrings

Every public module, class, and function should have a docstring. Use triple double-quotes. The first line is a brief summary. If more detail is needed, leave a blank line and continue.

```python
def enroll_student(name: str, course_id: int) -> bool:
    """Enroll a student in a course.

    Args:
        name: The student's full name.
        course_id: The numeric ID of the course.

    Returns:
        True if enrollment succeeded, False otherwise.
    """
```

## Practical Examples

### Before: messy code

```python
import os,sys
from collections import OrderedDict
import json
import math
from pathlib import Path

def Calc(x,y,operation):
  if operation=="add":
    return x+y
  elif operation == "subtract":
      return x -y
  elif operation=="multiply":
    return x*y

class student_record:
    def __init__(self, Name, AGE, scores):
        self.Name=Name
        self.AGE = AGE
        self.scores=scores
    def GetAverage(self):
        return sum(self.scores)/len(self.scores)
    def is_passing(self):
        avg=self.GetAverage()
        if avg>=50:
            return True
        else:
            return False
```

### After: clean code

```python
import json
import math
import os
import sys
from collections import OrderedDict
from pathlib import Path


def calculate(x: float, y: float, operation: str) -> float:
    """Perform a basic arithmetic operation on two numbers."""
    if operation == "add":
        return x + y
    elif operation == "subtract":
        return x - y
    elif operation == "multiply":
        return x * y
    raise ValueError(f"Unknown operation: {operation}")


class StudentRecord:
    """Represents an academic record for a single student."""

    PASSING_THRESHOLD = 50.0

    def __init__(self, name: str, age: int, scores: list[float]) -> None:
        self.name = name
        self.age = age
        self.scores = scores

    def get_average(self) -> float:
        """Return the arithmetic mean of all scores."""
        return sum(self.scores) / len(self.scores)

    def is_passing(self) -> bool:
        """Check whether the student's average meets the passing threshold."""
        return self.get_average() >= self.PASSING_THRESHOLD
```

### Using black and isort

```bash
# Install tools
pip install black isort pylint

# Format a file with black
black my_script.py

# Sort imports
isort my_script.py

# Check for style issues
pylint my_script.py
```

## Guided Practice

1. Create a file called `messy_code.py` with the following content:

```python
import random
import os
from datetime import datetime
import sys

def processData(data_list,threshold):
    result=[]
    for Item in data_list:
        if Item>threshold:
            result.append(Item)
    return result

class employee_manager:
    def __init__(self,company_name):
        self.CompanyName=company_name
        self.employees=[]
    def AddEmployee(self,name,salary):
        self.employees.append({"name":name,"salary":salary})
    def getTotalPayroll(self):
        Total=0
        for emp in self.employees:
            Total+=emp["salary"]
        return Total
    def getHighEarners(self,min_salary):
        return [e for e in self.employees if e["salary"]>=min_salary]
```

2. Identify every PEP 8 violation: naming, spacing, import order, missing type hints, missing docstrings.

3. Rewrite the file to follow PEP 8. Add type hints and docstrings.

4. Run `black messy_code.py` and `isort messy_code.py` on your cleaned version to confirm there are no remaining formatting issues.

5. Run `pylint messy_code.py` and address any warnings.

## Daily Challenge

You are given the following file. Refactor it completely to follow PEP 8, add type hints, add docstrings, and fix any logical issues you find.

```python
import json,os
from pathlib import Path
import sys
import csv

FILENAME="inventory.csv"

class inventoryItem:
  def __init__(self,name,Quantity,Price):
    self.name=name
    self.Quantity=Quantity
    self.Price=Price
  def TotalValue(self):
    return self.Quantity*self.Price
  def __str__(self):
    return f"{self.name}: {self.Quantity} units @ ${self.Price}"

class InventoryManager:
  def __init__(self):
    self.items=[]
  def add_item(self,name,qty,price):
    self.items.append(inventoryItem(name,qty,price))
  def RemoveItem(self,name):
    self.items=[i for i in self.items if i.name!=name]
  def GetTotalValue(self):
    total=0
    for item in self.items:
      total+=item.TotalValue()
    return total
  def SaveToFile(self,filename):
    with open(filename,"w") as f:
      writer=csv.writer(f)
      writer.writerow(["name","quantity","price"])
      for item in self.items:
        writer.writerow([item.name,item.Quantity,item.Price])
  def loadFromFile(self,filename):
    with open(filename,"r") as f:
      reader=csv.DictReader(f)
      for row in reader:
        self.add_item(row["name"],int(row["quantity"]),float(row["price"]))

mgr=InventoryManager()
mgr.add_item("Laptop",10,45000)
mgr.add_item("Mouse",50,1500)
mgr.add_item("Keyboard",30,3000)
print(f"Total inventory value: ${mgr.GetTotalValue()}")
mgr.SaveToFile(FILENAME)
```

Requirements:
- Fix all naming conventions (classes PascalCase, methods/variables snake_case).
- Add type hints to all function signatures.
- Add a docstring to every class and public method.
- Sort imports properly.
- Use 4-space indentation consistently.
- Wrap the script execution in `if __name__ == "__main__":`.
- Run `pylint` on your final version and achieve a score of 8.0 or higher.

## Expected Output

Your refactored code should:
- Pass `black --check` with no changes needed.
- Pass `isort --check` with no changes needed.
- Score 8.0+ on `pylint`.
- Produce identical functional output to the original when run.

## Assessment

1. What is the difference between `snake_case` and `PascalCase`, and when do you use each in Python?
2. Why should imports be grouped and ordered at the top of a file?
3. What is the purpose of type hints if Python does not enforce them at runtime?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-09/day-081/`

Include:
- `messy_code_refactored.py` (from Guided Practice)
- `inventory_clean.py` (from Daily Challenge)
- `pylint_output.txt` (the pylint report for your refactored challenge file)

## Additional Resources

- [PEP 8 -- Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [PEP 484 -- Type Hints](https://peps.python.org/pep-0484/)
- [black documentation](https://black.readthedocs.io/)

## Reflection

- Before today, how consistent was the style in your own Python code? What habits will you change?
- Why do you think the Python community agreed on a single style guide rather than letting every team decide on their own?
