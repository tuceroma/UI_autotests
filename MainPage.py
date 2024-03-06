from BaseApp import BasePage
from selenium.webdriver.common.by import By

class MainLocators:
    LOCATOR_MAIN = (By.CSS_SELECTOR, "h3.uk-card-title")
    LOCATOR_USERS = (By.ID, "menuUsersOpener")
    LOCATOR_USERS_ADD_USER = (By.ID, "menuUserAdd")
    LOCATOR_USERS_TABLE = (By.ID, "menuUsers")
    LOCATOR_AUTHORIZATION = (By.ID, "menuAuth")
    LOCATOR_OPTIONS = (By.ID, "menuMore")

class MainMethods(BasePage):
    def check_main_title(self):
        return self.find_element(MainLocators.LOCATOR_MAIN)

    def transfer_add_user_page(self):
        menu_users = self.find_element(MainLocators.LOCATOR_USERS).click()
        return self.find_element(MainLocators.LOCATOR_USERS_ADD_USER).click()

    def transfer_authorization_page(self):
        return self.find_element(MainLocators.LOCATOR_AUTHORIZATION).click()

    def transfer_table_page(self):
        menu_users = self.find_element(MainLocators.LOCATOR_USERS).click()
        return self.find_element(MainLocators.LOCATOR_USERS_TABLE).click()

    def transfer_options_page(self):
        return self.find_element(MainLocators.LOCATOR_OPTIONS).click()
