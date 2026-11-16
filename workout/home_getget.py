from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://google.com")

title = driver.title
print(title)

# handle = driver.current_window_handle
# print(handle)

driver.quit()