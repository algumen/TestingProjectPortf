# we can store test data in this module like users
import random

random_string = ''.join([random.choice(list('123456789qwertyuiopasdfghjklzxcvbnm')) for x in range(9)])
email = "ivanovivan64858+" + random_string + "@gmail.com"
login = password = "auto_" + random_string

users = [
    {"name": "autotest_login_admin", "email": "autotest_admin@ukr.net", "login": "autotest_admin",
     "password": "*******"},

    {"name": "valid_login_user", "email": "valid_user@ukr.net", "login": "valid_user", "password": "*******"},
    {"name": "user_unchange", "email": "user_unchange@ukr.net", "login": "user_unchange", "password": "*******"},

    {"name": "remittee_login_user", "email": "remittee_user@ukr.net", "login": "remittee_user",
     "password": "*******"},

    {"name": "invalid_login_user", "email": "inv_login_user@ukr.net", "login": "invalid_user",
     "password": "*******", \
     "message": "ERR_MES_LOGIN_1"},

    {"name": "user_reg_exist_email", "email": "ivanovivan64859+999999@gmail.com", "login": "alg_test777",
     "password": "*******", "captcha": "1111", "message": "ERR_MES_EMAIL_OCCUPIED"},

    {"name": "user_reg_exist_login", "email": "ivanovivan64859+777777@gmail.com", "login": "alg_test5",
     "password": "*******", \
     "captcha": "1111", "message": "ERR_MES_LOGIN_OCCUPIED"},

    {"name": "invalid_reg_user_1", "email": "", "login": "staff", "password": "*******", "captcha": "1111",
     "message": "ERR_MES_EMAIL_REQUIRED"},

    {"name": "invalid_reg_user_2", "email": "inv_reg_user_2@ukr.net", "login": "", "password": "*******",
     "captcha": "1111", "message": "ERR_MES_LOGIN_REQUIRED"},

    {"name": "invalid_reg_user_3", "email": "inv_reg_user_3@ukr.net", "login": "invalid_reg_user_3", "password": "",
     "captcha": "1111", "message": "ERR_MES_PASS_REQUIRED"},

    {"name": "invalid_reg_user_4", "email": "inv_reg_user_4@ukr.net", "login": "invalid_reg_user_4", \
     "password": "*******", "captcha": "", "message": "ERR_MES_CAPTCH_REQUIRED"},

    {"name": "invalid_reg_user_5", "email": "inv_reg_user_5@ukr.net", "login": "логин_рус",
     "password": "*******", "captcha": "1111", "message": "ERR_MES_INVALID_LOGIN",
     "message_add": "ERR_MES_LOGIN_CYRILLIC"},

    {"name": "valid_reg_user", "email": email, "login": login, "password": password, "captcha": "1111",
     "message": "REGISTRATION_MES_OK"}

]


def get_user(name):
    try:
        for user in users:
            if user["name"] == name:
                return user
    except:
        print("\n     User %s is not defined, enter a valid user.\n" % name)
