# Day 020: Module 2 Project — Student Result Processing System

## Learning Objectives

- Apply all data structure concepts from Module 2 in a complete project.
- Design a data model using lists, dictionaries, tuples, and sets.
- Process and analyze data using loops and comprehensions.
- Handle errors and edge cases in a real data processing scenario.
- Produce professional, formatted output from computed data.

## Introduction

Today you will build your second major project: a Student Result Processing System. This system will store student records, compute grades, generate statistics, and produce formatted result sheets. It brings together everything from Module 2: lists, tuples, sets, dictionaries, loops, comprehensions, and exception handling.

This is the kind of system that schools, universities, and testing organizations actually build. You are solving a real problem.

## Project: Student Result Processing System

### Problem Statement

Build a Python program that manages and processes student examination results. The system must handle data entry, grade computation, statistical analysis, and formatted report generation.

### Requirements

1. **Data Storage**

   Store each student as a dictionary:
   ```python
   {
       "name": "Amina Ibrahim",
       "matric": "CSC/2024/001",
       "scores": {"Math": 85, "English": 72, "Science": 90, "History": 68, "CompSci": 88}
   }
   ```

   Store all students in a list.

2. **Core Features**

   The system must support:
   - Adding new student records with validation.
   - Viewing all student results in a formatted table.
   - Calculating individual student statistics (average, grade, pass/fail).
   - Generating class-wide statistics.
   - Finding top and bottom performers.
   - Searching for a student by name or matric number.

3. **Grading Scale**

   | Average   | Grade | Remark        |
   | --------- | ----- | ------------- |
   | 70 - 100  | A     | Excellent     |
   | 60 - 69   | B     | Very Good     |
   | 50 - 59   | C     | Good          |
   | 45 - 49   | D     | Pass          |
   | 0 - 44    | F     | Fail          |

4. **Pass/Fail Rules**
   - A student passes if their average is 45 or above.
   - A student with any single subject below 30 is flagged for review regardless of average.

5. **Class Statistics**
   - Class average
   - Highest and lowest individual averages
   - Number of passes and failures
   - Best and worst subject (by class average)
   - Distribution of grades (how many A's, B's, C's, etc.)

6. **Menu System**

   ```
   ===== STUDENT RESULT PROCESSING SYSTEM =====

   1. Add Student Record
   2. View All Results
   3. Search Student
   4. Class Statistics
   5. Top/Bottom Performers
   6. Subject Analysis
   7. Exit

   Enter choice:
   ```

### Starter Code

```python
# =============================================
# GeekInk Python Engineering
# Module 2 Project: Student Result Processing
# =============================================


def get_valid_score(subject):
    """Get a validated score (0-100) for a subject."""
    while True:
        try:
            score = int(input(f"  {subject}: "))
            if 0 <= score <= 100:
                return score
            print("  Score must be between 0 and 100.")
        except ValueError:
            print("  Please enter a valid number.")


def calculate_average(scores):
    """Calculate the average of a dictionary of scores."""
    values = list(scores.values())
    return sum(values) / len(values)


def determine_grade(average):
    """Return the letter grade and remark for a given average."""
    if average >= 70:
        return "A", "Excellent"
    elif average >= 60:
        return "B", "Very Good"
    elif average >= 50:
        return "C", "Good"
    elif average >= 45:
        return "D", "Pass"
    else:
        return "F", "Fail"


def add_student(students):
    """Add a new student record."""
    print("\n--- Add Student Record ---")
    name = input("Student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    matric = input("Matric number: ").strip()

    subjects = ["Math", "English", "Science", "History", "CompSci"]
    print("Enter scores:")
    scores = {}
    for subject in subjects:
        scores[subject] = get_valid_score(subject)

    student = {"name": name, "matric": matric, "scores": scores}
    students.append(student)
    print(f"Record added for {name}.")


def view_all_results(students):
    """Display all student results in a formatted table."""
    if not students:
        print("\nNo student records found.")
        return

    print(f"\n{'Name':<20} {'Matric':<15} ", end="")
    subjects = list(students[0]["scores"].keys())
    for subj in subjects:
        print(f"{subj:>6}", end=" ")
    print(f"{'Avg':>6} {'Grade':>5} {'Status':>8}")
    print("-" * 90)

    for student in students:
        avg = calculate_average(student["scores"])
        grade, remark = determine_grade(avg)
        has_critical = any(s < 30 for s in student["scores"].values())
        status = "REVIEW" if has_critical else ("PASS" if avg >= 45 else "FAIL")

        print(f"{student['name']:<20} {student['matric']:<15} ", end="")
        for subj in subjects:
            print(f"{student['scores'][subj]:>6}", end=" ")
        print(f"{avg:>6.1f} {grade:>5} {status:>8}")


# TODO: Implement search_student(students)
# TODO: Implement class_statistics(students)
# TODO: Implement top_bottom_performers(students)
# TODO: Implement subject_analysis(students)


def main():
    students = [
        {
            "name": "Amina Ibrahim",
            "matric": "CSC/2024/001",
            "scores": {"Math": 85, "English": 72, "Science": 90, "History": 68, "CompSci": 88},
        },
        {
            "name": "Bashir Yusuf",
            "matric": "CSC/2024/002",
            "scores": {"Math": 55, "English": 60, "Science": 48, "History": 52, "CompSci": 65},
        },
        {
            "name": "Chioma Okafor",
            "matric": "CSC/2024/003",
            "scores": {"Math": 92, "English": 88, "Science": 95, "History": 78, "CompSci": 90},
        },
        {
            "name": "Danjuma Abdullahi",
            "matric": "CSC/2024/004",
            "scores": {"Math": 40, "English": 35, "Science": 28, "History": 42, "CompSci": 45},
        },
        {
            "name": "Esther Nwankwo",
            "matric": "CSC/2024/005",
            "scores": {"Math": 70, "English": 65, "Science": 72, "History": 60, "CompSci": 68},
        },
    ]

    while True:
        print("\n===== STUDENT RESULT PROCESSING SYSTEM =====")
        print("1. Add Student Record")
        print("2. View All Results")
        print("3. Search Student")
        print("4. Class Statistics")
        print("5. Top/Bottom Performers")
        print("6. Subject Analysis")
        print("7. Exit")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_all_results(students)
        elif choice == "3":
            # TODO: search_student(students)
            print("Search feature — implement this!")
        elif choice == "4":
            # TODO: class_statistics(students)
            print("Statistics feature — implement this!")
        elif choice == "5":
            # TODO: top_bottom_performers(students)
            print("Top/Bottom feature — implement this!")
        elif choice == "6":
            # TODO: subject_analysis(students)
            print("Subject analysis — implement this!")
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-7.")


if __name__ == "__main__":
    main()
```

### Implementation Tasks

Complete the TODO sections:

1. **`search_student(students)`**: Search by name (partial match, case-insensitive) or matric number. Display the full record for matching students.

2. **`class_statistics(students)`**: Display class average, pass/fail counts, grade distribution, highest and lowest averages.

3. **`top_bottom_performers(students, n=3)`**: Show the top `n` and bottom `n` students by average. Use list comprehensions to compute averages, then sort.

4. **`subject_analysis(students)`**: For each subject, show class average, highest score (and who), lowest score (and who). Identify the strongest and weakest subjects.

## Features Checklist

- [ ] Add new students with validated scores.
- [ ] View all results in a formatted table.
- [ ] Search by name or matric number.
- [ ] Class-wide statistics with grade distribution.
- [ ] Top and bottom performers identified.
- [ ] Per-subject analysis completed.
- [ ] Invalid inputs handled without crashes.
- [ ] Menu loops until exit.

## Assessment

| Criteria                  | Weight |
| ------------------------- | ------ |
| Correct calculations      | 25%    |
| Data structure usage      | 20%    |
| Error handling             | 15%    |
| Output formatting         | 15%    |
| Code organization          | 15%    |
| Completeness              | 10%    |

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-02/day-020/`

Your submission should include:
- `result_system.py` containing your complete project.

## Additional Resources

- Review Days 11-19 for data structure techniques.
- [Python Official Docs — Sorting HOW TO](https://docs.python.org/3/howto/sorting.html)

## Reflection

- Which data structure was most useful for this project, and why?
- What was the most challenging feature to implement?
- How would you improve this system if you had more time?
