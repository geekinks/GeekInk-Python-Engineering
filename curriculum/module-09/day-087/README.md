# Day 087: Git and GitHub Workflows

## Learning Objectives

- Understand the core Git commands for daily development work.
- Use branches to work on features without affecting the main codebase.
- Choose between merge and rebase for integrating changes.
- Resolve merge conflicts confidently.
- Follow a professional branching strategy suitable for team collaboration.

## Introduction

Git is the version control system used by virtually every professional software team in the world. You have been using basic Git commands throughout this course --- `git add`, `git commit`, `git push`. Today you will learn the workflows that teams use to collaborate on the same codebase without stepping on each other's work.

The central idea is branching. Instead of everyone committing directly to the `main` branch, each developer creates a separate branch for their feature or bug fix. They work on that branch independently, and when their work is ready, they merge it back into `main`. This means `main` always contains working, reviewed code, while experimental or in-progress work stays isolated on branches.

Conflicts happen when two people change the same lines in the same file. Git cannot automatically decide which change to keep, so it asks you to resolve the conflict manually. This sounds intimidating, but with practice it becomes routine. Understanding how to read conflict markers and make the right decision is an essential skill.

## Concepts

### Git Workflow Overview

```
main ──────────────────────────────────────────►
  │                                        ▲
  └── feature/add-login ──── commits ──── merge
```

### Essential Commands

```bash
# Check current status
git status

# Create and switch to a new branch
git checkout -b feature/my-feature

# Stage changes
git add filename.py

# Commit with a message
git commit -m "Add login validation"

# Push branch to remote
git push -u origin feature/my-feature

# Switch back to main
git checkout main

# Pull latest changes from remote
git pull origin main

# Merge a branch into current branch
git merge feature/my-feature

# Delete a branch after merging
git branch -d feature/my-feature
```

### Branching Strategies

**Feature Branch Workflow** (most common for small teams):
1. Create a branch from `main` for each feature.
2. Work, commit, and push to that branch.
3. Open a Pull Request for review.
4. Merge into `main` after approval.

**Branch Naming Conventions:**
- `feature/add-user-registration`
- `fix/login-error-handling`
- `docs/update-readme`

### Merge vs Rebase

**Merge** creates a merge commit that preserves the full branch history:
```bash
git checkout main
git merge feature/my-feature
```

**Rebase** replays your commits on top of the latest main, creating a linear history:
```bash
git checkout feature/my-feature
git rebase main
```

Use merge for shared branches and PRs. Use rebase for cleaning up local commits before pushing.

### Resolving Conflicts

When Git cannot automatically merge, it marks the conflicting sections:

```
<<<<<<< HEAD
def greet(name):
    return f"Hello, {name}!"
=======
def greet(name):
    return f"Hi there, {name}!"
>>>>>>> feature/new-greeting
```

To resolve:
1. Open the file and find the conflict markers.
2. Decide which version to keep (or combine them).
3. Remove the `<<<<<<<`, `=======`, and `>>>>>>>` markers.
4. Stage the file: `git add filename.py`
5. Complete the merge: `git commit`

## Practical Examples

### Example: Complete feature branch workflow

```bash
# 1. Start from an up-to-date main
git checkout main
git pull origin main

# 2. Create a feature branch
git checkout -b feature/student-search

# 3. Make changes
# ... edit files ...
git add search.py
git commit -m "Add student search by name"

# ... more changes ...
git add search.py test_search.py
git commit -m "Add unit tests for student search"

# 4. Push to remote
git push -u origin feature/student-search

# 5. (Open a Pull Request on GitHub)

# 6. After PR is approved, merge
git checkout main
git pull origin main
git merge feature/student-search

# 7. Push the updated main
git push origin main

# 8. Clean up
git branch -d feature/student-search
git push origin --delete feature/student-search
```

### Example: Useful Git commands

```bash
# View commit history (compact)
git log --oneline --graph --all

# See what changed in the last commit
git diff HEAD~1

# Undo the last commit but keep changes
git reset --soft HEAD~1

# Stash work in progress
git stash
git stash pop  # restore later

# See all branches
git branch -a
```

## Guided Practice

This exercise simulates a team workflow on your local machine using two branches.

1. Initialize a new practice repository:

```bash
mkdir git-workflow-practice
cd git-workflow-practice
git init
```

2. Create initial content on main:

```python
# app.py
def greet(name):
    return f"Hello, {name}!"

def farewell(name):
    return f"Goodbye, {name}!"

if __name__ == "__main__":
    print(greet("Amina"))
    print(farewell("Amina"))
```

```bash
git add app.py
git commit -m "Initial commit: greeting app"
```

3. Create a feature branch and make changes:

```bash
git checkout -b feature/add-formal-greeting
```

Edit `app.py` to add:
```python
def formal_greet(name, title="Mr."):
    return f"Good day, {title} {name}."
```

```bash
git add app.py
git commit -m "Add formal greeting function"
```

4. Switch back to main and make a conflicting change:

```bash
git checkout main
```

Edit the `greet` function to change its message:
```python
def greet(name):
    return f"Welcome, {name}!"
```

```bash
git add app.py
git commit -m "Update greeting message"
```

5. Merge the feature branch:

```bash
git merge feature/add-formal-greeting
```

6. If there is a conflict, resolve it. Keep both the updated greeting and the new formal_greet function.

7. Verify the final file is correct and commit.

## Daily Challenge

Simulate a two-developer workflow that includes branching, parallel work, a merge conflict, and resolution.

1. Create a repository with a Python file `student_registry.py`:

```python
class StudentRegistry:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name):
        self.students[student_id] = {"name": name, "courses": []}

    def get_student(self, student_id):
        return self.students.get(student_id)

    def list_students(self):
        return list(self.students.values())
```

2. Commit this to main.

3. Create branch `feature/enroll-course` and add an `enroll` method.

4. Switch back to main, create branch `feature/add-gpa` and add a `gpa` field to the student dict in `add_student`.

5. Merge `feature/enroll-course` into main first (should be clean).

6. Then merge `feature/add-gpa` into main (this should conflict because both branches modified `add_student`).

7. Resolve the conflict so that the final `add_student` method includes both the `courses` list and the `gpa` field.

8. Document the entire process: every command you ran, what the conflict looked like, and how you resolved it.

## Expected Output

A completed `student_registry.py` on main that includes:
- The original `add_student`, `get_student`, `list_students` methods.
- The new `enroll` method from one branch.
- The `gpa` field from the other branch.

A document (`workflow_log.md`) recording every Git command and the conflict resolution.

## Assessment

1. Why should developers work on feature branches instead of committing directly to main?
2. What is the difference between `git merge` and `git rebase`?
3. Describe the three-step process for resolving a merge conflict.

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-09/day-087/`

Include:
- `student_registry.py` (final merged version)
- `workflow_log.md` (record of all commands and decisions)

## Additional Resources

- [Pro Git Book (free)](https://git-scm.com/book/en/v2)
- [GitHub Flow guide](https://docs.github.com/en/get-started/using-github/github-flow)

## Reflection

- How comfortable are you now with resolving merge conflicts compared to before this lesson?
- In a team of 5 developers, what would happen if everyone committed directly to main without branches?
