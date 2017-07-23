import unittest
import driver

class ErpTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = driver.browser()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
