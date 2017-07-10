from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import sys, unittest
sys.path.append("./models")
import myunit, login, const

class loginTest(myunit.ErpTest):

    def test_citymanager_login_role(self):
        login.Login().user_login(self.driver, const.CITY_MANAGER)
        sleep(1)
        role_element = WebDriverWait(self.driver, 20, 0.5).until(lambda driver: self.driver.find_element_by_xpath('//*[@id="react-app"]/div/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]'))
        self.assertEqual(role_element.get_attribute('innerHTML'), u'城市经理')
        login.Login().user_logout(self.driver)

if __name__ == '__main__':
    unittest.main()
