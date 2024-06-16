import pytest
from selene import browser
from selenium import webdriver
import os


@pytest.fixture(autouse=True)
def browser_management():
    # driver_options = webdriver.FirefoxOptions()
    # driver_options.add_argument('--headless')
    # browser.config.driver_options = driver_options

    # browser.config.driver = webdriver.Firefox()

    browser.config.window_width = os.getenv('window_width', '2050')
    browser.config.window_height = os.getenv('window_width', '1441')
    browser.config.timeout = float(os.getenv('timeout', '5.0'))


