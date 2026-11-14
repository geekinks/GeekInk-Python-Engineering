# Week 10 Thursday: Responsible scraping and scheduling

## Learning objectives

- Explain robots.txt and  HTML.
- Apply today's ideas in a working implementation.
- Test normal and failure behaviour before sharing the result.

## Concepts students must understand

- robots.txt
- HTML
- BeautifulSoup
- scheduler

## Detailed lesson content

Scrape only public pages when terms and robots guidance permit, at a gentle rate, and prefer an official API. Parse saved HTML first. Scheduling should run a tested, idempotent command.

Plan input, processing, output, and failure behaviour before coding. Make a small working version first; add complexity only after observing correct output.

## Code example

~~~python
from bs4 import BeautifulSoup
html = '<h1>Notice</h1>'
print(BeautifulSoup(html, 'html.parser').h1.text)
~~~

## Practical coding activity

Parse a local HTML sample.

## Guided exercise

Write a checklist before any network scraping.

## Independent exercise

Build the attendance/report automation feature and a schedule plan.

## Expected output

A report is generated from local sample input.

## Homework or assignment

Add error handling for missing and malformed files.

## Recommended learning resources

- [Official Python documentation](https://docs.python.org/3/)
- [Week resources](resources.md)
- Existing retained repository material where relevant

