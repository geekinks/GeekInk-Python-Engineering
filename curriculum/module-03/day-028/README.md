# Day 028: Working with CSV and JSON

## Learning Objectives

- Read and write CSV files using Python's `csv` module.
- Use `DictReader` and `DictWriter` for more readable CSV handling.
- Read and write JSON files using Python's `json` module.
- Convert between Python data structures and JSON format.
- Choose the right file format for different use cases.

## Introduction

Plain text files work for simple data, but structured data needs structured formats. CSV (Comma-Separated Values) is the standard for tabular data — spreadsheets, database exports, and data feeds all use it. JSON (JavaScript Object Notation) is the standard for nested, hierarchical data — APIs, configuration files, and modern web services use it everywhere.

Python has built-in modules for both formats. Learning to work with CSV and JSON fluently is essential because almost every real-world project involves reading data from external sources or exporting data for other systems to consume. After this lesson, you will be able to load, process, and save structured data with confidence.

## Concepts

### CSV Files

A CSV file stores tabular data as plain text, with each row on a new line and values separated by commas.

```
name,age,city
Amina,20,Kano
Musa,22,Abuja
```

### The `csv` Module

- `csv.reader(file)` — Reads rows as lists.
- `csv.writer(file)` — Writes rows as lists.
- `csv.DictReader(file)` — Reads rows as dictionaries (using the header row as keys).
- `csv.DictWriter(file, fieldnames)` — Writes dictionaries as rows.

### JSON Files

JSON represents data as key-value pairs (objects) and ordered lists (arrays). It maps naturally to Python dictionaries and lists.

```json
{"name": "Amina", "age": 20, "courses": ["Python", "Data Science"]}
```

### The `json` Module

- `json.load(file)` — Reads JSON from a file into a Python object.
- `json.dump(obj, file)` — Writes a Python object to a file as JSON.
- `json.loads(string)` — Parses a JSON string.
- `json.dumps(obj)` — Converts a Python object to a JSON string.

## Practical Examples

```python
import csv
import json


# Writing a CSV file
students = [
    ["Name", "Score", "Grade"],
    ["Amina", 85, "A"],
    ["Musa", 72, "B"],
    ["Fatima", 91, "A"],
]

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(students)


# Reading a CSV file
with open("students.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
# ['Name', 'Score', 'Grade']
# ['Amina', '85', 'A']
# ...


# Using DictReader (recommended for readability)
with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['Name']}: {row['Score']} ({row['Grade']})")


# Using DictWriter
records = [
    {"name": "Ibrahim", "score": 67, "grade": "C"},
    {"name": "Halima", "score": 88, "grade": "A"},
]

with open("new_students.csv", "w", newline="") as f:
    fieldnames = ["name", "score", "grade"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(records)


# Writing JSON
data = {
    "school": "GeekInk Academy",
    "year": 2024,
    "students": [
        {"name": "Amina", "scores": [85, 90, 78]},
        {"name": "Musa", "scores": [72, 68, 80]},
    ]
}

with open("school.json", "w") as f:
    json.dump(data, f, indent=2)


# Reading JSON
with open("school.json", "r") as f:
    loaded = json.load(f)
    print(loaded["school"])
    for student in loaded["students"]:
        avg = sum(student["scores"]) / len(student["scores"])
        print(f"  {student['name']}: average = {avg:.1f}")


# Converting between JSON strings and Python objects
student_json = '{"name": "Fatima", "age": 19}'
student_dict = json.loads(student_json)
print(student_dict["name"])    # Fatima

back_to_json = json.dumps(student_dict, indent=2)
print(back_to_json)
```

## Guided Practice

Build a student grade processor that reads from CSV and exports to JSON.

**Step 1:** Create a CSV file `grades.csv`:

```python
import csv

data = [
    {"name": "Amina", "math": "85", "english": "90", "science": "78"},
    {"name": "Musa", "math": "72", "english": "68", "science": "80"},
    {"name": "Fatima", "math": "91", "english": "95", "science": "88"},
]

with open("grades.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "math", "english", "science"])
    writer.writeheader()
    writer.writerows(data)

print("grades.csv created.")
```

**Step 2:** Read the CSV, calculate averages, and build a results list:

```python
import csv

results = []

with open("grades.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        scores = [int(row["math"]), int(row["english"]), int(row["science"])]
        avg = sum(scores) / len(scores)
        results.append({
            "name": row["name"],
            "scores": {"math": int(row["math"]), "english": int(row["english"]), "science": int(row["science"])},
            "average": round(avg, 1),
            "passed": avg >= 50
        })

for r in results:
    status = "PASS" if r["passed"] else "FAIL"
    print(f"{r['name']}: {r['average']} — {status}")
```

**Step 3:** Export results to JSON:

```python
import json

with open("results.json", "w") as f:
    json.dump({"results": results}, f, indent=2)

print("Results exported to results.json")
```

## Daily Challenge

Build a **contact manager** called `contacts.py` that stores contacts in both CSV and JSON formats.

The program must support:

1. **Add a contact** — Name, phone, email, city.
2. **View all contacts** — Display all contacts in a formatted table.
3. **Search contacts** — Search by name (case-insensitive partial match).
4. **Save to CSV** — Export all contacts to `contacts.csv`.
5. **Save to JSON** — Export all contacts to `contacts.json`.
6. **Load from CSV** — Load contacts from `contacts.csv`.
7. **Load from JSON** — Load contacts from `contacts.json`.
8. **Exit**.

Requirements:
- Contacts are stored as a list of dictionaries in memory while the program runs.
- CSV export should include a header row.
- JSON export should use `indent=2` for readability.
- Handle the case where the file does not exist when loading.
- The menu should loop until the user exits.

## Expected Output

```
=== Contact Manager ===
1. Add contact
2. View all contacts
3. Search contacts
4. Save to CSV
5. Save to JSON
6. Load from CSV
7. Load from JSON
8. Exit

Choice: 1
Name: Amina Bello
Phone: 08012345678
Email: amina@example.com
City: Kano
Contact added!

Choice: 2
+----------------+-------------+---------------------+--------+
| Name           | Phone       | Email               | City   |
+----------------+-------------+---------------------+--------+
| Amina Bello    | 08012345678 | amina@example.com   | Kano   |
+----------------+-------------+---------------------+--------+

Choice: 4
Contacts saved to contacts.csv

Choice: 8
Goodbye!
```

## Assessment

1. What is the difference between `csv.reader` and `csv.DictReader`? When would you choose one over the other?
2. What does `json.dump()` do differently from `json.dumps()`?
3. A CSV file stores all values as strings. How do you handle numeric data when reading from CSV?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-03/day-028/`

Include your `contacts.py` file. Do not include generated CSV or JSON files.

## Additional Resources

- [Python Docs: csv module](https://docs.python.org/3/library/csv.html)
- [Python Docs: json module](https://docs.python.org/3/library/json.html)

## Reflection

- When would you choose CSV over JSON for storing data, and vice versa?
- Think about an application you use daily. What kind of data might it store in files? Would CSV or JSON be more appropriate?
