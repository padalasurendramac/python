from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)


driver.get('http://amazon.in')
driver.find_element(By.LINK_TEXT, 'Best Sellers').click()
time.sleep(5)
driver.back()
#back to previous page method driver.back()
time.sleep(5)
driver.forward()
#forword method driver.forward()
time.sleep(5)
driver.back()

driver.refresh()
#refresh page driver.refresh()
time.sleep(5)
driver.quit()