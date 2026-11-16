import pytest
from selenium.webdriver.common.by import By

@pytest.mark.basic
@pytest.mark.regression
def test_typos(browser):
    browser.get("http://the-internet.herokuapp.com/typos")

    correct_text = "Sometimes you'll see a typo, other times you won't."
    found_correct_text = False

    for i in range(1, 11):
        browser.refresh()

        target_elem = browser.find_elements(By.TAG_NAME, "p")
        actual_text = target_elem[1].text

        if actual_text == correct_text:
            found_correct_text = True
            print(f"Корректный текст найден на {i} обновлении страницы")
            break

    assert found_correct_text, "За 10 рефрешей ожидаемый текст не отобразился"
