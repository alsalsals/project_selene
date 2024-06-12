import os.path

import requests
import allure
from selene import by, be, have, query
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from tests import steps_allure as step


def test_check_name_on_github_page():
    """ Open github and check name on the pages """
    browser.open('https://github.com/alsalsals')
    browser.element('[itemprop="name"]').should(have.text('Alsu Fayzullina'))


def test_download_readme_by_href():
    """ Open github, download the readme and check text"""
    browser.open('https://github.com/alsalsals/project_selene/blob/master/README.md')

    href_readme = browser.element('[data-testid="raw-button"]').get(query.attribute('href'))
    file_readme = requests.get(href_readme).content

    with open('README.md', 'wb') as f:
        f.write(file_readme)

    with open('README.md') as f:
        text = f.read()
        assert "to generate reports after test run: allure serve tests/allure-result" in text


def test_download_readme_by_button():
    """ Open github, download the readme and check text"""
    currient_dir = os.path.dirname(os.path.abspath(__file__))
    if not os.path.exists('tmp'):
        os.mkdir('tmp')
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": os.path.join(currient_dir, 'tmp'),
        "download.prompt_for_download": False,
    }

    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                              options=options)

    browser.config.driver = driver
    # browser.config.hold_browser_open = True

    browser.open('https://github.com/alsalsals/project_selene/blob/master/README.md')
    browser.element('[data-testid="download-raw-button"]').click()

    with open('tmp/README.md') as f:
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

