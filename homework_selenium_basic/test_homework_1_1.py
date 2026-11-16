import pytest
from selenium.webdriver.common.by import By


@pytest.mark.basic
@pytest.mark.smoke
def test_add_remove_elements(browser):
    browser.get("http://the-internet.herokuapp.com/add_remove_elements/")

    add_element = browser.find_element(By.XPATH, "//button[text()='Add Element']")

    add_element.click()
    add_element.click()

    delete_elements = browser.find_elements(By.XPATH, '//button[text()="Delete"]')

    assert len(delete_elements) == 2, "Должно быть два элемента DELETE"
    assert delete_elements[0].is_displayed(), "Первый элемент должен отображаться"
    assert delete_elements[1].is_displayed(), "Второй элемент должен отображаться"

    delete_elements[0].click()

    delete_elements = browser.find_elements(By.XPATH, '//button[text()="Delete"]')

    assert len(delete_elements) == 1, "После удаления должна остаться одна кнопка Delete"
