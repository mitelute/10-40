from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from urllib.parse import urljoin, urlparse
import time
# checking All of the images href link of Bonga University website to find broken image link
driver = webdriver.Chrome()
start_url = "https://bongau.edu.et/"
driver.get(start_url)
time.sleep(5)
link_elements = driver.find_elements(By.TAG_NAME, "a")
links = set()

for elem in link_elements:
    href = elem.get_attribute('href')
    if href and urlparse(href).netloc == urlparse(start_url).netloc:
        links.add(href)

print(f"Total internal links found: {len(links)}")
links.add(start_url)
broken_images = []

for link in links:
    try:
        driver.get(link)
        time.sleep(3)  
        images = driver.find_elements(By.TAG_NAME, "img")
        print(f"\nChecking {len(images)} images in page: {link}")

        for img in images:
            src = img.get_attribute('src')
            if not src:
                continue

            full_src = urljoin(link, src)

            try:
                response = requests.get(full_src, timeout=10)
                if response.status_code != 200:
                    print(f"[Broken] {full_src} on page {link} - Status {response.status_code}")
                    broken_images.append({
                        "page": link,
                        "image_src": full_src,
                        "status_code": response.status_code
                    })
            except Exception as e:
                print(f"[Broken] {full_src} on page {link} - Error: {e}")
                broken_images.append({
                    "page": link,
                    "image_src": full_src,
                    "status_code": str(e)
                })
    
    except Exception as e:
        print(f"Failed to open page {link} - Error: {e}")

driver.quit()

print("\nSummary of broken images found:")
for broken in broken_images:
    print(f"Page: {broken['page']} | Image: {broken['image_src']} | Status: {broken['status_code']}")

import csv
with open('ALLbroken_images_report.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['page', 'image_src', 'status_code']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for broken in broken_images:
        writer.writerow(broken)

print("\nBroken images report saved to ALLbroken_images_report.csv")
