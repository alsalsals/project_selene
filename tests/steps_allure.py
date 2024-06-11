import allure
from selene import browser, by, be
from selene.support.shared.jquery_style import s


@allure.step("Open github")
def open_github():
    browser.open('https://github.com/')


@allure.step("Search and go to 'alsalsals/project_selene'")
def search_repo(repo):
    s('.header-search-button').click()
    s('#query-builder-test').send_keys(repo).press_enter()
    s(by.link_text('alsalsals/project_selene')).click()
    s('#issues-tab').click()


@allure.step("Looking for 'for test' issue")
def looking_for_issue(text):
    s(by.partial_text(text)).should(be.visible)
