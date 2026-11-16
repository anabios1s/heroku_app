import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://saucedemo.com")

# logo = driver.find_element(By.CLASS_NAME, "login_logo")
# logo_text = logo.text
# print(logo_text)

# login_button = driver.find_element(By.ID, "login-button")
# login_button.click()
# time.sleep(5)

# login_button = driver.find_element(By.ID, "user-name")
# login_button.send_keys(Keys.RETURN)
# time.sleep(5)

login_button = driver.find_element(By.ID, "user-name")
login_button.send_keys("standard_user")
login_button.clear()
time.sleep(5)



driver.quit()