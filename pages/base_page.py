from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from config.constants import *

class BasePage():

    def __init__(self, browser):
        self.browser = browser


    def open (self, url):
        self.browser.get(url)

    def home_page_load(self, locator, time=10):
        try:
            WebDriverWait(self.browser, time).until(
            EC.visibility_of_element_located((locator))
        )
        except(NoSuchElementException, TimeoutException):
            return False
        return True
    
    def button_entrance(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(
            EC.element_to_be_clickable((locator))
        )
    
    def ch_list_entance(self, locator, time=10):
        try:
            WebDriverWait(self.browser, time).until(
            EC.visibility_of_element_located((locator))
        )
        except(NoSuchElementException, TimeoutException):
            return False
        return True

    def field_email(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(
            EC.element_to_be_clickable((locator))
        )
    
    def ch_field_email(self, locator, email, time=15):
        try:
            WebDriverWait(self.browser, time).until(
            EC.text_to_be_present_in_element_value((locator),email)
            )
        except(NoSuchElementException, TimeoutException):
            return False
        return True
    
    def field_password(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(
            EC.element_to_be_clickable((locator))
        )
    
    def ch_field_password(self, locator, password, time=15):
        try:
            WebDriverWait(self.browser, time).until(
            EC.text_to_be_present_in_element_value((locator),password)
            )
        except(NoSuchElementException, TimeoutException):
            return False
        return True
    
    def button_authorization(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(
            EC.visibility_of_element_located((locator))
        )
    
    def ch_succes_authorization(self, locator, time=10):
        try:
            WebDriverWait(self.browser, time).until(
            EC.visibility_of_element_located((locator))
        )
        except(NoSuchElementException, TimeoutException):
            return False
        return True