import time

import selenium
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

driver: WebDriver = selenium.webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.implicitly_wait(5)
# driver
# 5 seconds is max time out.. 2 seconds (3 seconds save)
