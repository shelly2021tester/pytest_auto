import pytest
from selenium import webdriver
from pytest_f.config.testconfig import url,driver_path


@pytest.fixture(scope='session')
def test_logsystem():
    browser = webdriver.Chrome(executable_path=driver_path)
    browser.get(url)
    browser.maximize_window()
    browser.implicitly_wait(10)  # 隐形等待
    yield browser
    browser.quit()


