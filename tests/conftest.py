import pytest
from selenium.webdriver.firefox import webdriver
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="drivers/chromedriver 6")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="drivers/geckodriver 3")
    elif browser_name == "safari":
        print("safari")
    elif browser_name == "internetexplorer":
        print("IE")
    driver.get("http://192.237.130.56:4007/ ")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
