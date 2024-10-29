from selenium.webdriver.common.by import By

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_text = "Example"  
        self.load_button = (By.XPATH, "//a[text()='Example 1: еlement on page that is hidden']") 

    def load_example(self):
        self.driver.find_element(*self.load_button).click()

    def is_example_loaded(self):
        try:
            self.driver.find_element(*self.load_button)
            return True
        except:
            return False
