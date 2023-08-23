import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome()
#@pytest.mark.order(1)
@pytest.mark.smoke
def test_launch():
    driver.get("https://www.myntra.com")
#@pytest.mark.order(2)
@pytest.mark.smoke
def test_title():
    print(driver.title)

