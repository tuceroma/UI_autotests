from AuthorizationPage import AuthorizationMethods
from MainPage import MainMethods
from AddUserPage import AddUserMethods
from TablePage import TableMethods
from OptionsPage import OptionsMethods


def test_authorization1_1(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver).check_main_title()
    assert main_title.is_displayed() and main_title.text == "Добро пожаловать!"

def test_authorization2_2(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("ro@mail.ru", "12345")
    assert authorization_page.check_error().text == "Неверный E-Mail или пароль"

def test_authorization3_3(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.click_on_the_enter_button()
    assert authorization_page.check_error().text == "Неверный формат E-Mail"

def test_authorization4_4(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "12345")
    assert authorization_page.check_error().text == "Неверный E-Mail или пароль"

def test_authorization5_5(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@mail.ru", "test")
    assert authorization_page.check_error().text == "Неверный E-Mail или пароль"

def test_authorization6_6(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.enter_password("test")
    authorization_page.click_on_the_enter_button()
    assert authorization_page.check_error().text == "Неверный формат E-Mail"

def test_authorization7_7(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.enter_login("test@protei.ru")
    authorization_page.click_on_the_enter_button()
    assert authorization_page.check_error().text == "Неверный E-Mail или пароль"

def test_authorization8_8(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.enter_login("test")
    authorization_page.enter_password("test@protei.ru")
    authorization_page.click_on_the_enter_button()
    assert authorization_page.check_error().text == "Неверный формат E-Mail"

def test_authorization9_9(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.enter_login("""“♣” , “”‘~!@#$%^&*()?>,./\<][ /*<!–”", “${code}”;–>""")
    authorization_page.enter_password("test")
    authorization_page.click_on_the_enter_button()
    assert authorization_page.check_error().text == "Неверный E-Mail или пароль"

def test_authorization10_10(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.enter_login("     test@protei.ru")
    authorization_page.enter_password("test")
    authorization_page.click_on_the_enter_button()
    assert authorization_page.check_error().text == "Неверный E-Mail или пароль"

def test_authorization11_11(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.enter_login("test@protei.ru")
    authorization_page.enter_password("     test")
    authorization_page.click_on_the_enter_button()
    assert authorization_page.check_error().text == "Неверный E-Mail или пароль"

def test_authorization12_12(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.enter_login("              ")
    authorization_page.enter_password("test")
    authorization_page.click_on_the_enter_button()
    assert authorization_page.check_error().text == "Неверный формат E-Mail"

def test_authorization13_13(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.enter_login("test@protei.ru")
    authorization_page.enter_password("Test")
    authorization_page.click_on_the_enter_button()
    assert authorization_page.check_error().text == "Неверный E-Mail или пароль"

def test_authorization14_14(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.enter_login("Test@protei.ru")
    authorization_page.enter_password("test")
    authorization_page.click_on_the_enter_button()
    assert authorization_page.check_error().text == "Неверный E-Mail или пароль"

def test_authorization15_15(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.fast_add_user("roma@mail.ru", "123", "Roma")
    add_user.click_on_the_button_ok()
    add_user.transfer_authorization_page()
    authorization_page.authorization_full("roma@mail.ru", "123")
    main_title = MainMethods(driver).check_main_title()
    assert main_title.is_displayed() and main_title.text == "Добро пожаловать!"

def test_transfer_add_user_page_16(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_page = MainMethods(driver)
    main_page.transfer_add_user_page()
    add_user_page = AddUserMethods(driver).check_add_user_page()
    assert add_user_page.is_displayed() and add_user_page.text == "Добавление пользователя"

def test_transfer_authorization_page_17(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_page = MainMethods(driver)
    main_page.transfer_authorization_page()
    auth = authorization_page.check_authorization_page()
    assert auth.is_displayed() and auth.text == "Привет с демо-сайта для автотестов!"

def test_transfer_table_page_18(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_page = MainMethods(driver)
    main_page.transfer_table_page()
    table_page = TableMethods(driver).check_table_page()
    assert table_page.is_displayed() and table_page.text == "ДОБАВИТЬ ПОЛЬЗОВАТЕЛЯ"

def test_transfer_options_page_19(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_page = MainMethods(driver)
    main_page.transfer_options_page()
    options_page = OptionsMethods(driver).check_options_page()
    assert options_page.is_displayed() and options_page.text == "НТЦ ПРОТЕЙ"

def test_transfer_add_user_page_from_table_20(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_page = MainMethods(driver)
    main_page.transfer_table_page()
    table_page = TableMethods(driver)
    table_page.transfer_add_user_page()
    add_user_page = AddUserMethods(driver).check_add_user_page()
    assert add_user_page.is_displayed() and add_user_page.text == "Добавление пользователя"

def test_add1_21(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.add_login("roma@mail.ru")
    add_user.add_password("123")
    add_user.add_name("Roma")
    add_user.select_gender("Мужской")
    add_user.select_option("Вариант 1.1")
    add_user.select_checkbox({"checkbox1": "вкл", "checkbox2": "выкл", "checkbox3": "выкл"})
    add_user.click_on_the_enter_button()
    checkk = add_user.check_success()
    assert checkk.is_displayed() and checkk.text == "Данные добавлены."

def test_add2_22(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.click_on_the_enter_button()
    checkk = add_user.check_error_format_email()
    assert checkk.is_displayed() and checkk.text == "Неверный формат E-Mail"

def test_add3_23(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.fast_add_user("roma@mail.ru", "123", "Roma")
    add_user.click_on_the_button_ok()
    add_user.fast_add_user("roma@mail.ru", "123", "Roma")
    checkk = add_user.check_success()
    assert checkk.text != "Данные добавлены."

def test_add4_24(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.fast_add_user("roma    @mail.ru", "123", "Roma")
    checkk = add_user.check_success()
    assert checkk.text != "Данные добавлены."

def test_add5_25(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.fast_add_user("@mail.ru", "123", "Roma")
    checkk = add_user.check_error_format_email()
    assert checkk.is_displayed() and checkk.text == "Неверный формат E-Mail"

def test_add6_26(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.fast_add_user("roma@", "123", "Roma")
    checkk = add_user.check_error_format_email()
    assert checkk.is_displayed() and checkk.text == "Неверный формат E-Mail"

def test_add7_27(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.fast_add_user("romcsdsssssssssssssssssssssssssssssssssssssssssdscdsscdcsddssddddddddssda@mail.ru", "123", "Roma")
    checkk = add_user.check_length_error()
    assert checkk.is_displayed() and checkk.text == "ОШИБКА! FAIL"

def test_add8_28(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.fast_add_user("romamail.ru", "123", "Roma")
    checkk = add_user.check_error_format_email()
    assert checkk.is_displayed() and checkk.text == "Неверный формат E-Mail"

def test_add9_29(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.fast_add_user("!#$%&'*+-/=?^`{|}~@mail.ru", "123", "Roma")
    checkk = add_user.check_error_format_email()
    assert checkk.is_displayed() and checkk.text == "Неверный формат E-Mail"

def test_add10_30(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.fast_add_user("roma@mail.ru", "12dsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssddvdfvdfdfdfdffddfdfdffvdvdfdfdfdf3", "Roma")
    checkk = add_user.check_length_error()
    assert checkk.is_displayed() and checkk.text == "ОШИБКА! FAIL"

def test_add11_31(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.fast_add_user("roma@mail.ru", "123", "Romaваааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааавааааааааааааааааааааааааааааа")
    checkk = add_user.check_length_error()
    assert checkk.is_displayed() and checkk.text == "ОШИБКА! FAIL"


def test_add12_pairwise1_32(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.add_password("12dsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssddvdfvdfdfdfdffddfdfdffvdvdfdfdfdf3")
    add_user.add_name("Romaваааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааавааааааааааааааааааааааааааааа")
    add_user.select_gender("Женский")
    add_user.select_option("Вариант 1.2")
    add_user.select_checkbox({"checkbox1": "выкл", "checkbox2": "выкл", "checkbox3": "выкл"})
    add_user.click_on_the_enter_button()
    checkk = add_user.check_error_format_email()
    assert checkk.is_displayed() and checkk.text == "Неверный формат E-Mail"

def test_add13_pairwise2_33(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.add_password("123")
    add_user.select_gender("Мужской")
    add_user.select_option("Вариант 1.1")
    add_user.select_checkbox({"checkbox1": "вкл", "checkbox2": "вкл", "checkbox3": "вкл"})
    add_user.click_on_the_enter_button()
    checkk = add_user.check_error_format_email()
    assert checkk.is_displayed() and checkk.text == "Неверный формат E-Mail"

def test_add14_pairwise_3_34(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.add_password("12dsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssddvdfvdfdfdfdffddfdfdffvdvdfdfdfdf3")
    add_user.add_name("Roma")
    add_user.select_gender("Женский")
    add_user.select_option("Вариант 1.2")
    add_user.select_checkbox({"checkbox1": "выкл", "checkbox2": "выкл", "checkbox3": "выкл"})
    add_user.click_on_the_enter_button()
    checkk = add_user.check_error_format_email()
    assert checkk.is_displayed() and checkk.text == "Неверный формат E-Mail"

def test_add15_pairwise4_35(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.add_login("roma@mail.ru")
    add_user.add_password("12dsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssddvdfvdfdfdfdffddfdfdffvdvdfdfdfdf3")
    add_user.select_gender("Женский")
    add_user.select_option("Вариант 1.1")
    add_user.select_checkbox({"checkbox1": "выкл", "checkbox2": "вкл", "checkbox3": "выкл"})
    add_user.click_on_the_enter_button()
    checkk = add_user.check_error_name()
    assert checkk.is_displayed() and checkk.text == "Поле Имя не может быть пустым"

def test_add16_pairwise5_36(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.add_login("roma@mail.ru")
    add_user.add_password("123")
    add_user.add_name("Roma")
    add_user.select_gender("Мужской")
    add_user.select_option("Вариант 1.2")
    add_user.select_checkbox({"checkbox1": "вкл", "checkbox2": "выкл", "checkbox3": "вкл"})
    add_user.click_on_the_enter_button()
    checkk = add_user.check_success()
    assert checkk.is_displayed() and checkk.text == "Данные добавлены."

def test_add17_pairwise6_37(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.add_login("roma@mail.ru")
    add_user.add_password("12dsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssddvdfvdfdfdfdffddfdfdffvdvdfdfdfdf3")
    add_user.add_name("12dsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssddvdfvdfdfdfdffddfdfdffvdvdfdfdfdf3")
    add_user.select_gender("Женский")
    add_user.select_option("Вариант 1.1")
    add_user.select_checkbox({"checkbox1": "выкл", "checkbox2": "вкл", "checkbox3": "выкл"})
    add_user.click_on_the_enter_button()
    checkk = add_user.check_length_error()
    assert checkk.is_displayed() and checkk.text == "ОШИБКА! FAIL"

def test_add18_pairwise7_38(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.add_login("roma@mail.ru")
    add_user.select_gender("Мужской")
    add_user.select_option("Вариант 1.1")
    add_user.select_checkbox({"checkbox1": "вкл", "checkbox2": "вкл", "checkbox3": "вкл"})
    add_user.click_on_the_enter_button()
    checkk = add_user.check_error_name()
    assert checkk.is_displayed() and checkk.text == "Поле Имя не может быть пустым"

def test_add19_pairwise8_39(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.add_login("roma")
    add_user.add_password("12dsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssddvdfvdfdfdfdffddfdfdffvdvdfdfdfdf3")
    add_user.add_name("Roma")
    add_user.select_gender("Мужской")
    add_user.select_option("Вариант 1.2")
    add_user.select_checkbox({"checkbox1": "вкл", "checkbox2": "выкл", "checkbox3": "вкл"})
    add_user.click_on_the_enter_button()
    checkk = add_user.check_error_format_email()
    assert checkk.is_displayed() and checkk.text == "Неверный формат E-Mail"

def test_add20_pairwise9_40(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.add_login("roma")
    add_user.add_name("12dsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssddvdfvdfdfdfdffddfdfdffvdvdfdfdfdf3")
    add_user.select_gender("Женский")
    add_user.select_option("Вариант 1.2")
    add_user.select_checkbox({"checkbox1": "выкл", "checkbox2": "выкл", "checkbox3": "выкл"})
    add_user.click_on_the_enter_button()
    checkk = add_user.check_error_format_email()
    assert checkk.is_displayed() and checkk.text == "Неверный формат E-Mail"

def test_add21_pairwise10_41(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.add_login("roma")
    add_user.add_password("123")
    add_user.select_gender("Мужской")
    add_user.select_option("Вариант 1.1")
    add_user.select_checkbox({"checkbox1": "вкл", "checkbox2": "вкл", "checkbox3": "вкл"})
    add_user.click_on_the_enter_button()
    checkk = add_user.check_error_format_email()
    assert checkk.is_displayed() and checkk.text == "Неверный формат E-Mail"

def test_add22_pairwise11_42(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.add_login("roma")
    add_user.add_password("123")
    add_user.add_name("12dsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssddvdfvdfdfdfdffddfdfdffvdvdfdfdfdf3")
    add_user.select_gender("Мужской")
    add_user.select_option("Вариант 1.1")
    add_user.select_checkbox({"checkbox1": "вкл", "checkbox2": "вкл", "checkbox3": "вкл"})
    add_user.click_on_the_enter_button()
    checkk = add_user.check_error_format_email()
    assert checkk.is_displayed() and checkk.text == "Неверный формат E-Mail"

def test_add23_pairwise12_43(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.add_login("roma")
    add_user.add_password("12dsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssddvdfvdfdfdfdffddfdfdffvdvdfdfdfdf3")
    add_user.select_gender("Женский")
    add_user.select_option("Вариант 1.2")
    add_user.select_checkbox({"checkbox1": "выкл", "checkbox2": "выкл", "checkbox3": "выкл"})
    add_user.click_on_the_enter_button()
    checkk = add_user.check_error_format_email()
    assert checkk.is_displayed() and checkk.text == "Неверный формат E-Mail"

def test_add24_pairwise13_44(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.add_login("roma")
    add_user.add_name("Roma")
    add_user.select_gender("Мужской")
    add_user.select_option("Вариант 1.1")
    add_user.select_checkbox({"checkbox1": "вкл", "checkbox2": "вкл", "checkbox3": "вкл"})
    add_user.click_on_the_enter_button()
    checkk = add_user.check_error_format_email()
    assert checkk.is_displayed() and checkk.text == "Неверный формат E-Mail"

def test_add25_pairwise14_45(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.add_login("roma")
    add_user.add_password("123")
    add_user.add_name("12dsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssddvdfvdfdfdfdffddfdfdffvdvdfdfdfdf3")
    add_user.select_gender("Женский")
    add_user.select_option("Вариант 1.2")
    add_user.select_checkbox({"checkbox1": "выкл", "checkbox2": "выкл", "checkbox3": "выкл"})
    add_user.click_on_the_enter_button()
    checkk = add_user.check_error_format_email()
    assert checkk.is_displayed() and checkk.text == "Неверный формат E-Mail"

def test_add26_pairwise15_46(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.select_gender("Женский")
    add_user.select_option("Вариант 1.1")
    add_user.select_checkbox({"checkbox1": "выкл", "checkbox2": "вкл", "checkbox3": "выкл"})
    add_user.click_on_the_enter_button()
    checkk = add_user.check_error_format_email()
    assert checkk.is_displayed() and checkk.text == "Неверный формат E-Mail"

def test_add27_pairwise16_47(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.add_password("123")
    add_user.add_name("Roma")
    add_user.select_gender("Мужской")
    add_user.select_option("Вариант 1.2")
    add_user.select_checkbox({"checkbox1": "вкл", "checkbox2": "выкл", "checkbox3": "вкл"})
    add_user.click_on_the_enter_button()
    checkk = add_user.check_error_format_email()
    assert checkk.is_displayed() and checkk.text == "Неверный формат E-Mail"

def test_add28_pairwise17_48(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.add_password("12dsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssddvdfvdfdfdfdffddfdfdffvdvdfdfdfdf3")
    add_user.add_name("12dsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssddvdfvdfdfdfdffddfdfdffvdvdfdfdfdf3")
    add_user.select_gender("Женский")
    add_user.select_option("Вариант 1.1")
    add_user.select_checkbox({"checkbox1": "выкл", "checkbox2": "вкл", "checkbox3": "выкл"})
    add_user.click_on_the_enter_button()
    checkk = add_user.check_error_format_email()
    assert checkk.is_displayed() and checkk.text == "Неверный формат E-Mail"

def test_add29_pairwise18_49(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.add_password("123")
    add_user.select_gender("Мужской")
    add_user.select_option("Вариант 1.2")
    add_user.select_checkbox({"checkbox1": "вкл", "checkbox2": "выкл", "checkbox3": "вкл"})
    add_user.click_on_the_enter_button()
    checkk = add_user.check_error_format_email()
    assert checkk.is_displayed() and checkk.text == "Неверный формат E-Mail"

def test_add30_pairwise19_50(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.add_password("12dsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssddvdfvdfdfdfdffddfdfdffvdvdfdfdfdf3")
    add_user.add_name("Roma")
    add_user.select_gender("Женский")
    add_user.select_option("Вариант 1.1")
    add_user.select_checkbox({"checkbox1": "выкл", "checkbox2": "вкл", "checkbox3": "выкл"})
    add_user.click_on_the_enter_button()
    checkk = add_user.check_error_format_email()
    assert checkk.is_displayed() and checkk.text == "Неверный формат E-Mail"

def test_add31_pairwise20_51(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.add_name("12dsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssddvdfvdfdfdfdffddfdfdffvdvdfdfdfdf3")
    add_user.select_gender("Мужской")
    add_user.select_option("Вариант 1.2")
    add_user.select_checkbox({"checkbox1": "вкл", "checkbox2": "выкл", "checkbox3": "вкл"})
    add_user.click_on_the_enter_button()
    checkk = add_user.check_error_format_email()
    assert checkk.is_displayed() and checkk.text == "Неверный формат E-Mail"

def test_add32_pairwise21_52(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.add_password("123")
    add_user.add_name("Roma")
    add_user.select_gender("Женский")
    add_user.select_option("Вариант 1.1")
    add_user.select_checkbox({"checkbox1": "выкл", "checkbox2": "вкл", "checkbox3": "выкл"})
    add_user.click_on_the_enter_button()
    checkk = add_user.check_error_format_email()
    assert checkk.is_displayed() and checkk.text == "Неверный формат E-Mail"

def test_add33_pairwise22_53(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.add_password("12dsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssddvdfvdfdfdfdffddfdfdffvdvdfdfdfdf3")
    add_user.add_name("12dsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssddvdfvdfdfdfdffddfdfdffvdvdfdfdfdf3")
    add_user.select_gender("Мужской")
    add_user.select_option("Вариант 1.2")
    add_user.select_checkbox({"checkbox1": "вкл", "checkbox2": "выкл", "checkbox3": "вкл"})
    add_user.click_on_the_enter_button()
    checkk = add_user.check_error_format_email()
    assert checkk.is_displayed() and checkk.text == "Неверный формат E-Mail"

def test_add34_pairwise23_54(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.add_login("roma@mail.ru")
    add_user.add_password("123")
    add_user.add_name("12dsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssddvdfvdfdfdfdffddfdfdffvdvdfdfdfdf3")
    add_user.select_gender("Мужской")
    add_user.select_option("Вариант 1.1")
    add_user.select_checkbox({"checkbox1": "вкл", "checkbox2": "вкл", "checkbox3": "вкл"})
    add_user.click_on_the_enter_button()
    checkk = add_user.check_length_error()
    assert checkk.is_displayed() and checkk.text == "ОШИБКА! FAIL"

def test_add35_pairwise24_55(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.add_login("roma@mail.ru")
    add_user.add_password("12dsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssddvdfvdfdfdfdffddfdfdffvdvdfdfdfdf3")
    add_user.select_gender("Женский")
    add_user.select_option("Вариант 1.2")
    add_user.select_checkbox({"checkbox1": "выкл", "checkbox2": "выкл", "checkbox3": "выкл"})
    add_user.click_on_the_enter_button()
    checkk = add_user.check_error_name()
    assert checkk.is_displayed() and checkk.text == "Поле Имя не может быть пустым"

def test_add36_pairwise25_56(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.add_login("roma@mail.ru")
    add_user.add_name("Roma")
    add_user.select_gender("Мужской")
    add_user.select_option("Вариант 1.1")
    add_user.select_checkbox({"checkbox1": "вкл", "checkbox2": "вкл", "checkbox3": "вкл"})
    add_user.click_on_the_enter_button()
    checkk = add_user.check_error_password()
    assert checkk.is_displayed() and checkk.text == "Поле Пароль не может быть пустым"

def test_add37_pairwise26_57(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.add_login("roma@mail.ru")
    add_user.add_password("123")
    add_user.add_name("12dsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssddvdfvdfdfdfdffddfdfdffvdvdfdfdfdf3")
    add_user.select_gender("Женский")
    add_user.select_option("Вариант 1.2")
    add_user.select_checkbox({"checkbox1": "выкл", "checkbox2": "выкл", "checkbox3": "выкл"})
    add_user.click_on_the_enter_button()
    checkk = add_user.check_length_error()
    assert checkk.is_displayed() and checkk.text == "ОШИБКА! FAIL"

def test_add38_pairwise27_58(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.add_login("roma@mail.ru")
    add_user.add_password("12dsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssddvdfvdfdfdfdffddfdfdffvdvdfdfdfdf3")
    add_user.select_gender("Мужской")
    add_user.select_option("Вариант 1.1")
    add_user.select_checkbox({"checkbox1": "вкл", "checkbox2": "вкл", "checkbox3": "вкл"})
    add_user.click_on_the_enter_button()
    checkk = add_user.check_error_name()
    assert checkk.is_displayed() and checkk.text == "Поле Имя не может быть пустым"

def test_add39_pairwise28_59(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.add_login("roma@mail.ru")
    add_user.add_name("Roma")
    add_user.select_gender("Женский")
    add_user.select_option("Вариант 1.2")
    add_user.select_checkbox({"checkbox1": "выкл", "checkbox2": "выкл", "checkbox3": "выкл"})
    add_user.click_on_the_enter_button()
    checkk = add_user.check_error_password()
    assert checkk.is_displayed() and checkk.text == "Поле Пароль не может быть пустым"

def test_add40_pairwise29_60(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.add_login("roma")
    add_user.add_name("12dsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssddvdfvdfdfdfdffddfdfdffvdvdfdfdfdf3")
    add_user.select_gender("Мужской")
    add_user.select_option("Вариант 1.2")
    add_user.select_checkbox({"checkbox1": "вкл", "checkbox2": "выкл", "checkbox3": "вкл"})
    add_user.click_on_the_enter_button()
    checkk = add_user.check_error_format_email()
    assert checkk.is_displayed() and checkk.text == "Неверный формат E-Mail"

def test_add41_pairwise30_61(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.add_login("roma")
    add_user.add_password("123")
    add_user.select_gender("Женский")
    add_user.select_option("Вариант 1.1")
    add_user.select_checkbox({"checkbox1": "выкл", "checkbox2": "вкл", "checkbox3": "выкл"})
    add_user.click_on_the_enter_button()
    checkk = add_user.check_error_format_email()
    assert checkk.is_displayed() and checkk.text == "Неверный формат E-Mail"

def test_add42_pairwise31_62(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.add_login("roma")
    add_user.add_password("12dsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssddvdfvdfdfdfdffddfdfdffvdvdfdfdfdf3")
    add_user.add_name("Roma")
    add_user.select_gender("Мужской")
    add_user.select_option("Вариант 1.2")
    add_user.select_checkbox({"checkbox1": "вкл", "checkbox2": "выкл", "checkbox3": "вкл"})
    add_user.click_on_the_enter_button()
    checkk = add_user.check_error_format_email()
    assert checkk.is_displayed() and checkk.text == "Неверный формат E-Mail"

def test_add43_pairwise32_63(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.add_login("roma")
    add_user.add_name("12dsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssddvdfvdfdfdfdffddfdfdffvdvdfdfdfdf3")
    add_user.select_gender("Женский")
    add_user.select_option("Вариант 1.1")
    add_user.select_checkbox({"checkbox1": "выкл", "checkbox2": "вкл", "checkbox3": "выкл"})
    add_user.click_on_the_enter_button()
    checkk = add_user.check_error_format_email()
    assert checkk.is_displayed() and checkk.text == "Неверный формат E-Mail"

def test_add44_pairwise33_64(driver):
    authorization_page = AuthorizationMethods(driver)
    authorization_page.go_to_site()
    authorization_page.authorization_full("test@protei.ru", "test")
    main_title = MainMethods(driver)
    main_title.transfer_add_user_page()
    add_user = AddUserMethods(driver)
    add_user.add_login("roma")
    add_user.add_password("123")
    add_user.select_gender("Мужской")
    add_user.select_option("Вариант 1.2")
    add_user.select_checkbox({"checkbox1": "вкл", "checkbox2": "выкл", "checkbox3": "вкл"})
    add_user.click_on_the_enter_button()
    checkk = add_user.check_error_format_email()
    assert checkk.is_displayed() and checkk.text == "Неверный формат E-Mail"