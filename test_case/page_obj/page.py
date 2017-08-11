from selenium import webdriver
import time

class Page:
    def __init__(self, driver):
        self.driver = driver

    def find(self, ele_xpath, sleep=False):
        if sleep == True: time.sleep(10)
        return self.driver.find_element_by_xpath(ele_xpath)

    def alert(self, cmd='accept', sleep=False):
        if sleep == True: time.sleep(10)
        if cmd == 'accept': self.driver.switch_to_alert().accept()
