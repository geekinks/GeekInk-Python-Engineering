# Day 066: Dialogs and Menus

## Learning Objectives

- Use Tkinter's built-in dialog boxes: messagebox and filedialog.
- Create application menus with the Menu widget.
- Build cascading (nested) menus for organized navigation.
- Add a menu bar and file dialogs to a text editor application.

## Introduction

Menus and dialogs are standard components of every desktop application. The menu bar at the top of the window provides organized access to all application features — File, Edit, View, Help. Dialog boxes communicate with the user for confirmations, warnings, file selection, and more.

Tkinter includes ready-made dialog modules that save you from building these common interactions from scratch. The `messagebox` module provides alert, confirmation, and input dialogs. The `filedialog` module provides file open and save dialogs that use the operating system's native file browser.

Adding menus and dialogs to an application transforms it from a simple form into something that feels like a complete tool. Today you will learn to create both and begin building a text editor application.

## Concepts

### messagebox Module

```python
from tkinter import messagebox
```

| Function | Purpose | Returns |
|----------|---------|---------|
| `showinfo(title, message)` | Information alert | `"ok"` |
| `showwarning(title, message)` | Warning alert | `"ok"` |
| `showerror(title, message)` | Error alert | `"ok"` |
| `askyesno(title, message)` | Yes/No question | `True` or `False` |
| `askokcancel(title, message)` | OK/Cancel question | `True` or `False` |
| `askretrycancel(title, message)` | Retry/Cancel question | `True` or `False` |

### filedialog Module

```python
from tkinter import filedialog
```

| Function | Purpose | Returns |
|----------|---------|---------|
| `askopenfilename()` | Select a file to open | File path string (empty if cancelled) |
| `asksaveasfilename()` | Select location to save | File path string (empty if cancelled) |
| `askdirectory()` | Select a directory | Directory path string |

Both accept `filetypes` to filter visible files:

```python
filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
```

### Menu Widget

A `Menu` widget creates a menu bar or a dropdown menu:

```python
# Create the menu bar
menubar = tk.Menu(root)
root.config(menu=menubar)

# Create a dropdown menu
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)

# Add items to the dropdown
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
```

### Keyboard Shortcuts

Add accelerator labels and key bindings:

```python
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
root.bind("<Control-o>", lambda e: open_file())
```

## Practical Examples

### Message Dialogs

```python
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Dialog Examples")
root.geometry("350x250")

def info_dialog():
    messagebox.showinfo("Information", "Operation completed successfully.")

def warning_dialog():
    messagebox.showwarning("Warning", "This action cannot be undone.")

def confirm_dialog():
    response = messagebox.askyesno("Confirm", "Are you sure you want to delete this item?")
    if response:
        result.config(text="Item deleted.")
    else:
        result.config(text="Deletion cancelled.")

tk.Button(root, text="Show Info", command=info_dialog, width=20).pack(pady=10)
tk.Button(root, text="Show Warning", command=warning_dialog, width=20).pack(pady=10)
tk.Button(root, text="Confirm Delete", command=confirm_dialog, width=20).pack(pady=10)

result = tk.Label(root, text="", font=("Arial", 12))
result.pack(pady=15)

root.mainloop()
```

### File Dialogs

```python
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title("File Dialog Example")
root.geometry("400x200")

def open_file():
    path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[("Python Files", "*.py"), ("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if path:
        label.config(text=f"Selected: {path}")

def save_file():
    path = filedialog.asksaveasfilename(
        title="Save file as",
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if path:
        label.config(text=f"Save to: {path}")

tk.Button(root, text="Open File", command=open_file).pack(pady=15)
tk.Button(root, text="Save File", command=save_file).pack(pady=5)
label = tk.Label(root, text="No file selected", wraplength=350)
label.pack(pady=15)

root.mainloop()
```

### Complete Menu Bar

```python
import tkinter as tk
from tkinter import messagebox

def about():
    messagebox.showinfo("About", "GeekInk Text Tool v1.0")

root = tk.Tk()
root.title("Menu Demo")
root.geometry("400x300")

menubar = tk.Menu(root)
root.config(menu=menubar)

# File menu
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", accelerator="Ctrl+N")
file_menu.add_command(label="Open", accelerator="Ctrl+O")
file_menu.add_command(label="Save", accelerator="Ctrl+S")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Edit menu
edit_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", accelerator="Ctrl+Z")
edit_menu.add_command(label="Redo", accelerator="Ctrl+Y")
edit_menu.add_separator()
edit_menu.add_command(label="Cut", accelerator="Ctrl+X")
edit_menu.add_command(label="Copy", accelerator="Ctrl+C")
edit_menu.add_command(label="Paste", accelerator="Ctrl+V")

# Help menu
help_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

tk.Label(root, text="Application with menus", font=("Arial", 14)).pack(pady=50)

root.mainloop()
```

## Guided Practice

Build a **Note Taker** application with menus and file dialogs.

**Step 1:** Create the window with a Text widget.

```python
import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title("Note Taker")
root.geometry("600x400")

text_area = tk.Text(root, font=("Courier", 12), wrap="word")
text_area.pack(fill="both", expand=True, padx=5, pady=5)
```

**Step 2:** Implement file operations.

```python
current_file = None

def new_file():
    global current_file
    if text_area.get("1.0", tk.END).strip():
        if not messagebox.askyesno("New File", "Discard current content?"):
            return
    text_area.delete("1.0", tk.END)
    current_file = None
    root.title("Note Taker")

def open_file():
    global current_file
    path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All", "*.*")])
    if path:
        with open(path, "r") as f:
            text_area.delete("1.0", tk.END)
            text_area.insert("1.0", f.read())
        current_file = path
        root.title(f"Note Taker - {path}")

def save_file():
    global current_file
    if current_file:
        with open(current_file, "w") as f:
            f.write(text_area.get("1.0", tk.END))
        messagebox.showinfo("Saved", "File saved successfully.")
    else:
        save_as_file()

def save_as_file():
    global current_file
    path = filedialog.asksaveasfilename(defaultextension=".txt",
                                         filetypes=[("Text Files", "*.txt")])
    if path:
        with open(path, "w") as f:
            f.write(text_area.get("1.0", tk.END))
        current_file = path
        root.title(f"Note Taker - {path}")
```

**Step 3:** Create the menu bar.

```python
menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file, accelerator="Ctrl+N")
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

root.bind("<Control-n>", lambda e: new_file())
root.bind("<Control-o>", lambda e: open_file())
root.bind("<Control-s>", lambda e: save_file())

root.mainloop()
```

## Daily Challenge

Extend the Note Taker from the guided practice into a more complete application:

1. Add an "Edit" menu with Cut, Copy, Paste, and Select All options that work with the text area.
2. Add a "Help" menu with an "About" dialog showing the application name and version.
3. Add a confirmation dialog when the user tries to exit with unsaved changes (use `root.protocol("WM_DELETE_WINDOW", on_close)`).
4. Add a status bar at the bottom showing the current file name or "Untitled".
5. Add an "Insert" menu with a "Date/Time" option that inserts the current date and time at the cursor position.

Save the file as `note_taker.py`.

## Expected Output

A note-taking application with a full menu bar. Users can create, open, and save text files. Edit operations work on selected text. Attempting to close with unsaved work triggers a confirmation. The status bar shows the current file name.

## Assessment

1. What is the difference between `messagebox.askyesno()` and `messagebox.askokcancel()`?
2. What does `tearoff=0` do when creating a `Menu`?
3. How do you add a keyboard shortcut that both appears in the menu and actually triggers the function?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-07/day-066/`

Include your `note_taker.py` file.

## Additional Resources

- [Tkinter messagebox](https://docs.python.org/3/library/tkinter.messagebox.html)
- [Tkinter filedialog](https://docs.python.org/3/library/dialog.html)

## Reflection

- How do menus improve the user experience compared to placing every action as a button on the main window?
- What other dialogs would be useful in a text editor (think about Find, Replace, Font settings)?
