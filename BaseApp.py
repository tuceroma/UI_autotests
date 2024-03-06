from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://149.255.118.78:7080"

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")

