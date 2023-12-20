import csv
import time
from pathlib import Path
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

# set up Chrome driver
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Remote('http://localhost:4444/wd/hub', options=options)

path = "https://www.amazon.com/s?k=macbook+pro&crid=EQLJOW3I877&sprefix=macbook+pro%2Caps%2C467&ref=nb_sb_noss_1"
# navigate to amazon homepage
driver.get(path)

time.sleep(10)
# find searchbar and input
outer_html = driver.page_source

# Print or store the outer HTML content
print(outer_html)

file_path = 'page_content2.txt'
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(outer_html)


# quit driver
driver.quit()
