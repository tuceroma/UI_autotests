from BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class AddUserLocators:
    LOCATOR_ADD_EMAIL_FIELD = (By.ID, "dataEmail")
    LOCATOR_ADD_PASSWORD_FIELD = (By.ID, "dataPassword")
    LOCATOR_ADD_NAME_FIELD = (By.ID, "dataName")
    LOCATOR_SELECT_GENDER_FIELD = (By.ID, "dataGender")
    LOCATOR_SELECT_OPTION_RADIO1 = (By.ID, "dataSelect11")
    LOCATOR_SELECT_OPTION_RADIO2 = (By.ID, "dataSelect12")
    LOCATOR_SELECT_CHECKBOX1 = (By.ID, "dataSelect21")
    LOCATOR_SELECT_CHECKBOX2 = (By.ID, "dataSelect22")
    LOCATOR_SELECT_CHECKBOX3 = (By.ID, "dataSelect23")
    LOCATOR_ENTER_ADD_BUTTON = (By.ID, "dataSend")
    LOCATOR_ADD_USER_PAGE = (By.CSS_SELECTOR, ".uk-legend")
    LOCATOR_SUCCESS = (By.CSS_SELECTOR, "div.uk-modal-body")
    LOCATOR_ERROR_FORMAT_EMAIL = (By.ID, "emailFormatError")
    LOCATOR_BUTTON_OK = (By.CSS_SELECTOR, "button.uk-button.uk-button-primary.uk-modal-close")
    LOCATOR_LENGTH_ERROR = (By.CSS_SELECTOR, "div.uk-modal-body")
    LOCATOR_ERROR_NAME = (By.ID, "blankNameError")
    LOCATOR_ERROR_PASSWORD = (By.ID, "blankPasswordError")
    LOCATOR_AUTHORIZATION = (By.ID, "menuAuth")


class AddUserMethods(BasePage):

    def check_error_name(self):
        return self.find_element(AddUserLocators.LOCATOR_ERROR_NAME)

    def check_error_password(self):
        return self.find_element(AddUserLocators.LOCATOR_ERROR_PASSWORD)

    def check_add_user_page(self):
        return self.find_element(AddUserLocators.LOCATOR_ADD_USER_PAGE)

    def add_login(self, login):
        add_login = self.find_element(AddUserLocators.LOCATOR_ADD_EMAIL_FIELD).send_keys(login)
        return add_login

    def add_password(self, password):
        add_password = self.find_element(AddUserLocators.LOCATOR_ADD_PASSWORD_FIELD).send_keys(password)
        return add_password

    def add_name(self, name):
        add_name = self.find_element(AddUserLocators.LOCATOR_ADD_NAME_FIELD).send_keys(name)
        return add_name

    def select_gender(self, gender):
        dropdown = self.find_element(AddUserLocators.LOCATOR_SELECT_GENDER_FIELD)
        select_gender = Select(dropdown)
        return select_gender.select_by_visible_text(gender)

    def select_option(self, option):
        if(option == "Вариант 1.1"):
            select1 = self.find_element(AddUserLocators.LOCATOR_SELECT_OPTION_RADIO1)
            if(select1.is_selected() is False):
                return select1.click()
        if(option == "Вариант 1.2"):
            select2 = self.find_element(AddUserLocators.LOCATOR_SELECT_OPTION_RADIO2)
            if (select2.is_selected() is False):
                return select2.click()

    def select_checkbox(self, d):
        dict_checkbox = {"checkbox1": AddUserLocators.LOCATOR_SELECT_CHECKBOX1, "checkbox2": AddUserLocators.LOCATOR_SELECT_CHECKBOX2, "checkbox3": AddUserLocators.LOCATOR_SELECT_CHECKBOX3}
        for key, value in d.items():
            check = self.find_element(dict_checkbox[key])
            if(value == "вкл" and check.is_selected() is False):
                check.click()
            if (value == "выкл" and check.is_selected()):
                check.click()

    def click_on_the_enter_button(self):
        return self.find_element(AddUserLocators.LOCATOR_ENTER_ADD_BUTTON).click()

    def check_success(self):
        return self.find_element(AddUserLocators.LOCATOR_SUCCESS)

    def check_error_format_email(self):
        return self.find_element(AddUserLocators.LOCATOR_ERROR_FORMAT_EMAIL)

    def fast_add_user(self, email, password, name):
        self.add_login(email)
        self.add_password(password)
        self.add_name(name)
        return self.click_on_the_enter_button()

    def click_on_the_button_ok(self):
        return self.find_element(AddUserLocators.LOCATOR_BUTTON_OK).click()

    def check_length_error(self):
        return self.find_element(AddUserLocators.LOCATOR_LENGTH_ERROR)

    def transfer_authorization_page(self):
        return self.find_element(AddUserLocators.LOCATOR_AUTHORIZATION).click()