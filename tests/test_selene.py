from selene.support.shared.jquery_style import s
from selene import browser, by, be


def test_github():
    browser.open('')

    s(".header-search-button").click()
    s("#query-builder-test").send_keys("eroshenkoam/allure-example").submit()
    #s("#query-builder-test").submit()

    s(by.link_text("eroshenkoam/allure-example")).click()

    s("#issues-tab").click()

    s(by.partial_text("#88")).should(be.visible)