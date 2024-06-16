import os.path
from urllib.parse import urljoin

import requests
import allure
from selene import by, be, have, query, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from tests import steps_allure as step

base_url = 'https://github.com/alsalsals/'


def test_check_title():
    """ Open github and tittle """
    with allure.step("Open github"):
        browser.open(base_url)

    with allure.step("Check tittle of the page"):
        browser.should(have.title('alsalsals (Alsu Fayzullina) · GitHub'))

    with allure.step("Check name of the page"):
        browser.element('[itemprop="name"]').should(have.text('Alsu Fayzullina'))


def test_check_project_selene():
    """ Check project_selene name """
    with allure.step("Open github"):
        browser.open(base_url)

    with allure.step("project_selene"):
        browser.all('.repo').first.should(have.text('project_selene'))


def test_download_readme_by_href():
    """ Open github, download the readme and check text"""
    with allure.step("Open github's README"):
        browser.open(urljoin(base_url,'/project_selene/blob/master/README.md'))

    with allure.step("Get href of the Readme.md file"):
        href_readme = browser.element('[data-testid="raw-button"]').get(query.attribute('href'))

    with allure.step("Download the file's content"):
        file_readme = requests.get(href_readme).content

    with allure.step("Write the content in file"):
        with open('tmp/README.md', 'wb') as f:
            f.write(file_readme)

    with allure.step("Check the text in the file"):
        with open('tmp/README.md') as f:
            text = f.read()
            assert "allure serve tests/allure-result" in text


def test_download_readme_by_button():
    """ Open github, download the readme and check text"""
    curient_dir = os.path.dirname(os.path.abspath(__file__))
    if not os.path.exists('tmp'):
        os.mkdir('tmp')
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": os.path.join(curient_dir, 'tmp'),
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
        browser.open(base_url)

    with allure.step("Search 'alsalsals/project_selene'"):
        s('.header-search-button').click()
        s('#query-builder-test').send_keys('alsalsals/project_selene').press_enter()

    with allure.step("Go to 'alsalsals/project_selene'"):
        s(by.link_text('alsalsals/project_selene')).click()
        s('#issues-tab').click()

    with allure.step("Looking for 'for test' issue"):
        s(by.partial_text('for test')).with_(timeout=10).should(be.visible)


def test_search_issue_with_allure_fixture():
    """ Open github and search issue """
    step.open_github()
    step.search_repo('alsalsals/project_selene')
    step.looking_for_issue('for test')


def test_open_docs():
    """ Check project_selene name """
    with allure.step("Open github"):
        browser.open(base_url)

    with allure.step("Open repositories list page"):
        browser.element('#repositories-tab').perform(command.js.click)
    with allure.step("Scroll into view element"):
        browser.element('[href*="your-github-profile"]').perform(command.js.scroll_into_view)
        browser.driver.execute_script("document.querySelector('.body-height').style.transform='scale(.65)'")


