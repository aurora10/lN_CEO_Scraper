from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import random


options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Remote('http://localhost:4444/wd/hub', options=options)


driver.get("https://www.linkedin.com/")

time.sleep(10)

username = driver.find_element("xpath", "//input[@name='session_key']")
password = driver.find_element("xpath", "//input[@name='session_password']")

username.send_keys("robert@marketorix.com")
password.send_keys("w2vGWGqJNEc2iCTBkH8SaGZ")
time.sleep(8)

submit = driver.find_element("xpath", "//button[@type='submit']")
driver.execute_script("arguments[0].click()", submit)

time.sleep(6)

print("Loggedin successfully")

# seach for job title of CEO:

driver.get("https://www.linkedin.com/search/results/PEOPLE/?keywords=ceo&origin=SWITCH_SEARCH_VERTICAL&sid=~u5")


# get outer html
outer_html = driver.page_source
time.sleep(4)

file_path = 'page_content-ln.html'
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(outer_html)
# Print or store the outer HTML content
print(outer_html)


driver.quit()
