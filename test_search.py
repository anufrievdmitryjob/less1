import pytest
import time
from selene import browser, by, have
from selene.support.conditions import be


@pytest.fixture(scope="function", autouse=True)
def setup_browser():
    browser.config.window_width = 1280
    browser.config.window_height = 720
    browser.config.timeout = 10

    print("Браузер настроен")

    yield

    browser.quit()
    print("Браузер закрыт")

def test_search_in_google():
    try:
        browser.open("https://ya.ru")
        time.sleep(0.5)

        browser.element('[name="text"]').type("pytest selene")
        time.sleep(1.5)

        browser.element('[name="text"]').press_enter()

        browser.element(by.partial_text("pytest-selene")).should(be.visible)
        print ("Всё нашлось!")
    except Exception as e:
        print ("Не вышло!")