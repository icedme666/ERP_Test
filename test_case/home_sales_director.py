from selenium import webdriver
import sys
sys.path.append("./modules")
sys.path.append("./data")
sys.path.append("./page_obj")
import myunit, user_info, api_option, homepage

class HomeSalesDirectorTest(myunit.ErpTest):
    ''' 销售总监主页 '''

    @classmethod
    def setUpClass(self):
        print('销售总监主页')
        myunit.ErpTest.setUpClass()
        self.home = homepage.Homepage( self.driver, user_info.SALES_DIRECTOR )
        sales_director = api_option.UserApi(user_info.SALES_DIRECTOR)
        self.my_stats = sales_director.get_my_stats()
        self.new_orders = api_option.OrderApi().get_orders(token=sales_director.get_token(), page=1, per_page=5, order='updated_at%20desc')['data']
        self.status = user_info.SALES_DIRECTOR_STATUS

    @classmethod
    def tearDownClass(self):
        myunit.ErpTest.tearDownClass()

    def test_1_pending_count(self):
        ''' 销售总监：待处理订单数量 '''
        self.assertEqual( self.home.get_count('pending_count'), str(self.my_stats['pending_count']))

    def test_2_onging_count(self):
        ''' 销售总监：进行中订单数量 '''
        self.assertEqual( self.home.get_count('onging_count'), str(self.my_stats['onging_count']))

    def test_3_closed_count(self):
        ''' 销售总监：已完成订单数量 '''
        self.assertEqual( self.home.get_count('closed_count'), str(self.my_stats['closed_count']))

    def test_4_terminated_count(self):
        ''' 销售总监：已取消订单数量 '''
        self.assertEqual( self.home.get_count('terminated_count'), str(self.my_stats['terminated_count']))

    def test_5_employed_count(self):
        ''' 销售总监：店铺经理数量 '''
        self.assertEqual( self.home.get_count('store_manager_count'), str(self.my_stats['store_manager_count']))

    def test_6_new_orders_1_model(self):
        ''' 销售总监：最新5条订单之1--车型 '''
        self.assertEqual(self.home.get_new_orders('1', 'model'), self.new_orders[0]['model']['name'])

    def test_7_new_orders_1_name(self):
        ''' 销售总监：最新5条订单之1--姓名 '''
        self.assertEqual(self.home.get_new_orders( '1', 'name')[72:-20], self.new_orders[0]['name'])

    def test_8_new_orders_1_aasm_state(self):
        ''' 销售总监：最新5条订单之1--订单状态 '''
        key =self.new_orders[0]['aasm_state']
        status_str = self.home.get_new_orders( '1', 'aasm_state1') + '(' + self.home.get_new_orders( '1', 'aasm_state2')[69:-65] + ')'
        self.assertEqual( status_str, self.status[key])

    def test_9_new_orders_1_update_time(self):
        ''' 销售总监：最新5条订单之1--更新时间 '''
        time = self.new_orders[0]['updated_at'][:10] + ' ' +  self.new_orders[0]['updated_at'][11:19]
        self.assertEqual( self.home.get_new_orders('1', 'updated_at'), time)

    def test__10_new_orders_2_model(self):
        ''' 销售总监：最新5条订单之2--车型 '''
        self.assertEqual(self.home.get_new_orders('2', 'model'), self.new_orders[1]['model']['name'])

    def test__11_new_orders_2_name(self):
        ''' 销售总监：最新5条订单之2--姓名 '''
        self.assertEqual(self.home.get_new_orders( '2', 'name')[72:-20], self.new_orders[1]['name'])

    def test__12_new_orders_2_aasm_state(self):
        ''' 销售总监：最新5条订单之2--订单状态 '''
        key =self.new_orders[1]['aasm_state']
        status_str = self.home.get_new_orders( '2', 'aasm_state1') + '(' + self.home.get_new_orders( '2', 'aasm_state2')[69:-65] + ')'
        self.assertEqual( status_str, self.status[key])

    def test__13_new_orders_2_update_time(self):
        ''' 销售总监：最新5条订单之2--更新时间 '''
        time = self.new_orders[1]['updated_at'][:10] + ' ' +  self.new_orders[1]['updated_at'][11:19]
        self.assertEqual( self.home.get_new_orders('2', 'updated_at'), time)

    def test__14_new_orders_3_model(self):
        ''' 销售总监：最新5条订单之3--车型 '''
        self.assertEqual(self.home.get_new_orders('3', 'model'), self.new_orders[2]['model']['name'])

    def test__15_new_orders_3_name(self):
        ''' 销售总监：最新5条订单之3--姓名 '''
        self.assertEqual(self.home.get_new_orders( '3', 'name')[72:-20], self.new_orders[2]['name'])

    def test__16_new_orders_3_aasm_state(self):
        ''' 销售总监：最新5条订单之3--订单状态 '''
        key =self.new_orders[2]['aasm_state']
        status_str = self.home.get_new_orders( '3', 'aasm_state1') + '(' + self.home.get_new_orders( '3', 'aasm_state2')[69:-65] + ')'
        self.assertEqual( status_str, self.status[key])

    def test__17_new_orders_3_update_time(self):
        ''' 销售总监：最新5条订单之3--更新时间 '''
        time = self.new_orders[2]['updated_at'][:10] + ' ' +  self.new_orders[2]['updated_at'][11:19]
        self.assertEqual( self.home.get_new_orders('3', 'updated_at'), time)

    def test__18_new_orders_4_model(self):
        ''' 销售总监：最新5条订单之4--车型 '''
        self.assertEqual(self.home.get_new_orders('4', 'model'), self.new_orders[3]['model']['name'])

    def test__19_new_orders_4_name(self):
        ''' 销售总监：最新5条订单之4--姓名 '''
        self.assertEqual(self.home.get_new_orders( '4', 'name')[72:-20], self.new_orders[3]['name'])

    def test___20_new_orders_4_aasm_state(self):
        ''' 销售总监：最新5条订单之4--订单状态 '''
        key =self.new_orders[3]['aasm_state']
        status_str = self.home.get_new_orders( '4', 'aasm_state1') + '(' + self.home.get_new_orders( '4', 'aasm_state2')[69:-65] + ')'
        self.assertEqual( status_str, self.status[key])

    def test___21_new_orders_4_update_time(self):
        ''' 销售总监：最新5条订单之4--更新时间 '''
        time = self.new_orders[3]['updated_at'][:10] + ' ' +  self.new_orders[3]['updated_at'][11:19]
        self.assertEqual( self.home.get_new_orders('4', 'updated_at'), time)

    def test___22_new_orders_5_model(self):
        ''' 销售总监：最新5条订单之5--车型 '''
        self.assertEqual(self.home.get_new_orders('5', 'model'), self.new_orders[4]['model']['name'])

    def test___23_new_orders_5_name(self):
        ''' 销售总监：最新5条订单之5--姓名 '''
        self.assertEqual(self.home.get_new_orders( '5', 'name')[72:-20], self.new_orders[4]['name'])

    def test___24_new_orders_5_aasm_state(self):
        ''' 销售总监：最新5条订单之5--订单状态 '''
        key =self.new_orders[4]['aasm_state']
        status_str = self.home.get_new_orders( '5', 'aasm_state1') + '(' + self.home.get_new_orders( '5', 'aasm_state2')[69:-65] + ')'
        self.assertEqual( status_str, self.status[key])

    def test___25_new_orders_5_update_time(self):
        ''' 销售总监：最新5条订单之5--更新时间 '''
        time = self.new_orders[4]['updated_at'][:10] + ' ' +  self.new_orders[4]['updated_at'][11:19]
        self.assertEqual( self.home.get_new_orders('5', 'updated_at'), time)
