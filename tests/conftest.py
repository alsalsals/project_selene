import pytest
from selene import browser
import os


@pytest.fixture(autouse=True)
def browser_management():
    browser.config.window_width = os.getenv('window_width', '1024')
    browser.config.window_height = os.getenv('window_width', '768')
    browser.config.timeout = float(os.getenv('timeout', '30.0'))
