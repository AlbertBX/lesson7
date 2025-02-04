import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from form import Forma

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    yield driver
    driver.quit()

def test_search (driver):
    page = Forma(driver)
    page.name ('Иван')
    page.surname ('Петров')
    page.address ('Ленина, 55-3')
    page.e_mail('test@skypro.com')
    page.phone('+7985899998787')
    page.city ('Москва')
    page.contry ('Россия')
    page.job_position ('QA')
    page.company ('Skypro')
    
    assert "danger" in driver.find_element(By.ID, "zip-code"
                                           ).get_attribute("class")

    fields = ['first-name', 'last-name', 'address', 'e-mail', 'phone', 'city',
              'country', 'job-position', 'company']

    for field in fields:
        assert "success" in driver.find_element(By.ID, field
                                                ).get_attribute("class")
        
    sleep(5)    
  