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
        self.find(user_ele.PASSWORD_INPUT).clear()
        self.find(user_ele.USER_NAME_INPUT).send_keys(role['username'])
        self.find(user_ele.PASSWORD_INPUT).send_keys(role['password'])
        self.find(user_ele.PASSWORD_INPUT).send_keys(Keys.ENTER)
        time.sleep(10)

    def logout(self):
        self.find(user_ele.USER_CENTER_BUTTON).click()
        time.sleep(const.WAIT_TIME)
        self.find(user_ele.LOGOUT_BUTTON).click()
        self.driver.quit()
