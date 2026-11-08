# Day 031: Procedural vs Object-Oriented Programming

## Learning Objectives

- Understand what procedural programming is and where its limitations appear.
- Recognize the problems of managing state with plain variables and functions.
- Understand the motivation behind object-oriented programming.
- Begin thinking in terms of objects, attributes, and behaviors.
- Identify real-world entities that map to classes and objects.

## Introduction

Until now, you have been writing procedural code — defining variables and functions, calling them in sequence. This approach works well for small programs, but as your software grows, procedural code becomes increasingly difficult to manage. Variables multiply, functions need more and more parameters, and changing one part of the program breaks another.

Object-oriented programming (OOP) addresses this by organizing code around objects — entities that bundle related data (attributes) and behavior (methods) together. Instead of passing a student's name, age, ID, and grades to every function separately, you create a Student object that carries all of its own data and knows how to perform its own operations.

This lesson introduces the "why" of OOP. Before learning the syntax, you need to understand the problem it solves. This module integrates with the comprehensive OOP curriculum in the `python-oop/` directory. For a deeper dive into today's topic, see the corresponding lecture.

**Reference:** [Lecture 01 — Python & OOP Introduction](../../../python-oop/lectures/01-python-oop-introduction.md)

## Concepts

### Procedural Programming

In procedural programming, you organize code as a sequence of instructions. Data is stored in variables, and functions operate on that data.

```python
student_name = "Amina"
student_age = 20
student_scores = [85, 90, 78]

def calculate_average(scores):
    return sum(scores) / len(scores)

avg = calculate_average(student_scores)
print(f"{student_name}: {avg}")
```

This works fine for one student. But what about 100 students?

### The State Sprawl Problem

```python
student1_name = "Amina"
student1_age = 20
student1_scores = [85, 90, 78]

student2_name = "Musa"
student2_age = 22
student2_scores = [72, 68, 80]

# Every function needs all the pieces passed separately
def print_report(name, age, scores):
    avg = sum(scores) / len(scores)
    print(f"{name} (age {age}): average = {avg:.1f}")
```

As the program grows, you end up with dozens of loosely connected variables and functions that have long parameter lists. Adding a new field (like "department") means modifying every function.

### Thinking in Objects

OOP asks: "What are the things (entities) in this problem, and what data and behavior does each one have?"

For a school system:
- A **Student** has a name, age, ID, and scores. It can calculate its average and check if it passed.
- A **Course** has a name, code, and list of enrolled students. It can add or remove students.
- A **Lecturer** has a name, department, and list of courses they teach.

Each entity becomes a class. Each instance of a class is an object.

### Why OOP Matters in Engineering

- **Organization:** Related data and behavior live together.
- **Reusability:** A class defined once can create unlimited objects.
- **Maintainability:** Changes to one class do not cascade through the entire program.
- **Modeling:** Real-world systems map naturally to objects and relationships.

## Practical Examples

```python
# The procedural way — managing multiple students
students = [
    {"name": "Amina", "age": 20, "scores": [85, 90, 78]},
    {"name": "Musa", "age": 22, "scores": [72, 68, 80]},
    {"name": "Fatima", "age": 19, "scores": [91, 95, 88]},
]

def get_average(student):
    return sum(student["scores"]) / len(student["scores"])

def is_passing(student, threshold=50):
    return get_average(student) >= threshold

for s in students:
    avg = get_average(s)
    status = "PASS" if is_passing(s) else "FAIL"
    print(f"{s['name']}: {avg:.1f} — {status}")

# Problems:
# - Nothing stops you from creating a dict without "scores"
# - No validation on data
# - Functions don't belong to the student — they float separately
# - Adding a new operation means another standalone function


# A preview of the OOP way (you will learn this syntax tomorrow)
class Student:
    def __init__(self, name, age, scores):
        self.name = name
        self.age = age
        self.scores = scores

    def average(self):
        return sum(self.scores) / len(self.scores)

    def is_passing(self, threshold=50):
        return self.average() >= threshold

amina = Student("Amina", 20, [85, 90, 78])
print(f"{amina.name}: {amina.average():.1f}")
print(f"Passing: {amina.is_passing()}")

# Notice: the student KNOWS how to calculate its own average
# Data and behavior are bundled together
```

## Guided Practice

Identify objects in a real-world scenario.

**Scenario:** You are designing a library management system.

**Step 1:** List the entities (nouns) in the system.
- Book
- Member
- Librarian
- Loan

**Step 2:** For each entity, list its attributes (data) and behaviors (actions).

| Entity | Attributes | Behaviors |
|--------|-----------|-----------|
| Book | title, author, ISBN, available | check_out(), return_book(), display_info() |
| Member | name, member_id, borrowed_books | borrow(), return_book(), view_history() |
| Librarian | name, employee_id | add_book(), remove_book(), register_member() |
| Loan | book, member, date_borrowed, due_date | is_overdue(), calculate_fine() |

**Step 3:** Think about relationships.
- A Member borrows many Books (through Loans).
- A Book can have one active Loan at a time.
- A Librarian manages Books and Members.

## Daily Challenge

Choose ONE of the following real-world systems and perform an object analysis:

1. **Hospital Management System**
2. **Restaurant Ordering System**
3. **Online Store (E-Commerce)**
4. **School Examination System**

For your chosen system, create a file called `object_analysis.py` that contains:

1. A comment block listing at least 4 entities (classes) you would create.
2. For each entity, list its attributes and behaviors as comments.
3. Show the relationships between entities (which entity uses or contains another).
4. Write a procedural version that manages 3 items (using dictionaries and functions).
5. In comments, explain what problems the procedural version has that OOP would solve.

Example structure:

```python
"""
Object Analysis: Hospital Management System

Entities:
1. Patient — name, age, patient_id, medical_history
   Behaviors: add_record(), view_history(), schedule_appointment()

2. Doctor — name, specialization, doctor_id, patients
   Behaviors: diagnose(), prescribe(), view_schedule()

3. ...

Relationships:
- A Doctor treats many Patients
- A Patient can visit many Doctors
- ...
"""

# Procedural version
patients = [
    {"name": "Amina", "age": 30, "condition": "Flu"},
    {"name": "Musa", "age": 45, "condition": "Malaria"},
    {"name": "Fatima", "age": 25, "condition": "Check-up"},
]

def diagnose(patient, diagnosis):
    patient["condition"] = diagnosis
    print(f"Dr. diagnosed {patient['name']} with {diagnosis}")

# ... more procedural code ...

# Problems with this approach:
# 1. No validation — any key can be added/removed from dicts
# 2. Functions are disconnected from the data they operate on
# 3. Adding new features requires modifying many functions
# 4. No way to enforce that a patient always has required fields
```

## Expected Output

A well-documented analysis showing clear thinking about entities, attributes, behaviors, and relationships, along with a working procedural example that demonstrates the limitations OOP will solve.

## Assessment

1. What is the main difference between procedural programming and object-oriented programming?
2. What is "state sprawl" and why is it a problem in procedural programs?
3. In your own words, what does it mean to "think in objects"?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-04/day-031/`

Include your `object_analysis.py` file.

## Additional Resources

- [Lecture 01 — Python & OOP Introduction](../../../python-oop/lectures/01-python-oop-introduction.md)
- [Python Docs: Classes](https://docs.python.org/3/tutorial/classes.html)

## Reflection

- Look at a program you wrote earlier in this bootcamp. Can you identify parts of it that would benefit from being organized as objects?
- Why do you think OOP became the dominant paradigm for building large software systems?
