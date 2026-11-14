# Week 04 Monday: Text files and pathlib

## Learning objectives

- Explain context manager and  file mode.
- Apply today's ideas in a small Python program.
- Inspect output and improve the program after a test run.

## Concepts students must understand

- context manager
- file mode
- Path
- encoding

## Detailed lesson content

Use a context manager so files close even if code fails. pathlib represents paths safely across operating systems; do not assume the current folder is a particular location.

Before coding, describe the input, processing, and output in ordinary language. Run the smallest possible version, then extend it one change at a time. Read the error message before asking for help.

## Code example

~~~python
from pathlib import Path
Path('notes.txt').write_text('Study Python\n', encoding='utf-8')
~~~

## Practical coding activity

Write and read a notes file.

## Guided exercise

Create a data directory only if it does not exist.

## Independent exercise

Save and load one student name from a text file.

## Expected output

A file is created and its content prints.

## Homework or assignment

Organise your project with src, data, and tests folders.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Relevant retained examples in the repository, where referenced above

