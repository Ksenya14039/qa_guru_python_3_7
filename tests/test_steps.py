import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser

@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'ksenya')
@allure.feature('Задачи в репозитории')
@allure.story('Посредством лямбда шагов')
@allure.link('https://github.com', name='Testing')
def test_github_issue():
    with allure.step('Открыть главную страницу'):
        browser.config.window_height = 1920
        browser.config.window_width = 1620
        browser.open('https://github.com/')

    with allure.step('Найти репозиторий'):
        browser.element('.header-search-input').click()
        browser.element('.header-search-input').send_keys('eroshenkoam/allure-example')
        browser.element('.header-search-input').submit()

    with allure.step('Открыть репозиторий'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Открыть таб issues'):
        browser.element('#issues-tab').click()

    with allure.step('Проверить наличие issue с номером 68'):
        browser.element(by.partial_text('#68')).should(be.visible)