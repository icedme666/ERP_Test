from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys, time
sys.path.append("./data")
import user_ele, page

#用户页面操作
class Login(page.Page):
    def __init__(self, driver):
        page.Page.__init__(self, driver)

    def login(self, role):
        self.find(user_ele.USER_NAME_INPUT).clear()
        self.find(user_ele.USER_NAME_INPUT).send_keys(role['username'])
        self.find(user_ele.PASSWORD_INPUT).clear()
        self.find(user_ele.PASSWORD_INPUT).send_keys(role['password'])
        self.find(user_ele.PASSWORD_INPUT).send_keys(Keys.ENTER)
        time.sleep(10)

    def logout(self, role=None):
        self.find(user_ele.USER_CENTER_BUTTON, sleep=True).click()
        if role == None: self.find(user_ele.LOGOUT_BUTTON, sleep=True).click()
        if role == 'sales_director': self.find(user_ele.SALES_DIRECTOR_LOGOUT_BUTTON, sleep=True).click()
        self.alert(sleep=True)
        time.sleep(10)

    def get_login_title(self):
        return self.find(user_ele.LOGIN_TITLE).get_attribute('innerHTML')
