from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from contextlib import contextmanager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support.event_firing_webdriver import *
from selenium.common.exceptions import StaleElementReferenceException
import os


class Page(object):
    def __init__(self, driver, base_url=''):
        self.base_url = base_url
        self.driver = driver

    def find_displayed_element(self, *locator):
        count_time = 0
        count_elements = len(self.driver.find_elements(*locator))
        while count_time < 200 and count_elements <= 0:
            sleep(0.1)
            count_elements = len(self.driver.find_elements(*locator))
            count_time += 1
        if count_elements == 1:
            element = self.driver.find_elements(*locator)[0]
            # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
            if not element.is_displayed():
                count_time = 0
                while count_time < 200 and element.is_displayed() is False:
                    sleep(0.1)
                    count_time += 1
            if count_elements == 1 and not element.is_displayed():
                print("********!!!!!!!!!! Element found but not visible - ", locator)
        elif count_elements == 0:
            raise NoSuchElementException("********!!!!!!!!!! Element was not found - ", locator)
        return self.driver.find_elements(*locator)[0]

    @contextmanager
    def wait_for_page_load(self, timeout=30):
        old_page = self.driver.find_element_by_tag_name('html')
        yield
        WebDriverWait(self.driver, timeout).until(staleness_of(old_page))

    def wait_for_page_reload(self, locator):
        with self.wait_for_page_load(timeout=30):
            self.find_displayed_element(*locator)

    def wait_to_load_elements_qty(self, locator, elements_qty):
        count_time = 0
        count_elements = len(self.driver.find_elements(*locator))
        while count_time < 100 and count_elements != elements_qty:
            count_elements = len(self.driver.find_elements(*locator))
            # print("**************************real q-ty of elements", count_elements, "desired q-ty of elements", elements_qty)
            sleep(0.3)
            count_time += 1
        if count_elements != elements_qty:
            raise NoSuchElementException("********!!!!!!!!!! Something wrong with q-ty of searched elements - ",
                                         "real q-ty of elements", count_elements, "desired q-ty of elements",
                                         elements_qty)

    def wait_balance_change(self, initial_balance):
        count_time = 0
        while count_time < 100 and round(initial_balance - self.get_balance(), 2) == 0:
            sleep(0.1)
            count_time += 1
        return abs(round(initial_balance - self.get_balance(), 2))

    def count_load_elements(self, locator):
        count_time = 0
        count_elements = len(self.driver.find_elements(*locator))
        while count_time < 100 and count_elements <= 0:
            count_elements = len(self.driver.find_elements(*locator))
            sleep(0.1)
            count_time += 1

        count_time = 0
        count_elements = 0
        while count_time < 5 and count_elements != len(self.driver.find_elements(*locator)):
            count_elements = len(self.driver.find_elements(*locator))
            sleep(1)
            count_time += 1
        if count_elements == 0:
            raise NoSuchElementException("********!!!!!!!!!! No accessible bets were found - ", locator)
        return len(self.driver.find_elements(*locator))

    def open(self, url):
        url = self.base_url + url
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def hover(self, *locator):
        element = self.find_displayed_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def is_unique_element_displayed(self, *locator):
        count_time = 0
        count_elements = len(self.driver.find_elements(*locator))
        while count_time < 40 and count_elements == 0:
            count_elements = len(self.driver.find_elements(*locator))
            sleep(0.1)
            count_time += 1
        if count_elements == 1:
            element = self.find_displayed_element(*locator)
            if not element.is_displayed():
                count_time = 0
                while count_time < 40 and element.is_displayed() == False:
                    sleep(0.1)
                    count_time += 1
            if element.is_displayed():
                return True
            elif count_elements == 1 and not element.is_displayed():
                print("********!!!!!!!!!! Element found but not visible**************")
                return False
        elif count_elements == 0:
            print("********!!!!!!!!!! Element was not found**************")
            return False
        elif count_elements > 0:
            print("********!!!!!!!!!! More than 1 element were found************** - ", count_elements)
            return False

    def is_element_not_displayed(self, *locator):
        result = True
        count_time = 0
        count_elements = len(self.driver.find_elements(*locator))
        while count_time < 40 and count_elements <= 0:
            sleep(0.1)
            count_elements = len(self.driver.find_elements(*locator))
            count_time += 1
        if count_elements > 0:
            element = self.driver.find_elements(*locator)[0]
            # WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
            result = element.is_displayed()
            if result:
                count_time = 0
                while count_time < 40 and result is False:
                    sleep(0.1)
                    count_time += 1
        return result
