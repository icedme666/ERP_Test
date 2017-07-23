from selenium import webdriver
import sys, time
sys.path.append("./modules")
sys.path.append("./data")
sys.path.append("./page_obj")
import myunit, user_info, order_info, api_option, order_detail

class ConfirmContractTest(myunit.ErpTest):
    ''' 订单流程：1.确认合同 '''

    @classmethod
    def setUpClass(self):
        print('城市经理确认合同')
        myunit.ErpTest.setUpClass()
        self.api_order = api_option.OrderApi()
        self.api_order.execute('sign')
        self.order_page = order_detail.OrderDetail(self.driver, user_info.STORE_MANAGER)

    @classmethod
    def tearDownClass(self):
        myunit.ErpTest.tearDownClass()

    def test_1_before_name(self):
        ''' 操作前订单详情： 客户姓名 '''
        name = self.order_page.get_detai_value('name')
        self.assertEqual( name, self.api_order.data['name'] )

    def test_2_before_telephone(self):
        ''' 操作前订单详情： 客户电话 '''
        telephone = self.order_page.get_detai_value('telephone')
        self.assertEqual( telephone, self.api_order.data['telephone'] )

    def test_3_check(self):
        ''' 发送确认合同请求 '''
        self.order_page.send_values( 'confirm_contract', order_info.random_confirm_contract_params() )
        self.order_page.check( 'confirm_contract')
        self.api_order.get_a_order()
        status_message = self.order_page.get_status_message()
        self.assertEqual( status_message , '店铺经理已确认合同,待资源部确认车源')

    def test_4_after_selling_price(self):
        ''' 操作后订单详情： 合同应收款总额 '''
        selling_price = float(self.order_page.get_detai_value('selling_price').replace(',', ''))
        self.assertEqual(selling_price, self.api_order.data['selling_price'])

    def test_5_after_body_price(self):
        ''' 操作后订单详情： 车身售价 '''
        body_price = float(self.order_page.get_detai_value('body_price').replace(',', ''))
        self.assertEqual(body_price, self.api_order.data['body_price'])

    def test_6_after_selling_deposit_amount(self):
        ''' 操作后订单详情： 客户订金收取 '''
        selling_deposit_amount = float(self.order_page.get_detai_value('selling_deposit_amount').replace(',', ''))
        self.assertEqual(selling_deposit_amount, self.api_order.data['selling_deposit_amount'])

    def test_7_after_contract_number(self):
        ''' 操作后订单详情： 订单编号 '''
        contract_number = self.order_page.get_detai_value('contract_number')
        self.assertEqual(contract_number, self.api_order.data['contract_number'])
