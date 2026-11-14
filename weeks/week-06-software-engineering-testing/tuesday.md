# Week 06 Tuesday: Debugging, logging, and documentation

## Learning objectives

- Explain breakpoint and  traceback.
- Apply today's ideas in a small Python program.
- Inspect output and improve the program after a test run.

## Concepts students must understand

- breakpoint
- traceback
- logger
- README

## Detailed lesson content

Reproduce a bug before changing code. Logging records useful context for maintainers; do not log secrets. Documentation should tell a new person how to install, run, test, and contribute.

Before coding, describe the input, processing, and output in ordinary language. Run the smallest possible version, then extend it one change at a time. Read the error message before asking for help.

## Code example

~~~python
import logging
logging.basicConfig(level=logging.INFO)
logging.info('Loading records')
~~~

## Practical coding activity

Read a traceback and identify file, line, and exception.

## Guided exercise

Replace one temporary print with a useful log line.

## Independent exercise

Write a README for an earlier project.

## Expected output

A log message appears during a normal run.

## Homework or assignment

Record one bug report with reproduction steps.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Relevant retained examples in the repository, where referenced above

