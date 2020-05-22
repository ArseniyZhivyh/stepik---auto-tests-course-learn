# -*- coding: utf-8 -*-
"""
Created on Thu May 21 10:38:51 2020

@author: ars14
"""
from selenium.common.exceptions import NoSuchElementException
class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    def open(self): 
        self.browser.get(self.url)
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
            except (NoSuchElementException):
                return False
            return True
