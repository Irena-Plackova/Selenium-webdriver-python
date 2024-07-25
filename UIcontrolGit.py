import time

import selenium
from selenium.webdriver.common.by import By

driver = selenium.webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)


checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

print(len(checkboxes))

for checkboxes in checkboxes:
    if checkboxes.get_attribute("value") == "option2":
        checkboxes.click()

        assert checkboxes.is_selected()
        break

radiobuttons = driver.find_elements(By.CSS_SELECTOR,"radioButton")

time.sleep(5)