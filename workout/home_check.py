import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://saucedemo.com")

# driver.is_selected()
# driver.is_displayed()
# driver.is_enabled()

login_button = driver.find_element(By.ID, "user-name")
print(login_button.is_displayed())
print(login_button.is_enabled())
print(login_button.is_selected())
login_button.send_keys("standard_user")
login_button.clear()
time.sleep(5)



driver.quit()