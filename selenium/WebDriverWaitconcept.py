from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec #this is like ec=expected_conditions
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://facebook.com/')
#this is also dynamic wait
wait = WebDriverWait(driver, 10)
#below is condition to wait until(inside brack is for pass as one element)
email_id = wait.until(ec.presence_of_element_located((By.ID, 'email')))

email_id.send_keys('test@gmail.com')



