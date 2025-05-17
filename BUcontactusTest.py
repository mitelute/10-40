from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# test cases: empty forms, and inavalid email & phone
# skipped for valid email because it pass with @ symbol only even if for incorrect email
test_cases = [
    {
        "name": "each_fields_empty",
        "form_data": {
            "contact_name": "",
            "phone": "",
            "email_from": "",
            "partner_name": "",
            "name": "",
            "description": "",
        }
    },
    {
        "name": "invalid_email_and_phone",
        "form_data": {
            "contact_name": "Testing BU",
            "phone": "090000num",
            "email_from": "testexample.com", 
            "partner_name": "empty partner name",
            "name": "default Subject field",
            "description": "illegal description for my issue",
        }
    }
]

driver = webdriver.Chrome()
driver.maximize_window()

for test in test_cases:
    test_name = test["name"]
    form_data = test["form_data"]

    driver.get("https://bongau.edu.et/contactus")
    # Wait for form to load
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "contact_name"))
        )
    except Exception as e:
        print(f"Page load error in {test_name}: {e}")
        continue
    # send test data
    for name, value in form_data.items():
        try:
            field = driver.find_element(By.NAME, name)
            field.clear()
            field.send_keys(value)
        except Exception as e:
            print(f"Error filling field '{name}' in {test_name}: {e}")
    # click submit button 
        send_button = driver.find_element(By.CLASS_NAME, "o_website_form_send")
        driver.execute_script("arguments[0].click();", send_button)
        time.sleep(1)

    time.sleep(5)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{test_name}_{timestamp}.png"
    driver.save_screenshot(filename)
    print(f"Screenshot saved: {filename}")

    time.sleep(3)
driver.quit()
