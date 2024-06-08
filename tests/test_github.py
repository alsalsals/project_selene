from selene import browser, by, be, have


def test_check_name_on_github_page():
    """ Open github and check name on the pages """
    browser.open('https://github.com/alsalsals')
    browser.element('[itemprop="name"]').should(have.text('Alsu Fayzullina'))


def test_download_selene_project():
    """ Open github and download the project """
    browser.open('https://github.com/alsalsals')
    browser.element(by.text('project_selene')).click()
    browser.all('//button').element_by(have.text('Code')).click()
    browser.all('[data-component*="ActionList.Item--DividerContainer"]').element_by(have.text('Download ZIP')).click()
