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


# def test_create_issue():
#     """  """
#     with allure.step(" Open ... "):
#         browser.open('https://translate.yandex.ru/ocr')
#
#     with allure.step(""):
#         browser.element('#issues-tab').perform(command.js.click)
#
#     with allure.step(""):
#         browser.element('[data-ga-click*="create new issue"]').click()
#         browser.element('[data-ga-click*="create new issue"]').perform(command.js.scroll_into_view)
#         browser.driver.execute_script("document.querySelector('.body-height').style.transform='scale(.65)'")
