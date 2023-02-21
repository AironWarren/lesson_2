from selene.support.shared import browser
import pytest


@pytest.fixture()
def open_browser():
    browser.config.window_height = 900
    browser.config.window_width = 900
    browser.open('https://google.com')




