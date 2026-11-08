# Day 011: Lists

## Learning Objectives

- Create lists and understand them as ordered, mutable collections.
- Access and modify list elements using indexing and slicing.
- Use common list methods: `append()`, `insert()`, `remove()`, `pop()`, `sort()`, `reverse()`.
- Determine list length with `len()` and check membership with `in`.
- Understand the difference between lists and the data types learned so far.

## Introduction

So far, you have worked with individual values: one name, one score, one price. But real programs deal with collections of data — a list of students, a set of scores, a sequence of transactions. Lists are Python's most versatile data structure for storing ordered collections.

A list can hold any number of items, and those items can be of any type. You can add items, remove them, sort them, search through them, and much more. Lists are fundamental to nearly every Python program you will write.

## Concepts

### Creating Lists

```python
# Empty list
students = []

# List with initial values
scores = [85, 92, 78, 90, 88]

# Mixed types (valid but usually avoided)
mixed = ["Amina", 25, 3.8, True]
```

### Indexing and Slicing

Lists use the same indexing as strings:

```python
fruits = ["mango", "banana", "orange", "guava", "pawpaw"]
#          0         1         2         3        4
#         -5        -4        -3        -2       -1

print(fruits[0])      # "mango"
print(fruits[-1])     # "pawpaw"
print(fruits[1:3])    # ["banana", "orange"]
```

### Mutability

Unlike strings, lists can be changed in place:

```python
fruits[0] = "apple"   # Replace first item
```

### Common List Methods

| Method              | Action                                    |
| ------------------- | ----------------------------------------- |
| `.append(item)`     | Add item to the end                       |
| `.insert(i, item)`  | Insert item at index `i`                  |
| `.remove(item)`     | Remove first occurrence of item           |
| `.pop(i)`           | Remove and return item at index `i`       |
| `.pop()`            | Remove and return last item               |
| `.sort()`           | Sort in ascending order (in place)        |
| `.reverse()`        | Reverse the list (in place)               |
| `.index(item)`      | Return index of first occurrence          |
| `.count(item)`      | Count occurrences of item                 |
| `.copy()`           | Return a shallow copy                     |
| `.clear()`          | Remove all items                          |

## Practical Examples

```python
# Building a list step by step
shopping = []
shopping.append("rice")
shopping.append("beans")
shopping.append("oil")
shopping.insert(0, "bread")  # Add at the beginning
print(shopping)  # ["bread", "rice", "beans", "oil"]
```

```python
# Removing items
removed = shopping.pop()     # Removes "oil", returns it
print(removed)               # "oil"
shopping.remove("beans")     # Removes "beans"
print(shopping)              # ["bread", "rice"]
```

```python
# Sorting
numbers = [42, 17, 8, 95, 33, 61]
numbers.sort()
print(numbers)  # [8, 17, 33, 42, 61, 95]

numbers.sort(reverse=True)
print(numbers)  # [95, 61, 42, 33, 17, 8]
```

```python
# Useful operations
names = ["Zainab", "Musa", "Fatima", "Umar", "Aisha"]
print(len(names))             # 5
print("Musa" in names)        # True
print("Ibrahim" in names)     # False
print(min([10, 5, 20, 3]))    # 3
print(max([10, 5, 20, 3]))    # 20
print(sum([10, 5, 20, 3]))    # 38
```

```python
# Iterating over a list
cities = ["Kano", "Lagos", "Abuja", "Kaduna"]
for city in cities:
    print(f"Welcome to {city}")
```

## Guided Practice

Create a file called `shopping_list.py`:

1. Start with an empty list.
2. Add five items to it using `append()`.
3. Print the list and its length.
4. Insert an item at position 2.
5. Remove the last item using `pop()`.
6. Sort the list alphabetically.
7. Print the final list.

```python
shopping = []

shopping.append("yam")
shopping.append("tomatoes")
shopping.append("pepper")
shopping.append("onions")
shopping.append("maggi")

print(f"Shopping list ({len(shopping)} items): {shopping}")

shopping.insert(2, "palm oil")
print(f"After insert: {shopping}")

removed = shopping.pop()
print(f"Removed: {removed}")

shopping.sort()
print(f"Sorted: {shopping}")
print(f"Final list ({len(shopping)} items): {shopping}")
```

## Daily Challenge

Build a program called `todo_manager.py` that implements a simple to-do list manager:

1. Display a menu with these options:
   - 1: Add a task
   - 2: View all tasks
   - 3: Remove a task (by number)
   - 4: Mark a task as done (move it to a "completed" list)
   - 5: View completed tasks
   - 6: Exit

2. The program should keep running until the user chooses to exit.

3. When viewing tasks, display them numbered:
   ```
   Your Tasks:
   1. Buy groceries
   2. Study Python
   3. Call Amina
   ```

4. When removing or completing a task, ask for the task number.

5. Handle invalid inputs gracefully (non-numeric input, out-of-range numbers).

Example interaction:

```
===== TO-DO MANAGER =====

1. Add task
2. View tasks
3. Remove task
4. Complete task
5. View completed
6. Exit

Choice: 1
Enter task: Study Python Day 11
Task added!

Choice: 2
Your Tasks:
1. Study Python Day 11

Choice: 1
Enter task: Review Day 10 project
Task added!

Choice: 4
Your Tasks:
1. Study Python Day 11
2. Review Day 10 project
Complete task number: 1
"Study Python Day 11" marked as done!

Choice: 5
Completed Tasks:
1. Study Python Day 11

Choice: 6
Goodbye!
```

## Expected Output

A fully interactive to-do manager that allows adding, viewing, removing, and completing tasks, with persistent state during the session and graceful error handling.

## Assessment

1. What is the difference between `list.remove(item)` and `list.pop(index)`?
2. What happens if you try to access `my_list[10]` when the list only has 3 items?
3. How do you check if an item exists in a list without causing an error?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-02/day-011/`

Your submission should include:
- `todo_manager.py` containing your solution to the daily challenge.

## Additional Resources

- [Python Official Docs — Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
- [Python Official Docs — Sequence Types](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)

## Reflection

- How are lists different from the individual variables you used in Module 1?
- Think of a real-world scenario where you would use a list in a program. What kind of data would it hold?
