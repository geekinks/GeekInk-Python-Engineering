# Day 063: Layout Management

## Learning Objectives

- Master the `grid()` geometry manager for structured layouts.
- Understand row and column spanning, padding, and the `sticky` option.
- Use `Frame` containers to organize groups of widgets.
- Build complex, nested layouts for real applications.

## Introduction

A well-designed layout is what separates a usable application from a frustrating one. Users expect controls to be aligned, grouped logically, and spaced consistently. The `grid()` geometry manager gives you precise control over widget placement by treating the window as a table of rows and columns.

Professional GUI applications use nested containers: frames within frames, each managing its own group of widgets. This approach mirrors the principle of separation of concerns — each frame is responsible for a logical section of the interface, making the code easier to maintain and modify.

Today you will build increasingly complex layouts, culminating in a calculator interface that demonstrates grid-based design at its most practical.

## Concepts

### The grid() System

`grid()` places widgets in a table structure defined by `row` and `column` indices (starting at 0). Tkinter sizes rows and columns to fit the largest widget in each.

```python
widget.grid(row=0, column=0)
```

### Key grid() Options

| Option       | Description |
|-------------|-------------|
| `row`       | Row index (0-based) |
| `column`    | Column index (0-based) |
| `rowspan`   | Number of rows the widget spans |
| `columnspan`| Number of columns the widget spans |
| `padx`      | Horizontal padding (pixels) outside the widget |
| `pady`      | Vertical padding (pixels) outside the widget |
| `ipadx`     | Internal horizontal padding |
| `ipady`     | Internal vertical padding |
| `sticky`    | Which sides the widget sticks to: `"n"`, `"s"`, `"e"`, `"w"`, or combinations like `"ew"` (stretch horizontally) or `"nsew"` (fill cell) |

### The sticky Option

By default, a widget sits centered in its grid cell. `sticky` controls alignment and stretching:

- `sticky="w"` — align to the left (west)
- `sticky="e"` — align to the right (east)
- `sticky="ew"` — stretch to fill the full width
- `sticky="nsew"` — fill the entire cell

### Column and Row Configuration

To make columns or rows expand when the window is resized:

```python
root.columnconfigure(0, weight=1)  # column 0 will expand
root.rowconfigure(0, weight=1)     # row 0 will expand
```

A `weight` of 0 (the default) means the row or column will not expand.

### Frame Containers

A `Frame` is an invisible container that groups related widgets. Each frame can use its own geometry manager independently.

```python
header_frame = tk.Frame(root, bg="#333333", height=60)
header_frame.grid(row=0, column=0, sticky="ew")

content_frame = tk.Frame(root)
content_frame.grid(row=1, column=0, sticky="nsew")
```

## Practical Examples

### Spanning Rows and Columns

```python
import tkinter as tk

root = tk.Tk()
root.title("Spanning Example")

# A header that spans two columns
header = tk.Label(root, text="Application Header", font=("Arial", 16), bg="#2c3e50", fg="white")
header.grid(row=0, column=0, columnspan=2, sticky="ew", ipady=10)

# Sidebar and main content
sidebar = tk.Label(root, text="Sidebar", bg="#ecf0f1", width=15)
sidebar.grid(row=1, column=0, sticky="ns", ipady=50)

content = tk.Label(root, text="Main Content Area", bg="white", width=30)
content.grid(row=1, column=1, sticky="nsew", ipady=50)

# Footer spanning two columns
footer = tk.Label(root, text="Footer", bg="#2c3e50", fg="white")
footer.grid(row=2, column=0, columnspan=2, sticky="ew", ipady=5)

root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)

root.mainloop()
```

### Nested Frames

```python
import tkinter as tk

root = tk.Tk()
root.title("Nested Frames")
root.geometry("400x300")

# Top frame with pack
top_frame = tk.Frame(root, bg="#34495e", height=50)
top_frame.pack(fill="x")
tk.Label(top_frame, text="Dashboard", fg="white", bg="#34495e",
         font=("Arial", 14)).pack(pady=10)

# Bottom frame split into two columns using grid
bottom_frame = tk.Frame(root)
bottom_frame.pack(fill="both", expand=True)

left_panel = tk.Frame(bottom_frame, bg="#ecf0f1", width=150)
left_panel.grid(row=0, column=0, sticky="ns")

right_panel = tk.Frame(bottom_frame, bg="white")
right_panel.grid(row=0, column=1, sticky="nsew")

bottom_frame.columnconfigure(1, weight=1)
bottom_frame.rowconfigure(0, weight=1)

# Add items to left panel
for i, item in enumerate(["Home", "Reports", "Settings"]):
    tk.Button(left_panel, text=item, width=15).grid(row=i, column=0, pady=5, padx=5)

# Add content to right panel
tk.Label(right_panel, text="Welcome to the Dashboard",
         font=("Arial", 14)).grid(row=0, column=0, padx=20, pady=20)

root.mainloop()
```

### Calculator Layout

```python
import tkinter as tk

root = tk.Tk()
root.title("Calculator Layout")
root.resizable(False, False)

# Display
display = tk.Entry(root, font=("Arial", 20), justify="right", bd=5, relief="sunken")
display.grid(row=0, column=0, columnspan=4, sticky="ew", padx=5, pady=5, ipady=10)

# Button labels in grid order
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (text, row, col) in buttons:
    tk.Button(root, text=text, font=("Arial", 16), width=5, height=2).grid(
        row=row, column=col, padx=2, pady=2
    )

# Clear button spanning full width
tk.Button(root, text="Clear", font=("Arial", 14), height=1).grid(
    row=5, column=0, columnspan=4, sticky="ew", padx=5, pady=5
)

root.mainloop()
```

## Guided Practice

Build a **Login Screen** layout using `grid()` and frames.

**Step 1:** Create the window and a centered frame.

```python
import tkinter as tk

root = tk.Tk()
root.title("Login")
root.geometry("400x350")
root.configure(bg="#f0f0f0")

# Center frame
login_frame = tk.Frame(root, bg="white", bd=2, relief="groove")
login_frame.place(relx=0.5, rely=0.5, anchor="center")
```

**Step 2:** Add a title label inside the frame.

```python
tk.Label(login_frame, text="Sign In", font=("Arial", 18, "bold"),
         bg="white").grid(row=0, column=0, columnspan=2, pady=(20, 15))
```

**Step 3:** Add username and password fields.

```python
tk.Label(login_frame, text="Username:", bg="white").grid(
    row=1, column=0, padx=(20, 5), pady=8, sticky="e")
username = tk.Entry(login_frame, width=22)
username.grid(row=1, column=1, padx=(5, 20), pady=8)

tk.Label(login_frame, text="Password:", bg="white").grid(
    row=2, column=0, padx=(20, 5), pady=8, sticky="e")
password = tk.Entry(login_frame, width=22, show="*")
password.grid(row=2, column=1, padx=(5, 20), pady=8)
```

**Step 4:** Add a login button that spans both columns.

```python
tk.Button(login_frame, text="Login", width=20,
          command=lambda: print(f"User: {username.get()}")
).grid(row=3, column=0, columnspan=2, pady=(15, 20))

root.mainloop()
```

## Daily Challenge

Build a **Calculator Layout** with the following requirements:

1. A display area at the top (use `Entry` with right-justified text) spanning four columns.
2. Number buttons 0-9 arranged in a standard calculator grid.
3. Operator buttons: +, -, *, /
4. A decimal point button and an equals button.
5. A "Clear" button spanning the full bottom row.
6. All buttons should have consistent size and spacing.
7. The layout should use `grid()` exclusively.

This challenge is about layout only. The buttons do not need to be functional yet (that comes tomorrow).

Save the file as `calculator_layout.py`.

## Expected Output

A window displaying a calculator interface with aligned buttons in a clean grid. Buttons do not perform calculations yet, but the layout is complete and visually consistent.

## Assessment

1. What does `columnspan=2` do when passed to `grid()`?
2. How does `sticky="ew"` differ from `sticky="nsew"`?
3. Why is it useful to group widgets inside a `Frame` before placing the frame in the main window?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-07/day-063/`

Include your `calculator_layout.py` file.

## Additional Resources

- [TkDocs: The Grid Geometry Manager](https://tkdocs.com/tutorial/grid.html)
- [Python Docs: tkinter.Grid](https://docs.python.org/3/library/tkinter.html#the-grid-geometry-manager)

## Reflection

- How does thinking in rows and columns compare to thinking about positioning in CSS or other layout systems you may have encountered?
- What challenges did you face when trying to make buttons uniform in size?
