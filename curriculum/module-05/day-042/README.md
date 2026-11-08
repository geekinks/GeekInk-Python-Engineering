# Day 042: Working with Files and Directories

## Learning Objectives

- Create, rename, copy, and delete files and directories programmatically.
- Traverse directory trees using `os.walk()` and `Path.rglob()`.
- Read file metadata such as size, modification time, and permissions.
- Build a script that finds duplicate files based on content.

## Introduction

Yesterday you learned to navigate the filesystem. Today you will learn to modify it: creating directories, renaming files, copying content, and cleaning up what you no longer need. These operations form the backbone of automation scripts used in DevOps, data pipelines, and system administration.

A common real-world task is walking an entire directory tree -- not just the top-level folder, but every subfolder within it. Python gives you `os.walk()` for this, which yields each directory along with its subdirectories and files. The `pathlib` equivalent is `Path.rglob()`, which recursively matches patterns across an entire tree.

You will also learn to inspect file metadata -- the information about a file rather than its contents. Knowing a file's size, when it was last modified, or whether it is a symbolic link lets you write intelligent scripts that make decisions based on real file properties.

## Concepts

### Creating and Removing

- `Path.mkdir(parents=True, exist_ok=True)` -- create a directory and all parent directories.
- `Path.touch()` -- create an empty file or update its modification time.
- `Path.unlink()` -- delete a file.
- `Path.rmdir()` -- remove an empty directory.
- `shutil.rmtree(path)` -- remove a directory and all its contents (use with caution).
- `shutil.copy2(src, dst)` -- copy a file preserving metadata.
- `shutil.move(src, dst)` -- move or rename a file or directory.

### Walking Directory Trees

- `os.walk(top)` -- yields `(dirpath, dirnames, filenames)` for every directory in the tree.
- `Path.rglob(pattern)` -- recursively glob across all subdirectories.

### File Metadata

- `Path.stat()` -- returns a `stat_result` with size (`st_size`), modification time (`st_mtime`), etc.
- `os.path.getsize(path)` -- file size in bytes.
- `datetime.fromtimestamp(st_mtime)` -- convert modification time to a readable date.

## Practical Examples

```python
from pathlib import Path
import shutil

# Create a nested directory structure
base = Path("project_backup")
(base / "src" / "utils").mkdir(parents=True, exist_ok=True)
(base / "docs").mkdir(parents=True, exist_ok=True)

# Create some files
(base / "src" / "main.py").write_text("print('hello')\n")
(base / "src" / "utils" / "helpers.py").write_text("def add(a, b): return a + b\n")
(base / "docs" / "readme.txt").write_text("Project documentation\n")

print("Created project structure")
```

```python
from pathlib import Path
from datetime import datetime

# Walk a directory tree and report file sizes
base = Path("project_backup")
for item in base.rglob("*"):
    if item.is_file():
        stat = item.stat()
        mod_time = datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M")
        print(f"  {item.relative_to(base)}  |  {stat.st_size} bytes  |  modified: {mod_time}")
```

```python
import os

# os.walk example -- count files at each level
for dirpath, dirnames, filenames in os.walk("project_backup"):
    level = dirpath.replace("project_backup", "").count(os.sep)
    indent = "  " * level
    print(f"{indent}{os.path.basename(dirpath)}/  ({len(filenames)} files)")
```

```python
# Renaming and copying
from pathlib import Path
import shutil

src = Path("project_backup/docs/readme.txt")
dst = Path("project_backup/docs/README.md")

# Rename
src.rename(dst)
print(f"Renamed {src.name} -> {dst.name}")

# Copy
shutil.copy2(dst, Path("project_backup/docs/README_backup.md"))
print("Backup copy created")
```

## Guided Practice

Write a script that generates a directory report. Given a root folder, it should list every file with its path, size, and last modification date, then summarize the total number of files and total size.

```python
from pathlib import Path
from datetime import datetime


def generate_report(root_path):
    root = Path(root_path)
    if not root.is_dir():
        print(f"Error: {root_path} is not a valid directory.")
        return

    total_files = 0
    total_size = 0

    print(f"Directory Report: {root.resolve()}")
    print("-" * 70)
    print(f"{'Path':<40} {'Size':>10} {'Modified':>18}")
    print("-" * 70)

    for item in sorted(root.rglob("*")):
        if item.is_file():
            stat = item.stat()
            rel_path = str(item.relative_to(root))
            size_kb = stat.st_size / 1024
            mod_time = datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M")
            print(f"{rel_path:<40} {size_kb:>8.1f}KB {mod_time:>18}")
            total_files += 1
            total_size += stat.st_size

    print("-" * 70)
    print(f"Total: {total_files} files, {total_size / 1024:.1f} KB")


generate_report("project_backup")
```

## Daily Challenge

**Build a Duplicate File Finder**

Write a script called `duplicate_finder.py` that:

1. Accepts a directory path as input.
2. Recursively scans all files in that directory and its subdirectories.
3. Identifies duplicate files based on their content (not just their name). Use `hashlib.md5()` or `hashlib.sha256()` to compute a hash of each file's contents.
4. Groups duplicates together and prints them.
5. Reports the total number of duplicate groups found and how much space could be saved by removing duplicates.

Requirements:
- Use `pathlib` for path operations.
- Use `hashlib` for content hashing.
- Handle empty files and very large files gracefully (read in chunks).
- Do not delete any files -- only report duplicates.

Hint for hashing large files:

```python
import hashlib

def hash_file(filepath, chunk_size=8192):
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            hasher.update(chunk)
    return hasher.hexdigest()
```

## Expected Output

```
Scanning: /home/user/documents

Duplicate groups found:

  Group 1 (SHA-256: a3f2c8...):
    documents/report.txt (1.2 KB)
    documents/backup/report_copy.txt (1.2 KB)

  Group 2 (SHA-256: 7b9e1d...):
    documents/photo.jpg (245.0 KB)
    documents/archive/photo.jpg (245.0 KB)
    documents/old/photo_2023.jpg (245.0 KB)

Summary:
  2 duplicate groups found
  3 duplicate files (could remove to save 491.2 KB)
```

## Assessment

1. What is the difference between `os.walk()` and `Path.rglob()`? When would you prefer one over the other?
2. Why should you hash file contents in chunks rather than reading the entire file into memory at once?
3. What does `shutil.rmtree()` do, and why should you be cautious when using it?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-05/day-042/`

Include your `duplicate_finder.py` and a `README.md` with usage instructions.

## Additional Resources

- [shutil documentation](https://docs.python.org/3/library/shutil.html)
- [hashlib documentation](https://docs.python.org/3/library/hashlib.html)

## Reflection

- What are the risks of a script that deletes or moves files automatically? How would you add safety checks?
- Can you think of a scenario where two different files could produce the same hash? What is this called?
