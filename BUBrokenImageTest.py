from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://bongau.edu.et/about-bu-1")
#driver.get("https://bongau.edu.et/contactus")
#driver.get("https://bongau.edu.et/slides")
#TEST CASES to check the above links for image display
time.sleep(3)
img_elements = driver.find_elements(By.CLASS_NAME, "img-fluid.rounded-circle.d-block.mx-auto.shadow")

safely_loaded_images = []
brokenly_loaded_images = []

for img_element in img_elements:
    # Scroll to the image
    driver.execute_script("arguments[0].scrollIntoView();", img_element)
    time.sleep(1)

    img_src = img_element.get_attribute("src")
    is_displayed = driver.execute_script(
        "return arguments[0].complete && typeof arguments[0].naturalWidth != 'undefined' && arguments[0].naturalWidth > 0", 
        img_element
    )

    if is_displayed:
        safely_loaded_images.append(img_src)
    else:
        brokenly_loaded_images.append(img_src)

print("\n--- Loaded Images ---")
for src in safely_loaded_images:
    print(src)

print("\n---Not Displayed Images ---")
for src in brokenly_loaded_images:
    print(src)

driver.quit()
