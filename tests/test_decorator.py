import allure
from selene.support import by
from allure_commons.types import Severity
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'ksenya')
@allure.feature('Задачи в репозитории')
@allure.story('Шаги с декоратором')
@allure.link('https://github.com', name='Testing')
def test_decorator_steps():
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue_tab()
    should_see_issue_with_number('#68')


@allure.step('Открыть главную страницу')
def open_main_page():
    browser.config.window_height = 1920
    browser.config.window_width = 1620
    browser.open('https://github.com')


@allure.step('Найти репозиторий {repo}')
def search_for_repository(repo):
    s('.header-search-input').click()
    s('.header-search-input').send_keys(repo)
    s('.header-search-input').submit()


@allure.step('Перейти по ссылке репозитория {repo}')
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step('Открыть таб Issues')
def open_issue_tab():
    s('#issues-tab').click()


@allure.step('Проверить наличие Issue с номером {number}')
def should_see_issue_with_number(number):
    s(by.partial_text(number)).click()