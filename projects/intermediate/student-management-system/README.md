# Student Management System

**Module:** 4 — Object-Oriented Programming
**Day:** 40
**Difficulty:** Intermediate

---

## Problem Statement

Educational institutions need comprehensive systems to manage student records, course enrollments, attendance, and academic results. This project applies every OOP concept from Module 4 — classes, encapsulation, inheritance, polymorphism, abstraction, composition, and SOLID principles — to build a complete Student Management System.

## Reference Implementation

A complete, production-grade reference implementation exists in this repository:

- **Overview:** [python-oop/projects/student-management-system/Readme.md](../../../python-oop/projects/student-management-system/Readme.md)
- **Requirements:** [python-oop/projects/student-management-system/requirements.md](../../../python-oop/projects/student-management-system/requirements.md)
- **Architecture:** [python-oop/projects/student-management-system/architecture.md](../../../python-oop/projects/student-management-system/architecture.md)
- **Design:** [python-oop/projects/student-management-system/design.md](../../../python-oop/projects/student-management-system/design.md)
- **Source code:** [python-oop/projects/student-management-system/src/](../../../python-oop/projects/student-management-system/src/)
- **Tests:** [python-oop/projects/student-management-system/tests/](../../../python-oop/projects/student-management-system/tests/)

Study the reference implementation to understand the design decisions. Then build your own version independently.

## Objectives

- Model real-world entities as classes with attributes and methods.
- Apply encapsulation to protect data integrity.
- Use inheritance to share behavior between related entities.
- Implement polymorphism for flexible, extensible interfaces.
- Use abstraction to define contracts.
- Apply composition to build complex objects from simpler ones.
- Follow SOLID principles in your design.

## Requirements

### Core Entities

1. **User** (abstract base class) — name, email, ID.
2. **Student** (inherits User) — enrollment date, courses, results, attendance.
3. **Lecturer** (inherits User) — department, courses taught.
4. **Course** — name, code, credits, enrolled students, lecturer.
5. **Result** — student, course, score, grade.
6. **Attendance** — student, course, date, status (present/absent/excused).

### Functional Requirements

- Register and manage students and lecturers.
- Create courses and assign lecturers.
- Enroll students in courses.
- Record and calculate results with automatic grading.
- Track attendance and calculate attendance percentages.
- Generate reports (per student, per course, class-wide).

### Design Requirements

- Use an abstract base class for User.
- Encapsulate all entity state behind properties with validation.
- Use composition (students have results and attendance records).
- Apply at least one design pattern (e.g., Strategy for grading).
- Write unit tests for all core classes.

## Technologies

- Python 3.10+
- Standard library (`abc`, `datetime`, `unittest`)

## Implementation Milestones

| Milestone | Description |
| :--- | :--- |
| 1. User hierarchy | Create User ABC, Student, and Lecturer classes |
| 2. Course management | Create Course class, implement enrollment |
| 3. Results | Implement Result class and grading logic |
| 4. Attendance | Implement Attendance tracking |
| 5. CLI interface | Build a menu-driven interface |
| 6. Testing | Write unit tests for all classes |

## Testing Requirements

- Write at least 15 unit tests covering all core classes.
- Test edge cases: duplicate enrollment, invalid scores, empty records.
- Run tests with: `python3 -m unittest discover -s tests -p "test_*.py"`

## Expected Deliverables

1. Source code organized in a `src/` directory with separate modules per entity.
2. Unit tests in a `tests/` directory.
3. A `README.md` documenting how to run the project.

## Evaluation Criteria

| Criterion | Weight | Description |
| :--- | :--- | :--- |
| OOP concepts applied | 30% | Correct use of inheritance, encapsulation, polymorphism, abstraction, composition |
| Code quality | 20% | Clean, readable, PEP 8 compliant |
| Functionality | 20% | All required features working |
| Testing | 15% | Comprehensive unit tests passing |
| Design principles | 15% | SOLID principles followed, sensible class design |
