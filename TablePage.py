from BaseApp import BasePage
from selenium.webdriver.common.by import By

class TableLocators:
    LOCATOR_TABLE = (By.ID, "addUser")
    LOCATOR_ADD_USER_BUTTON = (By.ID, "addUser")

class TableMethods(BasePage):
    def check_table_page(self):
        return self.find_element(TableLocators.LOCATOR_TABLE)

    def transfer_add_user_page(self):
        return self.find_element(TableLocators.LOCATOR_ADD_USER_BUTTON).click()

