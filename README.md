# GeekInk Python Engineering

**100 Days. 100 Challenges. Real Engineering.**

A comprehensive, project-based Python Engineering Bootcamp by **GeekInk Innovations Ltd**.

---

## Mission

Empower aspiring software engineers, especially young people in Northern Nigeria, with practical programming skills, engineering thinking, collaborative learning, and the ability to build solutions to real-world problems.

---

## Table of Contents

- [Program Overview](#program-overview)
- [Curriculum](#curriculum)
- [Learning Outcomes](#learning-outcomes)
- [Project Milestones](#project-milestones)
- [Development Environment](#development-environment)
- [Getting Started](#getting-started)
- [Student Submission Workflow](#student-submission-workflow)
- [Assessment Criteria](#assessment-criteria)
- [Specializations](#specializations)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)
- [License](#license)

---

## Program Overview

GeekInk Python Engineering is a 100-day, project-based learning program that takes you from your first line of Python to building production-quality software. The curriculum is organized into 10 modules of 10 days each, progressing from fundamentals through object-oriented design, web development, data science, and machine learning.

Every day includes a focused lesson, practical examples, a coding challenge, and assessment criteria. Every module culminates in a real-world project milestone that you build, test, document, and present.

This is not a passive course. You will write code every day, collaborate with peers, review each other's work, and build a portfolio of projects that demonstrate genuine engineering skill.

---

## Curriculum

| Module | Title | Days | Key Topics |
| :--- | :--- | :---: | :--- |
| 01 | [Python Foundations](curriculum/module-01/) | 1--10 | Variables, data types, operators, strings, input/output, conditionals, debugging |
| 02 | [Data Structures and Problem Solving](curriculum/module-02/) | 11--20 | Lists, tuples, dictionaries, sets, loops, comprehensions, exception handling |
| 03 | [Functions, Modules and File Handling](curriculum/module-03/) | 21--30 | Functions, scope, lambda, modules, file I/O, CSV, JSON, virtual environments |
| 04 | [Object-Oriented Programming](curriculum/module-04/) | 31--40 | Classes, objects, encapsulation, inheritance, polymorphism, abstraction, SOLID |
| 05 | [Automation and Web Scraping](curriculum/module-05/) | 41--50 | OS/pathlib, regex, HTTP requests, APIs, Beautiful Soup, Selenium, email automation |
| 06 | [Database and Backend Engineering](curriculum/module-06/) | 51--60 | SQL, SQLite, PostgreSQL, SQLAlchemy, Flask, FastAPI, REST APIs, authentication |
| 07 | [GUI and Application Development](curriculum/module-07/) | 61--70 | Tkinter, widgets, event-driven programming, forms, database integration, packaging |
| 08 | [Data Science and Visualization](curriculum/module-08/) | 71--80 | Jupyter, NumPy, Pandas, data cleaning, Matplotlib, Seaborn, Plotly dashboards |
| 09 | [Software Engineering Practices](curriculum/module-09/) | 81--90 | PEP 8, testing, logging, Git workflows, documentation, Docker, CI/CD |
| 10 | [AI, Machine Learning and Capstone](curriculum/module-10/) | 91--100 | Scikit-learn, supervised/unsupervised learning, AI APIs, responsible AI, capstone |

Each module contains its own README with detailed day-by-day breakdown, learning objectives, and assessment criteria. See the [Curriculum Index](curriculum/README.md) for the complete syllabus.

---

## Learning Outcomes

By completing this program, you will be able to:

1. Write clean, well-structured Python code following professional conventions.
2. Design and implement object-oriented systems using established design principles.
3. Build and consume REST APIs with modern Python frameworks.
4. Work with relational databases and ORM tools.
5. Automate tasks, scrape web data responsibly, and integrate external APIs.
6. Build desktop applications with graphical user interfaces.
7. Analyze and visualize data using industry-standard Python libraries.
8. Write tests, use version control effectively, and follow CI/CD practices.
9. Apply machine learning fundamentals to solve practical problems.
10. Plan, build, document, and present a complete software project.

---

## Project Milestones

Each module concludes with a hands-on project that integrates the skills learned during those 10 days.

| Module | Project Milestone |
| :--- | :--- |
| 01 | Smart Personal Profile and Calculator |
| 02 | Student Result Processing System |
| 03 | Personal Expense Tracker |
| 04 | Student Management System |
| 05 | Automated Web Research Assistant |
| 06 | Student Management REST API |
| 07 | Desktop Inventory Management Application |
| 08 | Northern Nigeria Data Analysis Dashboard |
| 09 | Build, Test, Document and Deploy a Python Application |
| 10 | AI-Powered Python Solution (Capstone) |

Detailed project briefs are available in the [projects/](projects/) directory.

---

## Development Environment

Before starting, set up the following:

| Requirement | Version |
| :--- | :--- |
| Python | 3.10 or higher |
| Git | 2.30 or higher |
| Code Editor | VS Code (recommended) or any editor of your choice |
| pip | Latest (comes with Python) |
| Operating System | Windows 10+, macOS 12+, or Ubuntu 20.04+ |

### Setup Instructions

```bash
# 1. Verify Python is installed
python3 --version

# 2. Clone this repository
git clone https://github.com/geekinks/GeekInk-Python-Engineering.git
cd GeekInk-Python-Engineering

# 3. Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate    # Linux/macOS
# .venv\Scripts\activate     # Windows

# 4. Install dependencies
pip install -r requirements.txt
```

For detailed setup instructions, see [docs/environment-setup.md](docs/environment-setup.md).

---

## Getting Started

1. Read the [Student Guide](docs/student-guide.md) for a complete orientation.
2. Follow the [Environment Setup](docs/environment-setup.md) instructions.
3. Begin with [Module 01, Day 001](curriculum/module-01/day-001/).
4. Complete each day's lesson, guided practice, and daily challenge.
5. Submit your work following the [submission workflow](#student-submission-workflow).
6. Progress through all 10 modules over 100 days.

---

## Student Submission Workflow

1. Fork this repository to your own GitHub account.
2. Clone your fork locally.
3. Create your submission directory: `task/students/<your-github-username>/`.
4. For each day, save your work in: `task/students/<your-github-username>/module-XX/day-XXX/`.
5. Commit your work with clear, descriptive messages.
6. Push to your fork and open a Pull Request to this repository.

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed submission guidelines, PR templates, and code style requirements.

---

## Assessment Criteria

Student work is evaluated on five dimensions:

| Criterion | Weight | Description |
| :--- | :---: | :--- |
| Conceptual Understanding | 20% | Demonstrates grasp of core concepts and can explain reasoning |
| Practical Implementation | 30% | Code works correctly and solves the stated problem |
| Code Quality and Engineering Practices | 20% | Follows PEP 8, uses meaningful names, proper structure, error handling |
| Project Completion | 20% | Delivers all required features with tested, working functionality |
| Documentation and Presentation | 10% | Clear README, inline documentation where needed, organized submission |

For the full rubric with performance levels, see [docs/assessment-rubric.md](docs/assessment-rubric.md).

---

## Specializations

After completing the core 100-day curriculum, students can pursue focused specialization tracks:

- [Financial Python](specializations/financial-python/) -- Python for financial analysis, portfolio modeling, and forecasting.
- [Python Automation](specializations/automation/) -- Advanced automation, scripting, and DevOps tooling.
- [Data Science](specializations/data-science/) -- Deep data analysis, statistical modeling, and visualization.
- [Machine Learning](specializations/machine-learning/) -- Applied ML, model deployment, and AI engineering.

---

## Documentation

| Document | Description |
| :--- | :--- |
| [Student Guide](docs/student-guide.md) | How to use this repository, follow the curriculum, and submit work |
| [Instructor Guide](docs/instructor-guide.md) | Teaching philosophy, session structure, and mentorship guidelines |
| [Assessment Rubric](docs/assessment-rubric.md) | Grading framework with performance levels and criteria |
| [Environment Setup](docs/environment-setup.md) | Development environment installation and configuration |
| [Capstone Guidelines](docs/capstone-guidelines.md) | Final project requirements, evaluation, and presentation format |
| [Learning Resources](docs/learning-resources.md) | Recommended reading, official documentation, and community resources |

---

## Contributing

We welcome contributions from students, instructors, and the open-source community. Whether you are fixing a typo, improving an explanation, adding an exercise, or translating materials, your contribution matters.

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting a pull request.

---

## Acknowledgments

This curriculum is an original work by GeekInk Innovations Ltd, designed for community-driven technical education. It is inspired by the project-based teaching philosophy of modern Python bootcamps. All learning materials, examples, exercises, and projects are original GeekInk content.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

**GeekInk Innovations Ltd** -- Building the next generation of software engineers.
