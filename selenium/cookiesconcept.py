from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)


driver.get('https://www.reddit.com/')
print(driver.get_cookies())

driver.add_cookie({"name":"naveenPython","domain":"reddit.com","value":"python"})
#cookies add time domain name should be same

#print(driver.get_cookies())
cookies = driver.get_cookies()

for cook in cookies:
    print(cook)
