# Day 061: Introduction to Desktop Applications

## Learning Objectives

- Understand what graphical user interface (GUI) applications are and how they differ from command-line programs.
- Learn the concept of event-driven programming.
- Survey the major Python GUI frameworks: Tkinter, PyQt, and Kivy.
- Create a basic Tkinter window with custom properties.

## Introduction

Until now, every program you have built runs in a terminal. Users type commands, see text output, and interact line by line. Desktop applications replace that text interface with windows, buttons, menus, and forms. Nearly every application you use daily — file managers, text editors, calculators — is a GUI application.

GUI programming introduces a fundamentally different execution model called event-driven programming. Instead of your code running top to bottom and waiting for input at specific points, a GUI application starts a main loop that waits for events — button clicks, key presses, mouse movements — and dispatches them to handler functions. Understanding this shift is the foundation for everything in this module.

Python ships with Tkinter, a lightweight GUI toolkit that is easy to learn and sufficient for building practical desktop tools. While frameworks like PyQt and Kivy offer more power, Tkinter requires no extra installation and teaches the core patterns that transfer to any GUI framework.

## Concepts

### What Is a GUI?

A graphical user interface is a visual layer between the user and the program logic. It consists of windows (top-level containers) and widgets (interactive elements like buttons and text fields). The operating system draws these elements and forwards user interactions to your program.

### Event-Driven Programming

In a console program the flow is sequential: prompt, read input, process, print output. In a GUI program:

1. You build the interface (create windows, place widgets).
2. You register event handlers (functions to call when something happens).
3. You start the main event loop, which runs indefinitely, waiting for events.

The main loop is the heartbeat of a GUI application. Without it, the window appears and immediately closes.

### Python GUI Frameworks

| Framework | Comes with Python | Difficulty | Best For |
|-----------|------------------|------------|----------|
| Tkinter   | Yes              | Beginner   | Simple tools, learning GUI concepts |
| PyQt / PySide | No (pip install) | Intermediate | Professional desktop apps |
| Kivy      | No (pip install) | Intermediate | Touch/mobile interfaces |

We use Tkinter throughout this module because it is available everywhere Python runs and teaches transferable concepts.

### Tkinter Basics

Every Tkinter program follows three steps:

1. Create a root window with `tk.Tk()`.
2. Configure the window and add widgets.
3. Start the event loop with `root.mainloop()`.

## Practical Examples

### A Minimal Tkinter Window

```python
import tkinter as tk

# Step 1: Create the root window
root = tk.Tk()

# Step 2: Configure the window
root.title("My First GUI")
root.geometry("400x300")  # width x height in pixels

# Step 3: Start the event loop
root.mainloop()
```

### Setting Window Properties

```python
import tkinter as tk

root = tk.Tk()
root.title("GeekInk Application")
root.geometry("500x400")
root.configure(bg="#2c3e50")  # dark background color
root.resizable(False, False)  # prevent resizing

root.mainloop()
```

### Adding a Simple Label

```python
import tkinter as tk

root = tk.Tk()
root.title("Hello Tkinter")
root.geometry("400x200")

# A label is a widget that displays text
label = tk.Label(root, text="Welcome to GeekInk Python Engineering!")
label.pack(pady=50)  # pack places the widget and adds vertical padding

root.mainloop()
```

### Responding to a Button Click

```python
import tkinter as tk

def on_click():
    label.config(text="Button was clicked!")

root = tk.Tk()
root.title("Event Example")
root.geometry("300x200")

label = tk.Label(root, text="Click the button below")
label.pack(pady=20)

button = tk.Button(root, text="Click Me", command=on_click)
button.pack()

root.mainloop()
```

## Guided Practice

Build a personalized welcome window step by step.

**Step 1:** Create a new file called `welcome_app.py`. Import tkinter.

```python
import tkinter as tk

root = tk.Tk()
```

**Step 2:** Set the window title to your name, the size to 500x350, and the background to a color of your choice.

```python
root.title("Welcome - Your Name")
root.geometry("500x350")
root.configure(bg="#1a1a2e")
```

**Step 3:** Add a label with a welcome message. Set the font, text color, and background color.

```python
title_label = tk.Label(
    root,
    text="Welcome to My Application",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="#1a1a2e"
)
title_label.pack(pady=40)
```

**Step 4:** Add a second label with a description.

```python
desc_label = tk.Label(
    root,
    text="This is my first desktop application built with Python.",
    font=("Arial", 12),
    fg="#a0a0a0",
    bg="#1a1a2e"
)
desc_label.pack(pady=10)
```

**Step 5:** Add a button that changes the description text when clicked.

```python
def change_text():
    desc_label.config(text="You clicked the button! The GUI responded to your event.")

action_button = tk.Button(
    root,
    text="Click Me",
    font=("Arial", 12),
    command=change_text
)
action_button.pack(pady=30)
```

**Step 6:** Start the event loop.

```python
root.mainloop()
```

Run the file and verify that clicking the button changes the label text.

## Daily Challenge

Create a Tkinter window called **"GeekInk Profile Card"** with the following requirements:

1. Window title: "GeekInk Profile Card"
2. Window size: 450 x 400 pixels
3. A custom background color of your choice
4. Your name displayed in a large, bold font
5. Your role or aspiration (e.g., "Aspiring Software Engineer") in a smaller font
6. A "Show Bio" button that, when clicked, displays a short bio text in a label below the button
7. The window should not be resizable

Save the file as `profile_card.py`.

## Expected Output

When you run the program, a window appears with your name, role, and a button. Clicking "Show Bio" reveals a short paragraph about yourself. The window cannot be resized by dragging its edges.

## Assessment

1. What is the difference between a console application and a GUI application?
2. Explain what the `mainloop()` method does and why it is necessary.
3. In event-driven programming, what is an event handler?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-07/day-061/`

Include your `profile_card.py` file.

## Additional Resources

- [Tkinter Documentation (Python Official)](https://docs.python.org/3/library/tkinter.html)
- [TkDocs Tutorial](https://tkdocs.com/tutorial/index.html)

## Reflection

- How does the event-driven model change the way you think about program flow compared to sequential scripts?
- What kind of desktop tool would you find useful to build for yourself or your community?
