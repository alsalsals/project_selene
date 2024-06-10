import allure
from selene import browser, by, be, have
from selene.support.shared.jquery_style import s


def test_check_name_on_github_page():
    """ Open github and check name on the pages """
    browser.open('https://github.com/alsalsals')
    browser.element('[itemprop="name"]').should(have.text('Alsu Fayzullina'))


def test_download_project_selene():
    """ Open github and download the project """
    browser.open('https://github.com/alsalsals11')
    browser.element(by.text('project_selene')).click()
    browser.all('//button').element_by(have.text('Code')).click()
    browser.all('[data-component*="ActionList.Item--DividerContainer"]').element_by(
        have.text('Download ZIP')).click()


def test_search_issue():
    """ Open github and search issue """
    with allure.step("Open github"):
        browser.open('https://github.com/')

    with allure.step("Search 'alsalsals/project_selene'"):
        s('.header-search-button').click()
        s('#query-builder-test').send_keys('alsalsals/project_selene').press_enter()

    with allure.step("Go to 'alsalsals/project_selene'"):
        s(by.link_text('alsalsals/project_selene')).click()
        s('#issues-tab').click()

    with allure.step("Looking for 'for test' issue"):
        s(by.partial_text('for test')).should(be.visible)


