# Day 027: Reading and Writing Files

## Learning Objectives

- Open, read, and write files using Python's built-in `open()` function.
- Understand file modes: `"r"`, `"w"`, `"a"`, `"r+"`.
- Use the `with` statement to safely handle files.
- Read files line by line, in bulk, and as lists.
- Write and append text to files.

## Introduction

Programs that lose all their data when they close are not very useful. File handling lets your programs persist data between runs — saving user preferences, storing records, logging events, or generating reports. Every real application interacts with files in some way.

Python makes file handling straightforward with the built-in `open()` function. The most important practice is using the `with` statement, which guarantees the file is properly closed even if an error occurs. Engineers who forget to close files create resource leaks that can crash long-running applications. The `with` statement eliminates this risk entirely.

## Concepts

### Opening a File

```python
file = open("data.txt", "r")    # Open for reading
content = file.read()
file.close()                     # Must close manually
```

### File Modes

| Mode | Description |
|------|-------------|
| `"r"` | Read (default). File must exist. |
| `"w"` | Write. Creates file or overwrites existing content. |
| `"a"` | Append. Creates file or adds to the end. |
| `"r+"` | Read and write. File must exist. |
| `"x"` | Create. Fails if file already exists. |

### The `with` Statement

The `with` statement is the recommended way to work with files. It automatically closes the file when the block ends.

```python
with open("data.txt", "r") as file:
    content = file.read()
# File is automatically closed here
```

### Reading Methods

- `read()` — Reads the entire file as a single string.
- `readline()` — Reads one line at a time.
- `readlines()` — Reads all lines into a list.
- Iterating directly — `for line in file:` reads line by line (memory-efficient).

### Writing Methods

- `write(text)` — Writes a string to the file.
- `writelines(list)` — Writes a list of strings (no newlines added automatically).

## Practical Examples

```python
# Writing to a file
with open("greeting.txt", "w") as f:
    f.write("Hello, GeekInk!\n")
    f.write("Welcome to Day 27.\n")


# Reading the entire file
with open("greeting.txt", "r") as f:
    content = f.read()
    print(content)


# Reading line by line
with open("greeting.txt", "r") as f:
    for line in f:
        print(line.strip())


# Reading lines into a list
with open("greeting.txt", "r") as f:
    lines = f.readlines()
    print(lines)
    # ['Hello, GeekInk!\n', 'Welcome to Day 27.\n']


# Appending to a file
with open("greeting.txt", "a") as f:
    f.write("This line was appended.\n")


# Counting lines and words in a file
with open("greeting.txt", "r") as f:
    lines = f.readlines()
    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    print(f"Lines: {line_count}, Words: {word_count}")


# Writing a list of items
names = ["Amina", "Musa", "Fatima", "Ibrahim"]
with open("students.txt", "w") as f:
    for name in names:
        f.write(name + "\n")


# Reading back and processing
with open("students.txt", "r") as f:
    for i, line in enumerate(f, 1):
        print(f"{i}. {line.strip()}")


# Checking if a file exists before reading
import os

filename = "students.txt"
if os.path.exists(filename):
    with open(filename, "r") as f:
        print(f.read())
else:
    print(f"{filename} not found.")
```

## Guided Practice

Build a simple log system.

**Step 1:** Create a function that writes a log entry.

```python
from datetime import datetime

def write_log(message, filename="app.log"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as f:
        f.write(f"[{timestamp}] {message}\n")
```

**Step 2:** Create a function that reads and displays the log.

```python
def read_log(filename="app.log"):
    try:
        with open(filename, "r") as f:
            content = f.read()
            if content:
                print(content)
            else:
                print("Log is empty.")
    except FileNotFoundError:
        print("No log file found.")
```

**Step 3:** Use both functions.

```python
from datetime import datetime

def write_log(message, filename="app.log"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

def read_log(filename="app.log"):
    try:
        with open(filename, "r") as f:
            content = f.read()
            if content:
                print(content)
            else:
                print("Log is empty.")
    except FileNotFoundError:
        print("No log file found.")

write_log("Application started")
write_log("User Amina logged in")
write_log("Data processing completed")

print("=== Application Log ===")
read_log()
```

## Daily Challenge

Build a **note-taking application** called `notes.py` that persists notes to a text file called `notes.txt`.

The program must support the following operations through a simple command-line menu:

1. **Add a note** — Prompt the user for text and append it to `notes.txt` with a timestamp.
2. **View all notes** — Read and display all notes from the file, numbered.
3. **Search notes** — Prompt for a search term and display only notes that contain it (case-insensitive).
4. **Count notes** — Display the total number of notes stored.
5. **Clear all notes** — Delete all notes (after confirmation).
6. **Exit** — End the program.

Requirements:
- Use the `with` statement for all file operations.
- Handle the case where `notes.txt` does not yet exist.
- Each note should be stored as one line with format: `[YYYY-MM-DD HH:MM:SS] Note text here`
- The menu should loop until the user chooses to exit.

## Expected Output

```
=== Note Taking App ===
1. Add a note
2. View all notes
3. Search notes
4. Count notes
5. Clear all notes
6. Exit

Choose an option: 1
Enter your note: Learn about file handling in Python
Note saved!

Choose an option: 1
Enter your note: Review Day 26 modules exercise
Note saved!

Choose an option: 2
1. [2024-11-08 14:30:00] Learn about file handling in Python
2. [2024-11-08 14:30:15] Review Day 26 modules exercise

Choose an option: 3
Search for: file
Results:
1. [2024-11-08 14:30:00] Learn about file handling in Python

Choose an option: 4
Total notes: 2

Choose an option: 6
Goodbye!
```

## Assessment

1. What is the difference between `"w"` and `"a"` file modes? What happens to existing content in each case?
2. Why should you use `with open(...)` instead of `open()` followed by `file.close()`?
3. How would you read a very large file (millions of lines) without running out of memory?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-03/day-027/`

Include your `notes.py` file. Do not include `notes.txt` — it should be generated by running the program.

## Additional Resources

- [Python Docs: Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Python Docs: open() built-in function](https://docs.python.org/3/library/functions.html#open)

## Reflection

- Why is persisting data to files important for real-world applications?
- What problems could occur if a program crashes while writing to a file? How does the `with` statement help?
