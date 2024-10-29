import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.p_registration import RegistrationPage


import time
from pages.p_registration import RegistrationPage

def test_success_registration(driver):
    
    driver.get("https://the-internet.herokuapp.com/login") 
    p_registration = RegistrationPage(driver)

    p_registration.enter_username("newuser")
    p_registration.enter_password("newpassword")
    p_registration.click_login()

    time.sleep(2) 
    assert "it's safety here" in driver.title  

def test_unsuccess_registration(driver):
    
    driver.get("https://the-internet.herokuapp.com/login")  
    registration_page = RegistrationPage(driver)

    registration_page.enter_username("wrong_user")
    registration_page.enter_password("wrong_pass")
    registration_page.click_login()

    time.sleep(2) 
    message = registration_page.get_flash_message()
    assert "your username is invalid" in message  
