from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

def before_scenario(self, scenario):
    self.driver = webdriver.Chrome()
    self.tc = unittest.TestCase()
    self.by = By

    self.driver.get("http://localhost/")  


def after_scenario(self, scenario):
    self.driver.quit()