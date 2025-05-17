import difflib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

def get_section_text(driver, wait, section_css):
    try:
        section_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, section_css)))
        return section_element.text.strip()
    except:
        return "[Missing Element]"

def switch_language(driver, wait, language):
    dropdown_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.dropdown-toggle")))
    dropdown_button.click()
    time.sleep(1)

    lang_xpath = f"//a[contains(@class, 'dropdown-item') and contains(text(), '{language}')]"
    lang_option = wait.until(EC.element_to_be_clickable((By.XPATH, lang_xpath)))
    lang_option.click()
    time.sleep(3)

    clean_href = driver.current_url.split("#")[0]
    print(f"Navigating to {language} version: {clean_href}")
    driver.get(clean_href)
    time.sleep(3)

def compute_similarity(text1, text2):
    ratio = difflib.SequenceMatcher(None, text1, text2).ratio()
    return round(ratio * 100, 2)

driver = webdriver.Edge()
driver.maximize_window()
#driver.get("https://bongau.edu.et/contactus") #to check for d/t pages
driver.get("https://bongau.edu.et/about-bu")
wait = WebDriverWait(driver, 15)
time.sleep(3)
# Get the full section text for Amharic version
switch_language(driver, wait, "አምሃርኛ")
amharic_section_text = get_section_text(driver, wait, "div.s_title")  
print("Amharic Section Text:", amharic_section_text)

# Get the full section text for English version
switch_language(driver, wait, "English (US)")
english_section_text = get_section_text(driver, wait, "div.s_title") 
print("English Section Text:", english_section_text)

# Compute similarity between English and Amharic content( if more than 80%, then they are almost similarity)
similarity = compute_similarity(english_section_text, amharic_section_text)
print(f"Similarity: {similarity}%")

if similarity > 80:
    print("The texts are considered similar.")
else:
    print("The texts are different.")

print("Current URL:", driver.current_url)
driver.quit()
