from selenium.webdriver.common.by import By


# for maintainability we can separate web objects by page name

class MainPageLocators(object):
    # LOGO = (By.ID, 'nav-logo')
    # ACCOUNT = (By.ID, 'nav-link-yourAccount')
    SIGNUP_BTN = (By.XPATH, "//a[@href='#registration']")
    LOGIN_BTN = (By.XPATH, "//a[@href='#login']")
    LOGOUT_BTN = (By.XPATH, "//a[@href='/logout']")
    USERNAME = (By.XPATH, "//a[contains(@class,'userinfo__nick')]")
    REGISTRATION_MES_OK = (By.XPATH, "//*[@class='event_message']")
    # LoginPageLocators:
    EMAIL = (By.XPATH, "//input[@name='email']")
    LOGIN_1 = (By.XPATH, "//input[@name='login']")  # for LOGIN existting user
    LOGIN_2 = (By.XPATH, "//input[@name='nick']")  # for SIGNUP NEW user
    PASSWORD_1 = (By.XPATH, "//div[@id='login']//input[@name='password' and @type='text']")  # for LOGIN existting user
    PASSWORD_2 = (By.XPATH, "//*[@id='registration']//*[@name='password'][2]")  # for SIGNUP NEW user
    CAPTCHA_1 = (By.XPATH, "//*[@id='login']/div/div/div[2]/form/div[5]/div/div/input")
    CAPTCHA_2 = (By.XPATH, "//*[@id='registration']/div/div/div[2]/form/div[8]/div/input")
    SUBMIT_1 = (By.XPATH, "//*[@id='login']/div/div/div[2]/form/div[5]/button")  # for LOGIN existting user
    SUBMIT_2 = (By.XPATH, "//*[@id='registration']/div/div/div[2]/form/button")  # for SIGNUP NEW user
    ERR_MES_LOGIN_1 = (By.XPATH, "//*[@id='login']/div/div/div[2]/form/div[2]/div[1]")
    # ERR_MES_LOGIN_1 = (By.XPATH, "//*[@id='registration']//*[@name='password'][2]")   # XPATH невидимого но присутствующего в DOM пароля (форма РЕГИСТРАЦИИ) для теста правильной обработки видимлсти
    ERR_MES_EMAIL_REQUIRED = (By.XPATH, '//*[@id="registration"]/div/div/div[2]/form/div[1]/span[1]')
    ERR_MES_LOGIN_REQUIRED = (By.XPATH, '//*[@id="registration"]/div/div/div[2]/form/div[2]/span[3]')
    ERR_MES_PASS_REQUIRED = (By.XPATH, '//*[@id="registration"]/div/div/div[2]/form/div[3]/span[3]')
    ERR_MES_CAPTCH_REQUIRED = (By.XPATH, '//*[@id="registration"]/div/div/div[2]/form/div[8]/div/span[1]')
    CLOSE_BTN = (By.XPATH, "//div[@id='login']//button[@aria-label='Close']")
    ERR_MES_EMAIL_OCCUPIED = (By.XPATH, "//*[@id='registration']/div/div/div[2]/form/div[1]/span[3]")
    ERR_MES_LOGIN_OCCUPIED = (By.XPATH, "//*[@id='registration']/div/div/div[2]/form/div[2]/span[6]")
    ERR_MES_INVALID_LOGIN = (By.XPATH, "//*[@id='registration']/div/div/div[2]/form/div[2]/span[5]")
    ERR_MES_LOGIN_CYRILLIC = (By.XPATH, "//*[@id='registration']/div/div/div[2]/form/div[2]/span[7]")
    LETTER_EMAIL = (
    By.XPATH, "//*[@id='message-htmlpart1']/div/div/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/p[1]/a")
    LETTER_LINK = (
    By.XPATH, "//*[@id='message-htmlpart1']/div/div/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/p[5]/a")

    BALANCE = (By.XPATH, "//a[contains(@class, 'userinfo__balance')]//span[1]")
    LANG = (By.XPATH, "/html/body/div[3]/div/div[1]/header/div[1]/div/div[3]/div/span/span")
    LANG_SET = (By.XPATH, "/html/body/div[3]/div/div[1]/header/div[1]/div/div[3]/div/div/ul")

    POKER_PAGE_BTN = (By.XPATH, "//div[contains(@class, 'pd-header__body')]//a[contains(@href,'/poker')]")
    CASINO_PAGE_BTN = (By.XPATH, "//div[contains(@class, 'pd-header__body')]//a[contains(@href,'/games')]")
    BETS_PAGE_BTN = (By.XPATH, "//div[contains(@class, 'pd-header__body')]//a[contains(@href,'/sports')]")
    BETS_IFRAME = (By.XPATH, "//*[@id='sport_iframe_1']")
    CASHIER_ECOMPAY_IFRAME = (By.XPATH, "//iframe[contains(@class, 'pd-cashier__iframe')]")

    CURRENCY_RUB = (By.XPATH, "//*[@id='registration']/div/div/div[2]/form/div[5]/span[4]/label")
    CURRENCY_EUR = (By.XPATH, "//*[@id='registration']/div/div/div[2]/form/div[5]/span[1]/label")
    CURRENCY_USD = (By.XPATH, "//*[@id='registration']/div/div/div[2]/form/div[5]/span[2]/label")
    CURRENCY_KZT = (By.XPATH, "//*[@id='registration']/div/div/div[2]/form/div[5]/span[3]/label")

    CASHIER_PAGE_BTN = (By.XPATH, "//a[text()='Касса']")
    MONEY_TRANSFERS_PAGE_BTN = (By.XPATH, "//a[contains(@href, 'cashier/transfers')]")

    NAV_MENU = (By.XPATH, "//*[@class='pd-external-links__icon_content___3Y3tC']")
    FRIENDS_BTN = (By.XPATH, "//*[@href='https://friends.poker']")

    BLOCKED_MES = (By.XPATH, "//*[@class='blocked']")

    HEADER_PICTURE_HANDLER_1 = (By.XPATH, "//*[@class='pd-carousel__pager___3fba-']/li[1]")
    CHAT = (By.XPATH, "//*[@class='support-trigger-text-wrapper']")


class PokerPageLocators(MainPageLocators):
    DOWNLOAD_BTN = (By.XPATH, "/html/body/div[3]/div/div[2]/div/div/div/div[1]/div[1]/div/a[1]")
    GREEN_POKER_TXT_1 = (By.XPATH, "/html/body/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div[1]")
    GREEN_POKER_VIDEO_PLAY = (By.XPATH, "//*[@id='play-video-a']")
    GREEN_POKER_VIDEO = (By.XPATH, "/html/body/div[3]/div/div[2]/div/div/div/div[2]/div[1]/div[1]/div[2]/div[2]")
    PLAY_POKER_BROWS_LNK = (By.XPATH, "//*[@class='pd-download-poker__flash_text___12W1x']")


class CasinoPageLocators(MainPageLocators):
    CASINO_PAGE_BTN = (By.XPATH, "//div[contains(@class, 'pd-header__body')]//a[contains(@href, '/games')]")
    TOP = (By.XPATH, "//div[contains(@class, 'pd-casino-menu__inner')]/ul/li[1]")
    NEW = (By.XPATH, "//div[contains(@class, 'pd-casino-menu__inner')]/ul/li[2]")
    SLOTS = (By.XPATH, "//div[contains(@class, 'pd-casino-menu__inner')]/ul/li[3]")
    LIVE_DEALERS = (By.XPATH, "//div[contains(@class, 'pd-casino-menu__inner')]/ul/li[4]")
    TABLE = (By.XPATH, "//div[contains(@class, 'pd-casino-menu__inner')]/ul/li[5]")
    OTHER = (By.XPATH, "//div[contains(@class, 'pd-casino-menu__inner')]/ul/li[6]")
    RECENTLY = (By.XPATH, "//div[contains(@class, 'pd-casino-menu__inner')]/ul/li[7]")
    SEARCH_BTN = (By.XPATH, "//a[contains(@class, 'pd-casino-menu__link')]")
    SEARCH_GAMES = (By.XPATH, "//input[contains(@class, 'pd-casino-menu__input')]")
    CASINO_SEARCH_ELM_BBW = (By.XPATH, "//div[@class='pd-game__content___3Tm9C']")


class BetsPageLocators(MainPageLocators):
    BETS_MENU = (By.XPATH, "//*[@id='mnu_row']")
    LIVE_BETTING_TAB = (By.XPATH, "//*[@id='live_betting']//div[@class='tabSelectorHeading']")
    TOP_MATCHES_TAB = (By.XPATH, "//*[@id='live_betting']//div[@class='tabSelectorHeading']")
    DATA_PANEL_TAB = (By.ID, "data_panel")

    UPCOMING_BTN = (By.XPATH, "//*[@id='mnu_row']/div[2]/a")
    OVERVIEW_BTN = (By.XPATH, "//*[@id='mnu_row']/div[3]/a")
    LOGIN_WIN = (By.XPATH, "//*[@id='login']/div")

    BETS_LIVE = (By.XPATH, "//*[@class='displayFlex maOdds']/a")
    BETS_LIVE_RELATIVES = (By.XPATH, ".//a")
    BETS_LIVE_BLOCKS = (By.XPATH, "//*[@class='displayFlex maOdds']")

    BETS_IN_TICKET = (By.XPATH, "//*[@class='stake_item_panel displayFlex']")
    BET_AMOUNT = (By.XPATH, "//*[@id='betAmountInput']")
    BET_AMOUNT_MAX = (By.XPATH, "//*[@class='btnMax coupBtn ns transAll']")
    POSSIB_WIN_MAX = (
        By.XPATH,
        "//*[@class = 'betCouponRow betAmountRow jb displayFlex padded']/*[@class='btnMax coupBtn ns transAll']")
    PLACE_BET_BTN = (By.XPATH, "//input[@class='btn_bet ternBtn transAll']")
    CONGRAT_BET_MES = (By.XPATH, "//*[@class='congratText']")
    FAVOR_AMOUNT_BTN_1 = (By.ID, "favaritAmount1")
    FAVOR_AMOUNT_BTN_2 = (By.ID, "favaritAmount2")
    FAVOR_AMOUNT_BTN_3 = (By.ID, "favaritAmount3")

    SYSTEM_TAB = (By.XPATH, "//*[@class='bet_type_selector displayFlex cpColor']/div[3]")

    BLOCK_DISCLOSE = (By.XPATH, "//*[@id='top_ten']/div/div[2]/div[1]/div/div[3]/label/div[2]")


class ProfilePageLocators(MainPageLocators):
    CASHIER_ECOMPAY_DEPOSIT_TAB = (By.XPATH, "//li[contains(@class, 'deposit')]")
    CASHIER_ECOMPAY_WITHDRAW_TAB = (By.XPATH, "//li[contains(@class, 'payout')]")
    CASHIER_ECOMPAY_DEPOSIT = (By.XPATH, "//div[contains(@class, 'deposit_widget')]/div[@class='item_inner']")
    CASHIER_ECOMPAY_WITHDRAW = (By.XPATH, "//div[contains(@class, 'payout_widget')]/div[@class='item_inner']")

    CASHIER_ECOMPAY_DEPOSIT_CARDNMBR = (By.XPATH, "//input[@id='new_card_number']")
    CASHIER_ECOMPAY_DEPOSIT_CARDHLDR = (By.XPATH, "//input[@id='card_holder']")
    CASHIER_ECOMPAY_DEPOSIT_CARDRMBR = (By.XPATH, "//*[@class='remember_card']")
    CASHIER_ECOMPAY_DEPOSIT_CVV = (By.XPATH, "//input[@id='cvv']")
    CASHIER_ECOMPAY_DEPOSIT_AMOUNT = (By.XPATH, "//input[@id='amount_input']")
    CASHIER_ECOMPAY_DEPOSIT_SUBMIT = (By.XPATH, "//button[@id='submit_button']")
    CASHIER_ECOMPAY_DEPOSIT_CLOSE = (By.XPATH, "(//span[text()='OK'])[1]")

    CASHIER_ECOMPAY_WITHDRAW_AMOUNT = (By.XPATH, "//input[@name='amount']")
    CASHIER_ECOMPAY_WITHDRAW_SUBMIT = (By.XPATH, "//button[@type='submit']")
    CASHIER_ECOMPAY_WITHDRAW_CLOSE = (By.XPATH, "(//span[text()='OK'])[1]")

    MONEY_TRANSFERS_REMITTEE_NAME = (By.XPATH, "//input[contains(@class, 'transfers__input_name')]")
    MONEY_TRANSFERS_SUM = (By.XPATH, "//input[contains(@class, 'transfers__input_sum')]")
    MONEY_TRANSFERS_SUBMIT_BTN = (By.XPATH, "//button[contains(@class, 'button_theme_primary')]")


class AdminPageLocators(object):
    AP_WITHDRAWALS_WAITING_FOR_PAYOUT = (By.XPATH, "(//a[text()='Waiting for pay'])[1]")
    AP_WITHDRAWALS_PAYOUT = (By.XPATH, "//a[contains(text(), 'Выплата')]")
    AP_WITHDRAWALS_MAKE_PAYOUT = (By.XPATH, "//a[@name='payout' and @delete-other='0']")
    AP_WITHDRAWALS_MAKE_PAYOUT_CONFIRMED = (By.XPATH, "//button[@id='payout-confirmed']")
    AP_WITHDRAWALS_MAKE_PAYOUT_CLOSE = (By.XPATH, "//a[@class='close']")
    AP_MONEY_TRANSFER_APPROVE_LINK = (By.XPATH,
                                      "//td[span[text()='1001.0']]/following-sibling::td[a[@class='js-approve-reject-button']]/a[@data-form-submit-value='Approve']")  # Аппрув заявки на перевод с суммой 1000 рублей
    AP_MONEY_TRANSFER_APPROVE_COMMENT = (By.XPATH, "//input[@name='comment_for_user']")
    AP_MONEY_TRANSFER_APPROVE_COMMENT_BTN = (By.XPATH, "//input[@name='submit' and @value='Approve']")


class FriendsPageLocators(object):
    LOGIN_BTN = (By.XPATH, "//*[@href='#login']")
    REGISTER_BTN = (By.XPATH, "//*[@href='#register']")
