# Day 064: Event Handling

## Learning Objectives

- Understand how Tkinter processes events through its main loop.
- Use the `command` parameter to handle button clicks.
- Use the `bind()` method to respond to keyboard and mouse events.
- Work with event objects to extract information about user interactions.
- Make the calculator layout from Day 063 fully functional.

## Introduction

Event handling is the mechanism that makes GUI applications interactive. When a user clicks a button, presses a key, or moves the mouse, the operating system generates an event. Tkinter's main loop intercepts these events and calls the appropriate handler function in your code.

There are two primary ways to handle events in Tkinter. The `command` parameter is the simpler approach — you pass a function reference to a button and it gets called when the button is clicked. The `bind()` method is more powerful — it lets you respond to any event on any widget, including key presses, mouse motion, window resizing, and focus changes.

Understanding event handling is essential for building applications that react to user input in real time. Every interactive feature, from form validation to drag-and-drop, is built on top of the event system.

## Concepts

### The command Parameter

The simplest way to handle a button click:

```python
def handle_click():
    print("Button clicked!")

button = tk.Button(root, text="Click", command=handle_click)
```

The function is passed by name without parentheses. Writing `command=handle_click()` would call the function immediately and pass its return value instead.

### Passing Arguments to Callbacks

Since `command` takes a function with no arguments, use `lambda` to pass values:

```python
def show_number(n):
    print(f"You pressed {n}")

tk.Button(root, text="5", command=lambda: show_number(5))
```

### The bind() Method

`bind()` connects any event to any widget:

```python
widget.bind("<event_pattern>", handler_function)
```

The handler receives an `event` object with information about what happened.

### Common Event Patterns

| Pattern           | Description |
|-------------------|-------------|
| `<Button-1>`      | Left mouse click |
| `<Button-3>`      | Right mouse click |
| `<Double-Button-1>` | Double left click |
| `<Key>`           | Any key press |
| `<Return>`        | Enter key |
| `<Escape>`        | Escape key |
| `<KeyPress-a>`    | The "a" key |
| `<Motion>`        | Mouse movement |
| `<FocusIn>`       | Widget gains focus |
| `<FocusOut>`      | Widget loses focus |
| `<Configure>`     | Widget is resized |

### The Event Object

When using `bind()`, the handler receives an event object with these attributes:

- `event.widget` — the widget that received the event
- `event.x`, `event.y` — mouse position relative to the widget
- `event.char` — the character typed (for key events)
- `event.keysym` — the key name (e.g., `"Return"`, `"Escape"`)

## Practical Examples

### Button Command with Lambda

```python
import tkinter as tk

def update_label(color):
    display.config(text=f"You selected: {color}", bg=color, fg="white")

root = tk.Tk()
root.title("Color Picker")
root.geometry("300x200")

display = tk.Label(root, text="Pick a color", font=("Arial", 14))
display.pack(pady=20)

frame = tk.Frame(root)
frame.pack()

for color in ["#e74c3c", "#2ecc71", "#3498db", "#9b59b6"]:
    tk.Button(frame, bg=color, width=5, height=2,
              command=lambda c=color: update_label(c)).pack(side="left", padx=5)

root.mainloop()
```

### Binding Keyboard Events

```python
import tkinter as tk

def on_key(event):
    label.config(text=f"Key: {event.keysym}  Char: '{event.char}'")

root = tk.Tk()
root.title("Key Logger")
root.geometry("350x150")

label = tk.Label(root, text="Press any key...", font=("Arial", 16))
label.pack(pady=30)

root.bind("<Key>", on_key)
root.mainloop()
```

### Binding Mouse Events

```python
import tkinter as tk

def on_click(event):
    label.config(text=f"Clicked at ({event.x}, {event.y})")

def on_motion(event):
    coords.config(text=f"Mouse: ({event.x}, {event.y})")

root = tk.Tk()
root.title("Mouse Events")
root.geometry("400x300")

label = tk.Label(root, text="Click anywhere in the window", font=("Arial", 12))
label.pack(pady=20)

coords = tk.Label(root, text="Mouse: (0, 0)")
coords.pack(pady=10)

root.bind("<Button-1>", on_click)
root.bind("<Motion>", on_motion)
root.mainloop()
```

### A Functional Calculator

```python
import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.expression = ""

        self.display = tk.Entry(root, font=("Arial", 20), justify="right",
                                bd=5, relief="sunken")
        self.display.grid(row=0, column=0, columnspan=4, sticky="ew",
                          padx=5, pady=5, ipady=10)

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
        ]

        for (text, row, col) in buttons:
            if text == "=":
                cmd = self.calculate
            else:
                cmd = lambda t=text: self.append(t)
            tk.Button(root, text=text, font=("Arial", 16), width=5, height=2,
                      command=cmd).grid(row=row, column=col, padx=2, pady=2)

        tk.Button(root, text="Clear", font=("Arial", 14), height=1,
                  command=self.clear).grid(row=5, column=0, columnspan=4,
                                            sticky="ew", padx=5, pady=5)

        root.bind("<Key>", self.on_key)

    def append(self, char):
        self.expression += char
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
            self.expression = result
        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.display.delete(0, tk.END)

    def on_key(self, event):
        if event.char in "0123456789.+-*/":
            self.append(event.char)
        elif event.keysym == "Return":
            self.calculate()
        elif event.keysym == "Escape":
            self.clear()

root = tk.Tk()
Calculator(root)
root.mainloop()
```

## Guided Practice

Take your calculator layout from Day 063 and make it functional.

**Step 1:** Define a variable to hold the current expression.

```python
expression = ""
```

**Step 2:** Write a function to append characters to the display.

```python
def press(char):
    global expression
    expression += str(char)
    display.delete(0, tk.END)
    display.insert(tk.END, expression)
```

**Step 3:** Write a function to evaluate the expression.

```python
def evaluate():
    global expression
    try:
        result = str(eval(expression))
        display.delete(0, tk.END)
        display.insert(tk.END, result)
        expression = result
    except Exception:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        expression = ""
```

**Step 4:** Write a function to clear the display.

```python
def clear():
    global expression
    expression = ""
    display.delete(0, tk.END)
```

**Step 5:** Connect each button to the appropriate function using `command=lambda`.

**Step 6:** Add keyboard bindings so users can also type numbers and press Enter.

## Daily Challenge

Make the calculator layout from Day 063 fully functional with these requirements:

1. Clicking number buttons appends digits to the display.
2. Clicking operator buttons appends the operator.
3. Clicking "=" evaluates the expression and shows the result.
4. Clicking "Clear" resets the display.
5. If the expression is invalid, display "Error" instead of crashing.
6. Keyboard support: number keys, operator keys, Enter for "=", Escape for clear.
7. After showing a result, typing a number starts a new expression; typing an operator continues from the result.

Save the file as `calculator.py`.

## Expected Output

A working calculator that handles basic arithmetic. Users can click buttons or type on the keyboard. Invalid expressions show "Error" and the calculator recovers gracefully.

## Assessment

1. What is the difference between `command=my_func` and `command=my_func()`?
2. How does `bind()` differ from the `command` parameter?
3. What information does the `event` object provide when handling a key press?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-07/day-064/`

Include your `calculator.py` file.

## Additional Resources

- [Tkinter Events and Bindings](https://docs.python.org/3/library/tkinter.html#bindings-and-events)
- [TkDocs: Event Handling](https://tkdocs.com/tutorial/concepts.html#events)

## Reflection

- How does connecting a function to a button click compare to other callback patterns you have seen (for example, passing functions as arguments)?
- What was the trickiest part of making the calculator respond correctly to both clicks and key presses?
