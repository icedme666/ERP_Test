from selenium import webdriver
import unittest
from driver import browser

class ErpTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = browser()
        self.driver.maximize_window()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
