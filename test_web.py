from selene import browser
from selene import be, have


def test_open_selene(open_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    assert browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_open_error(open_browser):
    browser.element('[name="q"]').should(be.blank).type('qwerqwerfwqeferwfverdsvgsrtevsrtevsretv').press_enter()
    assert browser.element('[id="search"]').should(have.no.text('Selene - User-oriented Web UI browser tests in Python'))
