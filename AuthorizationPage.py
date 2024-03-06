from BaseApp import BasePage
from selenium.webdriver.common.by import By

class AuthorizationLocators:
    LOCATOR_LOGIN_FIELD = (By.ID, "loginEmail")
    LOCATOR_PASSWORD_FIELD = ((By.ID, "loginPassword"))
    LOCATOR_ENTER_BUTTON = (By.ID, "authButton")
    LOCATOR_ERROR = (By.CSS_SELECTOR, "div[id='authAlertsHolder'].uk-margin.uk-form-row")
    LOCATOR_AUTHORIZATION_TITLE = (By.CSS_SELECTOR, ".uk-legend")

class AuthorizationMethods(BasePage):

    def check_authorization_page(self):
        return self.find_element(AuthorizationLocators.LOCATOR_AUTHORIZATION_TITLE)

    def enter_login(self, login):
        login_field = self.find_element(AuthorizationLocators.LOCATOR_LOGIN_FIELD).send_keys(login)
        return login_field

    def enter_password(self, password):
        password_field = self.find_element(AuthorizationLocators.LOCATOR_PASSWORD_FIELD).send_keys(password)
        return password_field

    def click_on_the_enter_button(self):
        return self.find_element(AuthorizationLocators.LOCATOR_ENTER_BUTTON).click()

    def check_error(self):
        return self.find_element(AuthorizationLocators.LOCATOR_ERROR)

    def authorization_full(self, login, password):
        self.enter_login(login)
        self.enter_password(password)
        return self.click_on_the_enter_button()