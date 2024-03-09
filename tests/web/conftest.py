import os

import pytest
from allure_commons._allure import attach
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options




def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='100.0'
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv(dotenv_path=".env.credentials")


DEFAULT_BROWSER_VERSION = "100.0"


@pytest.fixture(scope='session')
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver
    browser.config.window_height = 1920
    browser.config.window_width = 1400
    browser.config.timeout = 8.0
    browser.config.base_url = 'https://www.litres.ru/'

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()


@pytest.fixture(scope='function')
def real_browser():
    browser.config.base_url = 'https://www.litres.ru/'
    browser.config.window_height = 1920
    browser.config.window_width = 1400
    browser.config.timeout = 8.0
    # driver_options = webdriver.ChromeOptions()
    # driver_options.add_argument('--headless')
    options = Options()
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-setuid-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--incognito')
    # browser.config.driver_options = driver_options
    browser.open('')

    yield browser

    browser.quit()
