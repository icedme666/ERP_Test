from selenium import webdriver
import sys, time, random, unittest
sys.path.append("./models")
sys.path.append("./data")
import myunit, login, order, const

class ConfirmContractTest(myunit.ErpTest):
    ''' 订单流程：1.确认合同 '''

    @classmethod
    def setUpClass(self):
        print('城市经理确认合同')
        myunit.ErpTest.setUpClass()
        self.test_order = order.Order()
        self.test_order.execute('sign')
        login.Login().user_login(self.driver, const.CITY_MANAGER)
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

    def test_3_check(self):
        ''' 发送确认合同请求 '''
        random_values = {
            'selling_price': random.randint(0, 999999),  #合同应收款总额
            'body_price': random.randint(0, 999999),  #车身售价
            'selling_deposit_amount': random.randint(0, 999999),  #客户订金收取
            'contract_number': 'ABCD201706'+ str(random.randint(10,30)) + 'X' #订单编号
        }
        self.test_order.confirm_contract_send_value( self.driver, random_values)
        self.test_order.check(self.driver, 'confirm_contract')
        message_element = self.driver.find_element_by_xpath(const.STATUS_MESSAGE)
        self.assertEqual(message_element.get_attribute('innerHTML'), '城市经理已确认合同,待资源部确认车源')

    def test_4_after_selling_price(self):
        ''' 操作后订单详情： 合同应收款总额 '''
        self.assertEqual(self.test_order.confirm_contract_get_value( self.driver )['selling_price'], self.test_order.order_data['selling_price'])

    def test_5_after_body_price(self):
        ''' 操作后订单详情： 车身售价 '''
        self.assertEqual(self.test_order.confirm_contract_get_value( self.driver )['body_price'], self.test_order.order_data['body_price'])

    def test_6_after_selling_deposit_amount(self):
        ''' 操作后订单详情： 客户订金收取 '''
        self.assertEqual(self.test_order.confirm_contract_get_value( self.driver )['selling_deposit_amount'], self.test_order.order_data['selling_deposit_amount'])

    def test_7_after_contract_number(self):
        ''' 操作后订单详情： 订单编号 '''
        self.assertEqual(self.test_order.confirm_contract_get_value( self.driver )['contract_number'], self.test_order.order_data['contract_number'])
