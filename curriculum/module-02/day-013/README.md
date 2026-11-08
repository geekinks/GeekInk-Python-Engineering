# Day 013: Dictionaries

## Learning Objectives

- Create dictionaries and understand key-value pair storage.
- Access, add, modify, and delete dictionary entries.
- Use dictionary methods: `.keys()`, `.values()`, `.items()`, `.get()`.
- Work with nested dictionaries for complex data.
- Choose between dictionaries and lists based on the problem.

## Introduction

A list stores items by position (index 0, 1, 2...), but sometimes you need to store data by a meaningful label. A dictionary stores data as key-value pairs: instead of accessing item number 3, you access the item labeled "name" or "score". This is how most real-world data is structured — student records, configuration settings, API responses, and database rows all use key-value mapping.

Dictionaries are one of the most used data structures in Python. After today, you will use them in nearly every project.

## Concepts

### Creating Dictionaries

```python
student = {
    "name": "Abubakar Sadiq",
    "age": 22,
    "department": "Computer Science",
    "gpa": 3.75
}
```

Keys must be immutable types (strings, numbers, tuples). Values can be anything.

### Accessing and Modifying

```python
print(student["name"])        # Abubakar Sadiq
print(student.get("email", "Not provided"))  # Safe access with default

student["age"] = 23           # Modify existing
student["email"] = "abu@example.com"  # Add new key
del student["gpa"]            # Delete a key
```

### Dictionary Methods

| Method        | Returns                                |
| ------------- | -------------------------------------- |
| `.keys()`     | All keys                               |
| `.values()`   | All values                             |
| `.items()`    | All key-value pairs as tuples          |
| `.get(k, d)`  | Value for key `k`, or `d` if missing   |
| `.pop(k)`     | Remove key `k` and return its value    |
| `.update(d)`  | Merge another dictionary into this one |

### Iterating Over Dictionaries

```python
for key in student:
    print(key, student[key])

for key, value in student.items():
    print(f"{key}: {value}")
```

## Practical Examples

```python
# Product catalog
product = {
    "name": "Laptop",
    "brand": "HP",
    "price": 450000,
    "in_stock": True
}

print(f"{product['name']} by {product['brand']}: {product['price']:,} Naira")
```

```python
# Counting occurrences
text = "banana"
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1
print(char_count)  # {'b': 1, 'a': 3, 'n': 2}
```

```python
# Nested dictionaries
school = {
    "CSC301": {
        "title": "Data Structures",
        "lecturer": "Dr. Aminu",
        "credits": 3
    },
    "CSC305": {
        "title": "Operating Systems",
        "lecturer": "Dr. Fatima",
        "credits": 3
    }
}

print(school["CSC301"]["title"])      # Data Structures
print(school["CSC305"]["lecturer"])   # Dr. Fatima
```

```python
# Merging dictionaries
defaults = {"theme": "light", "language": "en", "font_size": 14}
user_prefs = {"theme": "dark", "font_size": 16}

settings = {**defaults, **user_prefs}
print(settings)  # {'theme': 'dark', 'language': 'en', 'font_size': 16}
```

## Guided Practice

Create a file called `word_counter.py`:

1. Ask the user to enter a sentence.
2. Split it into words.
3. Count how many times each word appears using a dictionary.
4. Print the results sorted by frequency (most common first).

```python
sentence = input("Enter a sentence: ").lower()
words = sentence.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

sorted_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True)

print("\nWord Frequencies:")
for word, count in sorted_words:
    print(f"  {word:<15} {count}")
```

## Daily Challenge

Build a program called `phone_book.py` that implements a contact manager:

1. Store contacts in a dictionary where the key is the contact name and the value is another dictionary containing phone number and email.

2. Provide a menu:
   - 1: Add a contact
   - 2: Search for a contact by name
   - 3: Update a contact's phone or email
   - 4: Delete a contact
   - 5: List all contacts
   - 6: Exit

3. Search should be case-insensitive (store names in title case).

4. Display contacts in a formatted table:

```
===== CONTACTS =====
Name              Phone           Email
------------------------------------------------------
Amina Bello       08012345678     amina@email.com
Yusuf Ibrahim     07098765432     yusuf@email.com
------------------------------------------------------
Total: 2 contacts
```

5. Handle edge cases: duplicate names, searching for non-existent contacts, empty phone book.

## Expected Output

A fully interactive phone book application that persists contacts during the session, supports CRUD operations, and displays contacts in a formatted table.

## Assessment

1. What is the difference between `dict["key"]` and `dict.get("key")`?
2. Can a dictionary have two entries with the same key? What happens if you assign to an existing key?
3. How would you check if a key exists in a dictionary?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-02/day-013/`

Your submission should include:
- `phone_book.py` containing your solution to the daily challenge.

## Additional Resources

- [Python Official Docs — Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [Python Official Docs — Mapping Types](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)

## Reflection

- How is a dictionary different from a list in how it organizes data?
- Think of a real-world dataset that would be best represented as a dictionary. Why?
