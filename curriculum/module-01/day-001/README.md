# Day 001: Welcome to Python

## Learning Objectives

- Understand what Python is and why it is widely used in software engineering.
- Install Python on your computer and verify the installation.
- Write and run your first Python program.
- Understand the basic structure of a Python script.
- Use the `print()` function to display output.

## Introduction

Python is one of the most popular programming languages in the world. It is used in web development, data science, automation, artificial intelligence, and many other fields. Companies like Google, Netflix, and Instagram use Python in their technology stacks. Its clear syntax and readability make it an excellent first language for beginners.

Learning Python is not just about learning a programming language. It is about developing the ability to think logically, break problems into smaller parts, and build solutions that work. Throughout this 100-day bootcamp, you will go from writing your first line of code to building complete software applications.

In this first lesson, you will set up your development environment, understand how Python executes code, and write your very first program.

## Concepts

### What is Python?

Python is a high-level, interpreted programming language created by Guido van Rossum and first released in 1991. "High-level" means it is designed to be easy for humans to read and write. "Interpreted" means Python executes your code line by line, rather than compiling everything before running.

### Why Learn Python?

- **Readable syntax**: Python code reads almost like English.
- **Versatile**: Used for web apps, data analysis, automation, AI, and more.
- **Large community**: Millions of developers worldwide contribute libraries and help each other.
- **In demand**: Python developers are sought after across industries.

### How Python Runs Code

When you write a Python script (a `.py` file), the Python interpreter reads it from top to bottom, executing each instruction in order.

```
You write code -> Python interpreter reads it -> Computer executes it -> You see the result
```

### The `print()` Function

`print()` is a built-in function that displays text or values on the screen. It is the simplest way to see output from your program.

## Practical Examples

```python
# Your very first Python program
print("Hello, World!")
```

```python
# Printing multiple lines
print("Welcome to GeekInk Python Engineering")
print("100 Days. 100 Challenges. Real Engineering.")
print("Let us begin!")
```

```python
# Printing numbers
print(42)
print(3.14)
```

```python
# Printing multiple values in one line
print("My name is", "Amina", "and I am", 20, "years old")
```

```python
# Using the sep and end parameters
print("Python", "is", "powerful", sep="-")
print("Line one", end=" ")
print("continues here")
```

## Guided Practice

Follow these steps to write and run your first program:

1. Open your text editor or IDE (VS Code is recommended).
2. Create a new file called `hello.py`.
3. Type the following code:

```python
print("Hello, World!")
print("My name is [Your Name]")
print("I am learning Python at GeekInk Innovations")
print("This is Day 1 of 100")
```

4. Save the file.
5. Open your terminal or command prompt.
6. Navigate to the folder where you saved the file.
7. Run the program:

```bash
python hello.py
```

8. You should see your messages printed on the screen.

Now try modifying the messages and running the program again. Experiment with what you can print.

## Daily Challenge

Write a Python program called `about_me.py` that prints the following information about yourself:

- Your full name
- Your age
- Your city or state
- One fun fact about yourself
- Why you want to learn Python

Each piece of information should be on its own line. Use descriptive labels, for example:

```
Name: Aisha Bello
Age: 22
Location: Kano, Nigeria
Fun fact: I can solve a Rubik's cube in under two minutes
Goal: I want to build software that helps students learn better
```

## Expected Output

Your program should produce clean, readable output with five lines, each containing a label and a value. The exact content will vary based on your personal information.

## Assessment

1. What does the `print()` function do in Python?
2. What file extension do Python scripts use?
3. If you write `print("Hello" "World")`, what will Python display? Why?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-01/day-001/`

Your submission should include:
- `about_me.py` containing your solution to the daily challenge.

## Additional Resources

- [Python Official Tutorial — Getting Started](https://docs.python.org/3/tutorial/index.html)
- [Installing Python](https://www.python.org/downloads/)

## Reflection

- What surprised you about how Python works compared to what you expected?
- Describe in your own words what happens when you run a Python script.
