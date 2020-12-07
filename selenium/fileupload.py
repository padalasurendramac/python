from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('https://mail.rediff.com/cgi-bin/login.cgi')

driver.find_element(By.NAME, 'proceed').click()
time.sleep(3)
#js pop windows
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
#alert.dismiss()
alert.send_keys('h1')
#main window again select
driver.swith_to.default_content()


time.sleep(3)
driver.quit()

driver.get('http://www.londonfreelance.org/courses/frames/index.html')
driver.switch_to.frame('main')

#main ( also we can count 123 (2)
#another method frame_element = driver.find_element(By.NAME, 'main')
#driver.switch_to.frame(frame_element)

headerValue = driver.find_element(By.CSS_SELECTOR, 'body > h2').text

print(headerValue)

driver.switch_to.default_content()
#default method alternative parent method
#driver.switch_to.parent_frame()

