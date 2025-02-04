from time import sleep
from selenium.webdriver.common.by import By

class Forma:

    def __init__(self, driver): 
        self.driver = driver
                
    def name (self, query):
        self.driver.find_element(By.NAME, 'first-name').send_keys(query)
    def surname (self, query): 
        self.driver.find_element(By.NAME, 'last-name').send_keys(query)
    def address (self, query):
        self.driver.find_element(By.NAME, 'address').send_keys(query)
    def e_mail (self, query):
        self.driver.find_element(By.NAME, 'e-mail').send_keys(query)
    def phone (self, query):
        self.driver.find_element(By.NAME, 'phone').send_keys(query)
    def city (self, query):   
        self.driver.find_element(By.NAME, 'city').send_keys(query)
    def contry (self, query):
        self.driver.find_element(By.NAME, 'country').send_keys(query)
    def job_position (self, query): 
        self.driver.find_element(By.NAME, 'job-position').send_keys(query)
    def company (self, query):    
        self.driver.find_element(By.NAME, 'company').send_keys(query)
        
        self.driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-'
                                      'outline-primary mt-3"]').click()
      
        
        
        
       

    
