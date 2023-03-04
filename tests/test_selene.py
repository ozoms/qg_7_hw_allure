from selene import by, be
from selene.support.shared import browser


def test_github():
    browser.config.hold_browser_open = True
    browser.open('https://github.com/')

    browser.element('.header-search-input').click().set_value('eroshenkoam/allure-example').submit()

    browser.element('[href="/eroshenkoam/allure-example"]').click()

    browser.element('#issues-tab').click()

    browser.element(by.partial_text('#76')).should(be.visible)
