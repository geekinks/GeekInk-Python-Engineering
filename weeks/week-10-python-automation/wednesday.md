# Week 10 Wednesday: Command-line applications and APIs

## Learning objectives

- Explain argparse and  command.
- Apply today's ideas in a working implementation.
- Test normal and failure behaviour before sharing the result.

## Concepts students must understand

- argparse
- command
- API
- timeout

## Detailed lesson content

A command-line interface makes a script reusable. Parse arguments clearly and provide help text. API clients need timeouts, status checks, and respectful request rates.

Plan input, processing, output, and failure behaviour before coding. Make a small working version first; add complexity only after observing correct output.

## Code example

~~~python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--month', required=True)
print(parser.parse_args())
~~~

## Practical coding activity

Add a required report-date argument.

## Guided exercise

Make a GET request design that checks a response status.

## Independent exercise

Build a report command with --input and --output.

## Expected output

Help text explains the command.

## Homework or assignment

Document one offline sample-data mode.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Existing retained repository material where relevant

