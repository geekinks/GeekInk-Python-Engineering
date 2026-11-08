"""
Smart Personal Profile and Calculator
Module 1 Project — GeekInk Python Engineering

Build an interactive program that collects user information,
performs calculations, and displays a formatted profile card.
"""

from datetime import datetime

CURRENT_YEAR = datetime.now().year


def get_valid_number(prompt, min_value=None, max_value=None):
    """Prompt the user until they enter a valid number within the given range."""
    # TODO: Implement a loop that:
    # 1. Displays the prompt
    # 2. Tries to convert input to a float
    # 3. Checks if the value is within min_value and max_value (if provided)
    # 4. Returns the valid number
    # 5. Prints an error message and re-prompts on invalid input
    pass


def calculate_bmi(weight_kg, height_m):
    """Calculate Body Mass Index from weight (kg) and height (m)."""
    # TODO: Return weight / height^2
    pass


def get_bmi_category(bmi):
    """Return the BMI category as a string."""
    # TODO: Return one of:
    # "Underweight" if bmi < 18.5
    # "Normal" if 18.5 <= bmi < 25
    # "Overweight" if 25 <= bmi < 30
    # "Obese" if bmi >= 30
    pass


def display_profile(name, birth_year, height, weight, hobby, age, bmi, category):
    """Display a formatted profile card with all information."""
    # TODO: Print a bordered profile card, for example:
    #
    # ╔══════════════════════════════════╗
    # ║      PERSONAL PROFILE CARD      ║
    # ╠══════════════════════════════════╣
    # ║  Name:       Amina Yusuf        ║
    # ║  Birth Year: 2000               ║
    # ║  Age:        25 years           ║
    # ║  Age:        9125 days          ║
    # ║  Age:        219000 hours       ║
    # ║  Height:     1.65 m             ║
    # ║  Weight:     60.0 kg            ║
    # ║  BMI:        22.04 (Normal)     ║
    # ║  Hobby:      Reading            ║
    # ╚══════════════════════════════════╝
    pass


def main():
    """Main program entry point."""
    print("Welcome to the Smart Personal Profile Generator!")
    print("-" * 45)

    # TODO: Collect user input
    # name = input(...)
    # birth_year = get_valid_number(...)
    # height = get_valid_number(...)
    # weight = get_valid_number(...)
    # hobby = input(...)

    # TODO: Perform calculations
    # age = CURRENT_YEAR - birth_year
    # age_in_days = age * 365
    # age_in_hours = age_in_days * 24
    # bmi = calculate_bmi(weight, height)
    # category = get_bmi_category(bmi)

    # TODO: Display the profile card
    # display_profile(...)

    pass


if __name__ == "__main__":
    main()
