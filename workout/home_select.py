import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
add_element = driver.find_element(By.XPATH, '//button[text()="Add Element"]')
add_element.click()
add_element.click()
delete_elements = driver.find_element(By.XPATH, '//button[text()="Delete"]')

assert len(delete_elements) == 2, "Должно быть два элемента DELETE"
assert add_element.is_displayed(), "Элемент должен отображаться"

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