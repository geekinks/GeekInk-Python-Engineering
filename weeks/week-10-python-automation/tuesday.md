# Week 10 Tuesday: CSV and Excel processing

## Learning objectives

- Explain csv and  rows.
- Apply today's ideas in a working implementation.
- Test normal and failure behaviour before sharing the result.

## Concepts students must understand

- csv
- rows
- columns
- spreadsheet
- summary

## Detailed lesson content

CSV is lightweight and built into Python. Excel files need an added library, so teach the data flow with CSV first: load, validate, transform, and report.

Plan input, processing, output, and failure behaviour before coding. Make a small working version first; add complexity only after observing correct output.

## Code example

~~~python
import csv
with open('attendance.csv', newline='') as f:
    rows = list(csv.DictReader(f))
print(len(rows))
~~~

## Practical coding activity

Count attendance records from CSV.

## Guided exercise

Calculate attendance percentage with missing-value handling.

## Independent exercise

Produce an attendance summary CSV.

## Expected output

A report shows totals and percentages.

## Homework or assignment

Install an Excel library only if the cohort needs it.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Existing retained repository material where relevant

