# Week 10 Monday: Filesystem automation

## Learning objectives

- Explain Path and  glob.
- Apply today's ideas in a working implementation.
- Test normal and failure behaviour before sharing the result.

## Concepts students must understand

- Path
- glob
- rename
- idempotence

## Detailed lesson content

Automation should be safe to run twice. Preview changes, use explicit folders, and never delete or overwrite data without a recovery plan. pathlib keeps paths portable.

Plan input, processing, output, and failure behaviour before coding. Make a small working version first; add complexity only after observing correct output.

## Code example

~~~python
from pathlib import Path
for file in Path('inbox').glob('*.txt'):
    print(file.name)
~~~

## Practical coding activity

List target files without changing them.

## Guided exercise

Create a preview mode for a file organiser.

## Independent exercise

Organise files by extension in a test directory.

## Expected output

A dry run lists planned changes.

## Homework or assignment

Add a backup step before any rename.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Existing retained repository material where relevant

