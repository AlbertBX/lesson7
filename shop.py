import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Shop:
    def __init__(self, driver): 
        self.driver = driver

    def user_name (self,query):
        self.driver.find_element(By.ID, 'user-name').send_keys(query)

    def password(self, query):
        self.driver.find_element(By.ID, 'password').send_keys(query)
        self.driver.find_element(By.ID, 'login-button').click()
    def add_to_cart(self):
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()

    def shopping(self):
        self.driver.find_element(By.ID, 'shopping_cart_container').click()
        self.driver.find_element(By.ID, 'checkout').click()

    def first_name(self, query):
        self.driver.find_element(By.ID, 'first-name').send_keys(query)
    
    def last_name(self, query):
        self.driver.find_element(By.ID, 'last-name').send_keys(query)
    
    def postal_code(self, query):
        self.driver.find_element(By.ID, 'postal-code').send_keys(query)
        self.driver.find_element(By.ID, 'continue').click()

    def get_search_result(self):
        self.driver.find_element(By.CSS_SELECTOR, 'div[class="summary_total_label"]').text.print(self)
      
   