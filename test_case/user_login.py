from selenium import webdriver
import sys, time
sys.path.append("./modules")
sys.path.append("./data")
sys.path.append("./page_obj")
import myunit, user_info, api_option, login, homepage

class LoginTest(myunit.ErpTest):

    @classmethod
    def setUpClass(self):
        print('各角色用户登录')
        myunit.ErpTest.setUpClass()
        self.login_page = login.Login(self.driver)
        self.homepage = homepage.Homepage(self.driver)

    @classmethod
    def tearDownClass(self):
        myunit.ErpTest.tearDownClass()

    def test_1_store_manager_login(self):
        ''' 店铺经理登录 '''
        self.login_page.login(user_info.STORE_MANAGER)
        self.assertEqual( self.homepage.get_homepage_title(), '店铺经理' )

    def test_2_store_manager_logout(self):
        ''' 店铺经理退出 '''
        self.login_page.logout()
        self.assertEqual( self.login_page.get_login_title(), '登录' )

    def test_3_resource_manager_login(self):
        ''' 资源经理登录 '''
        self.login_page.login(user_info.RESOURCE_MANAGER)
        self.assertEqual( self.homepage.get_homepage_title(), '资源经理' )

    def test_4_resource_manager_logout(self):
        ''' 资源经理退出 '''
        self.login_page.logout()
        self.assertEqual( self.login_page.get_login_title(), '登录' )

    def test_5_capital_manager_login(self):
        ''' 资金经理登录 '''
        self.login_page.login(user_info.CAPITAL_MANAGER)
        self.assertEqual( self.homepage.get_homepage_title(), '资金经理' )

    def test_6_capital_manager_logout(self):
        ''' 资金经理退出 '''
        self.login_page.logout()
        self.assertEqual( self.login_page.get_login_title(), '登录' )

    def test_7_capital_assistant_login(self):
        ''' 资金助理登录 '''
        self.login_page.login(user_info.CAPITAL_ASSISTANT)
        self.assertEqual( self.homepage.get_homepage_title(), '资金助理' )

    def test_8_capital_assistant_logout(self):
        ''' 资金助理退出 '''
        self.login_page.logout()
        self.assertEqual( self.login_page.get_login_title(), '登录' )

    def test_9_capital_assistant_login(self):
        ''' 资金助理登录 '''
        self.login_page.login(user_info.CAPITAL_ASSISTANT)
        self.assertEqual( self.homepage.get_homepage_title(), '资金助理' )

    def test__10_capital_assistant_logout(self):
        ''' 资金助理退出 '''
        self.login_page.logout()
        self.assertEqual( self.login_page.get_login_title(), '登录' )

    def test__11_accountant_login(self):
        ''' 财务登录 '''
        self.login_page.login(user_info.ACCOUNTANT)
        self.assertEqual( self.homepage.get_homepage_title(), '财务' )

    def test__12_accountant_logout(self):
        ''' 财务退出 '''
        self.login_page.logout()
        self.assertEqual( self.login_page.get_login_title(), '登录' )

    def test__13_sales_director_login(self):
        ''' 销售总监登录 '''
        self.login_page.login(user_info.SALES_DIRECTOR)
        self.assertEqual( self.homepage.get_homepage_title(), '销售总监' )

    def test__14_sales_director_logout(self):
        ''' 销售总监退出 '''
        self.login_page.logout( role='sales_director' )
        self.assertEqual( self.login_page.get_login_title(), '登录' )
