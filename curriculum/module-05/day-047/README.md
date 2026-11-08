# Day 047: Advanced Web Scraping

## Learning Objectives

- Handle multi-page scraping with pagination.
- Submit forms and handle POST requests in scraping workflows.
- Recognize the limitations of static scraping when pages use dynamic (JavaScript) content.
- Save scraped data to CSV and JSON files.
- Build a price tracker that monitors product prices over time.

## Introduction

Yesterday you learned the fundamentals of parsing HTML with Beautiful Soup. Today you will tackle real-world scraping challenges: pages that split data across multiple pages, forms that require submission, and content that changes over time.

Pagination is everywhere on the web. Search results, product catalogs, and article archives all break their data into pages. To collect complete datasets, your scraper needs to follow "next page" links or increment page numbers until all data has been collected.

You will also learn to save scraped data persistently. A scraper that only prints results to the terminal is useful once; a scraper that writes to CSV or JSON files creates datasets you can analyze, compare, and build upon.

## Concepts

### Handling Pagination

Common pagination patterns:

1. **Numbered pages**: URLs like `/products?page=1`, `/products?page=2`.
2. **Next-page links**: the HTML contains a link to the next page.
3. **Load-more buttons**: the page fetches additional data via JavaScript (requires different tools).

Strategy: loop through pages until you find no more data or no "next" link.

### Submitting Forms

Some data requires submitting a form first. Use `requests.post()` with form data:

```python
response = requests.post(url, data={"field": "value"})
```

For session-based sites (login required), use `requests.Session()` to persist cookies.

### Saving Data

- **CSV**: tabular data with rows and columns. Use `csv.DictWriter`.
- **JSON**: nested or hierarchical data. Use `json.dump()`.

### Rate Limiting Your Scraper

Always add delays between requests:

```python
import time
time.sleep(1)  # Wait 1 second between requests
```

## Practical Examples

```python
import requests
from bs4 import BeautifulSoup
import time

# Scraping multiple pages (using books.toscrape.com -- a site built for scraping practice)
def scrape_books(max_pages=3):
    """Scrape book titles and prices from multiple pages."""
    books = []
    
    for page in range(1, max_pages + 1):
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"
        
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            print(f"  Page {page}: not found, stopping.")
            break
        
        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.find_all("article", class_="product_pod")
        
        for article in articles:
            title = article.find("h3").find("a")["title"]
            price = article.find("p", class_="price_color").text
            books.append({"title": title, "price": price})
        
        print(f"  Page {page}: found {len(articles)} books")
        time.sleep(1)  # Respectful delay
    
    return books


all_books = scrape_books(3)
print(f"\nTotal books collected: {len(all_books)}")
for book in all_books[:5]:
    print(f"  {book['title'][:50]:<50} {book['price']}")
```

```python
import csv
import json

# Saving scraped data to CSV
def save_to_csv(data, filename):
    if not data:
        return
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print(f"Saved {len(data)} records to {filename}")


# Saving scraped data to JSON
def save_to_json(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(data)} records to {filename}")


# Example usage with sample data
sample_data = [
    {"title": "Python Crash Course", "price": "$25.99"},
    {"title": "Automate the Boring Stuff", "price": "$19.99"},
]

save_to_csv(sample_data, "books.csv")
save_to_json(sample_data, "books.json")
```

```python
import requests

# Using sessions for sites that require login or maintain state
session = requests.Session()

# Set a custom user agent to identify your scraper
session.headers.update({
    "User-Agent": "GeekInk-Scraper/1.0 (educational project)"
})

# All requests through this session share cookies and headers
response = session.get("https://httpbin.org/cookies/set/session_id/abc123", timeout=10)
response = session.get("https://httpbin.org/cookies", timeout=10)
print("Cookies maintained:", response.json())
```

## Guided Practice

Build a script that scrapes books from `books.toscrape.com`, handles pagination, and saves results.

```python
import requests
from bs4 import BeautifulSoup
import csv
import time


def scrape_all_books(max_pages=5):
    """Scrape books with pagination, saving to CSV."""
    base_url = "https://books.toscrape.com/catalogue/page-{}.html"
    all_books = []
    
    for page_num in range(1, max_pages + 1):
        url = base_url.format(page_num)
        
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 404:
                print(f"No more pages after page {page_num - 1}.")
                break
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching page {page_num}: {e}")
            break
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        for article in soup.find_all("article", class_="product_pod"):
            title = article.find("h3").find("a")["title"]
            price_text = article.find("p", class_="price_color").text
            price = float(price_text.replace("£", "").replace("Â", ""))
            
            rating_tag = article.find("p", class_="star-rating")
            rating_class = rating_tag["class"][1] if rating_tag else "Zero"
            rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
            rating = rating_map.get(rating_class, 0)
            
            all_books.append({
                "title": title,
                "price": price,
                "rating": rating,
                "page": page_num,
            })
        
        print(f"  Scraped page {page_num}")
        time.sleep(1)
    
    # Save to CSV
    if all_books:
        with open("books_catalog.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["title", "price", "rating", "page"])
            writer.writeheader()
            writer.writerows(all_books)
    
    return all_books


books = scrape_all_books(3)
print(f"\nCollected {len(books)} books")
print(f"Average price: £{sum(b['price'] for b in books) / len(books):.2f}")
print(f"5-star books: {sum(1 for b in books if b['rating'] == 5)}")
```

## Daily Challenge

**Build a Price Tracker**

Write a script called `price_tracker.py` that monitors product prices over time using `books.toscrape.com` as the data source.

Your script should:

1. Scrape the first page of books and record the title and price.
2. Save results to a JSON file (`price_history.json`) with a timestamp.
3. On subsequent runs, load the previous data, scrape again, and compare prices.
4. Report any price changes (increases, decreases, new products, removed products).
5. Maintain a history of all price snapshots.

Requirements:
- Use Beautiful Soup for parsing.
- Use `json` for persistent storage.
- Include timestamps using `datetime`.
- Print a clear comparison report.
- Add a 1-second delay between requests.

Data structure for `price_history.json`:

```json
{
  "snapshots": [
    {
      "timestamp": "2025-03-15T10:30:00",
      "products": [
        {"title": "A Light in the Attic", "price": 51.77},
        {"title": "Tipping the Velvet", "price": 53.74}
      ]
    }
  ]
}
```

## Expected Output

```
=== Price Tracker ===

Scraping current prices...
  Found 20 products on page 1.

Comparing with previous snapshot (2025-03-15 10:30):
  No price changes detected.
  All 20 products still available.

Snapshot saved to price_history.json
Total snapshots: 2
```

## Assessment

1. How do you handle pagination when scraping a website? What signals indicate there are no more pages?
2. Why is it important to add delays between scraping requests?
3. What is the difference between saving scraped data as CSV versus JSON? When would you choose each format?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-05/day-047/`

Include `price_tracker.py`, `price_history.json` (a sample output), and a `README.md`.

## Additional Resources

- [books.toscrape.com](https://books.toscrape.com/) -- a website built specifically for scraping practice
- [csv module documentation](https://docs.python.org/3/library/csv.html)

## Reflection

- How would your scraper need to change if a website redesigned its HTML structure?
- What are the ethical boundaries between collecting publicly available data and violating user privacy?
