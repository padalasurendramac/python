from selenium import  webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time;

browserName = "chrome"

if browserName == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())

elif browserName == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browserName == "safari":
    driver = webdriver.Safari()
else:
    print('Please pass the correct browser name :'+ browserName)

driver.implicitly_wait(5)
driver.get("https://facebook.com")
driver.find_element(By.ID, "email").send_keys("8801762428")
driver.find_element(By.ID, "pass").send_keys("8801762428")
driver.find_element(By.ID, "u_0_b").click()

time.sleep(1000)
driver.quit()
