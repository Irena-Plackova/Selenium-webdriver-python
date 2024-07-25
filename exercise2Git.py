import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

driver.find_element(By.XPATH, "//input[@id='username']").send_keys("contact@rahulshettyacademy.com")
# 5 seconds is max time out.. 2 seconds (3 seconds save)
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("123456")
driver.find_element(By.XPATH, "//div[@class='form-check-inline']//label[1]//span[2]").click()
driver.find_element(By.XPATH, "//input[@id='signInBtn']")

driver.find_element(By.XPATH, "//input[@id='terms']").click()


driver.find_element(By.XPATH, "//div[@class='form-check-inline']//label[1]//span[2]").click()

select = Select(driver.find_element(By.XPATH, "//select[@class='form-control']"))
select.select_by_value("stud")

driver.find_element(By.XPATH, "//input[@id='signInBtn']").click()
time.sleep(10)

