import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome()

#def test_launch():
    #driver.get("https://www.amazon.in/")
#def test_title():
    #print(driver.title)
#@pytest.mark.parametrize("item",[('iphone'),('oppo'),('redmi')])
@pytest.mark.regression
@pytest.mark.parametrize("item,expected_result",[('iphone','Amazon.in : iphone'),('oppo','Amazon.in : oppo'),('redmi','Amazon.in : redmi')])
def test_searchproduct(item,expected_result):
    driver.get("https://www.amazon.in/")
    driver.find_element(By.ID,'twotabsearchtextbox').send_keys(item)
    driver.find_element(By.ID,'nav-search-submit-button').click()
    actual_title=driver.title
   #if item in actual_title:
        #print("test is pass")
    #else:
        #print("test is fail")
    assert actual_title == expected_result,"failed due to mismatch of title"