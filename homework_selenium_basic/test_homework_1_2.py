import pytest
from selenium.webdriver.common.by import By


@pytest.mark.basic
@pytest.mark.smoke
def test_checkboxes(browser):
    browser.get("http://the-internet.herokuapp.com/checkboxes")

    checkboxes = browser.find_elements(By.CSS_SELECTOR, "[type='checkbox']")

    assert not checkboxes[0].is_selected(), "Первый чекбокс ожидался НЕ отмеченным при открытии страницы!"
    assert checkboxes[1].is_selected(), "Второй чекбокс ожидался отмеченным при открытии страницы!"

    checkboxes[0].click()
    assert checkboxes[0].is_selected(), "Первый чекбокс ожидался отмеченным"
    assert checkboxes[1].is_selected(), "Второй чекбокс ожидался отмеченным"

    checkboxes[1].click()
    assert checkboxes[0].is_selected(), "Первый чекбокс ожидался отмеченным"
    assert not checkboxes[1].is_selected(), "Второй чекбокс ожидался НЕ отмеченным!"
