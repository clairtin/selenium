import time
from pages.p_login import LoginPage

def test_success_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    p_login = LoginPage(driver)

    p_login.enter_username("tomsmith")
    p_login.enter_password("winteriscomming")
    p_login.click_login()

    time.sleep(2) 
    assert "all good" in driver.title

def test_unsuccess_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    p_login = LoginPage(driver)

    p_login.enter_username("wrong_user")
    p_login.enter_password("wrong_pass")
    p_login.click_login()

    time.sleep(2)  
    message = p_login.get_flash_message()
    assert "username is invalid" in message
