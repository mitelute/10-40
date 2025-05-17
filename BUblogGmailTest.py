from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
#testing without @ symbol & invalid email
#testing with @ but invalid email
#testing with valid email
driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://bongau.edu.et/blog/demo-post-5/post/latest-news-6#")
time.sleep(5)

def test_subscription(email):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'js_subscribe_email')))
    email_input = driver.find_element(By.CLASS_NAME, 'js_subscribe_email')
    subscribe_button = driver.find_element(By.CLASS_NAME, 'js_subscribe_btn')
    driver.execute_script("arguments[0].removeAttribute('disabled')", email_input)
    email_input.clear()
    time.sleep(5)
    email_input.send_keys(email)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(subscribe_button))
    time.sleep(5)
    ActionChains(driver).move_to_element(subscribe_button).click().perform()
    time.sleep(5)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"blog_subscribe_{timestamp}.png"
    driver.save_screenshot(filename)

# Test with an invalid emails
print("done first case")
invalid_email = "invalid-email"
print("Testing with fully invalid email:")
test_subscription(invalid_email)
print("done second case")
invalid_email = "invalidwith@.com"
print("Testing with invalid with @ symboll:")
test_subscription(invalid_email)
#skipped for valid email because it pass with @ symbol even if for incorrect email
driver.quit()
