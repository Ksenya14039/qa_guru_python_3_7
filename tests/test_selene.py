import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from allure_commons.types import Severity


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'ksenya')
@allure.feature('Задачи в репозитории')
@allure.story('Чистый selene (без шагов')
@allure.link('https://github.com', name='Testing')
def test_github():
    browser.config.window_height = 1920
    browser.config.window_width = 1620
    browser.open('https://github.com/')

    browser.element('.header-search-input').click()
    browser.element('.header-search-input').send_keys('eroshenkoam/allure-example')
    browser.element('.header-search-input').submit()

    browser.element(by.link_text('eroshenkoam/allure-example')).click()

    browser.element('#issues-tab').click()

    browser.element(by.partial_text('#68')).should(be.visible)