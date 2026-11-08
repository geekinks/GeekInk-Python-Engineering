# Day 046: Web Scraping with Beautiful Soup

## Learning Objectives

- Understand what web scraping is and when it is appropriate to use.
- Parse HTML documents using Beautiful Soup.
- Navigate the DOM tree with `find()`, `find_all()`, and CSS selectors.
- Extract text, attributes, and links from web pages.
- Practice responsible scraping: respect `robots.txt`, rate limits, and terms of service.

## Introduction

Web scraping is the process of extracting data from web pages programmatically. While APIs provide structured data intentionally, scraping lets you collect information from pages that were designed for human readers. This is a powerful technique, but it comes with responsibilities.

Beautiful Soup is a Python library that makes it easy to parse HTML and XML documents. It turns the raw HTML of a web page into a navigable tree of Python objects, letting you search for elements by tag, class, ID, or CSS selector.

**Responsible scraping is non-negotiable.** Before scraping any website, you must check its `robots.txt` file (e.g., `https://example.com/robots.txt`), read its terms of service, and respect rate limits. Do not scrape sites that explicitly forbid it. Do not overwhelm servers with rapid requests. Do not scrape personal data without consent. Violating these principles can have legal consequences and is unethical.

## Concepts

### HTML Basics for Scraping

HTML is structured as nested tags:
```html
<div class="article">
  <h2>Title</h2>
  <p class="summary">Summary text here.</p>
  <a href="https://example.com/full">Read more</a>
</div>
```

Key terms:
- **Tag**: `<h2>`, `<p>`, `<a>`, `<div>`
- **Attribute**: `class="summary"`, `href="..."`
- **Text content**: the text between opening and closing tags.

### Beautiful Soup

Install with: `pip install beautifulsoup4`

Key methods:
- `BeautifulSoup(html, "html.parser")` -- parse an HTML string.
- `soup.find("tag")` -- find the first matching element.
- `soup.find_all("tag")` -- find all matching elements.
- `soup.select("css_selector")` -- find elements by CSS selector.
- `element.text` or `element.get_text()` -- extract text content.
- `element["attribute"]` or `element.get("attribute")` -- get an attribute value.

### Responsible Scraping Checklist

1. Check `robots.txt` before scraping.
2. Read the site's terms of service.
3. Add delays between requests (`time.sleep()`).
4. Identify your scraper with a descriptive `User-Agent` header.
5. Do not scrape personal or private information.
6. Cache responses to avoid repeated requests during development.
7. If an API exists, prefer it over scraping.

## Practical Examples

```python
from bs4 import BeautifulSoup

# Parse a simple HTML string
html = """
<html>
<body>
  <h1>Welcome to GeekInk</h1>
  <div class="courses">
    <div class="course">
      <h2>Python Engineering</h2>
      <p class="duration">100 Days</p>
      <a href="/python">Learn more</a>
    </div>
    <div class="course">
      <h2>Web Development</h2>
      <p class="duration">60 Days</p>
      <a href="/web">Learn more</a>
    </div>
  </div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

# Find the page title
title = soup.find("h1")
print(f"Page title: {title.text}")

# Find all courses
courses = soup.find_all("div", class_="course")
for course in courses:
    name = course.find("h2").text
    duration = course.find("p", class_="duration").text
    link = course.find("a")["href"]
    print(f"  {name} ({duration}) -> {link}")
```

```python
from bs4 import BeautifulSoup

# Using CSS selectors
html = """
<table id="results">
  <tr><th>Name</th><th>Score</th></tr>
  <tr><td>Amina</td><td>95</td></tr>
  <tr><td>Usman</td><td>88</td></tr>
  <tr><td>Fatima</td><td>92</td></tr>
</table>
"""

soup = BeautifulSoup(html, "html.parser")

# Select all data rows (skip the header)
rows = soup.select("#results tr")[1:]  # skip first row (header)
for row in rows:
    cells = row.find_all("td")
    name = cells[0].text
    score = int(cells[1].text)
    print(f"  {name}: {score}")
```

```python
import requests
from bs4 import BeautifulSoup
import time

# Fetching and parsing a real web page (example.com is safe to scrape)
response = requests.get("https://example.com", timeout=10)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

title = soup.find("title").text
heading = soup.find("h1").text
paragraphs = soup.find_all("p")

print(f"Title: {title}")
print(f"Heading: {heading}")
print(f"Paragraphs: {len(paragraphs)}")
for p in paragraphs:
    print(f"  {p.get_text(strip=True)[:80]}...")
```

## Guided Practice

Build a script that parses a sample HTML page and extracts a list of books with their details.

```python
from bs4 import BeautifulSoup

# Simulated bookstore page
html = """
<html>
<body>
<div class="book-list">
  <div class="book" data-isbn="978-0-13-468599-1">
    <h3 class="title">The Pragmatic Programmer</h3>
    <span class="author">David Thomas, Andrew Hunt</span>
    <span class="price">$49.99</span>
    <span class="rating" data-stars="5">Excellent</span>
  </div>
  <div class="book" data-isbn="978-0-596-51774-8">
    <h3 class="title">JavaScript: The Good Parts</h3>
    <span class="author">Douglas Crockford</span>
    <span class="price">$29.99</span>
    <span class="rating" data-stars="4">Very Good</span>
  </div>
  <div class="book" data-isbn="978-1-491-95038-8">
    <h3 class="title">Fluent Python</h3>
    <span class="author">Luciano Ramalho</span>
    <span class="price">$59.99</span>
    <span class="rating" data-stars="5">Excellent</span>
  </div>
</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

books = []
for book_div in soup.find_all("div", class_="book"):
    book = {
        "isbn": book_div.get("data-isbn"),
        "title": book_div.find("h3", class_="title").text,
        "author": book_div.find("span", class_="author").text,
        "price": book_div.find("span", class_="price").text,
        "rating": int(book_div.find("span", class_="rating")["data-stars"]),
    }
    books.append(book)

print(f"{'Title':<35} {'Author':<25} {'Price':>8} {'Stars':>5}")
print("-" * 78)
for book in books:
    print(f"{book['title']:<35} {book['author']:<25} {book['price']:>8} {'*' * book['rating']:>5}")
```

## Daily Challenge

**Build a News Headline Scraper**

Write a script called `headline_scraper.py` that extracts headlines from a web page. To avoid scraping sites that disallow it, **work with a local HTML file** that simulates a news page.

Step 1: Create a file called `sample_news.html`:

```html
<!DOCTYPE html>
<html>
<head><title>GeekInk Daily News</title></head>
<body>
<div class="news-container">
  <article class="story">
    <h2><a href="/tech/python-4">Python 4.0 Announced with Revolutionary Features</a></h2>
    <span class="category">Technology</span>
    <span class="date">2025-03-15</span>
    <p class="summary">The Python Software Foundation has announced major changes coming in the next release.</p>
  </article>
  <article class="story">
    <h2><a href="/education/coding-schools">Northern Nigeria Coding Schools See 200% Growth</a></h2>
    <span class="category">Education</span>
    <span class="date">2025-03-14</span>
    <p class="summary">Tech hubs across Kano, Kaduna, and Sokoto report unprecedented enrollment numbers.</p>
  </article>
  <article class="story">
    <h2><a href="/business/fintech-boom">Nigerian Fintech Startups Attract Record Investment</a></h2>
    <span class="category">Business</span>
    <span class="date">2025-03-13</span>
    <p class="summary">Venture capital firms invested over $500M in Nigerian fintech companies this quarter.</p>
  </article>
  <article class="story">
    <h2><a href="/tech/open-source">Open Source Contributions from Africa Double in 2025</a></h2>
    <span class="category">Technology</span>
    <span class="date">2025-03-12</span>
    <p class="summary">African developers now make up 8% of global open source contributions.</p>
  </article>
</div>
</body>
</html>
```

Step 2: Your script should:

1. Read and parse the HTML file.
2. Extract each article's title, link, category, date, and summary.
3. Display them in a formatted table.
4. Filter articles by category if the user provides one.
5. Save the extracted data to a CSV file.

Requirements:
- Use Beautiful Soup for parsing.
- Write a reusable function for extraction.
- Save output to CSV using the `csv` module.

## Expected Output

```
=== GeekInk Daily News Headlines ===

All Articles:
  1. [Technology] Python 4.0 Announced with Revolutionary Features (2025-03-15)
     Python Software Foundation has announced major changes...
  2. [Education] Northern Nigeria Coding Schools See 200% Growth (2025-03-14)
     Tech hubs across Kano, Kaduna, and Sokoto report...
  3. [Business] Nigerian Fintech Startups Attract Record Investment (2025-03-13)
     Venture capital firms invested over $500M...
  4. [Technology] Open Source Contributions from Africa Double in 2025 (2025-03-12)
     African developers now make up 8%...

Saved 4 articles to headlines.csv
```

## Assessment

1. What is the difference between `soup.find()` and `soup.find_all()`?
2. Why is it important to check `robots.txt` before scraping a website?
3. How would you extract the value of the `href` attribute from an `<a>` tag using Beautiful Soup?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-05/day-046/`

Include `headline_scraper.py`, `sample_news.html`, and `headlines.csv`.

## Additional Resources

- [Beautiful Soup documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [robots.txt specification](https://www.robotstxt.org/)

## Reflection

- What ethical considerations should guide your decision to scrape a website?
- How would your scraping approach change if the target page loaded its content using JavaScript?
