import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from calc import Calculator

operations = ['7','+','8','-']
text = '15'

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()

def test_search (driver):
    main_calc = Calculator(driver)
    main_calc.send('5')
    main_calc.get_operations()
    main_calc.get_search_result
    result=main_calc.get_search_result()
    assert result == text
