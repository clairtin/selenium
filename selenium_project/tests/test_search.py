from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


BASE_URL = "https://the-internet.herokuapp.com"

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

def test_search_with_results(setup):
   
    driver = setup
    
    search_input = driver.find_element(By.ID, "search_input") 
    search_input.send_keys("valid_keyword") 
    search_button = driver.find_element(By.ID, "search_button") 
    search_button.click()
    
    
    results = driver.find_elements(By.SOME_NAME, "result_item") 
    assert len(results) > 0, "Результаты поиска должны отображаться при наличии совпадений"

def test_search_no_results(setup):
    
    driver = setup
   
    search_input = driver.find_element(By.ID, "search_input") 
    search_input.send_keys("nonexistent_keyword") 
    search_button = driver.find_element(By.ID, "search_button")  
    search_button.click()
    
   
    no_results_message = driver.find_element(By.ID, "no_results_message") 
    assert no_results_message.is_displayed(), "отсутствии результатов"


