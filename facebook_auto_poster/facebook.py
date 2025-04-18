from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Firefox()
driver.get("http://facebook.com")

emailelement = driver.find_element(By.XPATH, '//*[@id="email"]')
emailelement.send_keys('')

passelement = driver.find_element(By.XPATH, '//*[@id="pass"]')
passelement.send_keys('')

elem = driver.find_element(By.XPATH, '//*[@id="loginbutton"]')
elem.click()

statuselement = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[@name='xhpc_message']"))
)
statuselement.send_keys('Hi There')

buttons = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.TAG_NAME, 'button'))
)

for button in buttons:
    if button.text == 'Post':
        button.click()
        break

sleep(5)
driver.quit()