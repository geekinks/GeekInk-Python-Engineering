"""
Student Result Processing System
Module 2 Project — GeekInk Python Engineering

Build a system that stores, analyzes, and displays student
academic performance using Python data structures.
"""


# Sample data to get started — add more students as needed
SUBJECTS = ["Mathematics", "English", "Science", "History"]

students = [
    {
        "id": "STU001",
        "name": "Aisha Bello",
        "scores": {"Mathematics": 78, "English": 65, "Science": 82, "History": 71},
    },
    {
        "id": "STU002",
        "name": "Ibrahim Musa",
        "scores": {"Mathematics": 55, "English": 48, "Science": 60, "History": None},
    },
    {
        "id": "STU003",
        "name": "Fatima Yusuf",
        "scores": {"Mathematics": 92, "English": 88, "Science": 95, "History": 90},
    },
]


def calculate_average(scores):
    """Calculate the average of available scores, ignoring None values."""
    # TODO: Filter out None values, return the average of remaining scores.
    # Return 0 if no valid scores exist.
    pass


def assign_grade(average):
    """Assign a letter grade based on the average score."""
    # TODO: A: 70+, B: 60-69, C: 50-59, D: 40-49, F: below 40
    pass


def add_student(student_list):
    """Prompt the user for student details and add to the list."""
    # TODO: Ask for name, generate an ID, collect scores for each subject.
    # Validate that scores are between 0 and 100.
    pass


def display_results_table(student_list):
    """Display all students in a formatted table with scores, averages, and grades."""
    # TODO: Print a header row, then each student's data in aligned columns.
    # Show "N/A" for missing scores.
    # Example output:
    #
    # ID      | Name           | Math | Eng  | Sci  | Hist | Avg   | Grade
    # --------|----------------|------|------|------|------|-------|------
    # STU001  | Aisha Bello    |   78 |   65 |   82 |   71 | 74.00 |  A
    # STU002  | Ibrahim Musa   |   55 |   48 |   60 |  N/A | 54.33 |  C
    pass


def display_top_performers(student_list, count=3):
    """Display the top N students by average score."""
    # TODO: Sort students by average score (descending), display top N.
    pass


def display_subject_statistics(student_list):
    """Display per-subject statistics: highest, lowest, and average."""
    # TODO: For each subject, calculate and display stats.
    pass


def search_student(student_list, query):
    """Search for a student by name or ID (case-insensitive)."""
    # TODO: Return matching students or an empty list.
    pass


def main():
    """Main menu loop."""
    print("Student Result Processing System")
    print("=" * 35)

    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. View All Results")
        print("3. View Top Performers")
        print("4. View Subject Statistics")
        print("5. Search Student")
        print("6. Exit")

        choice = input("\nSelect an option (1-6): ").strip()

        # TODO: Implement menu option handling
        if choice == "6":
            print("Goodbye!")
            break
        else:
            print("Option not yet implemented.")


if __name__ == "__main__":
    main()
