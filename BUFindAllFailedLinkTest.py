from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from urllib.parse import urlparse
import time

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://bongau.edu.et/")
time.sleep(3)  

visited_links = set()
broken_links = []
#this testing scan all links and finally collect  broken links from BU website
#first, the home page will be opened and then after all other links are checked in the background for 3 or 4 minutes.
links = driver.find_elements(By.TAG_NAME, "a")

for link in links:
    href = link.get_attribute("href")

    # Skip if href is None, duplicate, or not HTTP/S
    if not href or href in visited_links:
        continue

    parsed = urlparse(href)
    if parsed.scheme not in ["http", "https"]:
        continue

    visited_links.add(href)
    print(f"Checking: {href}") # to display each page during loading d/t pages/links
    try:
        # HEAD for faster checking
        response = requests.head(href, allow_redirects=True, timeout=10)
        if response.status_code >= 400:
            broken_links.append((href, response.status_code))
    except requests.exceptions.RequestException as e:
        broken_links.append((href, str(e)))

driver.quit()
# summary
print("\nBroken Links Report:")
if broken_links:
    for url, issue in broken_links:
        print(f"[{issue}] - {url}")
else:
    print("No broken links found.")
