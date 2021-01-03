import pytest

from selenium import webdriver


@pytest.fixture
def browser():
    browser = webdriver.Firefox()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
