# -*- coding: utf-8 -*-
"""
Created on Thu May 21 10:38:51 2020

@author: ars14
"""
class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self): 
        self.browser.get(self.url)

