import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from shop import Shop
summa = "Total: $58.29"

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

def test_search (driver):
    page = Shop(driver)
    page.user_name("standard_user")
    page.password("secret_sauce")
    page.add_to_cart()
    page.shopping()
    page.first_name ("Хакимов")
    page.last_name ("Альберт")
    page.postal_code(453100)
    page.postal_code
    result=page.get_search_result
    
    assert result == summa
