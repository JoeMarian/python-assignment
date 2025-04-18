from selenium import webdriver

import time

driver = webdriver.Chrome()

driver.get('http://www.amazon.in')

driver.maximize_window()

time.sleep(5)

select = driver.find_element_by_link_text('Electronics')

select.click()

time.sleep(5)

select_1 = driver.find_element_by_link_text('Audio')

select_1.click()