import pytest
from selene import browser
import os


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = os.getenv('base_url', 'https://github.com/alsalsals')
    browser.config.window_width = os.getenv('window_width', '1024')
    browser.config.window_height = os.getenv('window_width', '768')
    browser.config.timeout = float(os.getenv('timeout', '3.0'))




