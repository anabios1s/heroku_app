from selenium import webdriver

driver = webdriver.Chrome()
driver.set_window_size(100,100)
driver.get("http://google.com")
size = driver.get_window_size()
print(size["width"])
print(size["height"])
position = driver.get_window_position()
print(position["x"])
print(position["y"])
driver.quit()