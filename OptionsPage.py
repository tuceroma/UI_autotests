from BaseApp import BasePage
from selenium.webdriver.common.by import By

class OptionsLocators:
    LOCATOR_OPTION = (By.CSS_SELECTOR, "h3.uk-card-title")

class OptionsMethods(BasePage):
    def check_options_page(self):
        return self.find_element(OptionsLocators.LOCATOR_OPTION)
