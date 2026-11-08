# Day 069: Error Handling and Polish

## Learning Objectives

- Implement user-friendly error messages in GUI applications.
- Add input validation feedback that guides users toward correct input.
- Use visual indicators (colors, labels) to communicate application state.
- Manage application state to prevent invalid operations.

## Introduction

A working application and a good application are different things. Working means the code runs without crashing. Good means the user never feels lost, confused, or frustrated. The difference is error handling and polish.

In command-line programs, error messages print to the terminal and the user reads them in context. In GUI applications, errors need to be communicated visually — through dialog boxes, colored borders, inline labels, or status messages. A text field that turns red when the input is invalid is more helpful than a dialog box that interrupts the user's flow.

Today you will take the contact manager from Day 068 and add comprehensive error handling, validation feedback, and visual polish that makes it feel like a finished product.

## Concepts

### Levels of Error Feedback

1. **Prevention**: Disable buttons or options that do not apply in the current state (e.g., disable "Update" when no record is selected).
2. **Inline validation**: Show immediate feedback next to the field (a colored border, a small label below the field).
3. **Summary validation**: On form submission, check all fields and show a single message listing all errors.
4. **Graceful recovery**: When an operation fails (database error, file not found), show a clear message and keep the application in a usable state.

### Changing Widget Appearance for Feedback

```python
# Highlight an entry field with a red border
entry.config(highlightbackground="red", highlightcolor="red", highlightthickness=2)

# Reset to normal
entry.config(highlightthickness=0)

# Show inline error text
error_label = tk.Label(root, text="This field is required", fg="red", font=("Arial", 9))
```

### Disabling and Enabling Widgets

```python
button.config(state="disabled")  # Grey out the button
button.config(state="normal")    # Re-enable it
```

### Try/Except in GUI Context

```python
def save_record():
    try:
        conn.execute("INSERT INTO records ...")
        conn.commit()
        messagebox.showinfo("Success", "Record saved.")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "A record with that ID already exists.")
    except sqlite3.OperationalError as e:
        messagebox.showerror("Database Error", f"Could not save: {e}")
```

### Status Bar Updates

```python
def update_status(message, duration=3000):
    status_label.config(text=message)
    root.after(duration, lambda: status_label.config(text="Ready"))
```

The `after()` method schedules a function to run after a delay (in milliseconds), which is useful for temporary messages.

## Practical Examples

### Inline Validation

```python
import tkinter as tk

def validate_email(*args):
    email = email_var.get()
    if email and "@" not in email:
        email_error.config(text="Please enter a valid email address")
        email_entry.config(highlightbackground="red", highlightcolor="red", highlightthickness=2)
    else:
        email_error.config(text="")
        email_entry.config(highlightthickness=0)

root = tk.Tk()
root.title("Inline Validation")
root.geometry("400x200")

tk.Label(root, text="Email:").pack(anchor="w", padx=20, pady=(20, 0))

email_var = tk.StringVar()
email_var.trace_add("write", validate_email)

email_entry = tk.Entry(root, textvariable=email_var, width=35)
email_entry.pack(padx=20, pady=5, anchor="w")

email_error = tk.Label(root, text="", fg="red", font=("Arial", 9))
email_error.pack(anchor="w", padx=20)

root.mainloop()
```

### State-Aware Buttons

```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("State Management")
root.geometry("500x350")

tree = ttk.Treeview(root, columns=("name", "value"), show="headings", height=6)
tree.heading("name", text="Name")
tree.heading("value", text="Value")
tree.pack(padx=10, pady=10)

for item in [("Temperature", "32C"), ("Humidity", "65%"), ("Pressure", "1013hPa")]:
    tree.insert("", tk.END, values=item)

btn_frame = tk.Frame(root)
btn_frame.pack()

edit_btn = tk.Button(btn_frame, text="Edit", state="disabled", width=10)
delete_btn = tk.Button(btn_frame, text="Delete", state="disabled", width=10)
edit_btn.pack(side="left", padx=5)
delete_btn.pack(side="left", padx=5)

def on_select(event):
    if tree.selection():
        edit_btn.config(state="normal")
        delete_btn.config(state="normal")
    else:
        edit_btn.config(state="disabled")
        delete_btn.config(state="disabled")

tree.bind("<<TreeviewSelect>>", on_select)

root.mainloop()
```

### Temporary Status Messages

```python
import tkinter as tk

root = tk.Tk()
root.title("Status Demo")
root.geometry("400x200")

status = tk.Label(root, text="Ready", anchor="w", bg="#e0e0e0", padx=10)
status.pack(side="bottom", fill="x")

def show_status(message, color="black"):
    status.config(text=message, fg=color)
    root.after(3000, lambda: status.config(text="Ready", fg="black"))

def action_success():
    show_status("Item saved successfully.", "green")

def action_error():
    show_status("Error: could not save item.", "red")

tk.Button(root, text="Simulate Success", command=action_success).pack(pady=20)
tk.Button(root, text="Simulate Error", command=action_error).pack()

root.mainloop()
```

## Guided Practice

Take the Contact Manager from Day 068 and add these improvements:

**Step 1:** Disable Update and Delete buttons when no contact is selected.

```python
self.update_btn = tk.Button(btn_frame, text="Update", width=10,
                             command=self.update_contact, state="disabled")
self.delete_btn = tk.Button(btn_frame, text="Delete", width=10,
                             command=self.delete_contact, state="disabled")

def _on_select(self, event):
    selected = self.tree.selection()
    if selected:
        self.update_btn.config(state="normal")
        self.delete_btn.config(state="normal")
        # fill form...
    else:
        self.update_btn.config(state="disabled")
        self.delete_btn.config(state="disabled")
```

**Step 2:** Add a status bar with temporary messages.

```python
def _show_status(self, message, color="black"):
    self.status.config(text=message, fg=color)
    self.root.after(3000, lambda: self.status.config(text="Ready", fg="black"))
```

Call `self._show_status("Contact added.", "green")` after a successful add.

**Step 3:** Wrap database operations in try/except.

**Step 4:** Add email validation that highlights the email entry in red when the format is invalid.

## Daily Challenge

Take the Contact Manager (or your Book Library Manager from Day 068) and add comprehensive polish:

1. Disable Edit/Delete buttons when no row is selected; enable them when a row is selected.
2. Add inline validation for at least two fields (e.g., name required, email format).
3. Highlight invalid fields with a colored border.
4. Add a status bar that shows temporary success/error messages (auto-clear after 3 seconds).
5. Wrap all database operations in try/except with user-friendly error messages.
6. Add a record count display (e.g., "3 contacts" in the status bar).
7. Ask for confirmation before deleting a record.
8. After adding or updating a record, automatically select that record in the table.

Save the file as `polished_app.py`.

## Expected Output

An application that never crashes from user input errors, provides clear visual feedback, prevents invalid operations, and communicates success and failure through the status bar and inline validation.

## Assessment

1. Why is it better to disable a button that does not apply in the current state than to show an error when the user clicks it?
2. What is the purpose of `root.after()` and how does it differ from `time.sleep()`?
3. Describe two ways to provide validation feedback to the user in a GUI application.

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-07/day-069/`

Include your `polished_app.py` file.

## Additional Resources

- [Tkinter after() Method](https://docs.python.org/3/library/tkinter.html#tkinter.Misc.after)
- [TkDocs: Styles and Themes](https://tkdocs.com/tutorial/styles.html)

## Reflection

- Think about an application you use regularly. What error handling and polish features make it pleasant to use?
- How does investing time in error handling and polish affect the overall quality of your software?
