import pytest
from selenium.webdriver.support.wait import WebDriverWait
from data import users
from data.locators import *
from time import sleep
import allure
from selenium.webdriver.common.by import By
from pages import base
from selenium import webdriver
import random
from selenium.webdriver.support.ui import WebDriverWait
from flaky import flaky
import datetime
import cv2
import numpy as np
import os
from allure_commons._allure import attach
from allure_commons.types import AttachmentType

time_to_present_result = 0
time_to_enter_capcha = 0


@allure.feature("Authentification")  # Авторизация существующим пользователем
@flaky(max_runs=3)
@pytest.mark.parametrize('user', ["valid_login_user"])
def test_log_in_with_valid_user(app, user):
    app.main_page.login_ok(user)
    # if is_account_blocked() is True:
    #     account_unblock(user)
    sleep(time_to_present_result)
    app.make_screenshot()
    assert app.main_page.get_username() == users.get_user(user)['login']


@allure.feature(
    "Authentification")  # Авторизация существующим пользователем и существующим паролем, но от другого пользовател
@flaky(max_runs=3)
@pytest.mark.parametrize('user', ["invalid_login_user"])
def test_log_in_with_invalid_user(app, user):
    app.main_page.login_err(user)
    sleep(time_to_present_result)
    app.make_screenshot()
    assert app.main_page.is_unique_element_displayed(*getattr(MainPageLocators, users.get_user(user)["message"]))


@allure.feature("Authentification")  # Регистрация нового пользователя с существующим е-мэйлом
@flaky(max_runs=3)
@pytest.mark.parametrize('user', ["user_reg_exist_email"])
def test_sign_up_with_existed_mail(app, user):
    app.main_page.signup(user)
    sleep(time_to_present_result)
    sleep(time_to_enter_capcha)
    app.make_screenshot()
    assert app.main_page.is_unique_element_displayed(*getattr(MainPageLocators, users.get_user(user)["message"]))


@allure.feature("Authentification")  # Регистрация нового пользователя с существующим логином
@flaky(max_runs=3)
@pytest.mark.parametrize('user', ["user_reg_exist_login"])
def test_sign_up_with_existed_login(app, user):
    app.main_page.signup(user)
    sleep(time_to_present_result)
    sleep(time_to_enter_capcha)
    app.make_screenshot()
    assert app.main_page.is_unique_element_displayed(*getattr(MainPageLocators, users.get_user(user)["message"]))


@allure.feature(
    "Authentification")  # Регистрация нового пользователя с невалидными значениями - одно из полей незаполнено
@flaky(max_runs=3)
@pytest.mark.parametrize('user',
                         ["invalid_reg_user_1", "invalid_reg_user_2", "invalid_reg_user_3", "invalid_reg_user_4"])
def test_sign_up_with_invalid_user(app, user):
    app.main_page.signup(user)
    sleep(time_to_present_result)
    sleep(time_to_enter_capcha)
    app.make_screenshot()
    assert app.main_page.is_unique_element_displayed(*getattr(MainPageLocators, users.get_user(user)["message"]))


@allure.feature("Authentification")  # Регистрация нового пользователя с невалидными значениями - логин кириллицей
@flaky(max_runs=3)
@pytest.mark.parametrize('user',
                         ["invalid_reg_user_5"])
def test_sign_up_with_invalid_login(app, user):
    app.main_page.click_signup_button()
    app.main_page.enter_email(user)
    app.main_page.enter_login_2(user)
    sleep(time_to_present_result)
    app.make_screenshot()
    assert app.main_page.is_unique_element_displayed(*getattr(MainPageLocators, users.get_user(user)["message"]))

    app.main_page.enter_password_2(user)
    sleep(time_to_enter_capcha)
    app.main_page.enter_captcha_2(user)
    app.main_page.click_submit_button_2()
    sleep(time_to_present_result)
    app.make_screenshot()
    assert app.main_page.is_unique_element_displayed(*getattr(MainPageLocators, users.get_user(user)["message_add"]))


@allure.feature("Authentification")  # Регистрация нового пользователя с валидными значениями
@flaky(max_runs=3)
@pytest.mark.parametrize('user', ["valid_reg_user"])
def test_sign_up_with_valid_user(app, user):
    static_user = app.main_page.signup(user)
    print("*******************Создан пользователь - ", static_user)
    user_email = static_user['email']
    user_login = static_user['login']
    browser = app.main_page.driver
    app.make_screenshot()
    assert app.main_page.is_unique_element_displayed(*getattr(MainPageLocators, static_user["message"]))

    app.main_page.driver.get("http://*******.*******.online:8080/roundcube/")
    app.main_page.find_displayed_element(By.ID, "rcmloginuser").send_keys("catchall")
    app.main_page.find_displayed_element(By.ID, "rcmloginpwd").send_keys("CATCHALLcatchallPD123")
    app.main_page.find_displayed_element(By.ID, "rcmloginhost").send_keys("localhost")
    app.main_page.find_displayed_element(By.ID, "rcmloginsubmit").click()
    approve_reg = False
    count_time = 0
    while approve_reg == False and count_time < 60:
        # Выбираем самое первое письмо в Инбокс списке
        app.main_page.find_displayed_element(By.XPATH,
                                             "//*[@id='messagelist']/tbody//*[contains(@id, 'rcmrow')][1]").click()
        browser.find_element_by_xpath("//*[@id='messagelist']/tbody//*[contains(@id, 'rcmrow')][1]").click()
        # Если в письме нет поля с мэйлом - кликаем на Inbox
        if len(browser.find_elements(*MainPageLocators.LETTER_EMAIL)) <= 0:
            app.main_page.find_displayed_element(By.XPATH, "//*[@id='rcmliSU5CT1g']/a").click()  # Press Inbox
            sleep(1)
            count_time += 1
        else:  # Иначе проверяем мэйл - и если он совпадает с искомым - выходим из цикла
            login = app.main_page.find_displayed_element(*MainPageLocators.LETTER_EMAIL).text
            if login == user_email:  # Если логин = тексту в письме - кликаем по ссылке переходим к новому окну из письма в покердом
                # print("*******************Ссылка на активацию аккаунта - ", browser.find_elements_by_xpath("//*[@id='message-htmlpart1']/div/div/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/p[5]/a")[0].text)
                app.main_page.find_displayed_element(*MainPageLocators.LETTER_LINK).click()
                # wait to make sure there are two windows open
                WebDriverWait(browser, 10).until(lambda d: len(d.window_handles) == 2)
                # switch windows
                browser.switch_to_window(browser.window_handles[1])
                # wait to make sure the new window is loaded
                WebDriverWait(browser, 10).until(lambda d: d.title != "")
                approve_reg = True

            else:  # Иначе выходим из письма и ждем (1 секунду) появления новго пиcьма
                app.main_page.find_displayed_element(By.XPATH, "//*[@id='rcmliSU5CT1g']/a").click()  # Press Inbox
                sleep(1)
                count_time += 1

    if approve_reg is False:
        test_result = False

    elif app.main_page.get_username() != user_login:
        test_result = False

    elif app.main_page.get_username() == user_login:
        test_result = True
    sleep(time_to_present_result)
    app.make_screenshot()
    assert test_result


@allure.feature("Friends")  # Проверка захода в Friends c зарег пользователем и без
@flaky(max_runs=3)
@pytest.mark.parametrize('user', ["without_user", "valid_login_user"])
def test_check_friends_page(app, user):
    if user != "without_user":
        app.main_page.login_ok(user)
    window_before = app.main_page.driver.window_handles[0]
    app.main_page.click_nav_menu()
    friends_page = app.main_page.click_friends_btn()
    window_after = friends_page.driver.window_handles[1]
    friends_page.driver.switch_to_window(window_after)
    # friends_page.click_login_btn()
    sleep(time_to_present_result)
    app.make_screenshot()
    assert friends_page.is_unique_element_displayed(*FriendsPageLocators.LOGIN_BTN) and \
           friends_page.is_unique_element_displayed(*FriendsPageLocators.REGISTER_BTN)


@allure.feature("Poker")  # Проверка страницы POKER c зарег пользователем и без
@flaky(max_runs=3)
@pytest.mark.parametrize('user', ["without_user", "valid_login_user"])
def test_check_poker_page(app, user):
    if user != "without_user":
        app.main_page.login_ok(user)
    poker_page = app.main_page.click_poker_tab()
    poker_page.click_video_green_poker()
    sleep(time_to_present_result)
    app.make_screenshot()
    assert poker_page.is_unique_element_displayed(*PokerPageLocators.DOWNLOAD_BTN) and \
           poker_page.is_unique_element_displayed(*PokerPageLocators.GREEN_POKER_TXT_1)


@allure.feature("Casino")  # Проверка кнопок страницы Casino и поиска игр с зарег пользователем и без
@flaky(max_runs=3)
@pytest.mark.parametrize('user', ["without_user", "valid_login_user"])
def test_check_casino_page_search(app, user):
    if user != "without_user":
        app.main_page.login_ok(user)
    casino_page = app.main_page.click_casino_tab()
    casino_page.click_top_button()
    casino_page.click_new_button()
    casino_page.click_slots_button()
    casino_page.click_live_dealers_button()
    casino_page.click_table_button()
    casino_page.click_other_button()
    casino_page.search_casino_field()
    sleep(time_to_present_result)
    app.make_screenshot()
    assert casino_page.is_unique_element_displayed(*CasinoPageLocators.CASINO_SEARCH_ELM_BBW)


@allure.feature("Bets")  # Проверка элементов страницы BETS c зарег пользователем и без
@flaky(max_runs=3)
@pytest.mark.parametrize('user', ["without_user", "valid_login_user"])
def test_check_bets_page(app, user):
    if user != "without_user":
        app.main_page.login_ok(user)
    bets_page = app.main_page.click_bets_tab()
    sleep(time_to_present_result)
    app.make_screenshot()
    assert bets_page.is_unique_element_displayed(*BetsPageLocators.BETS_MENU) and \
           bets_page.is_unique_element_displayed(*BetsPageLocators.LIVE_BETTING_TAB)


@allure.feature("Bets")  # Одиночная ставка
@flaky(max_runs=3)
@pytest.mark.parametrize('user', ["valid_login_user"])
def test_check_bets_single(app, user):
    app.main_page.login_ok(user)
    bets_page = app.main_page.click_bets_tab()
    initial_balance = app.main_page.get_balance()
    bet_amount = bets_page.make_one_bet_favorite_rand_ok()
    balance_diff = bets_page.wait_balance_change(initial_balance)
    sleep(time_to_present_result)
    app.make_screenshot()
    assert balance_diff == bet_amount


@allure.feature("Bets")  # Мульти ставка
@flaky(max_runs=3)
@pytest.mark.parametrize('user', ["valid_login_user"])
def test_check_bets_multi(app, user):
    app.main_page.login_ok(user)
    bets_page = app.main_page.click_bets_tab()
    sleep(5)
    initial_balance = app.main_page.get_balance()
    bet_amount = 123.59
    bets_qty = random.randint(3, 5)
    bets_page.choose_min_bets_rand(bets_qty)
    bets_page.input_bet_amount(bet_amount)
    balance_diff = bets_page.wait_balance_change(initial_balance)
    sleep(time_to_present_result)
    app.make_screenshot()
    assert balance_diff == bet_amount


@allure.feature("Bets")  # Ставка системой
@flaky(max_runs=3)
@pytest.mark.parametrize('user', ["valid_login_user"])
def test_check_bets_system(app, user):
    app.main_page.login_ok(user)
    bets_page = app.main_page.click_bets_tab()
    sleep(15)
    initial_balance = app.main_page.get_balance()
    bet_amount = 523.59
    bets_qty = random.randint(3, 5)
    bets_page.choose_min_bets_rand(bets_qty)
    bets_page.click_bet_type_system()
    bets_page.input_bet_amount(bet_amount)
    balance_diff = bets_page.wait_balance_change(initial_balance)
    sleep(time_to_present_result)
    app.make_screenshot()
    assert balance_diff == bet_amount


@allure.feature("Cashier")  # Пополнение счета на 100 рублей во фрейме
@flaky(max_runs=3)
@pytest.mark.parametrize('user', ["valid_login_user"])
def test_deposit_visa(app, user, deposit_amount=100):
    app.main_page.login_ok(user)
    sleep(20)
    initial_balance = app.main_page.get_balance()
    profile_page = app.main_page.click_cashier()
    sleep(1.5)
    profile_page.make_deposit(deposit_amount)
    balance_diff = profile_page.wait_balance_change(initial_balance)
    app.make_screenshot()
    assert balance_diff == deposit_amount


@allure.feature("Cashier")  # Вывод 200 рублей на карту во фрейме
@flaky(max_runs=3)
@pytest.mark.parametrize('user', ["autotest_login_admin"])
def test_withdraw_visa(app, user, withdraw_amount=200):
    app.main_page.login_ok(user)
    sleep(25)
    initial_balance = app.main_page.get_balance()
    profile_page = app.main_page.click_cashier()
    sleep(1.5)
    profile_page.make_withdraw(withdraw_amount)
    admin_page = app.main_page.open_admin_page()
    admin_page.admin_approve_withdraw()
    balance_diff = profile_page.wait_balance_change(initial_balance)
    sleep(3)
    app.make_screenshot()
    assert balance_diff == withdraw_amount * 0.97  # тут учитывается комиссия в 3% для вывода в рублях


@allure.feature("Cashier")  # Перевод пользователю remittee_user 1001 рубля от autotest_admin
@flaky(max_runs=3)
@pytest.mark.parametrize(['user_sender', 'user_receiver'], [("autotest_login_admin", "remittee_login_user")])
def test_money_transfer_to_remittee(app, user_sender, user_receiver, transfer_amount=1001):
    app.main_page.login_ok(user_receiver)
    sleep(30)
    receiver_initial_balance = app.main_page.get_balance()
    app.main_page.click_logout_button()
    app.main_page.login_ok(user_sender)
    sender_initial_balance = app.main_page.get_balance()
    profile_page = app.main_page.click_money_transfers()
    profile_page.make_money_transfer(transfer_amount)
    admin_page = app.main_page.open_admin_page()
    admin_page.admin_approve_transfer()
    balance_diff_sender = profile_page.wait_balance_change(sender_initial_balance)
    app.make_screenshot()
    assert balance_diff_sender == transfer_amount  # проверка, что у отправителя перевода списана корректная сумма

    app.main_page.click_logout_button()
    app.main_page.login_ok(user_receiver)
    balance_diff_receiver = profile_page.wait_balance_change(receiver_initial_balance)
    app.make_screenshot()
    assert balance_diff_receiver == transfer_amount  # проверка, что получателю перевода пришла корректная сумма


@allure.feature("Webpage slicing")  # Проверка верстки страницы с зарег пользователем и без
@flaky(max_runs=3)
@pytest.mark.parametrize('user', ["without_user", "user_unchange"])
# @pytest.mark.parametrize('user', ["without_user"])
def test_check_webpage_markup(app, user):
    img_suffix = "wo_user"
    if user != "without_user":
        app.main_page.login_ok(user)
        img_suffix = "with_user"
    app.delete_file("result_" + img_suffix + ".png")
    app.main_page.wait_for_chat()
    total_height = app.driver.execute_script("return document.body.parentNode.scrollHeight")
    app.driver.set_window_size(1920, total_height)

    # Make sample screenshot
    # app.main_page.set_header_picture_1()
    # app.driver.save_screenshot("sample_" + img_suffix + ".png")

    sample_img = cv2.imread("sample_" + img_suffix + ".png")
    app.main_page.set_header_picture_1()
    app.driver.save_screenshot("testing_" + img_suffix + ".png")
    testing_img = cv2.imread("testing_" + img_suffix + ".png")
    difference = cv2.subtract(testing_img, sample_img)
    result = not np.any(difference)  # if difference is all zeros it will return False

    if result is True:
        print("The images are the same")
    else:
        result is False
        cv2.imwrite("result_" + img_suffix + ".png", difference)
        allure.attach.file("result_" + img_suffix + ".png", name="result_" + img_suffix + ".png",
                           attachment_type=AttachmentType.PNG)
        # print("the images are different")

    allure.attach.file("sample_" + img_suffix + ".png", name="sample_" + img_suffix + ".png",
                       attachment_type=AttachmentType.PNG)
    allure.attach.file("testing_" + img_suffix + ".png", name="testing_" + img_suffix + ".png",
                       attachment_type=AttachmentType.PNG)
    assert result
