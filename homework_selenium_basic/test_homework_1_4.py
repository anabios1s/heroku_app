import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.mark.basic
@pytest.mark.smoke
@pytest.mark.parametrize("symbol", ["a", "b", "e"])
def test_input_symbol(browser,symbol):
    browser.get("http://the-internet.herokuapp.com/inputs")
    input_field = browser.find_element(By.TAG_NAME, "input")

    input_field.send_keys(symbol)
    assert input_field.get_attribute("value") == "", "Этот буквенный символ доступен для ввода"
    print("\nПервый assert пройден - букву ввести нельзя")

@pytest.mark.basic
@pytest.mark.smoke
def test_inputs(browser):
    browser.get("http://the-internet.herokuapp.com/inputs")

    input_field = browser.find_element(By.TAG_NAME, "input")

    input_field.send_keys("7")
    assert input_field.get_attribute("value") == "7", "Ожидалось 7"
    print("Второй assert пройден - цифру ввести можно")

    input_field.send_keys(Keys.ARROW_UP)
    assert input_field.get_attribute("value") == "8", "Ожидалось 8"
    print("Третий assert пройден - нажатие стрелки вверх увеличивает число в поле на 1")

    input_field.send_keys(Keys.ARROW_DOWN)
    input_field.send_keys(Keys.ARROW_DOWN)
    assert input_field.get_attribute("value") == "6", "Ожидалось 6"
    print("Четвертый assert пройден - нажатие стрелки вниз дважды уменьшает число в поле на 2")
