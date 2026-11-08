# Day 041: Python Standard Library for Automation

## Learning Objectives

- Understand what automation means in software engineering and why Python excels at it.
- Navigate the filesystem using the `os` module (`os.getcwd`, `os.listdir`, `os.path`).
- Use `pathlib.Path` for modern, cross-platform file and directory operations.
- Apply `Path.glob` to match files by pattern.
- Build a script that organizes files into directories based on their extensions.

## Introduction

Automation is the practice of writing programs that perform repetitive tasks without human intervention. Instead of manually sorting files, renaming documents, or copying data between folders, you write a Python script that does it in seconds. This is one of the most immediately useful skills you can develop as an engineer.

Python ships with powerful standard-library modules for interacting with the operating system. The older `os` module provides functions like `os.getcwd()` (get current working directory), `os.listdir()` (list directory contents), and the `os.path` submodule for manipulating file paths. The newer `pathlib` module offers an object-oriented interface that is easier to read and less error-prone. In modern Python, `pathlib` is the preferred choice for most file-system tasks.

By the end of today, you will be comfortable navigating directories, listing files, checking whether paths exist, creating folders, and matching files by pattern. These are the building blocks for every automation script you will write.

## Concepts

### The `os` Module

The `os` module is Python's original interface to the operating system. Key functions include:

- `os.getcwd()` -- returns the current working directory as a string.
- `os.listdir(path)` -- returns a list of filenames in the given directory.
- `os.path.join(a, b)` -- joins path components with the correct separator for your OS.
- `os.path.isfile(path)` -- returns `True` if the path points to a file.
- `os.path.isdir(path)` -- returns `True` if the path points to a directory.
- `os.path.splitext(filename)` -- splits a filename into name and extension.

### The `pathlib` Module

`pathlib` represents paths as `Path` objects rather than raw strings. This makes code cleaner and more readable.

- `Path.cwd()` -- current working directory.
- `Path.home()` -- user home directory.
- `path.exists()` -- does the path exist?
- `path.is_file()` / `path.is_dir()` -- is it a file or directory?
- `path.mkdir(parents=True, exist_ok=True)` -- create directories recursively.
- `path.suffix` -- the file extension (e.g., `.txt`).
- `path.stem` -- the filename without extension.
- `path.glob(pattern)` -- match files using wildcard patterns.

## Practical Examples

```python
# Using the os module
import os

# Print current directory
print("Current directory:", os.getcwd())

# List files in current directory
for item in os.listdir("."):
    if os.path.isfile(item):
        name, ext = os.path.splitext(item)
        print(f"  File: {item}  (extension: {ext})")
```

```python
# Using pathlib (preferred in modern Python)
from pathlib import Path

current = Path.cwd()
print("Current directory:", current)

# List all .py files in the current directory
for py_file in current.glob("*.py"):
    print(f"  Python file: {py_file.name}")

# Check if a directory exists; create it if not
output_dir = current / "output"
output_dir.mkdir(exist_ok=True)
print(f"Output directory ready: {output_dir}")
```

```python
# Comparing os.path and pathlib
import os
from pathlib import Path

# os.path approach
full_path = os.path.join("data", "reports", "summary.csv")
print(full_path)

# pathlib approach -- cleaner and uses the / operator
full_path = Path("data") / "reports" / "summary.csv"
print(full_path)
```

## Guided Practice

Build a script that inventories a directory. Create a folder called `sample_files/` with some test files, then write a script to report on its contents.

```python
from pathlib import Path

# Step 1: Create a sample directory with test files
sample_dir = Path("sample_files")
sample_dir.mkdir(exist_ok=True)

test_files = ["report.txt", "data.csv", "photo.jpg", "notes.txt", "script.py", "image.png"]
for fname in test_files:
    (sample_dir / fname).touch()  # creates empty files

# Step 2: Count files by extension
extension_counts = {}
for item in sample_dir.iterdir():
    if item.is_file():
        ext = item.suffix.lower() if item.suffix else "(no extension)"
        extension_counts[ext] = extension_counts.get(ext, 0) + 1

# Step 3: Display the inventory
print(f"Directory: {sample_dir.resolve()}")
print(f"Total files: {sum(extension_counts.values())}")
print("\nBreakdown by extension:")
for ext, count in sorted(extension_counts.items()):
    print(f"  {ext}: {count} file(s)")
```

## Daily Challenge

**Build a File Organizer**

Write a Python script called `file_organizer.py` that:

1. Accepts a directory path as input (or defaults to the current directory).
2. Scans all files in that directory (not subdirectories).
3. Creates subdirectories named after each file extension (e.g., `txt`, `csv`, `py`, `jpg`).
4. Moves each file into the matching subdirectory.
5. Skips files that have no extension.
6. Prints a summary of how many files were moved and into which folders.

Requirements:
- Use `pathlib` for all path operations.
- Use `shutil.move()` to move files.
- Do not move the script itself.
- Handle the case where the target subdirectory already exists.

## Expected Output

```
Scanning: /home/user/messy_folder

Organizing files...
  report.txt -> txt/report.txt
  data.csv -> csv/data.csv
  photo.jpg -> jpg/photo.jpg
  notes.txt -> txt/notes.txt
  script.py -> py/script.py

Summary:
  txt: 2 files
  csv: 1 file
  jpg: 1 file
  py: 1 file

Total: 5 files organized into 4 folders.
```

## Assessment

1. What is the difference between `os.path.join()` and using the `/` operator with `pathlib.Path`?
2. Why is `path.mkdir(parents=True, exist_ok=True)` safer than `os.mkdir()`?
3. What does `Path.glob("*.csv")` return, and how does it differ from `os.listdir()`?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-05/day-041/`

Include your `file_organizer.py` script and a brief `README.md` describing how to run it.

## Additional Resources

- [pathlib documentation](https://docs.python.org/3/library/pathlib.html)
- [os module documentation](https://docs.python.org/3/library/os.html)
- [os.path documentation](https://docs.python.org/3/library/os.path.html)

## Reflection

- What types of repetitive file-management tasks could you automate with what you learned today?
- When would you choose `os.path` over `pathlib`, and vice versa?
