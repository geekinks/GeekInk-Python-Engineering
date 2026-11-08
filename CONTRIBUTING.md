# Contributing to GeekInk Python Engineering

Thank you for your interest in contributing to this project. Whether you are a student submitting coursework, an instructor improving materials, or a community member fixing a bug, this guide explains how to participate.

---

## Table of Contents

- [Student Submission Workflow](#student-submission-workflow)
- [Community Contributions](#community-contributions)
- [Code Style](#code-style)
- [Commit Message Conventions](#commit-message-conventions)
- [Pull Request Guidelines](#pull-request-guidelines)
- [Review Process](#review-process)
- [What Not to Submit](#what-not-to-submit)

---

## Student Submission Workflow

### 1. Fork and Clone

```bash
# Fork this repository on GitHub, then clone your fork
git clone https://github.com/<your-username>/GeekInk-Python-Engineering.git
cd GeekInk-Python-Engineering
```

### 2. Create Your Submission Branch

Create a branch named after yourself and the module you are working on:

```bash
git checkout -b <your-username>/module-01
```

### 3. Organize Your Work

Place your submissions in the following directory structure:

```
task/students/<your-github-username>/
    README.md                  # Your name, cohort, and learning journal
    module-01/
        day-001/
            solution.py        # Your solution for Day 1
            notes.md           # Optional: your notes and reflections
        day-002/
            solution.py
        ...
    module-02/
        day-011/
            solution.py
        ...
```

Each day's directory should contain your solution file(s) and any supporting files required by the exercise.

### 4. Commit Your Work

Write clear, descriptive commit messages:

```bash
git add task/students/<your-username>/module-01/day-001/
git commit -m "Add Day 001 solution: variables and data types"
```

### 5. Push and Open a Pull Request

```bash
git push origin <your-username>/module-01
```

Then open a Pull Request on GitHub targeting the `main` branch.

### 6. PR Description Template for Students

When opening a pull request, use this format in the description:

```markdown
## Student Submission

**Name:** [Your Name]
**GitHub:** [Your GitHub Username]
**Module:** [Module Number]
**Days Covered:** [e.g., Day 001 -- Day 010]

## Summary

Brief description of what you completed in this submission.

## Self-Assessment

- [ ] All daily challenges completed
- [ ] Code runs without errors
- [ ] Code follows PEP 8 style guidelines
- [ ] Each solution includes comments where the logic is non-obvious
- [ ] No secrets, credentials, or environment files included
- [ ] No __pycache__ or compiled files included
```

---

## Community Contributions

Instructors, mentors, and community members can contribute by:

- Fixing typos or broken links in lesson materials.
- Improving explanations or adding examples.
- Adding new exercises or challenges.
- Translating materials.
- Reporting issues.

### Steps

1. Fork and clone the repository.
2. Create a feature branch: `git checkout -b fix/typo-in-day-005`.
3. Make your changes.
4. Ensure any existing tests still pass.
5. Commit with a clear message.
6. Push and open a Pull Request.

---

## Code Style

All Python code in this repository should follow [PEP 8](https://peps.python.org/pep-0008/):

- Use 4 spaces for indentation (no tabs).
- Limit lines to 79 characters for code, 72 for comments and docstrings.
- Use `snake_case` for functions and variables.
- Use `PascalCase` for class names.
- Use `UPPER_SNAKE_CASE` for constants.
- Include a blank line at the end of every file.
- Use meaningful, descriptive names for variables and functions.

---

## Commit Message Conventions

Write commit messages in the imperative mood. Keep the subject line under 72 characters. Use the body for additional context when needed.

**Format:**

```
<type>: <short description>

<optional body explaining why, not what>
```

**Types:**

| Type | When to Use |
| :--- | :--- |
| `add` | Adding new files, features, or exercises |
| `fix` | Fixing a bug or correcting an error |
| `update` | Improving or changing existing content |
| `docs` | Documentation-only changes |
| `refactor` | Restructuring code without changing behavior |
| `test` | Adding or updating tests |

**Examples:**

```
add: Day 015 solution for dictionary comprehensions
fix: correct variable name typo in Day 003 example
docs: improve explanation of inheritance in Module 04 README
```

---

## Pull Request Guidelines

- One PR per module (for student submissions) or per logical change (for contributions).
- Ensure your code runs without errors before submitting.
- Fill in the PR description completely.
- Do not include unrelated changes.
- Respond to review feedback promptly.

---

## Review Process

1. A maintainer or instructor will review your PR within a few days.
2. You may receive feedback requesting changes. This is part of the learning process.
3. Make the requested changes, commit, and push. The PR updates automatically.
4. Once approved, a maintainer will merge your PR.

Students may also participate in peer reviews. Reviewing others' code is an excellent way to learn. Be constructive, specific, and respectful in your feedback.

---

## What Not to Submit

Do not include any of the following in your submissions:

- `__pycache__/` directories or `.pyc` files
- `.env` files or any credentials, API keys, or secrets
- `venv/`, `.venv/`, or any virtual environment directories
- `.DS_Store`, `Thumbs.db`, or other OS-generated files
- Compiled binaries or build artifacts
- Node modules or other unrelated dependency directories
- Large datasets (use a `.gitignore` or link to external sources)

The repository `.gitignore` is configured to exclude most of these, but verify your staged files before committing:

```bash
git status
```

---

## Questions

If you have questions about the submission process:

1. Check the [Student Guide](docs/student-guide.md).
2. Ask your instructor or mentor.
3. Open a GitHub Issue describing your question.

Thank you for contributing to GeekInk Python Engineering.
