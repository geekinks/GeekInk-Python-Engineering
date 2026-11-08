# Environment Setup Guide

**GeekInk Python Engineering — 100 Days. 100 Challenges. Real Engineering.**

This guide walks you through setting up the development environment for the GeekInk Python Engineering program.

---

## Table of Contents

- [Requirements](#requirements)
- [Installing Python](#installing-python)
- [Installing Git](#installing-git)
- [Setting Up VS Code](#setting-up-vs-code)
- [Cloning the Repository](#cloning-the-repository)
- [Creating a Virtual Environment](#creating-a-virtual-environment)
- [Installing Dependencies](#installing-dependencies)
- [Verifying Your Setup](#verifying-your-setup)
- [Troubleshooting](#troubleshooting)

---

## Requirements

- **Python 3.10 or later** (3.12+ recommended)
- **Git 2.30 or later**
- **A code editor** (VS Code recommended)
- **A terminal** (Command Prompt, PowerShell, Terminal, or any shell)
- **A GitHub account**

---

## Installing Python

### Windows

1. Download the latest Python installer from [python.org/downloads](https://www.python.org/downloads/).
2. Run the installer. **Check the box that says "Add Python to PATH"** before clicking Install.
3. After installation, open Command Prompt and verify:

```
python --version
```

If this shows `Python 3.10.x` or later, you are ready.

### macOS

macOS may come with Python 2 pre-installed. You need Python 3.

Option A — Official installer:
1. Download from [python.org/downloads](https://www.python.org/downloads/).
2. Run the installer and follow the prompts.

Option B — Homebrew:
```bash
brew install python
```

Verify:
```bash
python3 --version
```

### Linux (Debian/Ubuntu)

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

Verify:
```bash
python3 --version
```

For other distributions, use your package manager (`dnf`, `pacman`, etc.) to install `python3`.

---

## Installing Git

### Windows

Download and install Git from [git-scm.com](https://git-scm.com/download/win). Accept the default options during installation.

### macOS

```bash
brew install git
```

Or install the Xcode Command Line Tools, which include Git:
```bash
xcode-select --install
```

### Linux (Debian/Ubuntu)

```bash
sudo apt install git
```

### Configure Git

After installing, set your identity:

```bash
git config --global user.name "Your Full Name"
git config --global user.email "your.email@example.com"
```

Verify:
```bash
git --version
git config user.name
git config user.email
```

---

## Setting Up VS Code

1. Download and install VS Code from [code.visualstudio.com](https://code.visualstudio.com/).
2. Open VS Code and install the **Python** extension by Microsoft:
   - Press `Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (macOS) to open Extensions.
   - Search for "Python" and install the one published by Microsoft.
3. Recommended additional extensions:
   - **Pylance** — Advanced Python language support (often installed with the Python extension).
   - **GitLens** — Enhanced Git integration and history.

### Configure VS Code for Python

Open VS Code settings (`Ctrl+,` or `Cmd+,`) and set:

- **Python: Default Interpreter Path** — Point to your virtual environment's Python (set after creating the venv below).
- **Editor: Tab Size** — Set to `4` (PEP 8 standard).
- **Files: Insert Final Newline** — Enable.
- **Files: Trim Trailing Whitespace** — Enable.

---

## Cloning the Repository

### Fork First

Go to [github.com/geekinks/GeekInk-Python-Engineering](https://github.com/geekinks/GeekInk-Python-Engineering) and click **Fork**.

### Clone Your Fork

```bash
git clone https://github.com/YOUR-USERNAME/GeekInk-Python-Engineering.git
cd GeekInk-Python-Engineering
```

### Add the Upstream Remote

```bash
git remote add upstream https://github.com/geekinks/GeekInk-Python-Engineering.git
```

To pull updates from the main repository later:
```bash
git fetch upstream
git merge upstream/main
```

---

## Creating a Virtual Environment

Always use a virtual environment to isolate project dependencies.

### Create

```bash
python3 -m venv .venv
```

On Windows, use `python` instead of `python3` if that is how your installation is configured.

### Activate

Linux / macOS:
```bash
source .venv/bin/activate
```

Windows (Command Prompt):
```
.venv\Scripts\activate
```

Windows (PowerShell):
```
.venv\Scripts\Activate.ps1
```

When activated, your terminal prompt will show `(.venv)` at the beginning.

### Deactivate

When you are done working:
```bash
deactivate
```

---

## Installing Dependencies

With your virtual environment activated:

```bash
pip install -r requirements.txt
```

This installs all Python packages used throughout the curriculum.

---

## Verifying Your Setup

Run the following checks to confirm everything is working:

```bash
# Python version (should be 3.10+)
python3 --version

# pip is available
pip --version

# Git is configured
git config user.name
git config user.email

# Virtual environment is active (should show .venv path)
which python3    # Linux/macOS
where python     # Windows

# Test a simple Python script
python3 -c "print('GeekInk Python Engineering is ready.')"
```

If all commands succeed, your environment is ready.

---

## Troubleshooting

### "python3: command not found" (Linux/macOS)

Python may not be installed or not in your PATH. Reinstall using the instructions above and verify the installation directory is on your PATH.

### "python: command not found" (Windows)

During installation, you likely did not check "Add Python to PATH." Reinstall Python and check that box, or manually add the Python installation directory to your system PATH.

### "pip: command not found"

Ensure pip is installed:
```bash
python3 -m ensurepip --upgrade
```

### Virtual environment activation fails on Windows PowerShell

You may need to change the execution policy:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Permission errors on Linux

Do not use `sudo pip install`. Always use a virtual environment instead.

### Git push asks for password every time

Set up SSH keys for GitHub. Follow the [GitHub SSH setup guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

### Cannot clone — repository not found

Make sure you forked the repository first, and that you are cloning your fork (your username in the URL), not the main repository directly.

---

## Next Steps

Once your environment is set up:

1. Read the [Student Guide](student-guide.md) to understand the daily workflow.
2. Open `curriculum/module-01/day-001/README.md` and begin Day 1.
