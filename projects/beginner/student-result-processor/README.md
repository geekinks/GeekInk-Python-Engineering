# Student Result Processing System

**Module:** 2 — Data Structures and Problem Solving
**Day:** 20
**Difficulty:** Beginner

---

## Problem Statement

Schools and training programs need systems to manage student academic records efficiently. This project challenges students to build a result processing system that stores, analyzes, and displays student performance data using Python's core data structures: lists, dictionaries, tuples, and sets.

## Objectives

- Use lists, dictionaries, and tuples to model real-world data.
- Apply loops, comprehensions, and conditional logic to process records.
- Handle missing or invalid data gracefully using exception handling.
- Format tabular output for readability.
- Implement sorting and filtering on structured data.

## Requirements

### Functional Requirements

1. **Student record storage:**
   - Each student has a name, ID, and a dictionary of subject scores.
   - Support at least 5 students and 4 subjects.

2. **Score management:**
   - Add new students with their scores.
   - Update scores for existing students.
   - Handle missing scores (a student may not have taken all subjects).

3. **Calculations:**
   - Average score per student.
   - Average score per subject.
   - Letter grade per student (A: 70+, B: 60-69, C: 50-59, D: 40-49, F: below 40).
   - Class average across all students.

4. **Analysis and display:**
   - Display a formatted results table with all students, scores, averages, and grades.
   - Identify and display the top 3 performers.
   - Identify and display students who failed (average below 40).
   - Display subject-wise statistics (highest, lowest, average per subject).

5. **Menu-driven interface:**
   - Add student
   - View all results
   - View top performers
   - View subject statistics
   - Search student by name or ID
   - Exit

### Non-Functional Requirements

- The program must not crash on missing data or invalid input.
- Output tables must be aligned and readable.
- Code must be organized into functions.

## Features

| Feature | Description |
| :--- | :--- |
| Record management | Add and update student records |
| Grade calculation | Automatic letter grade assignment |
| Statistical analysis | Per-student and per-subject statistics |
| Ranking | Top and bottom performer identification |
| Search | Find students by name or ID |
| Formatted output | Aligned tabular display |

## Suggested Architecture

```
student_result_processor.py
├── Data storage (list of dictionaries or dictionary of dictionaries)
├── Input functions
│   ├── add_student()
│   └── get_valid_score()
├── Calculation functions
│   ├── calculate_average()
│   ├── assign_grade()
│   └── calculate_subject_stats()
├── Display functions
│   ├── display_results_table()
│   ├── display_top_performers()
│   └── display_subject_statistics()
├── Search functions
│   └── search_student()
└── main() — menu loop
```

## Technologies

- Python 3.10+
- Standard library only

## Implementation Milestones

| Milestone | Description |
| :--- | :--- |
| 1. Data model | Define the student record structure, add sample data |
| 2. Add student | Implement the add student flow with validation |
| 3. Calculations | Implement average and grade calculations |
| 4. Results table | Display all results in a formatted table |
| 5. Analysis | Add top performers, failures, and subject stats |
| 6. Menu system | Wire everything together with a menu loop |

## Testing Requirements

Manually verify the following scenarios:

| Scenario | Expected Behavior |
| :--- | :--- |
| Student with all scores present | Correct average and grade displayed |
| Student with missing scores | Missing scores shown as "N/A", average calculated from available scores |
| Student with average of exactly 70 | Grade is "A" |
| Search for non-existent student | "Student not found" message |
| Empty student list | Appropriate message, no crash |
| Non-numeric score input | Error message and re-prompt |

## Expected Deliverables

1. `student_result_processor.py` — The complete program.
2. Sample output showing the results table, top performers, and subject statistics.

## Evaluation Criteria

| Criterion | Weight | Description |
| :--- | :--- | :--- |
| Correct data modeling | 20% | Appropriate use of data structures |
| Calculation accuracy | 25% | Averages, grades, and statistics are correct |
| Error handling | 15% | Missing data and invalid input handled |
| Code organization | 20% | Functions are well-defined and reusable |
| Output quality | 10% | Tables are aligned and readable |
| Completeness | 10% | All menu options are functional |
