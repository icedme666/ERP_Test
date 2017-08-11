from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys, time
sys.path.append("./data")
import homepage_ele, page, login

#用户页面操作
class Homepage(page.Page):
    def __init__(self, driver, role=None):
        page.Page.__init__(self, driver)
        if role is not None:
            user_login = login.Login(self.driver)
            user_login.login(role)

    def get_homepage_title(self):
        return self.find(homepage_ele.USER_HOMEPAGE_TITLE).get_attribute('innerHTML')

    def get_count(self, count_key):
        return self.find(homepage_ele.COUNT[count_key]).get_attribute('innerHTML')

    def get_new_orders(self, sequence, key, status=None):
        return self.find(homepage_ele.NEW_ORDERS[key] % sequence).get_attribute('innerHTML') 
