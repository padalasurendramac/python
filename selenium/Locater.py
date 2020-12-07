from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import time

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")

print(driver.title)

username_url = driver.find_element(By.ID, 'Form_submitForm_subdomain')
first_name = driver.find_element(By.ID, "Form_submitForm_FirstName")
last_name = driver.find_element(By.ID, "Form_submitForm_LastName")
email = driver.find_element(By.ID, "Form_submitForm_Email")
feature_link = driver.find_element(By.LINK_TEXT, "Features")

username_url.send_keys("newworld")
time.sleep(5)
first_name.send_keys("group")
last_name.send_keys("test")
email.send_keys("surendra.padala2428@gmail.com")
time.sleep(10)
feature_link.click()
