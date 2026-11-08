# Day 062: Tkinter Widgets

## Learning Objectives

- Understand the most common Tkinter widgets: Label, Button, Entry, and Text.
- Learn how to configure widget appearance (font, color, size, relief).
- Use the three geometry managers: `pack()`, `grid()`, and `place()`.
- Build a simple form using widgets and layout managers.

## Introduction

Widgets are the building blocks of any GUI. Every element you see in a desktop application — a text field, a button, a dropdown menu, a checkbox — is a widget. Tkinter provides a core set of widgets that cover the needs of most applications.

Choosing the right widget for each piece of data and the right layout manager to arrange them is one of the first design decisions in GUI development. A well-organized interface guides users through a workflow, while a cluttered one creates confusion.

Today you will learn the most commonly used widgets and how to arrange them on screen. By the end, you will be able to build forms that collect user information through a visual interface instead of terminal prompts.

## Concepts

### Core Widgets

**Label** — Displays static text or images. Users cannot edit it.

```python
label = tk.Label(root, text="Name:", font=("Arial", 12))
```

**Button** — A clickable element that triggers a function.

```python
button = tk.Button(root, text="Submit", command=some_function)
```

**Entry** — A single-line text input field.

```python
entry = tk.Entry(root, width=30)
```

**Text** — A multi-line text input area.

```python
text_area = tk.Text(root, width=40, height=10)
```

### Widget Configuration

Every widget accepts configuration options as keyword arguments at creation or through the `.config()` method afterward:

- `text` — the displayed text
- `font` — a tuple like `("Arial", 14, "bold")`
- `fg` — foreground (text) color
- `bg` — background color
- `width` — width in characters (for text widgets) or pixels (for some widgets)
- `relief` — border style: `"flat"`, `"raised"`, `"sunken"`, `"groove"`, `"ridge"`
- `state` — `"normal"`, `"disabled"`, or `"readonly"`

### Geometry Managers

Tkinter provides three ways to position widgets:

**pack()** — Places widgets one after another (top to bottom by default).

```python
label.pack(side="top", pady=10)
```

**grid()** — Places widgets in a row/column grid. Best for forms and structured layouts.

```python
label.grid(row=0, column=0, padx=5, pady=5)
```

**place()** — Places widgets at exact pixel coordinates. Useful for precise positioning but does not adapt to window resizing.

```python
label.place(x=50, y=100)
```

Do not mix `pack()` and `grid()` in the same parent container — Tkinter will raise an error.

### Getting Values from Widgets

```python
# Get text from an Entry
name = entry.get()

# Get text from a Text widget (from line 1, character 0 to the end)
content = text_area.get("1.0", tk.END)
```

## Practical Examples

### Label and Button Interaction

```python
import tkinter as tk

def greet():
    name = name_entry.get()
    if name:
        greeting_label.config(text=f"Hello, {name}!")
    else:
        greeting_label.config(text="Please enter your name.")

root = tk.Tk()
root.title("Greeting App")
root.geometry("350x200")

tk.Label(root, text="Enter your name:").pack(pady=(20, 5))

name_entry = tk.Entry(root, width=25)
name_entry.pack(pady=5)

tk.Button(root, text="Greet", command=greet).pack(pady=10)

greeting_label = tk.Label(root, text="", font=("Arial", 14))
greeting_label.pack(pady=10)

root.mainloop()
```

### Using grid() for a Form Layout

```python
import tkinter as tk

root = tk.Tk()
root.title("Registration Form")
root.geometry("400x250")

# Row 0
tk.Label(root, text="First Name:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
first_name = tk.Entry(root, width=25)
first_name.grid(row=0, column=1, padx=10, pady=10)

# Row 1
tk.Label(root, text="Last Name:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
last_name = tk.Entry(root, width=25)
last_name.grid(row=1, column=1, padx=10, pady=10)

# Row 2
tk.Label(root, text="Email:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
email = tk.Entry(root, width=25)
email.grid(row=2, column=1, padx=10, pady=10)

# Row 3
def submit():
    print(f"Name: {first_name.get()} {last_name.get()}")
    print(f"Email: {email.get()}")

tk.Button(root, text="Submit", command=submit).grid(row=3, column=1, pady=20, sticky="e")

root.mainloop()
```

### Text Widget for Multi-line Input

```python
import tkinter as tk

def show_content():
    content = text_area.get("1.0", tk.END).strip()
    print(f"You wrote:\n{content}")

root = tk.Tk()
root.title("Notes")
root.geometry("400x350")

tk.Label(root, text="Write your notes below:").pack(pady=(10, 5))

text_area = tk.Text(root, width=45, height=12, font=("Courier", 11))
text_area.pack(padx=10, pady=5)

tk.Button(root, text="Print Notes", command=show_content).pack(pady=10)

root.mainloop()
```

## Guided Practice

Build a simple **Feedback Form** step by step.

**Step 1:** Create the root window.

```python
import tkinter as tk

root = tk.Tk()
root.title("Feedback Form")
root.geometry("450x400")
```

**Step 2:** Add a title label using `pack()`.

```python
tk.Label(root, text="We value your feedback", font=("Arial", 16, "bold")).pack(pady=15)
```

**Step 3:** Create a frame to hold the form fields (so we can use `grid()` inside it).

```python
form_frame = tk.Frame(root)
form_frame.pack(pady=10)
```

**Step 4:** Add labeled input fields using `grid()` inside the frame.

```python
tk.Label(form_frame, text="Name:").grid(row=0, column=0, padx=10, pady=8, sticky="e")
name_entry = tk.Entry(form_frame, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=8)

tk.Label(form_frame, text="Email:").grid(row=1, column=0, padx=10, pady=8, sticky="e")
email_entry = tk.Entry(form_frame, width=30)
email_entry.grid(row=1, column=1, padx=10, pady=8)
```

**Step 5:** Add a Text widget for detailed feedback.

```python
tk.Label(root, text="Your Feedback:").pack(pady=(10, 5))
feedback_text = tk.Text(root, width=50, height=6)
feedback_text.pack(padx=10)
```

**Step 6:** Add a submit button that prints the collected data.

```python
def submit_feedback():
    name = name_entry.get()
    email = email_entry.get()
    feedback = feedback_text.get("1.0", tk.END).strip()
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Feedback: {feedback}")

tk.Button(root, text="Submit Feedback", command=submit_feedback).pack(pady=15)

root.mainloop()
```

## Daily Challenge

Build a **Contact Information Form** with the following requirements:

1. A window titled "Contact Information" (size 500 x 450).
2. Fields arranged using `grid()`: Full Name, Phone Number, Email Address, City.
3. A multi-line "Notes" area below the grid fields using a `Text` widget.
4. A "Save Contact" button that prints all entered data to the terminal.
5. A "Clear" button that clears all fields.
6. Labels should be right-aligned and input fields left-aligned.

Save the file as `contact_form.py`.

## Expected Output

Running the program shows a window with neatly aligned form fields, a notes area, and two buttons. Clicking "Save Contact" prints the entered data. Clicking "Clear" empties all fields.

## Assessment

1. What is the difference between an `Entry` widget and a `Text` widget?
2. Why should you avoid mixing `pack()` and `grid()` in the same parent container?
3. How do you retrieve the text a user has typed into an `Entry` widget?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-07/day-062/`

Include your `contact_form.py` file.

## Additional Resources

- [Tkinter Widget Documentation](https://docs.python.org/3/library/tkinter.html#tkinter-widgets)
- [TkDocs: Basic Widgets](https://tkdocs.com/tutorial/widgets.html)

## Reflection

- Which geometry manager felt most natural to you and why?
- How does building a visual form compare to collecting the same information with `input()` calls in the terminal?
