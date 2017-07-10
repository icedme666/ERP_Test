from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import sys, time, random, unittest
sys.path.append("./models")
sys.path.append("./data")
import myunit, login, const, order

class ConfirmResourceTest(myunit.ErpTest):
    ''' 订单流程：2.确认车源 '''

    @classmethod
    def setUpClass(self):
        print('资源经理确认车源')
        myunit.ErpTest.setUpClass()
        self.test_order = order.Order()
        self.test_order.execute('confirm_contract')
        login.Login().user_login(self.driver, const.RESOURCE_MANAGER)
        self.test_order.get_order_detail(self.driver)
        time.sleep(const.WAIT_TIME)

    @classmethod
    def tearDownClass(self):
        time.sleep(const.WAIT_TIME)
        myunit.ErpTest.tearDownClass()

    def test_1_before_name(self):
        ''' 操作前订单详情： 客户姓名 '''
        name_element = self.driver.find_element_by_xpath(const.ORDER_DETAIL_ELEMENT['name'])
        self.assertEqual(name_element.get_attribute('innerHTML'), self.test_order.order_data['name'])

    def test_2_before_telephone(self):
        ''' 操作前订单详情： 客户电话 '''
        tele_element = self.driver.find_element_by_xpath(const.ORDER_DETAIL_ELEMENT['telephone'])
        self.assertEqual(tele_element.get_attribute('innerHTML'), self.test_order.order_data['telephone'])

    def test_3_before_selling_price(self):
        ''' 操作前订单详情： 合同应收款总额 '''
        self.assertEqual(self.test_order.confirm_contract_get_value( self.driver )['selling_price'], self.test_order.order_data['selling_price'])

    def test_4_before_body_price(self):
        ''' 操作前订单详情： 车身售价 '''
        self.assertEqual(self.test_order.confirm_contract_get_value( self.driver )['body_price'], self.test_order.order_data['body_price'])

    def test_5_before_selling_deposit_amount(self):
        ''' 操作前订单详情： 客户订金收取 '''
        self.assertEqual(self.test_order.confirm_contract_get_value( self.driver )['selling_deposit_amount'], self.test_order.order_data['selling_deposit_amount'])

    def test_6_before_contract_number(self):
        ''' 操作前订单详情： 订单编号 '''
        self.assertEqual(self.test_order.confirm_contract_get_value( self.driver )['contract_number'], self.test_order.order_data['contract_number'])

    def test_7_check(self):
        ''' 发送确认车源请求 '''
        random_values = {
            'buying_price': random.randint(0, 999999), #车身进价
            'buying_deposit_amount': random.randint(0, 999999), #资源订金支付
            'resource_contract_images': '/Users/iced_me/Desktop/Work/images/01.jpg', #资源合同图片集
        }
        self.test_order.confirm_resource_send_value( self.driver,random_values)
        self.test_order.check(self.driver, 'confirm_resource')
        message_element = self.driver.find_element_by_xpath(const.STATUS_MESSAGE)
        self.assertEqual(message_element.get_attribute('innerHTML'), '资源部已确认车源,待资金中心确认垫资')

    def test_8_after_buying_price(self):
        ''' 操作后订单详情： 车身进价 '''
        self.assertEqual(self.test_order.confirm_resource_get_value( self.driver )['buying_price'], self.test_order.order_data['buying_price'])

    def test_9_after_buying_deposit_amount(self):
        ''' 操作后订单详情： 资源订金支付 '''
        self.assertEqual(self.test_order.confirm_resource_get_value( self.driver )['buying_deposit_amount'], self.test_order.order_data['buying_deposit_amount'])

    def test__10_after_expected_time_of_pick_up(self):
        ''' 操作后订单详情： 预计提车时间 '''
        self.assertEqual(self.test_order.confirm_resource_get_value( self.driver )['expected_time_of_pick_up'], self.test_order.order_data['expected_time_of_pick_up'][0:10])
