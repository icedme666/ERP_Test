from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import sys, time, random, string,  unittest
sys.path.append("./models")
sys.path.append("./data")
import myunit, login, const, order

class ReceiveTest(myunit.ErpTest):
    ''' 订单流程：6.确认交车 '''

    @classmethod
    def setUpClass(self):
        print('城市经理确认交车')
        myunit.ErpTest.setUpClass()
        self.test_order = order.Order()
        self.test_order.execute('fill_capital')
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

    def test_7_before_buying_price(self):
        ''' 操作前订单详情： 车身进价 '''
        self.assertEqual(self.test_order.confirm_resource_get_value( self.driver )['buying_price'], self.test_order.order_data['buying_price'])

    def test_8_before_buying_deposit_amount(self):
        ''' 操作前订单详情： 资源订金支付 '''
        self.assertEqual(self.test_order.confirm_resource_get_value( self.driver )['buying_deposit_amount'], self.test_order.order_data['buying_deposit_amount'])

    def test_9_before_expected_time_of_pick_up(self):
        ''' 操作前订单详情： 预计提车时间 '''
        self.assertEqual(self.test_order.confirm_resource_get_value( self.driver )['expected_time_of_pick_up'], self.test_order.order_data['expected_time_of_pick_up'][0:10])

    def test__10_before_buying_advance(self):
        ''' 操作前订单详情： 预估垫资金额 '''
        self.assertEqual(self.test_order.confirm_capital_get_value( self.driver )['advance'], self.test_order.order_data['advance'])

    def test__11_before_freight(self):
        ''' 操作前订单详情: 大板运费 '''
        self.assertEqual(self.test_order.order_car_get_value( self.driver )['freight'], self.test_order.order_data['freight'])

    def test__12_before_actual_advance(self):
        ''' 操作前订单详情: 实际垫资金额 '''
        self.assertEqual(self.test_order.fill_capital_get_value( self.driver )['actual_advance'], self.test_order.order_data['actual_advance'])

    def test__13_before_actual_time_of_pick_up(self):
        ''' 操作前订单详情: 实际提车时间 '''
        self.assertEqual(self.test_order.fill_capital_get_value( self.driver )['actual_time_of_pick_up'], self.test_order.order_data['actual_time_of_pick_up'][0:10])

    def test__14_check(self):
        ''' 发送完成交车请求 '''
        #time.sleep(100000)
        random_values = {
            'plate_number': '闽D'+''.join(random.choice(string.ascii_letters.upper()) for x in range(5)),
            'procedure_images': '/Users/iced_me/Desktop/Work/images/04.jpg',
            'vehicles_delivery_images': '/Users/iced_me/Desktop/Work/images/05.jpg',
            'statement_images': '/Users/iced_me/Desktop/Work/images/06.jpg'
        }
        self.test_order.receive_send_value( self.driver, random_values)
        self.test_order.check(self.driver, 'receive')
        message_element = self.driver.find_element_by_xpath(const.STATUS_MESSAGE)
        self.assertEqual(message_element.get_attribute('innerHTML'), '城市经理已完成交车,待财务结算奖励')

    def test__15_after_actual_receive_at(self):
        ''' 操作后订单详情：实际交车日期 '''
        self.assertEqual(self.test_order.receive_get_value( self.driver )['actual_receive_at'], self.test_order.order_data['actual_receive_at'][0:10])

    def test__16_after_plate_number(self):
        ''' 操作后订单详情：车牌号 '''
        self.assertEqual(self.test_order.receive_get_value( self.driver )['plate_number'], self.test_order.order_data['plate_number'])
