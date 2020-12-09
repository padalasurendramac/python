from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
#driver.implicitly_wait(6)
#time out = 10
#dynamic wait
#imp wait will be applied for all the web element
#global wait
#only for web elements
#not for non web elements: title,urls,alerts
#dynamic wait


driver.get('https://facebook.com/')
email_name = driver.find_element(By.NAME, 'email')
email_name.send_keys('surendra.padala2428@gmail.com')
driver.find_element(By.NAME, 'pass').send-keys('test')