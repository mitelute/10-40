from selenium import webdriver
import time
# Start browser and open the main site
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://bongau.edu.et/")
time.sleep(2)

links = [
    "https://www.bongau.edu.et/contactus",
    "http://cloud.bongau.edu.et/",
    "https://mint.gov.et/"
]
# "https://172.16.20.20/",     "https://172.16.20.37/",    "https://172.16.20.45/",
# LAN accesbile links
for link in links:
    driver.execute_script(f"window.open('{link}', '_blank');")
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(3)  # Allow page to load
    driver.switch_to.window(driver.window_handles[0])  # Back to main tab
    time.sleep(1)

# Keep browser open for manually review
input("Press Enter to close the browser...")

driver.quit()
