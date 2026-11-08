# Day 040: Module 4 Project — Student Management System

## Learning Objectives

- Apply all OOP concepts (classes, encapsulation, inheritance, polymorphism, abstraction, composition) in a complete system.
- Design and implement a multi-entity domain model.
- Practice code organization, testing, and documentation.
- Demonstrate understanding through building, not just studying.

## Introduction

This is your Module 4 milestone project. Over the past ten days, you learned the core principles of object-oriented programming. Now you will apply them all together to build a Student Management System — a complete, multi-entity application that manages students, courses, grades, and attendance.

A comprehensive reference implementation already exists in this repository. Study it to understand the architectural patterns and design decisions, then build your own version. Your implementation does not need to be identical to the reference — it should demonstrate your understanding of OOP principles.

**Reference Implementation:** [Student Management System](../../../python-oop/projects/student-management-system/Readme.md)
- [Requirements](../../../python-oop/projects/student-management-system/requirements.md)
- [Architecture](../../../python-oop/projects/student-management-system/architecture.md)
- [Design](../../../python-oop/projects/student-management-system/design.md)
- [Source Code](../../../python-oop/projects/student-management-system/src/)
- [Tests](../../../python-oop/projects/student-management-system/tests/)

**OOP Lectures:** All lectures in [python-oop/lectures/](../../../python-oop/lectures/)

## Project Description

Build a Student Management System (SMS) that manages:

1. **Students** — Personal information, enrollment, grades, attendance.
2. **Courses** — Course details, enrolled students, assigned lecturers.
3. **Lecturers** — Personal information, assigned courses.
4. **Results** — Grade recording and GPA calculation.
5. **Attendance** — Attendance tracking and qualification checks.

## Requirements

### Core Entities

**User (Abstract Base Class)**
- Attributes: name, user_id, email
- Abstract method: `display_info()`
- Concrete method: `__str__()`

**Student (inherits User)**
- Additional: department, enrollment date, list of courses, results, attendance records
- Methods: enroll in course, view grades, view attendance, calculate GPA

**Lecturer (inherits User)**
- Additional: department, specialization, list of courses taught
- Methods: assign to course, record grade for student, view assigned courses

**Course**
- Attributes: code, name, credits, department, max capacity
- Composition: has enrolled students, has assigned lecturer
- Methods: add student, remove student, is full, display info

**Result**
- Attributes: student, course, score, grade letter
- Methods: calculate grade letter from score, display

**Attendance**
- Attributes: student, course, date, status (present/absent/excused)
- Methods: check attendance percentage, check exam qualification (minimum 75% attendance)

### OOP Principles Required

Your implementation must demonstrate:

| Principle | Where |
|-----------|-------|
| Encapsulation | Private/protected attributes with property access and validation |
| Inheritance | User -> Student, User -> Lecturer |
| Polymorphism | `display_info()` implemented differently in Student and Lecturer |
| Abstraction | User as an abstract base class with abstract methods |
| Composition | Course HAS students, Student HAS results, Student HAS attendance |

### Functional Requirements

Your SMS must support:

1. Register a new student.
2. Register a new lecturer.
3. Create a new course.
4. Enroll a student in a course.
5. Assign a lecturer to a course.
6. Record a student's grade for a course.
7. Record attendance for a student.
8. View a student's complete report (courses, grades, GPA, attendance).
9. View a course's details (enrolled students, lecturer, capacity).
10. Check if a student qualifies to sit for exams (attendance >= 75%).

## Suggested Architecture

```
day-040/
    models/
        __init__.py
        user.py          # Abstract User base class
        student.py       # Student class
        lecturer.py      # Lecturer class
        course.py        # Course class
        result.py        # Result class
        attendance.py    # Attendance class
    main.py              # CLI application or demo script
    README.md            # Your project documentation
```

You may use a simpler file structure (fewer files) if you prefer, as long as the code is well-organized.

## Implementation Milestones

### Milestone 1: Core Models
Create the User, Student, and Lecturer classes with proper inheritance and encapsulation.

### Milestone 2: Course Management
Create the Course class with enrollment and capacity management.

### Milestone 3: Results and Grading
Create the Result class with grade calculation. Implement grade recording through the Lecturer.

### Milestone 4: Attendance
Create the Attendance class with tracking and qualification checking.

### Milestone 5: Integration
Build a main script or CLI that ties everything together and demonstrates all features.

## Grading Scale

Use the following grade scale:

| Score | Grade |
|-------|-------|
| 70-100 | A |
| 60-69 | B |
| 50-59 | C |
| 45-49 | D |
| 0-44 | F |

## Testing Requirements

Write tests or demonstrate that:

1. Students and lecturers can be created with valid data.
2. Invalid data (negative age, empty name) is rejected.
3. Students can enroll in courses that are not full.
4. Enrollment in a full course is rejected.
5. Grades are recorded and GPA is calculated correctly.
6. Attendance percentage is calculated correctly.
7. Exam qualification check works (75% threshold).
8. Polymorphic `display_info()` works for both Student and Lecturer.

You can write formal tests using `unittest` or demonstrate correctness through a comprehensive demo script.

## Expected Deliverables

1. All source code files.
2. A `README.md` explaining your project, how to run it, and the OOP principles you applied.
3. A demo script or test file that demonstrates all features.

## Evaluation Criteria

| Criterion | Weight | Description |
|-----------|--------|-------------|
| OOP Design | 25% | Proper use of all five OOP principles |
| Functionality | 25% | All required features work correctly |
| Code Quality | 20% | Clean, readable, well-organized code |
| Encapsulation & Validation | 15% | Data protection and input validation |
| Documentation | 15% | README, docstrings, code comments where necessary |

## Example Demo Output

```
=== Student Management System ===

Registering students...
  Registered: Amina Bello (STU001) — Computer Science

Registering lecturers...
  Registered: Dr. Ibrahim (LEC001) — Computer Science

Creating courses...
  Created: CS101 — Introduction to Python (4 credits, capacity: 30)

Enrolling students...
  Amina enrolled in CS101

Assigning lecturers...
  Dr. Ibrahim assigned to CS101

Recording grades...
  Amina — CS101: 85 (Grade: A)

Recording attendance...
  Amina — CS101: Present (2024-11-01)
  Amina — CS101: Present (2024-11-02)
  Amina — CS101: Absent (2024-11-03)

=== Student Report: Amina Bello ===
  Department: Computer Science
  Courses: CS101
  GPA: 4.0
  CS101 Attendance: 66.7% — WARNING: Below exam threshold

=== Course Report: CS101 ===
  Course: Introduction to Python
  Lecturer: Dr. Ibrahim
  Enrolled: 1/30 students
  Students: Amina Bello
```

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-04/day-040/`

Include all source files and your project README.

## Additional Resources

- [Student Management System Reference](../../../python-oop/projects/student-management-system/Readme.md)
- [OOP Lectures (all)](../../../python-oop/lectures/)
- [OOP Exercises (all)](../../../python-oop/exercises/)
- [Capstone Assignments](../../../python-oop/projects/assignments/)

## Reflection

- Which OOP principle was the most challenging to apply? Why?
- How did the reference implementation help or hinder your own design?
- If you were to extend this system with one more feature (timetable, payments, notifications), how would you design it using OOP principles?
