import json

import allure
import requests
from allure_commons.types import AttachmentType
from selene import browser, have

URL_demowebshop = 'https://demowebshop.tricentis.com'
LOGIN = "alal@gmail.com"


def test_login_api():
    ''' Verify successful user login via API '''
    result = requests.post(
        url=URL_demowebshop+'/login',
        data={"Email": LOGIN, "Password": "Anime312", "RememberMe": False},
        allow_redirects=False
    )

    allure.attach(
        body=result.text,
        name="Response",
        attachment_type=AttachmentType.TEXT,
        extension='txt'
    )

    allure.attach(
        body=str(result.cookies),
        name="Cookies",
        attachment_type=AttachmentType.TEXT,
        extension='txt'
    )

    print(result.status_code)
    print(result.text)
    print(result.cookies)
    cookie = result.cookies.get('NOPCOMMERCE.AUTH')

    browser.open(URL_demowebshop)
    browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': cookie})
    browser.open(URL_demowebshop)

    with allure.step("Verify successful authorization"):
        browser.element(".account").should(have.text(LOGIN))
