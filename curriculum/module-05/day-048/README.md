# Day 048: Introduction to Selenium

## Learning Objectives

- Understand why browser automation is necessary when static scraping is not enough.
- Install and configure Selenium with a WebDriver.
- Navigate web pages, find elements, click buttons, and fill forms programmatically.
- Wait for dynamic content to load before interacting with it.
- Automate a form submission on a practice website.

## Introduction

Beautiful Soup works well for pages whose content is embedded in the initial HTML. But many modern websites load content dynamically using JavaScript: the HTML that arrives from the server is just a shell, and the real content appears after JavaScript runs in the browser.

Selenium solves this problem by automating a real web browser. Instead of downloading raw HTML, Selenium launches Chrome, Firefox, or another browser, navigates to a page, waits for JavaScript to execute, and then lets you interact with the fully rendered page. You can click buttons, fill in forms, scroll pages, and extract data just as a human user would.

Browser automation is also valuable beyond scraping. It is used for testing web applications, automating repetitive workflows, and generating screenshots. However, it is slower and more resource-intensive than static scraping, so use it only when Beautiful Soup alone is insufficient.

## Concepts

### How Selenium Works

1. You install a WebDriver (a small program that controls a specific browser).
2. Selenium launches the browser in the background (headless mode) or visibly.
3. You send commands: navigate to a URL, find elements, click, type, read text.
4. The browser executes JavaScript, renders the page, and responds.

### Setup

Install Selenium: `pip install selenium`

Modern Selenium (v4.6+) can automatically download and manage the WebDriver for you. No manual driver installation is needed in most cases.

### Finding Elements

- `driver.find_element(By.ID, "element_id")`
- `driver.find_element(By.CLASS_NAME, "class_name")`
- `driver.find_element(By.CSS_SELECTOR, "div.class > a")`
- `driver.find_element(By.XPATH, "//div[@class='item']")`
- `driver.find_elements(...)` returns a list of all matches.

### Waiting for Elements

Dynamic pages need time to load. Instead of `time.sleep()`, use explicit waits:

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "results"))
)
```

### Headless Mode

Run the browser without a visible window (useful for servers and automation scripts):

```python
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
```

## Practical Examples

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Launch Chrome in headless mode
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options)

try:
    # Navigate to a page
    driver.get("https://example.com")
    
    # Extract the page title and heading
    print(f"Page title: {driver.title}")
    
    heading = driver.find_element(By.TAG_NAME, "h1")
    print(f"Heading: {heading.text}")
    
    paragraphs = driver.find_elements(By.TAG_NAME, "p")
    print(f"Paragraphs found: {len(paragraphs)}")
    for p in paragraphs:
        print(f"  {p.text[:80]}")
finally:
    driver.quit()
```

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options)

try:
    # Navigate to a search page
    driver.get("https://www.python.org")
    
    # Find the search box and type a query
    search_box = driver.find_element(By.ID, "id-search-field")
    search_box.clear()
    search_box.send_keys("pathlib")
    search_box.send_keys(Keys.RETURN)
    
    # Wait for results and extract them
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".list-recent-events"))
    )
    
    results = driver.find_elements(By.CSS_SELECTOR, ".list-recent-events li")
    print(f"Search results for 'pathlib': {len(results)}")
    for r in results[:5]:
        print(f"  - {r.text[:80]}")
finally:
    driver.quit()
```

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(options=options)

try:
    # Take a screenshot
    driver.get("https://example.com")
    driver.save_screenshot("example_screenshot.png")
    print("Screenshot saved as example_screenshot.png")
    
    # Get the full page source (useful for combining with Beautiful Soup)
    page_source = driver.page_source
    print(f"Page source length: {len(page_source)} characters")
finally:
    driver.quit()
```

## Guided Practice

Build a script that uses Selenium to visit a practice form site and extract information.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scrape_with_selenium():
    """Demonstrate Selenium navigation and data extraction."""
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    
    driver = webdriver.Chrome(options=options)
    
    try:
        # Visit a page with dynamic content
        driver.get("https://books.toscrape.com/")
        
        print(f"Page title: {driver.title}")
        print(f"Current URL: {driver.current_url}")
        
        # Find all book titles
        books = driver.find_elements(By.CSS_SELECTOR, "article.product_pod h3 a")
        print(f"\nBooks on the page: {len(books)}")
        for book in books[:5]:
            title = book.get_attribute("title")
            print(f"  - {title}")
        
        # Click the "next" button to go to page 2
        next_button = driver.find_element(By.CSS_SELECTOR, "li.next a")
        next_button.click()
        
        # Wait for the new page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "article.product_pod"))
        )
        
        print(f"\nNavigated to: {driver.current_url}")
        books_page2 = driver.find_elements(By.CSS_SELECTOR, "article.product_pod h3 a")
        print(f"Books on page 2: {len(books_page2)}")
        for book in books_page2[:5]:
            print(f"  - {book.get_attribute('title')}")
        
    finally:
        driver.quit()


scrape_with_selenium()
```

## Daily Challenge

**Automate a Form Submission**

Write a script called `form_automator.py` that uses Selenium to interact with a practice form website.

Use the practice site: `https://the-internet.herokuapp.com/login`

Your script should:

1. Launch a headless Chrome browser.
2. Navigate to the login page.
3. Find the username and password fields.
4. Enter the credentials: username `tomsmith`, password `SuperSecretPassword!` (these are provided by the practice site).
5. Click the Login button.
6. Wait for the page to load and verify that login was successful by checking for a success message.
7. Navigate to the secure area and extract the page content.
8. Click the Logout button.
9. Verify that logout was successful.
10. Print a report of each step and its result.

Requirements:
- Use explicit waits instead of `time.sleep()`.
- Handle exceptions if elements are not found.
- Close the browser in a `finally` block.

## Expected Output

```
=== Form Automation Test ===

Step 1: Navigating to login page...
  URL: https://the-internet.herokuapp.com/login
  Page loaded successfully.

Step 2: Entering credentials...
  Username: tomsmith
  Password: ********

Step 3: Clicking Login...
  Success! Message: "You logged into a secure area!"

Step 4: Accessing secure area...
  Secure page content: "Welcome to the Secure Area..."

Step 5: Logging out...
  Logout successful. Returned to login page.

All steps completed successfully.
```

## Assessment

1. When should you use Selenium instead of Beautiful Soup for scraping?
2. What is headless mode, and why is it useful for automation scripts?
3. Why should you use explicit waits (`WebDriverWait`) instead of `time.sleep()` in Selenium scripts?

## Submission Instructions

Submit your solution to: `task/students/your-github-username/module-05/day-048/`

Include `form_automator.py` and a `README.md` explaining setup requirements.

## Additional Resources

- [Selenium Python documentation](https://selenium-python.readthedocs.io/)
- [The Internet - Heroku practice site](https://the-internet.herokuapp.com/)

## Reflection

- What are the trade-offs between scraping speed and accuracy when choosing between Beautiful Soup and Selenium?
- How could browser automation be used for testing your own web applications?
