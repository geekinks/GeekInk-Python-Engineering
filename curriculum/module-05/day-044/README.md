# Day 044: HTTP Requests

## Learning Objectives

- Understand how HTTP works: requests, responses, methods, and status codes.
- Install and use the `requests` library to make GET and POST requests.
- Handle response data, headers, and errors properly.
- Work with query parameters and custom headers.
- Build a script that fetches weather data from a public API.

## Introduction

Almost every modern application communicates over the internet using HTTP (Hypertext Transfer Protocol). When your browser loads a web page, it sends an HTTP request to a server and receives an HTTP response. As a Python engineer, you can make these same requests programmatically to fetch data, interact with web services, and integrate external data sources into your applications.

The `requests` library is Python's most popular tool for making HTTP requests. It provides a simple, intuitive interface that handles the complexity of HTTP for you: managing connections, encoding parameters, parsing responses, and handling redirects.

Understanding HTTP is foundational for everything in Modules 5 and 6. Web scraping, API integration, and backend development all depend on your ability to send and receive HTTP requests correctly.

## Concepts

### HTTP Methods

- **GET** -- retrieve data from a server. The most common method.
- **POST** -- send data to a server (e.g., submitting a form, creating a record).
- **PUT** -- update an existing resource on the server.
- **DELETE** -- remove a resource from the server.

### HTTP Status Codes

| Code | Meaning                 |
|------|-------------------------|
| 200  | OK -- request succeeded |
| 201  | Created -- resource created |
| 301  | Moved Permanently -- resource has a new URL |
| 400  | Bad Request -- something wrong with your request |
| 401  | Unauthorized -- authentication required |
| 403  | Forbidden -- you do not have access |
| 404  | Not Found -- resource does not exist |
| 500  | Internal Server Error -- something broke on the server |

### The `requests` Library

Install it with: `pip install requests`

Key features:
- `requests.get(url)` -- make a GET request.
- `requests.post(url, data=..., json=...)` -- make a POST request.
- `response.status_code` -- the HTTP status code.
- `response.text` -- response body as text.
- `response.json()` -- parse JSON response into a Python dictionary.
- `response.headers` -- response headers as a dictionary.
- `response.raise_for_status()` -- raise an exception if the request failed.

## Practical Examples

```python
import requests

# Simple GET request
response = requests.get("https://httpbin.org/get")
print(f"Status code: {response.status_code}")
print(f"Content type: {response.headers['Content-Type']}")
print(f"Response body (first 200 chars): {response.text[:200]}")
```

```python
import requests

# GET with query parameters
params = {"q": "python programming", "limit": 5}
response = requests.get("https://httpbin.org/get", params=params)

# The library builds the URL for you
print(f"Requested URL: {response.url}")
print(f"Response JSON: {response.json()}")
```

```python
import requests

# POST request with JSON data
data = {
    "name": "Amina",
    "course": "Python Engineering",
    "module": 5
}
response = requests.post("https://httpbin.org/post", json=data)
print(f"Status: {response.status_code}")
print(f"Server received: {response.json()['json']}")
```

```python
import requests

# Proper error handling
def fetch_url(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response
    except requests.exceptions.Timeout:
        print(f"Error: Request to {url} timed out.")
    except requests.exceptions.HTTPError as e:
        print(f"Error: HTTP {e.response.status_code} for {url}")
    except requests.exceptions.ConnectionError:
        print(f"Error: Could not connect to {url}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    return None

# Test with a valid and an invalid URL
result = fetch_url("https://httpbin.org/get")
if result:
    print(f"Success: received {len(result.text)} characters")

fetch_url("https://httpbin.org/status/404")
```

## Guided Practice

Build a simple script that fetches and displays a random fact from a public API.

```python
import requests


def get_random_fact():
    """Fetch a random fact from a public API."""
    url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        fact = data.get("text", "No fact available.")
        source = data.get("source", "Unknown")
        
        print("Random Fact:")
        print(f"  {fact}")
        print(f"  Source: {source}")
        
    except requests.exceptions.RequestException as e:
        print(f"Could not fetch fact: {e}")


def check_website_status(urls):
    """Check whether a list of websites are reachable."""
    print("\nWebsite Status Check:")
    print("-" * 50)
    for url in urls:
        try:
            response = requests.get(url, timeout=5)
            print(f"  {url:<35} -> {response.status_code} OK")
        except requests.exceptions.RequestException:
            print(f"  {url:<35} -> UNREACHABLE")


get_random_fact()

check_website_status([
    "https://www.python.org",
    "https://httpbin.org",
    "https://example.com",
])
```

## Daily Challenge

**Build a Weather Information Fetcher**

Write a script called `weather_fetcher.py` that:

1. Prompts the user for a city name.
2. Fetches current weather data from a free API. Use the [wttr.in](https://wttr.in) service, which requires no API key: `https://wttr.in/{city}?format=j1`
3. Parses the JSON response to extract: temperature, weather description, humidity, wind speed.
4. Displays the weather information in a clean, readable format.
5. Allows the user to check multiple cities in a loop until they type "quit".
6. Handles errors gracefully (invalid city, network issues, timeouts).

Requirements:
- Use `requests.get()` with a timeout.
- Use `response.json()` to parse the response.
- Handle all common error cases.
- Display data in a clean, aligned format.

## Expected Output

```
=== Weather Information Fetcher ===

Enter a city name (or 'quit' to exit): Kano

Weather for Kano:
  Temperature:  32 C
  Feels like:   35 C
  Description:  Partly cloudy
  Humidity:     45%
  Wind speed:   12 km/h

Enter a city name (or 'quit' to exit): London

Weather for London:
  Temperature:  14 C
  Feels like:   12 C
  Description:  Light rain
  Humidity:     78%
  Wind speed:   22 km/h

Enter a city name (or 'quit' to exit): quit
Goodbye!
```

## Assessment

1. What is the difference between `response.text` and `response.json()`?
2. Why should you always set a `timeout` parameter when making HTTP requests?
3. What does `response.raise_for_status()` do, and when should you use it?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-05/day-044/`

Include `weather_fetcher.py` and a `README.md`.

## Additional Resources

- [requests library documentation](https://docs.python-requests.org/en/latest/)
- [HTTP status codes reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

## Reflection

- How does making HTTP requests programmatically differ from using a browser?
- What security considerations should you keep in mind when making requests to external servers?
