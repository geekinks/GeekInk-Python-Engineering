# Python Environment Setup

## Install Python

- **Windows:** install Python 3.10+ from [python.org](https://www.python.org/downloads/), select Add Python to PATH, then run python --version.
- **macOS:** install from python.org or use brew install python; run python3 --version.
- **Linux (Debian/Ubuntu):** use sudo apt install python3 python3-venv python3-pip git; run python3 --version.

Install VS Code and its Microsoft Python extension. Use four-space indentation and select the project virtual environment as interpreter.

## Virtual environment, packages, and tests

~~~bash
python3 -m venv .venv
source .venv/bin/activate       # Linux/macOS
.venv\Scripts\Activate.ps1      # Windows PowerShell
python -m pip install --upgrade pip
python hello.py
python -m pytest
~~~

Install only packages required by the active lesson. If a command is not found, reopen the terminal, confirm the selected interpreter, and use python3 where appropriate. Keep an offline copy of the repository and activate the virtual environment before installing packages.
