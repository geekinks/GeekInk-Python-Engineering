# Python Basics Cheat Sheet

## Variables and Types

```python
name = "Amina"          # str
age = 22                # int
gpa = 3.75              # float
is_enrolled = True      # bool
```

## Type Conversion

```python
int("42")       # 42
float("3.14")   # 3.14
str(100)        # "100"
bool(0)         # False
bool(1)         # True
```

## String Operations

```python
text = "Hello, World"
text.upper()            # "HELLO, WORLD"
text.lower()            # "hello, world"
text.strip()            # Remove whitespace
text.replace("H", "J") # "Jello, World"
text.split(", ")        # ["Hello", "World"]
len(text)               # 12
f"Name: {name}"         # f-string formatting
```

## Lists

```python
fruits = ["mango", "banana", "orange"]
fruits.append("guava")
fruits.insert(0, "apple")
fruits.remove("banana")
fruits.pop()            # Remove and return last
fruits.sort()
len(fruits)
fruits[0]               # First item
fruits[-1]              # Last item
fruits[1:3]             # Slice
```

## Dictionaries

```python
student = {"name": "Musa", "age": 20, "grade": "A"}
student["name"]         # "Musa"
student.get("gpa", 0)   # 0 (default if missing)
student["gpa"] = 3.5    # Add/update
student.keys()
student.values()
student.items()
del student["age"]
```

## Conditionals

```python
if score >= 70:
    grade = "A"
elif score >= 60:
    grade = "B"
elif score >= 50:
    grade = "C"
else:
    grade = "F"
```

## Loops

```python
# For loop
for item in fruits:
    print(item)

for i in range(5):      # 0, 1, 2, 3, 4
    print(i)

for i, item in enumerate(fruits):
    print(i, item)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1
```

## Functions

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

result = greet("Fatima")
result = greet("Fatima", greeting="Salam")
```

## File Operations

```python
# Reading
with open("data.txt", "r") as f:
    content = f.read()

# Writing
with open("output.txt", "w") as f:
    f.write("Hello\n")

# Appending
with open("log.txt", "a") as f:
    f.write("New entry\n")
```

## List Comprehensions

```python
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
```

## Exception Handling

```python
try:
    result = int(input("Enter a number: "))
except ValueError:
    print("That is not a valid number")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Done")
```

## Common Built-in Functions

```python
len(items)          # Length
type(variable)      # Type
range(start, stop, step)
print(*args, sep=" ", end="\n")
input("Prompt: ")
int(), float(), str(), bool()
min(), max(), sum()
sorted(items)
enumerate(items)
zip(list1, list2)
```
