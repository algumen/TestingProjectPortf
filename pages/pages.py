from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from data.locators import MainPageLocators, CasinoPageLocators, PokerPageLocators, ProfilePageLocators, \
    BetsPageLocators, FriendsPageLocators, AdminPageLocators
from pages.base import Page
from data import users
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import shuffle, randint, random
import random
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import StaleElementReferenceException


# Page objects are written in this module.
# Depends on the page functionality we can have more functions for new classes

class MainPage(Page):
    def __init__(self, driver):
        self.locator = MainPageLocators
        super().__init__(driver)

    def click_login_button(self):
        self.find_displayed_element(*self.locator.LOGIN_BTN).click()

    def click_signup_button(self):
        self.find_displayed_element(*self.locator.SIGNUP_BTN).click()

    def click_logout_button(self):
        self.find_displayed_element(*self.locator.LOGOUT_BTN).click()

    def get_username(self):
        return self.find_displayed_element(*self.locator.USERNAME).text

    def enter_email(self, user):
        self.find_displayed_element(*self.locator.EMAIL).send_keys(users.get_user(user)["email"])

    def enter_login_1(self, user):
        self.find_displayed_element(*self.locator.LOGIN_1).send_keys(users.get_user(user)["login"])

    def enter_login_2(self, user):
        self.find_displayed_element(*self.locator.LOGIN_2).send_keys(users.get_user(user)["login"])

    def enter_password_1(self, user):
        self.find_displayed_element(*self.locator.PASSWORD_1).send_keys(users.get_user(user)["password"])

    def enter_password_2(self, user):
        self.find_displayed_element(*self.locator.PASSWORD_2).send_keys(users.get_user(user)["password"])

    def click_RUB_currency(self):
        self.find_displayed_element(*self.locator.CURRENCY_RUB).click()

    def enter_captcha_2(self, user):
        self.find_displayed_element(*self.locator.CAPTCHA_2).send_keys(users.get_user(user)["captcha"])

    def click_submit_button_1(self):
        self.find_displayed_element(*self.locator.SUBMIT_1).click()

    def click_submit_button_2(self):
        self.find_displayed_element(*self.locator.SUBMIT_2).click()

    def login_err(self, user):
        # with allure.step("Логинимся"):
        self.find_displayed_element(*self.locator.LOGIN_BTN).click()
        static_user = users.get_user(user)
        self.find_displayed_element(*self.locator.LOGIN_1).send_keys(static_user['login'])
        self.find_displayed_element(*self.locator.PASSWORD_1).send_keys(static_user['password'])
        # (keyring.get_password("system", static_user['login']))
        self.click_submit_button_1()

    def login_ok(self, user):
        self.login_err(user)
        self.wait_for_page_reload(self.locator.POKER_PAGE_BTN)

    def signup(self, user):
        # with allure.step("Заполняем данные нового пользователя"):
        self.find_displayed_element(*self.locator.SIGNUP_BTN).click()
        static_user = users.get_user(user)
        self.find_displayed_element(*self.locator.EMAIL).send_keys(static_user['email'])
        self.find_displayed_element(*self.locator.LOGIN_2).send_keys(static_user['login'])
        self.find_displayed_element(*self.locator.PASSWORD_2).send_keys(static_user['password'])
        self.click_RUB_currency()  # Выбор РУБ для РС если не работает регистрация на лире
        self.find_displayed_element(*self.locator.CAPTCHA_2).send_keys(static_user['captcha'])
        self.click_submit_button_2()
        return static_user

    def click_nav_menu(self):
        self.find_displayed_element(*self.locator.NAV_MENU).click()

    def click_friends_btn(self):
        self.find_displayed_element(*self.locator.FRIENDS_BTN).click()
        return FriendsPage(self.driver)

    def click_poker_tab(self):
        self.find_displayed_element(*self.locator.POKER_PAGE_BTN).click()
        return PokerPage(self.driver)

    def click_casino_tab(self):
        self.find_displayed_element(*self.locator.CASINO_PAGE_BTN).click()
        return CasinoPage(self.driver)

    def click_bets_tab(self):
        self.find_displayed_element(*self.locator.BETS_PAGE_BTN).click()
        self.driver.switch_to.frame(self.find_displayed_element(*self.locator.BETS_IFRAME))
        return BetsPage(self.driver)

    def open_admin_page(self):
        self.open("https://beta.*******.com/ka")
        return AdminPage(self.driver)

    def get_balance(self):
        self.driver.switch_to_default_content()
        # print("raw text balance", self.find_displayed_element(*self.locator.BALANCE).text)
        balance = self.find_displayed_element(*self.locator.BALANCE).text
        balance = round((float(''.join(i for i in balance if i.isdigit()))) / 100, 2)
        # print("balance after", balance)
        return balance

    def click_cashier(self):
        self.find_displayed_element(*self.locator.CASHIER_PAGE_BTN).click()
        self.driver.switch_to.frame(self.find_displayed_element(*self.locator.CASHIER_ECOMPAY_IFRAME))
        return ProfilePage(self.driver)

    def click_money_transfers(self):
        self.find_displayed_element(*self.locator.CASHIER_PAGE_BTN).click()
        self.find_displayed_element(*self.locator.MONEY_TRANSFERS_PAGE_BTN).click()
        return ProfilePage(self.driver)

    def get_lang(self):
        return self.find_displayed_element(*self.locator.LANG).text

    def close(self):
        self.find_displayed_element(*self.locator.CLOSE_BTN).click()

    def mail_confirmation(
            self):  # ToDO Написать универсальный метод подтверждения нового аккаунта для бэты (тоссер) и прода (гугл аккаунт)
        if "beta" in self.driver.current_url:
            print("Do mail_confirmation for beta because URL is - ", self.driver.current_url)

    def change_lang(self, language):
        lang = self.find_displayed_element(*self.locator.LANG)
        lang.click()
        lang_tab_element = self.find_displayed_element(*self.locator.LANG_SET)
        lang_qty = len(lang_tab_element.find_elements_by_css_selector("li"))
        i = 1
        # lang.click()
        while self.find_displayed_element(*self.locator.LANG).text != language and i < len(
                lang_tab_element.find_elements_by_css_selector("li")):
            webdriver.ActionChains(self.driver).move_to_element(lang).click(lang).perform()
            lang_tab_element.find_elements_by_css_selector("li")[i].click()
            i += 1
            sleep(10)

        if self.find_displayed_element(*self.locator.LANG).text != language and i == len(
                lang_tab_element.find_elements_by_css_selector(
                    "li")):  # len(lang_tab_element.find_elements_by_css_selector("li")):
            raise NoSuchElementException("********!!!!!!!!!! Language was not found - ", language)
            sleep(3)

    def wait_for_chat(self):
        self.find_displayed_element(*self.locator.CHAT)

    def set_header_picture_1(self):
        self.find_displayed_element(*self.locator.HEADER_PICTURE_HANDLER_1).click()


class ProfilePage(MainPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = ProfilePageLocators

    def make_deposit(self, deposit_amount):
        self.find_displayed_element(*self.locator.CASHIER_ECOMPAY_DEPOSIT).click()
        card_nbr_input = self.find_displayed_element(*self.locator.CASHIER_ECOMPAY_DEPOSIT_CARDNMBR)
        card_nbr = "1000000000000001"
        for character in card_nbr:  # need to be refactored and moved to base page methods
            card_nbr_input.send_keys(character)

        self.find_displayed_element(*self.locator.CASHIER_ECOMPAY_DEPOSIT_CARDHLDR).send_keys("Valid User")
        self.find_displayed_element(*self.locator.CASHIER_ECOMPAY_DEPOSIT_CVV).send_keys("111")
        self.find_displayed_element(*self.locator.CASHIER_ECOMPAY_DEPOSIT_AMOUNT).clear()
        self.find_displayed_element(*self.locator.CASHIER_ECOMPAY_DEPOSIT_AMOUNT).send_keys(deposit_amount)
        self.find_displayed_element(*self.locator.CASHIER_ECOMPAY_DEPOSIT_CARDRMBR).click()
        self.find_displayed_element(*self.locator.CASHIER_ECOMPAY_DEPOSIT_SUBMIT).click()
        self.find_displayed_element(*self.locator.CASHIER_ECOMPAY_DEPOSIT_CLOSE).click()

    def make_withdraw(self, withdraw_amount):
        self.find_displayed_element(*self.locator.CASHIER_ECOMPAY_WITHDRAW_TAB).click()
        self.find_displayed_element(*self.locator.CASHIER_ECOMPAY_WITHDRAW).click()
        self.find_displayed_element(*self.locator.CASHIER_ECOMPAY_WITHDRAW_AMOUNT).send_keys(withdraw_amount)
        self.find_displayed_element(*self.locator.CASHIER_ECOMPAY_WITHDRAW_SUBMIT).click()
        self.find_displayed_element(*self.locator.CASHIER_ECOMPAY_WITHDRAW_CLOSE).click()

    def make_money_transfer(self, transfer_amount):
        self.find_displayed_element(*self.locator.MONEY_TRANSFERS_REMITTEE_NAME).send_keys("remittee_user")
        self.find_displayed_element(*self.locator.MONEY_TRANSFERS_SUM).send_keys(transfer_amount)
        self.find_displayed_element(*self.locator.MONEY_TRANSFERS_SUBMIT_BTN).click()


class AdminPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = AdminPageLocators

    def admin_approve_withdraw(self):
        self.open("https://beta.*******.com/ka/users/show/5aeb01cb5f8aeb2959685a61/cash/payout")
        self.find_displayed_element(*self.locator.AP_WITHDRAWALS_WAITING_FOR_PAYOUT).click()
        self.find_displayed_element(*self.locator.AP_WITHDRAWALS_PAYOUT).click()
        self.find_displayed_element(*self.locator.AP_WITHDRAWALS_MAKE_PAYOUT).click()
        self.find_displayed_element(*self.locator.AP_WITHDRAWALS_MAKE_PAYOUT_CONFIRMED).click()
        self.find_displayed_element(*self.locator.AP_WITHDRAWALS_MAKE_PAYOUT_CLOSE).click()
        self.open("https://beta.*******.com")

    def admin_approve_transfer(self):
        self.open("https://beta.*******.com/ka/cash/moneytransfers")
        self.find_displayed_element(*self.locator.AP_MONEY_TRANSFER_APPROVE_LINK).click()
        self.find_displayed_element(*self.locator.AP_MONEY_TRANSFER_APPROVE_COMMENT).send_keys("autotest 1001 rub")
        self.find_displayed_element(*self.locator.AP_MONEY_TRANSFER_APPROVE_COMMENT_BTN).click()
        self.open("https://beta.*******.com")


class PokerPage(MainPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = PokerPageLocators

    def click_video_green_poker(self):
        self.find_displayed_element(*self.locator.GREEN_POKER_VIDEO).click()

    def click_download_main(self):
        self.find_displayed_element(*self.locator.DOWNLOAD_BTN).click()

    def click_play_poker_brows(self):
        self.find_displayed_element(*self.locator.PLAY_POKER_BROWS_LNK).click()


class CasinoPage(MainPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = CasinoPageLocators

    def click_top_button(self):
        self.find_displayed_element(*self.locator.TOP).click()

    def click_new_button(self):
        self.find_displayed_element(*self.locator.NEW).click()

    def click_slots_button(self):
        self.find_displayed_element(*self.locator.SLOTS).click()

    def click_live_dealers_button(self):
        self.find_displayed_element(*self.locator.LIVE_DEALERS).click()

    def click_table_button(self):
        self.find_displayed_element(*self.locator.TABLE).click()

    def click_other_button(self):
        self.find_displayed_element(*self.locator.OTHER).click()

    def click_recently_button(self):
        self.find_displayed_element(*self.locator.RECENTLY).click()

    def search_casino_field(self):
        self.find_displayed_element(*self.locator.SEARCH_BTN).click()
        self.find_displayed_element(*self.locator.SEARCH_GAMES).send_keys('Big Bad Wolf')
        self.find_displayed_element(*self.locator.SEARCH_GAMES).send_keys(Keys.RETURN)


class BetsPage(MainPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = BetsPageLocators

    def click_upcoming_btn(self):
        self.find_displayed_element(*self.locator.UPCOMING_BTN).click()

    def click_overview_btn(self):
        self.find_displayed_element(*self.locator.OVERVIEW_BTN).click()

    def choose_bet_single_rand(self):
        bets_qty = self.count_load_elements(self.locator.BETS_LIVE)
        bet_number = randint(0, bets_qty - 1)
        # bet_number =  bets_qty-1   # Для тестирования
        self.driver.find_elements(*self.locator.BETS_LIVE)[bet_number].click()
        # print("choosen bet number is - ", bet_number, "from total bets q-ty - ", bets_qty)

    def choose_min_bets_rand(self, bets_qty):
        self.driver.switch_to.frame(self.find_displayed_element(*self.locator.BETS_IFRAME))

        if len(self.driver.find_elements(*self.locator.BLOCK_DISCLOSE)) > 0:
            self.find_displayed_element(*self.locator.BLOCK_DISCLOSE).click()

        self.count_load_elements(self.locator.BETS_LIVE_BLOCKS)
        bloks = self.driver.find_elements(*self.locator.BETS_LIVE_BLOCKS)
        # print("all bloks - ", len(bloks), bloks)
        block_elements_list = []
        block_number = 1
        for block in bloks:
            block_elements_list.append(block.find_elements(*self.locator.BETS_LIVE_RELATIVES))
            block_number += 1

            # Subfunc - print sorted list with sublists values for debugging

        def print_sorted_list_with_sublists_values():
            block_number = 1
            for block_elements_sublist in block_elements_list:
                print("---------------------------")
                print("block_number - ", block_number)
                block_number += 1
                for block_element in block_elements_sublist:
                    print("block element bet - ", block_element.text, block_element)

        # print("block_elements_list before removing empties - ", len(block_elements_list), block_elements_list)
        # print_sorted_list_with_sublists_values()
        # Remove empty sublists
        cleaned_block_elements_list = []
        for block_elements_sublist in block_elements_list:
            if len(block_elements_sublist) != 0:
                cleaned_block_elements_list.append(block_elements_sublist)
        block_elements_list = cleaned_block_elements_list
        # print("block_elements_list after removing empties - ", len(block_elements_list), block_elements_list)
        # print_sorted_list_with_sublists_values()

        # Sort sublists inside
        for block_elements_sublist in block_elements_list:
            for i in range(len(block_elements_sublist) - 1):
                j = 1
                while j <= len(block_elements_sublist) - 1:
                    if float(block_elements_sublist[i].text) > float(block_elements_sublist[j].text):
                        block_elements_sublist[i], block_elements_sublist[j] = block_elements_sublist[j], \
                                                                               block_elements_sublist[i]
                    j += 1

        shuffle(block_elements_list)
        # print_sorted_list_with_sublists_values()
        # Click shuffled bet elements
        i = 0
        bets_real_qty = 0
        while len(block_elements_list) - i > 0 and i < bets_qty:
            # print("i = ", i)
            block_elements_list[i][0].click()
            bets_real_qty += 1
            i += 1
        # print("bets_real_qty", bets_real_qty )
        # sleep(1)

        self.wait_to_load_elements_qty(self.locator.BETS_IN_TICKET, bets_real_qty)
        # return bets_real_qty

    def click_place_bet(self):
        # sleep(5)
        self.find_displayed_element(*self.locator.PLACE_BET_BTN).click()

    def click_favorite_amount_rand(self, button_number):
        self.find_displayed_element(*self.locator.BET_AMOUNT)
        self.find_displayed_element(*self.locator.PLACE_BET_BTN)
        if button_number == 1:
            bet_button = self.find_displayed_element(*self.locator.FAVOR_AMOUNT_BTN_1)
        elif button_number == 2:
            bet_button = self.find_displayed_element(*self.locator.FAVOR_AMOUNT_BTN_2)
        elif button_number == 3:
            bet_button = self.find_displayed_element(*self.locator.FAVOR_AMOUNT_BTN_3)
        bet_button.click()
        return float(bet_button.get_attribute("value"))

    def click_bet_type_system(self):
        self.find_displayed_element(*self.locator.SYSTEM_TAB).click()

    def input_bet_amount(self, bet_amount):
        sleep(1)
        self.find_displayed_element(*self.locator.BET_AMOUNT).click()
        self.find_displayed_element(*self.locator.BET_AMOUNT).clear()
        self.find_displayed_element(*self.locator.BET_AMOUNT).send_keys(str(bet_amount))
        self.click_place_bet()
        self.find_displayed_element(*self.locator.CONGRAT_BET_MES)

    def make_one_bet_favorite_rand_ok(self):
        self.driver.switch_to.frame(self.find_displayed_element(*self.locator.BETS_IFRAME))
        self.choose_bet_single_rand()
        button_number = random.randint(1, 3)
        bet_amount = self.click_favorite_amount_rand(button_number)
        self.click_place_bet()
        self.find_displayed_element(*self.locator.CONGRAT_BET_MES)
        return bet_amount


class FriendsPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = FriendsPageLocators

    def click_login_btn(self):
        self.find_displayed_element(*self.locator.LOGIN_BTN).click()
