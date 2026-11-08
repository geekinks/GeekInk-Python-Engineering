# Student Guide

**GeekInk Python Engineering — 100 Days. 100 Challenges. Real Engineering.**

This guide explains how to use the GeekInk Python Engineering repository, follow the 100-day curriculum, submit your work, and build your engineering portfolio.

---

## Table of Contents

- [Getting Started](#getting-started)
- [Navigating the Curriculum](#navigating-the-curriculum)
- [Daily Workflow](#daily-workflow)
- [Submission Structure](#submission-structure)
- [Submitting Your Work via Pull Request](#submitting-your-work-via-pull-request)
- [Getting Help](#getting-help)
- [Building Your Portfolio](#building-your-portfolio)
- [Assessment Criteria](#assessment-criteria)

---

## Getting Started

### 1. Fork the Repository

Go to the [GeekInk Python Engineering](https://github.com/geekinks/GeekInk-Python-Engineering) repository on GitHub and click **Fork** to create your own copy.

### 2. Clone Your Fork

```bash
git clone https://github.com/YOUR-GITHUB-USERNAME/GeekInk-Python-Engineering.git
cd GeekInk-Python-Engineering
```

### 3. Install Python 3.10 or Later

Verify your Python version:

```bash
python3 --version
```

If you need to install Python, see the [Environment Setup Guide](environment-setup.md).

### 4. Create a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate   # Linux / macOS
# .venv\Scripts\activate    # Windows
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Set Up Git Identity

```bash
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

### 7. Add the Upstream Remote

```bash
git remote add upstream https://github.com/geekinks/GeekInk-Python-Engineering.git
```

This lets you pull updates from the main repository.

---

## Navigating the Curriculum

The curriculum is organized into **10 modules**, each containing **10 days** of lessons:

```
curriculum/
  module-01/          # Python Foundations (Days 1-10)
    day-001/
    day-002/
    ...
    day-010/
  module-02/          # Data Structures and Problem Solving (Days 11-20)
    day-011/
    ...
  ...
  module-10/          # AI, Machine Learning and Capstone (Days 91-100)
    day-091/
    ...
    day-100/
```

Each day's folder contains:

- **README.md** — The lesson itself, including objectives, concepts, examples, and the daily challenge.
- **examples/** — Runnable Python files that demonstrate the day's concepts (when applicable).
- **starter.py** — A scaffold for the daily challenge (when provided).

Start at `curriculum/module-01/day-001/README.md` and work through the days in order. Modules build on each other, so do not skip ahead unless you are confident in the prerequisites.

---

## Daily Workflow

Follow this routine for each day of the program:

1. **Read the Lesson README** — Understand the learning objectives and study the concepts.
2. **Run the Examples** — Execute any provided example scripts to see the concepts in action.
3. **Complete the Guided Practice** — Follow the guided coding activity in the lesson.
4. **Solve the Daily Challenge** — Work through the challenge independently. This is your primary assessment for the day.
5. **Write Your Solution** — Save your code in your personal submission directory (see below).
6. **Reflect** — Answer the reflection questions at the end of the lesson. Write your answers in a `reflection.md` file or as comments in your solution.
7. **Commit and Push** — Commit your work with a meaningful message and push to your fork.

---

## Submission Structure

Organize your submissions in the `task/students/` directory using your GitHub username:

```
task/students/your-github-username/
  README.md               # Brief intro about yourself
  module-01/
    day-001/
      solution.py          # Your daily challenge solution
      reflection.md        # Optional: your reflection notes
    day-002/
      solution.py
    ...
  module-02/
    day-011/
      solution.py
    ...
  module-04/
    milestone/
      README.md            # Your module milestone project
      main.py
      ...
```

### Rules for Submissions

- Use your actual GitHub username as your directory name.
- Keep one directory per day, named to match the curriculum (e.g., `day-001`).
- Include only source files. Do not submit:
  - Virtual environment directories (`.venv/`, `venv/`)
  - `__pycache__/` directories
  - `.env` files or secrets
  - IDE configuration files
  - Large binary files or datasets (unless the exercise requires a small one)
- For module milestone projects, create a `milestone/` directory inside the relevant module folder.

---

## Submitting Your Work via Pull Request

When you are ready to submit your work for review:

### 1. Sync with Upstream

```bash
git fetch upstream
git merge upstream/main
```

### 2. Create a Submission Branch

```bash
git checkout -b submission/your-username/module-01
```

Use a descriptive branch name that includes your username and the module or day range.

### 3. Add and Commit Your Work

```bash
git add task/students/your-username/module-01/
git commit -m "Submit Module 01 exercises (Days 1-10)"
```

Write clear commit messages. Describe what you completed, not just "added files."

### 4. Push to Your Fork

```bash
git push origin submission/your-username/module-01
```

### 5. Open a Pull Request

Go to your fork on GitHub and click **New Pull Request**. Set the base repository to `geekinks/GeekInk-Python-Engineering` and the base branch to `main`.

In your PR description, include:

- Which module and days you are submitting.
- A brief summary of what you learned.
- Any questions or areas where you need feedback.

### 6. Respond to Feedback

Instructors and peers may leave review comments on your PR. Address feedback by pushing additional commits to the same branch. Do not open a new PR for revisions.

---

## Getting Help

### GitHub Issues

If you find a bug in the curriculum, a broken example, or unclear instructions, open an issue on the main repository.

### GitHub Discussions

Use the Discussions tab for general questions, study group coordination, and sharing resources with fellow students.

### Peer Review

You are encouraged to review your peers' pull requests. Reading others' code is one of the most effective ways to learn. Be constructive and specific in your feedback.

### Instructor Office Hours

Your instructor will communicate office hours and communication channels at the start of the cohort. Use these for questions that require in-depth guidance.

---

## Building Your Portfolio

The 100-day program is designed to produce portfolio-ready work. To maximize this:

1. **Write clear README files** for your milestone projects explaining the problem, your approach, and how to run the code.
2. **Use meaningful commit messages** that show your thought process and progress.
3. **Refactor your solutions** after receiving feedback — employers value iteration.
4. **Pin your best projects** on your GitHub profile.
5. **Write about your learning journey** — a blog post or technical article about a challenge you solved demonstrates communication skills.
6. **Maintain clean repositories** — no leftover debug code, no commented-out blocks, no stale files.

By Day 100, you should have:

- A series of well-documented Python projects at increasing levels of complexity.
- Experience with Git workflows, pull requests, and code review.
- A capstone project demonstrating your ability to design, build, test, and present a complete application.

---

## Assessment Criteria

Your work is evaluated across five dimensions:

| Category | Weight | What Is Evaluated |
| :--- | :---: | :--- |
| Conceptual Understanding | 20% | Accuracy of explanations, reflection depth, ability to articulate concepts |
| Practical Implementation | 30% | Correctness of solutions, completeness of exercises, functionality of projects |
| Code Quality and Engineering Practices | 20% | Readability, structure, naming, error handling, use of Git |
| Project Completion | 20% | Delivery of milestone and capstone projects with all required features |
| Documentation and Presentation | 10% | README quality, inline documentation, presentation clarity |

For full details, see the [Assessment Rubric](assessment-rubric.md).

---

## Summary

1. Fork and clone the repository.
2. Set up Python and your development environment.
3. Work through one day at a time, starting from Day 1.
4. Submit your work in `task/students/your-github-username/`.
5. Open pull requests for review.
6. Learn from feedback and peer code.
7. Build a portfolio you are proud of.

Welcome to GeekInk Python Engineering. Start building.
