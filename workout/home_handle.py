from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://google.com")
first_window = driver.current_window_handle
print("Первая вкладка" + first_window)
driver.switch_to.new_window("tab")
second_window = driver.current_window_handle
driver.get("http://yandex.ru")
print("Вторая вкладка" + second_window)
handles = driver.window_handles
print(handles)
driver.switch_to.window(first_window)
driver.close()


# handle = driver.current_window_handle
# print(handle)
#
# driver.quit()