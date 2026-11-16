import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


@pytest.mark.basic
@pytest.mark.regression
def test_dropdown(browser):
    browser.get("http://the-internet.herokuapp.com/dropdown")

    dropdown = Select(browser.find_element(By.ID, "dropdown"))

    options = dropdown.options

    assert len(options) == 3, "Количество вариантов в списке не равно 3"
    assert options[1].text == "Option 1", "Текст не равен Option 1"
    assert options[2].text == "Option 2", "Текст не равен Option 2"

    dropdown.select_by_visible_text("Option 1")
    assert dropdown.first_selected_option.text == "Option 1", "Ожидалось Option 1"

    dropdown.select_by_visible_text("Option 2")
    assert dropdown.first_selected_option.text == "Option 2", "Ожидалось Option 2"
