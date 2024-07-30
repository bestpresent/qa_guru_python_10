from selene import browser
import pytest


@pytest.fixture(autouse=True)
def config_browser():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://github.com'
    yield
    browser.quit()
