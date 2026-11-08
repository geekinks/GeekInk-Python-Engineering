# Day 029: Virtual Environments and Dependency Management

## Learning Objectives

- Understand why virtual environments are necessary.
- Create and activate a virtual environment using `venv`.
- Install, manage, and freeze dependencies with `pip`.
- Create and use a `requirements.txt` file.
- Follow professional dependency management practices.

## Introduction

Imagine you are working on two projects. One needs version 2.0 of a library, and the other needs version 3.0. If both projects share the same Python installation, they will conflict. Virtual environments solve this by giving each project its own isolated set of installed packages.

Every professional Python project uses a virtual environment. It ensures that your project's dependencies are documented, reproducible, and do not interfere with other projects or your system Python. When a teammate clones your project, they run `pip install -r requirements.txt` inside a fresh virtual environment and get exactly the same setup you have. This is a foundational software engineering practice.

## Concepts

### What Is a Virtual Environment?

A virtual environment is an isolated Python installation within a directory. It has its own `python` executable and its own `pip`, completely separate from your system Python.

### Creating a Virtual Environment

```bash
python3 -m venv venv
```

This creates a directory called `venv` containing the isolated Python environment.

### Activating the Environment

On Linux/macOS:
```bash
source venv/bin/activate
```

On Windows:
```bash
venv\Scripts\activate
```

When activated, your terminal prompt shows `(venv)` and any `pip install` commands install into the virtual environment only.

### Deactivating

```bash
deactivate
```

### Installing Packages with `pip`

```bash
pip install requests
pip install flask==3.0.0
pip install "pandas>=2.0,<3.0"
```

### `pip freeze` and `requirements.txt`

```bash
pip freeze > requirements.txt
```

This saves a snapshot of all installed packages and their exact versions. Anyone can recreate your environment with:

```bash
pip install -r requirements.txt
```

### Why `.venv` Should Never Be Committed

The virtual environment directory contains hundreds of files specific to your operating system and Python version. It should be listed in `.gitignore`. Only `requirements.txt` is committed.

## Practical Examples

```bash
# Full workflow from scratch

# 1. Create a project directory
mkdir my_project
cd my_project

# 2. Create a virtual environment
python3 -m venv venv

# 3. Activate it
source venv/bin/activate    # Linux/macOS
# venv\Scripts\activate     # Windows

# 4. Verify isolation
which python                # Should point to venv/bin/python
pip list                    # Should show only pip and setuptools

# 5. Install packages
pip install requests
pip install python-dotenv

# 6. Freeze dependencies
pip freeze > requirements.txt

# 7. View requirements.txt
cat requirements.txt
# certifi==2024.2.2
# charset-normalizer==3.3.4
# idna==3.6
# python-dotenv==1.0.1
# requests==2.31.0
# urllib3==2.2.1

# 8. Deactivate
deactivate
```

```python
# Example Python script using an installed package
# (Run this after activating venv and installing requests)

import requests

response = requests.get("https://api.github.com")
print(f"Status: {response.status_code}")
print(f"GitHub API says: {response.json().get('current_user_url')}")
```

### Recreating an environment from requirements.txt

```bash
# On a new machine or after cloning a repository
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Upgrading and removing packages

```bash
pip install --upgrade requests
pip uninstall requests
pip list                         # See what is installed
pip show requests                # Details about a package
```

## Guided Practice

Set up a project with proper dependency management.

**Step 1:** Create a new project directory and virtual environment.

```bash
mkdir weather_app
cd weather_app
python3 -m venv venv
source venv/bin/activate
```

**Step 2:** Install a package.

```bash
pip install requests
```

**Step 3:** Write a simple script that uses the package.

Create `weather.py`:

```python
import requests

def get_weather_info():
    url = "https://api.github.com"
    response = requests.get(url)
    if response.status_code == 200:
        print("Connection successful!")
        print(f"Response contains {len(response.json())} keys")
    else:
        print(f"Error: status {response.status_code}")

if __name__ == "__main__":
    get_weather_info()
```

**Step 4:** Freeze dependencies.

```bash
pip freeze > requirements.txt
```

**Step 5:** Create a `.gitignore` for the project.

```
venv/
__pycache__/
*.pyc
.env
```

**Step 6:** Verify the project structure.

```
weather_app/
    .gitignore
    requirements.txt
    weather.py
    venv/           (not committed to git)
```

## Daily Challenge

Set up a complete Python project with proper dependency management.

1. Create a directory called `day-029-project/`.
2. Create a virtual environment inside it.
3. Install the following packages: `requests`, `python-dotenv`.
4. Create a `requirements.txt` using `pip freeze`.
5. Create a `.gitignore` that excludes `venv/`, `__pycache__/`, `.env`, and `*.pyc`.
6. Create a file called `project_info.py` that:
   - Imports `requests` and prints its version (`requests.__version__`).
   - Imports `dotenv` and prints its version.
   - Prints the Python version using `sys.version`.
   - Prints the path to the Python executable using `sys.executable` (to verify it is inside `venv`).
7. Create a `README.md` for the project that includes:
   - Project name and description.
   - Setup instructions (create venv, activate, install requirements).
   - How to run the script.

Submit the following files (NOT the `venv/` directory):
- `requirements.txt`
- `.gitignore`
- `project_info.py`
- `README.md`

## Expected Output

When running `project_info.py` inside the activated virtual environment:

```
requests version: 2.31.0
python-dotenv version: 1.0.1
Python version: 3.12.0 (main, Oct  2 2024, 00:00:00)
Python executable: /path/to/day-029-project/venv/bin/python
```

The exact versions and paths will vary on your system.

## Assessment

1. Why should you never install Python packages globally for a project?
2. What is the purpose of `requirements.txt`, and how do you generate it?
3. Why should the `venv/` directory be in `.gitignore` instead of committed to the repository?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-03/day-029/`

Include `requirements.txt`, `.gitignore`, `project_info.py`, and `README.md`. Do NOT include the `venv/` directory.

## Additional Resources

- [Python Docs: venv — Creation of virtual environments](https://docs.python.org/3/library/venv.html)
- [pip Documentation](https://pip.pypa.io/en/stable/)

## Reflection

- What would happen if every Python project on your computer shared the same installed packages?
- How does proper dependency management make it easier for a team to collaborate on a project?
