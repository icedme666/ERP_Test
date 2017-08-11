from selenium import webdriver
import sys, time
sys.path.append("./modules")
sys.path.append("./data")
sys.path.append("./page_obj")
import myunit, user_info, order_info, api_option, order_detail

class ConfirmCapitalTest(myunit.ErpTest):
    ''' 订单流程：3.确认垫资 '''

    @classmethod
    def setUpClass(self):
        print('资金经理确认垫资')
        myunit.ErpTest.setUpClass()
        self.api_order = api_option.OrderApi()
        self.api_order.execute('confirm_resource')
        self.order_page = order_detail.OrderDetail(self.driver, user_info.CAPITAL_MANAGER)

    @classmethod
    def tearDownClass(self):
        myunit.ErpTest.tearDownClass()

    def test_1_before_name(self):
        ''' 操作前订单详情： 客户姓名 '''
        name = self.order_page.get_detai_value('客户姓名')
        self.assertEqual( name, self.api_order.data['name'] )

    def test_2_before_telephone(self):
        ''' 操作前订单详情： 客户电话 '''
        telephone = self.order_page.get_detai_value('客户电话')
        self.assertEqual( telephone, self.api_order.data['telephone'] )

    def test_3_before_selling_price(self):
        ''' 操作前订单详情： 合同应收款总额 '''
        selling_price = float(self.order_page.get_detai_value('合同应收款总额(元)').replace(',', ''))
        self.assertEqual( selling_price, self.api_order.data['selling_price'] )

    def test_4_before_body_price(self):
        ''' 操作前订单详情： 车身售价 '''
        body_price = float(self.order_page.get_detai_value('车身售价(元)').replace(',', ''))
        self.assertEqual( body_price, self.api_order.data['body_price'] )

    def test_5_before_selling_deposit_amount(self):
        ''' 操作前订单详情： 客户订金收取 '''
        selling_deposit_amount = float(self.order_page.get_detai_value('客户订金收取(元)').replace(',', ''))
        self.assertEqual( selling_deposit_amount, self.api_order.data['selling_deposit_amount'] )

    def test_6_before_contract_number(self):
        ''' 操作前订单详情： 订单编号 '''
        contract_number = self.order_page.get_detai_value('订单编号')
        self.assertEqual( contract_number, self.api_order.data['contract_number'] )

    def test_7_before_buying_price(self):
        ''' 操作前订单详情： 车身进价 '''
        buying_price = float(self.order_page.get_detai_value('车身进价(元)').replace(',', ''))
        self.assertEqual( buying_price, self.api_order.data['buying_price'] )

    def test_8_before_buying_deposit_amount(self):
        ''' 操作前订单详情： 资源订金支付 '''
        buying_deposit_amount = float(self.order_page.get_detai_value('资源订金支付(元)').replace(',', ''))
        self.assertEqual( buying_deposit_amount, self.api_order.data['buying_deposit_amount'] )

    def test_9_before_expected_time_of_pick_up(self):
        ''' 操作前订单详情： 预计提车时间 '''
        expected_time_of_pick_up = self.order_page.get_detai_value('预计提车时间')
        self.assertEqual( expected_time_of_pick_up, self.api_order.data['expected_time_of_pick_up'][:10] )

    def test__10_check(self):
        ''' 发送确认垫资请求 '''
        self.order_page.send_values( 'confirm_capital', order_info.random_confirm_capital_params() )
        self.order_page.check()
        self.api_order.get_a_order()
        status_message = self.order_page.get_status_message()
        self.assertEqual( status_message, '资金中心已确认垫资,待资源部完成订车')

    def test__11_after_advance(self):
        ''' 操作后订单详情： 预估垫资金额 '''
        advance = float(self.order_page.get_detai_value('预估垫资金额(元)').replace(',', ''))
        self.assertEqual( advance, self.api_order.data['advance'] )
