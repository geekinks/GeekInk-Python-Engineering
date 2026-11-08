# Day 067: Building a Text Editor

## Learning Objectives

- Combine multiple Tkinter widgets into a cohesive application.
- Use the Text widget with a Scrollbar for handling large content.
- Implement file open, save, and edit operations in a unified interface.
- Add a status bar that tracks application state.

## Introduction

Building a complete application requires bringing together everything learned so far: widgets, layout, events, menus, and dialogs. A text editor is an ideal project for this because it uses nearly every GUI concept and produces a genuinely useful tool.

Today you will build a functional text editor from scratch. It will support creating, opening, and saving files, basic text editing operations, a scrollable text area, and a status bar. This is the kind of project that demonstrates your ability to design and implement a multi-feature desktop application.

The goal is not to replicate VS Code but to build something you could actually use for quick notes and editing — proof that you can ship a working tool.

## Concepts

### Text Widget with Scrollbar

The Text widget handles multi-line content, but for large documents you need a scrollbar:

```python
text_frame = tk.Frame(root)
text_frame.pack(fill="both", expand=True)

scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side="right", fill="y")

text_area = tk.Text(text_frame, yscrollcommand=scrollbar.set, wrap="word")
text_area.pack(side="left", fill="both", expand=True)

scrollbar.config(command=text_area.yview)
```

### Text Widget Operations

```python
# Insert text at the cursor
text_area.insert(tk.INSERT, "Hello")

# Get all content
content = text_area.get("1.0", tk.END)

# Get selected text
selected = text_area.get(tk.SEL_FIRST, tk.SEL_LAST)

# Delete selected text
text_area.delete(tk.SEL_FIRST, tk.SEL_LAST)

# Find text position
pos = text_area.search("word", "1.0", stopindex=tk.END)
```

### Tracking Changes

Use a modified flag to detect unsaved changes:

```python
text_area.edit_modified()    # Returns True if content changed
text_area.edit_modified(False)  # Reset the flag
```

### Window Close Protocol

Intercept the window close event:

```python
def on_close():
    if text_area.edit_modified():
        response = messagebox.askyesnocancel("Unsaved Changes", "Save before closing?")
        if response is True:
            save_file()
        elif response is None:
            return  # Cancel the close
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)
```

## Practical Examples

### Complete Text Editor

```python
import tkinter as tk
from tkinter import filedialog, messagebox
import os
from datetime import datetime


class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("GeekInk Editor")
        self.root.geometry("700x500")
        self.current_file = None

        self._create_menu()
        self._create_text_area()
        self._create_status_bar()
        self._bind_shortcuts()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def _create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file, accelerator="Ctrl+N")
        file_menu.add_command(label="Open", command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        file_menu.add_command(label="Save As", command=self.save_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.on_close)

        # Edit menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Undo", command=lambda: self.text.edit_undo(),
                              accelerator="Ctrl+Z")
        edit_menu.add_command(label="Redo", command=lambda: self.text.edit_redo(),
                              accelerator="Ctrl+Y")
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", command=self.cut, accelerator="Ctrl+X")
        edit_menu.add_command(label="Copy", command=self.copy, accelerator="Ctrl+C")
        edit_menu.add_command(label="Paste", command=self.paste, accelerator="Ctrl+V")
        edit_menu.add_separator()
        edit_menu.add_command(label="Select All", command=self.select_all,
                              accelerator="Ctrl+A")

        # Insert menu
        insert_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Insert", menu=insert_menu)
        insert_menu.add_command(label="Date/Time", command=self.insert_datetime)

        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.about)

    def _create_text_area(self):
        text_frame = tk.Frame(self.root)
        text_frame.pack(fill="both", expand=True)

        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side="right", fill="y")

        self.text = tk.Text(text_frame, font=("Courier", 12), wrap="word",
                            undo=True, yscrollcommand=scrollbar.set)
        self.text.pack(side="left", fill="both", expand=True, padx=2, pady=2)

        scrollbar.config(command=self.text.yview)

    def _create_status_bar(self):
        self.status = tk.Label(self.root, text="Untitled", anchor="w",
                               bg="#e0e0e0", padx=10)
        self.status.pack(fill="x", side="bottom")

    def _bind_shortcuts(self):
        self.root.bind("<Control-n>", lambda e: self.new_file())
        self.root.bind("<Control-o>", lambda e: self.open_file())
        self.root.bind("<Control-s>", lambda e: self.save_file())
        self.root.bind("<Control-a>", lambda e: self.select_all())

    def _update_title(self):
        name = os.path.basename(self.current_file) if self.current_file else "Untitled"
        self.root.title(f"{name} - GeekInk Editor")
        self.status.config(text=self.current_file or "Untitled")

    def new_file(self):
        if self.text.edit_modified():
            response = messagebox.askyesnocancel("New File", "Save current file?")
            if response is True:
                self.save_file()
            elif response is None:
                return
        self.text.delete("1.0", tk.END)
        self.text.edit_modified(False)
        self.current_file = None
        self._update_title()

    def open_file(self):
        path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("Python Files", "*.py"),
                       ("All Files", "*.*")]
        )
        if path:
            with open(path, "r") as f:
                self.text.delete("1.0", tk.END)
                self.text.insert("1.0", f.read())
            self.text.edit_modified(False)
            self.current_file = path
            self._update_title()

    def save_file(self):
        if self.current_file:
            with open(self.current_file, "w") as f:
                f.write(self.text.get("1.0", tk.END).rstrip("\n"))
            self.text.edit_modified(False)
        else:
            self.save_as()

    def save_as(self):
        path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("Python Files", "*.py"),
                       ("All Files", "*.*")]
        )
        if path:
            self.current_file = path
            self.save_file()
            self._update_title()

    def cut(self):
        self.text.event_generate("<<Cut>>")

    def copy(self):
        self.text.event_generate("<<Copy>>")

    def paste(self):
        self.text.event_generate("<<Paste>>")

    def select_all(self):
        self.text.tag_add("sel", "1.0", tk.END)
        return "break"

    def insert_datetime(self):
        self.text.insert(tk.INSERT, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def about(self):
        messagebox.showinfo("About", "GeekInk Editor v1.0\nA simple text editor built with Python and Tkinter.")

    def on_close(self):
        if self.text.edit_modified():
            response = messagebox.askyesnocancel("Exit", "Save before closing?")
            if response is True:
                self.save_file()
            elif response is None:
                return
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    TextEditor(root)
    root.mainloop()
```

## Guided Practice

Follow the complete example above and type it out yourself. As you do:

1. Run it after adding just the text area — verify it appears with a scrollbar.
2. Add the menu bar and test each menu item one at a time.
3. Add the status bar and verify it updates when you open a file.
4. Add the close handler and verify it prompts to save.
5. Test the undo/redo functionality by typing, undoing, and redoing.

## Daily Challenge

Extend the text editor with these additional features:

1. **Line numbers**: Display line numbers in a narrow panel on the left side of the text area. They should update as the user types or scrolls.
2. **Word count**: Show the word count and character count in the status bar, updating as the user types.
3. **Find and Replace**: Add a "Find" option to the Edit menu (Ctrl+F) that opens a small bar at the top of the text area with an entry field for searching. Highlight all matches in the text.

Save the file as `text_editor.py`.

## Expected Output

A text editor with line numbers on the left, a live word/character count in the status bar, and a find function that highlights matching text.

## Assessment

1. How do you connect a Scrollbar to a Text widget so they scroll together?
2. What does `text.edit_modified()` return and when is it useful?
3. Why do we use `root.protocol("WM_DELETE_WINDOW", on_close)` instead of just binding a key?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-07/day-067/`

Include your `text_editor.py` file.

## Additional Resources

- [Tkinter Text Widget](https://docs.python.org/3/library/tkinter.html#the-text-widget)
- [TkDocs: Text](https://tkdocs.com/tutorial/text.html)

## Reflection

- What features do you use most in your own text editor? How many of them could you implement with what you know now?
- How does organizing code into a class (like `TextEditor`) compare to writing everything as loose functions?
