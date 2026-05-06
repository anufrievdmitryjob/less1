import pytest
import time
from selene import browser, by, have


@pytest.fixture(scope="function", autouse=True)
def setup_browser():
    browser.config.window_width = 1280
    browser.config.window_height = 720
    browser.config.timeout = 3

    print("Браузер настроен")

    yield

    browser.quit()
    print("раузер закрыт")

def test_search_in_google():
    browser.open("https://www.google.com/ncr")
    time.sleep(3)

    browser.element('[name = "q"').type("petest selene")
    time.sleep(1)

    browser.element('[name = "q').press_enter()

    browser.element(by.partial_text("Selene - GitHub")).should(have.text("Selene - GitHub"))
    print ("Всё нашлось")