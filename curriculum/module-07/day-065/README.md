# Day 065: Forms and User Input

## Learning Objectives

- Use Tkinter variable classes (StringVar, IntVar, DoubleVar, BooleanVar) for reactive data binding.
- Implement form validation that provides feedback before submission.
- Use selection widgets: Checkbutton, Radiobutton, Combobox, and Spinbox.
- Build a complete registration form with input validation.

## Introduction

Real-world forms do more than collect text. They offer choices (dropdowns, checkboxes, radio buttons), enforce constraints (required fields, valid email formats, age ranges), and provide immediate feedback when something is wrong.

Tkinter provides variable classes that act as a bridge between your Python code and the widgets on screen. When a widget's value changes, the associated variable updates automatically, and vice versa. This reactive binding simplifies form handling significantly compared to manually reading every widget's state.

Today you will build a registration form that uses multiple input types and validates data before accepting it — the same kind of form logic that powers web signup pages, desktop settings panels, and mobile onboarding screens.

## Concepts

### Tkinter Variable Classes

| Class       | Python Type | Use Case |
|------------|-------------|----------|
| `StringVar` | `str`       | Text entries, labels |
| `IntVar`    | `int`       | Checkbuttons, radio selections |
| `DoubleVar` | `float`     | Numeric inputs |
| `BooleanVar`| `bool`      | Toggle states |

```python
name_var = tk.StringVar()
entry = tk.Entry(root, textvariable=name_var)

# Get the current value
print(name_var.get())

# Set a value programmatically
name_var.set("Default Name")
```

### Checkbutton

A toggle that represents a boolean choice:

```python
agreed = tk.BooleanVar()
check = tk.Checkbutton(root, text="I agree to terms", variable=agreed)
```

### Radiobutton

A set of mutually exclusive options sharing the same variable:

```python
gender = tk.StringVar(value="")
tk.Radiobutton(root, text="Male", variable=gender, value="male")
tk.Radiobutton(root, text="Female", variable=gender, value="female")
```

### Combobox (from ttk)

A dropdown selection list:

```python
from tkinter import ttk

state = tk.StringVar()
combo = ttk.Combobox(root, textvariable=state, values=["Kano", "Lagos", "Abuja"])
combo.set("Select State")
```

### Spinbox

A numeric input with increment/decrement arrows:

```python
age = tk.IntVar(value=18)
spin = tk.Spinbox(root, from_=1, to=120, textvariable=age, width=5)
```

### Input Validation

Validate before processing:

```python
def validate_form():
    errors = []
    if not name_var.get().strip():
        errors.append("Name is required.")
    if not email_var.get().strip() or "@" not in email_var.get():
        errors.append("Valid email is required.")
    return errors
```

## Practical Examples

### Variable Binding

```python
import tkinter as tk

root = tk.Tk()
root.title("Live Preview")
root.geometry("350x150")

name_var = tk.StringVar()

tk.Label(root, text="Type your name:").pack(pady=(20, 5))
tk.Entry(root, textvariable=name_var, width=30).pack()

preview = tk.Label(root, text="", font=("Arial", 14))
preview.pack(pady=15)

def update_preview(*args):
    preview.config(text=f"Hello, {name_var.get()}!")

name_var.trace_add("write", update_preview)

root.mainloop()
```

### Checkbuttons and Radiobuttons

```python
import tkinter as tk

def show_selections():
    interests = []
    if python_var.get():
        interests.append("Python")
    if data_var.get():
        interests.append("Data Science")
    if web_var.get():
        interests.append("Web Dev")
    result.config(text=f"Level: {level_var.get()}, Interests: {', '.join(interests)}")

root = tk.Tk()
root.title("Preferences")
root.geometry("350x300")

# Radio buttons for level
tk.Label(root, text="Experience Level:").pack(anchor="w", padx=20, pady=(15, 5))
level_var = tk.StringVar(value="beginner")
for level in ["beginner", "intermediate", "advanced"]:
    tk.Radiobutton(root, text=level.capitalize(), variable=level_var,
                   value=level).pack(anchor="w", padx=40)

# Checkbuttons for interests
tk.Label(root, text="Interests:").pack(anchor="w", padx=20, pady=(15, 5))
python_var = tk.BooleanVar()
data_var = tk.BooleanVar()
web_var = tk.BooleanVar()
tk.Checkbutton(root, text="Python", variable=python_var).pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Data Science", variable=data_var).pack(anchor="w", padx=40)
tk.Checkbutton(root, text="Web Development", variable=web_var).pack(anchor="w", padx=40)

tk.Button(root, text="Show Selections", command=show_selections).pack(pady=10)
result = tk.Label(root, text="")
result.pack()

root.mainloop()
```

### Combobox and Spinbox

```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Course Registration")
root.geometry("400x250")

frame = tk.Frame(root)
frame.pack(pady=20)

# Combobox for course selection
tk.Label(frame, text="Course:").grid(row=0, column=0, padx=10, pady=8, sticky="e")
course_var = tk.StringVar()
course_combo = ttk.Combobox(frame, textvariable=course_var, width=25,
                             values=["Python Foundations", "Data Structures",
                                     "OOP", "Web Development", "Data Science"])
course_combo.grid(row=0, column=1, padx=10, pady=8)
course_combo.set("Select a course")

# Spinbox for number of hours per week
tk.Label(frame, text="Hours/Week:").grid(row=1, column=0, padx=10, pady=8, sticky="e")
hours_var = tk.IntVar(value=5)
hours_spin = tk.Spinbox(frame, from_=1, to=40, textvariable=hours_var, width=5)
hours_spin.grid(row=1, column=1, padx=10, pady=8, sticky="w")

def register():
    print(f"Course: {course_var.get()}, Hours/Week: {hours_var.get()}")

tk.Button(root, text="Register", command=register).pack(pady=10)

root.mainloop()
```

## Guided Practice

Build a **Student Registration Form** step by step.

**Step 1:** Set up the window and a form frame.

```python
import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Student Registration")
root.geometry("500x550")

form = tk.Frame(root)
form.pack(padx=30, pady=20)

row = 0
```

**Step 2:** Add text entry fields with StringVar.

```python
name_var = tk.StringVar()
tk.Label(form, text="Full Name:").grid(row=row, column=0, sticky="e", pady=8)
tk.Entry(form, textvariable=name_var, width=30).grid(row=row, column=1, pady=8, padx=10)
row += 1

email_var = tk.StringVar()
tk.Label(form, text="Email:").grid(row=row, column=0, sticky="e", pady=8)
tk.Entry(form, textvariable=email_var, width=30).grid(row=row, column=1, pady=8, padx=10)
row += 1
```

**Step 3:** Add age with Spinbox.

```python
age_var = tk.IntVar(value=18)
tk.Label(form, text="Age:").grid(row=row, column=0, sticky="e", pady=8)
tk.Spinbox(form, from_=10, to=100, textvariable=age_var, width=5).grid(
    row=row, column=1, sticky="w", pady=8, padx=10)
row += 1
```

**Step 4:** Add gender with Radiobuttons and state with Combobox.

```python
gender_var = tk.StringVar(value="")
tk.Label(form, text="Gender:").grid(row=row, column=0, sticky="e", pady=8)
gender_frame = tk.Frame(form)
gender_frame.grid(row=row, column=1, sticky="w", padx=10)
tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="male").pack(side="left")
tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="female").pack(side="left")
row += 1

state_var = tk.StringVar()
tk.Label(form, text="State:").grid(row=row, column=0, sticky="e", pady=8)
states = ["Kano", "Lagos", "Abuja", "Kaduna", "Katsina", "Borno", "Sokoto"]
ttk.Combobox(form, textvariable=state_var, values=states, width=27).grid(
    row=row, column=1, pady=8, padx=10)
row += 1
```

**Step 5:** Add terms checkbox and submit button with validation.

```python
agree_var = tk.BooleanVar()
tk.Checkbutton(form, text="I agree to the terms and conditions",
               variable=agree_var).grid(row=row, column=0, columnspan=2, pady=10)
row += 1

def submit():
    errors = []
    if not name_var.get().strip():
        errors.append("Full name is required.")
    if "@" not in email_var.get():
        errors.append("Please enter a valid email.")
    if not gender_var.get():
        errors.append("Please select your gender.")
    if not state_var.get():
        errors.append("Please select your state.")
    if not agree_var.get():
        errors.append("You must agree to the terms.")
    if errors:
        messagebox.showwarning("Validation Error", "\n".join(errors))
    else:
        messagebox.showinfo("Success", f"Welcome, {name_var.get()}!")

tk.Button(form, text="Register", width=20, command=submit).grid(
    row=row, column=0, columnspan=2, pady=15)

root.mainloop()
```

## Daily Challenge

Build a **Job Application Form** with the following requirements:

1. Text fields: Full Name, Email, Phone Number (using StringVar).
2. A Combobox for "Position Applied For" with at least 5 job titles.
3. A Spinbox for "Years of Experience" (0 to 30).
4. Radiobuttons for "Employment Type": Full-time, Part-time, Contract.
5. Checkbuttons for skills: Python, SQL, Git, Communication (select all that apply).
6. A "Submit Application" button that validates:
   - Name is not empty.
   - Email contains "@".
   - A position is selected.
   - At least one skill is checked.
7. Show a success message with a summary if valid, or a warning listing all errors.

Save the file as `job_application.py`.

## Expected Output

A form window with all input types. Invalid submissions show a clear list of what needs to be corrected. A valid submission shows a summary dialog.

## Assessment

1. What advantage does `StringVar` provide over calling `entry.get()` directly?
2. How do you make Radiobuttons mutually exclusive?
3. What is the difference between a Checkbutton and a Radiobutton in terms of user interaction?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-07/day-065/`

Include your `job_application.py` file.

## Additional Resources

- [Tkinter Variable Classes](https://docs.python.org/3/library/tkinter.html#coupling-widget-variables)
- [TkDocs: Combobox](https://tkdocs.com/tutorial/widgets.html#combobox)

## Reflection

- What makes a form user-friendly? Think about error messages, default values, and layout.
- How does validating at submission time compare to validating as the user types?
