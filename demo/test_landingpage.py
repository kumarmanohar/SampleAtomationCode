import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pytest_html_reporter import attach
driver = webdriver.Chrome()
attach(data=driver.get_screenshot_as_png())
#@pytest.mark.order(1)
@pytest.mark.smoke
def test_launch():
    driver.get("https://demo.automationtesting.in/Index.html")
    attach(data=driver.get_screenshot_as_png())
    assert True== False
#@pytest.mark.order(3)
@pytest.mark.smoke
def test_title():
    print(driver.title)
#@pytest.mark.order(2)
#@pytest.mark.skip
@pytest.mark.smoke
def test_skipsigin():
    driver.find_element(By.ID,'btn2').click()

