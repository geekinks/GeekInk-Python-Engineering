# Week 04 Thursday: Build a persistent records feature

## Learning objectives

- Explain read-modify-write and  validation.
- Apply today's ideas in a small Python program.
- Inspect output and improve the program after a test run.

## Concepts students must understand

- read-modify-write
- validation
- report

## Detailed lesson content

A file-backed feature must load safely, update in memory, then save deliberately. Keep conversion and validation near the boundary where data enters the programme.

Before coding, describe the input, processing, and output in ordinary language. Run the smallest possible version, then extend it one change at a time. Read the error message before asking for help.

## Code example

~~~python
import csv
with open('students.csv', newline='', encoding='utf-8') as file:
    for row in csv.DictReader(file):
        print(row['name'])
~~~

## Practical coding activity

Load records and calculate an average.

## Guided exercise

Implement add, search, and report choices using JSON or CSV.

## Independent exercise

Build the week's student records feature.

## Expected output

A record remains available after rerunning the script.

## Homework or assignment

Add a sample data file and usage instructions.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Relevant retained examples in the repository, where referenced above

