# Day 045: Working with APIs

## Learning Objectives

- Understand what a REST API is and how it structures data exchange.
- Work with JSON response data, nested structures, and lists.
- Use API keys and authentication headers safely.
- Handle pagination to retrieve large datasets from APIs.
- Build a currency converter using a free exchange-rate API.

## Introduction

An API (Application Programming Interface) is a defined way for programs to communicate with each other. A REST API uses HTTP methods (GET, POST, PUT, DELETE) to let you read and write data on a remote server. When you fetch weather data, convert currencies, or retrieve social media posts, you are using REST APIs.

Yesterday you learned to make HTTP requests. Today you will focus on the patterns that make API interaction reliable and professional: reading documentation, authenticating, navigating paginated results, and handling rate limits. These skills are essential for building applications that depend on external data.

Most APIs return data as JSON -- the same format you learned to work with in Module 3. Your job as an engineer is to send the right request, parse the response, extract what you need, and handle any errors along the way.

## Concepts

### REST API Principles

- **Resources** are identified by URLs (e.g., `/api/users/42` refers to user 42).
- **HTTP methods** map to actions: GET (read), POST (create), PUT (update), DELETE (remove).
- **Responses** include a status code and a body, typically JSON.

### API Authentication

Many APIs require you to identify yourself. Common methods:

- **API key in query parameter**: `?api_key=YOUR_KEY`
- **API key in header**: `headers={"Authorization": "Bearer YOUR_KEY"}`
- **No auth**: public APIs that allow anonymous access.

Never hard-code API keys in your source code. Use environment variables or a `.env` file (which should be in `.gitignore`).

### Pagination

When an API has too many results to return at once, it breaks them into pages:

- **Page-based**: `?page=2&per_page=20`
- **Offset-based**: `?offset=20&limit=20`
- **Cursor-based**: the response includes a `next` URL or cursor token.

### Rate Limiting

APIs limit how many requests you can make per minute or hour. Respect these limits to avoid being blocked. Check response headers like `X-RateLimit-Remaining`.

## Practical Examples

```python
import requests

# Fetching data from a public API (no auth required)
response = requests.get("https://api.github.com/users/octocat", timeout=10)
response.raise_for_status()

user = response.json()
print(f"Username: {user['login']}")
print(f"Name: {user['name']}")
print(f"Public repos: {user['public_repos']}")
print(f"Followers: {user['followers']}")
```

```python
import requests
import os

# Using an API key from an environment variable
api_key = os.environ.get("API_KEY", "demo_key")

headers = {"Authorization": f"Bearer {api_key}"}
response = requests.get(
    "https://httpbin.org/bearer",
    headers=headers,
    timeout=10
)
print(f"Status: {response.status_code}")
```

```python
import requests

# Handling pagination -- fetch multiple pages of results
def fetch_all_repos(username, max_pages=3):
    """Fetch repositories for a GitHub user, handling pagination."""
    all_repos = []
    
    for page in range(1, max_pages + 1):
        response = requests.get(
            f"https://api.github.com/users/{username}/repos",
            params={"page": page, "per_page": 10},
            timeout=10
        )
        response.raise_for_status()
        
        repos = response.json()
        if not repos:
            break  # No more pages
        
        all_repos.extend(repos)
        print(f"  Page {page}: fetched {len(repos)} repos")
    
    return all_repos


repos = fetch_all_repos("octocat")
print(f"\nTotal repos fetched: {len(repos)}")
for repo in repos[:5]:
    print(f"  - {repo['name']}: {repo.get('description', 'No description')}")
```

```python
import requests
import json

# Working with nested JSON
response = requests.get("https://api.github.com/repos/python/cpython", timeout=10)
response.raise_for_status()

repo = response.json()

# Navigate the nested structure
print(f"Repository: {repo['full_name']}")
print(f"Stars: {repo['stargazers_count']:,}")
print(f"Language: {repo['language']}")
print(f"Owner type: {repo['owner']['type']}")
print(f"License: {repo['license']['name']}")
```

## Guided Practice

Write a script that fetches country information from the REST Countries API.

```python
import requests


def get_country_info(country_name):
    """Fetch and display information about a country."""
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        print(f"  Country '{country_name}' not found.")
        return
    except requests.exceptions.RequestException as e:
        print(f"  Error: {e}")
        return
    
    countries = response.json()
    country = countries[0]  # Take the first match
    
    name = country["name"]["common"]
    capital = country.get("capital", ["Unknown"])[0]
    population = country.get("population", 0)
    region = country.get("region", "Unknown")
    languages = country.get("languages", {})
    currencies = country.get("currencies", {})
    
    print(f"\n  Country: {name}")
    print(f"  Capital: {capital}")
    print(f"  Population: {population:,}")
    print(f"  Region: {region}")
    print(f"  Languages: {', '.join(languages.values())}")
    
    for code, info in currencies.items():
        print(f"  Currency: {info['name']} ({info.get('symbol', code)})")


print("=== Country Information Lookup ===")
for name in ["Nigeria", "Ghana", "Japan"]:
    get_country_info(name)
```

## Daily Challenge

**Build a Currency Converter**

Write a script called `currency_converter.py` that:

1. Uses a free exchange rate API. Recommended: `https://open.er-api.com/v6/latest/{base_currency}` (no API key required).
2. Prompts the user for: source currency code (e.g., USD), target currency code (e.g., NGN), and amount.
3. Fetches the current exchange rate.
4. Calculates and displays the converted amount.
5. Allows the user to perform multiple conversions in a loop.
6. Caches the exchange rates for a base currency so repeated lookups do not require extra API calls.
7. Lists available currencies if the user types "list".

Requirements:
- Validate that currency codes exist in the API response.
- Format monetary values to 2 decimal places.
- Handle network errors and invalid inputs gracefully.

## Expected Output

```
=== Currency Converter ===

Commands: enter currency codes to convert, 'list' for available currencies, 'quit' to exit.

From currency: USD
To currency: NGN
Amount: 100

100.00 USD = 160,250.00 NGN
Rate: 1 USD = 1,602.50 NGN

From currency: GBP
To currency: EUR
Amount: 50

50.00 GBP = 58.75 EUR
Rate: 1 GBP = 1.18 EUR

From currency: quit
Goodbye!
```

## Assessment

1. Why should API keys never be committed to a Git repository? How should you manage them instead?
2. What is pagination, and why do APIs use it instead of returning all results at once?
3. What is the purpose of the `timeout` parameter in `requests.get()`?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-05/day-045/`

Include `currency_converter.py` and a `README.md`.

## Additional Resources

- [GitHub REST API documentation](https://docs.github.com/en/rest)
- [REST Countries API](https://restcountries.com/)
- [Open Exchange Rates API](https://open.er-api.com/)

## Reflection

- What happens to your application if the API you depend on goes offline or changes its response format?
- How would you design your code to make it easy to switch from one API provider to another?
