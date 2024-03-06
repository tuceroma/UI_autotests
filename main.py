from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('http://149.255.118.78:7080')
    yield driver
    driver.close()

def test_1(driver):
    login = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.ID, "loginEmail"))).send_keys('test@protei.ru')

    password = driver.find_element(by=By.ID, value=('loginPassword')).send_keys('test')

    enter = driver.find_element(by=By.ID, value=('authButton')).click()
    main_title = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.TAG_NAME, "h3")))
    assert True
    assert main_title.is_displayed()
    assert main_title.get_attribute("class") == "uk-card-title"
    assert main_title.text == "Добро пожаловать!"
