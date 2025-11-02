# base/base_test.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from utilities.extent_manager import ExtentManager


@pytest.fixture(scope="class")
def setup(request):
    extent = ExtentManager.get_instance()
    test = extent.create_test(request.node.name)

    options = Options()
    options.add_argument("--remote-allow-origins=*")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 20)

    request.cls.driver = driver
    request.cls.wait = wait
    request.cls.extent = extent
    request.cls.test = test

    yield
    driver.quit()
    extent.flush()
