# Week 04 Tuesday: JSON and CSV data

## Learning objectives

- Explain JSON and  serialisation.
- Apply today's ideas in a small Python program.
- Inspect output and improve the program after a test run.

## Concepts students must understand

- JSON
- serialisation
- DictReader
- headers

## Detailed lesson content

JSON preserves nested Python-like data; CSV is portable tabular data. Inspect a file's headers and types before calculating with it.

Before coding, describe the input, processing, and output in ordinary language. Run the smallest possible version, then extend it one change at a time. Read the error message before asking for help.

## Code example

~~~python
import json
record = {'name': 'Musa', 'score': 76}
print(json.dumps(record))
~~~

## Practical coding activity

Save and reload a list of two records as JSON.

## Guided exercise

Read a CSV header and print each row as a dictionary.

## Independent exercise

Create sample student_records.json and students.csv.

## Expected output

The same record can be loaded after the script exits.

## Homework or assignment

Compare JSON and CSV in two sentences.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Relevant retained examples in the repository, where referenced above

