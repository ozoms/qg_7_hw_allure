import allure
from allure_commons.types import Severity
from selene import by, be
from selene.support.shared import browser


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "eroshenkoam")
@allure.feature("Задачи в репозитории")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link("https://github.com", name="Testing")
def test_step():
    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com/')

    with allure.step('Ищем репозиторий'):
        browser.element('.header-search-input').click().set_value('eroshenkoam/allure-example').submit()

    with allure.step('Переходим по ссылке репозитория'):
        browser.element('[href="/eroshenkoam/allure-example"]').click()

    with allure.step('Открываем tab issues'):
        browser.element('#issues-tab').click()

    with allure.step('Проверяем наличие issues с номером 76'):
        browser.element(by.partial_text('#76')).should(be.visible)
