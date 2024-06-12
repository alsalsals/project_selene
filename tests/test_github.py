import allure
from selene import browser, by, be, have, query
from selene.support.shared.jquery_style import s
import requests

from tests import steps_allure as step


def test_check_name_on_github_page():
    """ Open github and check name on the pages """
    browser.open('https://github.com/alsalsals')
    browser.element('[itemprop="name"]').should(have.text('Alsu Fayzullina'))


def test_download_readme():
    """ Open github and download the readme """
    browser.open('https://github.com/alsalsals/project_selene/blob/master/README.md')

    href_readme = browser.element('[data-testid="raw-button"]').get(query.attribute('href'))
    file_readme = requests.get(href_readme).content

    with open('README.md', 'wb') as f:
        f.write(file_readme)

    with open('README.md') as f:
        text = f.read()
        assert "to generate reports after test run: allure serve tests/allure-result" in text



def test_search_issue_with_allure_logs():
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


def test_search_issue_with_allure_fixture():
    """ Open github and search issue """
    step.open_github()
    step.search_repo('alsalsals/project_selene')
    step.looking_for_issue('for test')

