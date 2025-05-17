from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# Setup
driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://bongau.edu.et/am_ET/web/login")

def reset_fields():
    driver.find_element(By.ID, "login").clear()
    driver.find_element(By.ID, "password").clear()
    time.sleep(1)

# Test 1: Only Email Filled
reset_fields()
email_input = driver.find_element(By.ID, "login")
email_input.send_keys("mitiku.lute@aastustudent.edu.et")
driver.save_screenshot("test1_only_email_filled.png")
driver.find_element(By.XPATH, "//div[contains(@class, 'oe_login_buttons')]//button[@type='submit']").click()
time.sleep(3)
driver.save_screenshot("test1_result.png")
print("Test 1: Only email filled — submitted")

# Test 2: Only Password Filled
reset_fields()
password_input = driver.find_element(By.ID, "password")
password_input.send_keys("password")
driver.save_screenshot("test2_only_password_filled.png")
driver.find_element(By.XPATH, "//div[contains(@class, 'oe_login_buttons')]//button[@type='submit']").click()
time.sleep(3)
driver.save_screenshot("test2_result.png")
print("Test 2: Only password filled — submitted")

# Test 3: Both Fields Empty
reset_fields()
driver.save_screenshot("test3_both_fields_empty.png")
driver.find_element(By.XPATH, "//div[contains(@class, 'oe_login_buttons')]//button[@type='submit']").click()
time.sleep(3)
driver.save_screenshot("test3_result.png")
print("Test 3: Both fields empty — submitted")

# Test 4: Valid Credentials 
reset_fields()
driver.find_element(By.ID, "login").send_keys("mitiku.lute@aastustudent.edu.et")
driver.find_element(By.ID, "password").send_keys("11*******11")
driver.save_screenshot("test4_valid_credentials_filled.png")
driver.find_element(By.XPATH, "//div[contains(@class, 'oe_login_buttons')]//button[@type='submit']").click()
time.sleep(5)
driver.save_screenshot("test4_result.png")
print("Test 4: Valid login attempt submitted")

driver.quit()
