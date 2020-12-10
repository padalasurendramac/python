from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec #this is like ec=expected_conditions
from webdriver_manager.chrome import ChromeDriverManager
import time
options = Options()
options.add_arguments('--allow-running-insecure-content')
options.add_arguments('--ignore-certificate-errors')
#othermethods
#desired_capabilities = DesiredCapabilities().CHROME.copy()
#desired_capabilities['acceptInsecureCerts'] = True
#driver = webdriver.Chrome(Chrome.DriveManager().install(), desired_capabilities = desired_capabilities)
#or other methods
#options = Options()
#options.set_capability('acceptInsecureCerts', True)
#driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
driver = webdriver.Chrome(ChromeDriverManager().install(), options = options)
driver.implicitly_wait(10)

driver.get('https://expired.badssl.com/')

print(driver.find_element(By.TAG_NAME, 'h1').text)




#firfox
#above same method could use for firefox
from webdriver_manager.firefox import GeckoDriverManager

profile = webdriver.FirefoxProfile()
profile.accept_untrusted_certs = True
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=profile)

driver.implicitly_wait(10)

driver.get('https://expired.badssl.com/')

print(driver.find_element(By.TAG_NAME, 'h1').text)
