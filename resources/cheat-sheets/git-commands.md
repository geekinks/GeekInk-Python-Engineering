# Git Commands Cheat Sheet

## Setup

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## Starting a Project

```bash
git clone <url>             # Clone a repository
git init                    # Initialize a new repository
```

## Daily Workflow

```bash
git status                  # See what has changed
git add <file>              # Stage a specific file
git add .                   # Stage all changes
git commit -m "message"     # Commit staged changes
git push                    # Push to remote
git pull                    # Pull latest changes
```

## Branching

```bash
git branch                  # List branches
git branch <name>           # Create a branch
git checkout <name>         # Switch to a branch
git checkout -b <name>      # Create and switch
git merge <branch>          # Merge branch into current
git branch -d <name>        # Delete a branch
```

## Viewing History

```bash
git log                     # Full commit history
git log --oneline           # Compact history
git diff                    # Unstaged changes
git diff --staged           # Staged changes
```

## Undoing Changes

```bash
git checkout -- <file>      # Discard unstaged changes
git reset HEAD <file>       # Unstage a file
git stash                   # Temporarily save changes
git stash pop               # Restore stashed changes
```

## Working with Remotes

```bash
git remote -v               # List remotes
git fetch                   # Download remote changes
git push -u origin <branch> # Push and set upstream
```

## Student Submission Workflow

```bash
# 1. Fork the repository on GitHub
# 2. Clone your fork
git clone https://github.com/YOUR-USERNAME/GeekInk-Python-Engineering.git

# 3. Create a branch for your work
git checkout -b module-01-solutions

# 4. Add your work
# Place files in: task/students/YOUR-USERNAME/module-01/day-001/
git add task/students/YOUR-USERNAME/

# 5. Commit
git commit -m "Add Day 001 solution: personal profile generator"

# 6. Push
git push -u origin module-01-solutions

# 7. Open a Pull Request on GitHub
```

## Commit Message Guidelines

```
Add Day 005 solution: interactive profile generator
Fix calculation error in expense tracker
Update README with setup instructions
```

Keep messages short, specific, and in the imperative mood ("Add", not "Added").
