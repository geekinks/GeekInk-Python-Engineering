# Capstone Project Guidelines

**GeekInk Python Engineering — 100 Days. 100 Challenges. Real Engineering.**

The capstone project is the culminating assessment of the 100-day program. It spans Module 10 (Days 91-100) and requires you to design, build, test, document, and present an original Python application that solves a real-world problem.

---

## Table of Contents

- [Overview](#overview)
- [Timeline](#timeline)
- [Requirements](#requirements)
- [Project Proposal](#project-proposal)
- [Technical Requirements](#technical-requirements)
- [Deliverables](#deliverables)
- [Evaluation Criteria](#evaluation-criteria)
- [Presentation and Defense](#presentation-and-defense)
- [Portfolio Integration](#portfolio-integration)
- [Example Project Ideas](#example-project-ideas)

---

## Overview

The capstone is your opportunity to demonstrate everything you have learned across the 100-day program. Unlike daily challenges and module milestones, the capstone is self-directed: you choose the problem, design the solution, and build it end-to-end.

The project must be an **AI-powered Python application** that addresses a practical problem. It should integrate concepts from multiple modules: data handling, object-oriented design, API interaction, testing, and deployment readiness.

---

## Timeline

| Day | Activity |
| :--- | :--- |
| Day 91-92 | Explore ideas, research feasibility, write project proposal |
| Day 93-94 | Design architecture, define data models, plan features |
| Day 95-97 | Core implementation |
| Day 98 | Testing, debugging, and refinement |
| Day 99 | Documentation and deployment preparation |
| Day 100 | Final presentation and technical defense |

---

## Requirements

### Scope

Your project must:

- Solve a clearly defined, real-world problem.
- Be original work — not a tutorial copy, not a clone of an existing open-source project.
- Be feasible to build within 10 days given your current skill level.
- Be complex enough to demonstrate intermediate Python engineering skills.

### What "AI-Powered" Means

Your project must incorporate at least one of the following:

- A machine learning model trained with scikit-learn or a similar library.
- Integration with an AI API (such as a language model, image recognition, or recommendation service).
- Data analysis and prediction using statistical methods.
- An intelligent automation that makes decisions based on data.

The AI component must be meaningful to the application, not a superficial addition.

---

## Project Proposal

Before starting implementation, submit a written proposal (1-2 pages) covering:

1. **Problem Statement** — What problem are you solving? Who benefits from this solution?
2. **Proposed Solution** — How will your application address the problem?
3. **Target Users** — Who will use this application?
4. **Key Features** — List 4-6 core features.
5. **Technology Stack** — What libraries, frameworks, APIs, and data sources will you use?
6. **Data Sources** — Where will your data come from? Is it ethically sourced?
7. **AI/ML Component** — What is the intelligent component and how does it add value?
8. **Architecture Sketch** — A high-level diagram of the application's structure.
9. **Risk Assessment** — What could go wrong and how will you handle it?

Submit your proposal as `task/students/your-username/module-10/proposal.md`.

---

## Technical Requirements

Your capstone must meet these engineering standards:

### Code Quality

- Follow PEP 8 style conventions.
- Use meaningful variable and function names.
- Organize code into modules with clear separation of concerns.
- Use object-oriented design where appropriate.
- Handle errors gracefully with appropriate exception handling.

### Project Structure

```
capstone-project-name/
  README.md
  requirements.txt
  src/
    __init__.py
    main.py
    ...
  tests/
    __init__.py
    test_*.py
  data/           # if applicable
  docs/           # if applicable
```

### Testing

- Write unit tests using `unittest` or `pytest`.
- Aim for meaningful test coverage of core logic.
- All tests must pass.

### Version Control

- Use Git throughout development.
- Make frequent, descriptive commits.
- Your Git history should show the evolution of the project.

### Documentation

- Provide a comprehensive README (see Deliverables below).
- Include docstrings for public functions and classes.

### Dependencies

- List all dependencies in `requirements.txt` with pinned versions.
- Do not include unnecessary packages.
- Do not commit virtual environment directories.

---

## Deliverables

Submit the following in `task/students/your-username/module-10/capstone/`:

1. **Project Proposal** (`proposal.md`) — Your original proposal.
2. **Source Code** — Complete, runnable application code.
3. **Tests** — A test suite that validates core functionality.
4. **README.md** — A project README that includes:
   - Project title and description.
   - Problem statement.
   - Features.
   - Technology stack.
   - Installation and setup instructions.
   - Usage instructions with examples.
   - Architecture overview.
   - Testing instructions.
   - Known limitations.
   - Future improvements.
5. **Requirements File** (`requirements.txt`) — All dependencies.
6. **Presentation Slides or Notes** — Materials for your Day 100 presentation.

---

## Evaluation Criteria

The capstone is evaluated more rigorously than module milestones:

| Criterion | Weight | Description |
| :--- | :---: | :--- |
| Problem Definition | 10% | Clarity, relevance, and scope of the problem |
| Architecture and Design | 15% | Quality of abstractions, data models, and component organization |
| Implementation | 25% | Correctness, completeness, and functionality |
| Testing | 15% | Test coverage, test quality, and passing tests |
| Code Quality | 15% | PEP 8 compliance, readability, structure, error handling |
| Documentation | 10% | README quality, setup instructions, usage guide |
| Presentation and Defense | 10% | Clarity of explanation, ability to answer technical questions |

Total: 100%

A passing capstone requires at least 50% overall and at least 40% in each individual criterion.

---

## Presentation and Defense

On Day 100, you will present your capstone to instructors and peers. The presentation has two parts:

### Part 1: Project Presentation (10-15 minutes)

- Explain the problem you solved and why it matters.
- Demonstrate the working application.
- Walk through the architecture and key design decisions.
- Show your AI/ML component and explain how it works.
- Highlight one technical challenge you overcame.

### Part 2: Technical Defense (5-10 minutes)

Instructors will ask questions such as:

- Why did you choose this architecture?
- How would you scale this application?
- What would you change if you had more time?
- Explain how a specific function or class works.
- What tradeoffs did you make?

### Presentation Tips

- Practice your demo beforehand. Have a backup plan if a live demo fails.
- Focus on decisions and tradeoffs, not a line-by-line code walkthrough.
- Be honest about limitations — acknowledging gaps shows maturity.
- Prepare for questions about fundamentals (OOP, testing, data handling), not just your specific project.

---

## Portfolio Integration

Your capstone should be portfolio-ready:

1. **Standalone Repository** — Consider also publishing your capstone as its own GitHub repository with a polished README, so it stands independently on your profile.
2. **Pin It** — Pin the project on your GitHub profile.
3. **Screenshots or Demo** — Include screenshots or a short demo video/GIF in your README.
4. **Clean History** — Ensure your Git history is clean and meaningful (no "fix typo" chains or committed secrets).
5. **License** — Add an appropriate open-source license if you want others to use your work.
6. **Reflect** — Write a short blog post or article about what you built and what you learned. This demonstrates communication skills to employers.

---

## Example Project Ideas

These are starting points. You are encouraged to adapt them to problems relevant to your community or interests.

- **School Performance Predictor** — Analyze student data to predict academic performance and suggest interventions.
- **Crop Yield Estimator** — Use agricultural data to predict harvest yields for local farming communities.
- **Health Symptom Checker** — An application that takes symptom input and suggests possible conditions using a trained classifier.
- **Local Market Price Tracker** — Scrape or collect market prices, analyze trends, and predict future prices.
- **Automated Document Classifier** — Classify documents by type or topic using natural language processing.
- **Personal Finance Advisor** — Analyze spending data and provide budgeting recommendations.
- **Weather-Based Activity Recommender** — Combine weather API data with user preferences to suggest daily activities.
- **Inventory Management with Demand Forecasting** — Predict product demand and optimize stock levels.

Choose a problem you care about. The best capstones solve problems that matter to the builder.
