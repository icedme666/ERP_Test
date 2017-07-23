from selenium import webdriver
import sys, time
sys.path.append("./modules")
sys.path.append("./data")
sys.path.append("./page_obj")
import myunit, user_info, order_info, api_option, order_detail

class CloseTest(myunit.ErpTest):
    ''' 订单流程：7.完成结算 '''

    @classmethod
    def setUpClass(self):
        print('财务完成结算')
        myunit.ErpTest.setUpClass()
        self.api_order = api_option.OrderApi()
        self.api_order.execute('receive')
        self.order_page = order_detail.OrderDetail(self.driver, user_info.ACCOUNTANT)

    @classmethod
    def tearDownClass(self):
        myunit.ErpTest.tearDownClass()

    def test_1_before_name(self):
        ''' 操作前订单详情：客户姓名 '''
        name = self.order_page.get_detai_value('name')
        self.assertEqual( name, self.api_order.data['name'] )

    def test_2_before_telephone(self):
        ''' 操作前订单详情：客户电话 '''
        telephone = self.order_page.get_detai_value('telephone')
        self.assertEqual( telephone, self.api_order.data['telephone'] )

    def test_3_before_selling_price(self):
        ''' 操作前订单详情：合同应收款总额 '''
        selling_price = float(self.order_page.get_detai_value('selling_price').replace(',', ''))
        self.assertEqual( selling_price, self.api_order.data['selling_price'] )

    def test_4_before_body_price(self):
        ''' 操作前订单详情：车身售价 '''
        body_price = float(self.order_page.get_detai_value('body_price').replace(',', ''))
        self.assertEqual( body_price, self.api_order.data['body_price'] )

    def test_5_before_selling_deposit_amount(self):
        ''' 操作前订单详情：客户订金收取 '''
        selling_deposit_amount = float(self.order_page.get_detai_value('selling_deposit_amount').replace(',', ''))
        self.assertEqual( selling_deposit_amount, self.api_order.data['selling_deposit_amount'] )

    def test_6_before_contract_number(self):
        ''' 操作前订单详情：订单编号 '''
        contract_number = self.order_page.get_detai_value('contract_number')
        self.assertEqual( contract_number, self.api_order.data['contract_number'] )

    def test_7_before_buying_price(self):
        ''' 操作前订单详情：车身进价 '''
        buying_price = float(self.order_page.get_detai_value('buying_price').replace(',', ''))
        self.assertEqual( buying_price, self.api_order.data['buying_price'] )

    def test_8_before_buying_deposit_amount(self):
        ''' 操作前订单详情：资源订金支付 '''
        buying_deposit_amount = float(self.order_page.get_detai_value('buying_deposit_amount').replace(',', ''))
        self.assertEqual( buying_deposit_amount, self.api_order.data['buying_deposit_amount'] )

    def test_9_before_expected_time_of_pick_up(self):
        ''' 操作前订单详情：预计提车时间 '''
        expected_time_of_pick_up = self.order_page.get_detai_value('expected_time_of_pick_up')
        self.assertEqual( expected_time_of_pick_up, self.api_order.data['expected_time_of_pick_up'][:10] )

    def test__10_before_buying_advance(self):
        ''' 操作前订单详情： 预估垫资金额 '''
        advance = float(self.order_page.get_detai_value('advance').replace(',', ''))
        self.assertEqual( advance, self.api_order.data['advance'] )

    def test__11_before_freight(self):
        ''' 操作前订单详情: 大板运费 '''
        freight = float(self.order_page.get_detai_value('freight').replace(',', ''))
        self.assertEqual( freight, self.api_order.data['freight'] )

    def test__12_before_actual_advance(self):
        ''' 操作前订单详情: 实际垫资金额 '''
        actual_advance = float(self.order_page.get_detai_value('actual_advance').replace(',', ''))
        self.assertEqual( actual_advance, self.api_order.data['actual_advance'] )

    def test__13_before_actual_time_of_pick_up(self):
        ''' 操作前订单详情: 实际提车时间 '''
        actual_time_of_pick_up = self.order_page.get_detai_value('actual_time_of_pick_up')
        self.assertEqual( actual_time_of_pick_up, self.api_order.data['actual_time_of_pick_up'][:10] )

    def test__14_before_actual_receive_at(self):
        ''' 操作前订单详情：实际交车日期 '''
        actual_receive_at = self.order_page.get_detai_value('actual_receive_at')
        self.assertEqual( actual_receive_at, self.api_order.data['actual_receive_at'][:10] )

    def test__15_before_plate_number(self):
        ''' 操作前订单详情：车牌号 '''
        plate_number = self.order_page.get_detai_value('plate_number')
        self.assertEqual( plate_number, self.api_order.data['plate_number'] )

    def test__16_check(self):
        ''' 发送完成结算请求 '''
        self.order_page.send_images( 'close' )
        self.order_page.send_values( 'close' )
        self.order_page.check( 'close' )
        self.api_order.get_a_order()
        status_message = self.order_page.get_status_message()
        self.assertEqual( status_message, '订单已完成')
