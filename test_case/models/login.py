from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

class Login():

    def user_login(self, driver, role):
        username_element = driver.find_element_by_css_selector("input.rn-appearance-30o5oe:nth-child(3)")
        password_element = driver.find_element_by_css_selector("input.rn-appearance-30o5oe:nth-child(5)")
        username_element.clear()
        password_element.clear()
        username_element.send_keys(role['username'])
        password_element.send_keys(role['password'])
        password_element.send_keys(Keys.ENTER)

    def user_logout(self, driver):
        usercenter_element = WebDriverWait(driver, 20, 0.5).until(lambda driver: driver.find_element_by_xpath('//*[@id="react-app"]/div/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div[2]/div[3]'))
        usercenter_element.click()
        sleep(1)
        logout_element = WebDriverWait(driver, 20, 0.5).until(lambda driver: driver.find_element_by_xpath('//*[@id="react-app"]/div/div/div/div/div/div/div[2]/div[1]/div[1]/div[2]'))
        logout_element.click()
        driver.quit()
