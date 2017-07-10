from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import sys, unittest, random, string, http.client, json, time
sys.path.append("./models")
sys.path.append("./data")
import const

#订单API
class OrderAPI():

    def __init__(self):
        self.USER1_TOKEN = 'Token token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJpdHNteWNhci5jbiIsInVzZXJuYW1lIjoiMTgyNTkwMDAwMDkiLCJyb2xlIjoidXNlciJ9.bREYwz4odaJII3WOeqiYu5m2mrCbcBvnVOi5edPWr24'
        self.USER2_TOKEN = 'Token token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJpdHNteWNhci5jbiIsInVzZXJuYW1lIjoiMTU5NTgwNDMzMDMiLCJyb2xlIjoidXNlciJ9.SRGKTIW3PgZJ8EGl4A1OfEA5vTT-29C-woP9Z4RJTng'
        self.CITY_MANAGER_TOKEN = 'Token token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJpdHNteWNhci5jbiIsInVzZXJuYW1lIjoiMTgyNTkwMDAwMDQiLCJyb2xlIjoidXNlciJ9.BNzRm1mT8caCjKpzW7G-YaXHyefI82NE07XgiX4yAL0'
        self.RESOURCE_MANAGER_TOKEN = 'Token token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJpdHNteWNhci5jbiIsInVzZXJuYW1lIjoiMTgyNTkwMDAwMDUiLCJyb2xlIjoidXNlciJ9.etXjOGVuLx3yOSy_UE037oAsHDNcxZvMb1dKO-b3RfA'
        self.CAPITAL_MANAGER_TOKEN = 'Token token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJpdHNteWNhci5jbiIsInVzZXJuYW1lIjoiMTgyNTkwMDAwMDYiLCJyb2xlIjoidXNlciJ9.c8EIFXpPHwdqEWKsC9wK-3bxG6pKF5FbR6eoDQb-aBM'
        self.ACCOUNTANT_TOKEN = 'Token token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJpdHNteWNhci5jbiIsInVzZXJuYW1lIjoiMTgyNTkwMDAwMDgiLCJyb2xlIjoidXNlciJ9.fKov2on4KlpAgv2nQ3RBn-1Qtz0c8Nf4AosQpa9D1LM'

    def APIconnection(self, token, method, url, order_params):
        conn = http.client.HTTPConnection("staging.api.itsmycar.cn")
        headers = {'Authorization': token,  'Content-Type': 'application/json'}
        conn.request(method, url, json.dumps(order_params), headers)
        APIres = conn.getresponse()
        response = {
            'status': APIres.status,
            'reason': APIres.reason,
            'data': json.loads(APIres.read())
        }
        conn.close()
        print(response['status'], response['reason'])  #打印接口响应情况
        return response['data']

    def get_order(self):
        return self.APIconnection( self.USER1_TOKEN, "GET", "/v1/orders/%s" % self.order_id, "")

    def create(self):
        order_params = {
            'name': ''.join(random.choice(string.ascii_letters) for x in range(4)),
            'telephone': "1825906135" + str(random.randint(0,9)),
            'model_id': random.randint(2, 25)
        }
        data = self.APIconnection( self.USER1_TOKEN, "POST", "/v1/orders", order_params)
        self.order_id = data['id']

    def accept(self):
        self.APIconnection( self.USER2_TOKEN, "PUT", "/v1/orders/%s/accept" % self.order_id, "" )

    def sign(self):
        order_params = {
            'order_contract_images': const.IMAGES, #委托订购合同图片集
            'customer_info_images': const.IMAGES, #客户信息图片图片集
            'deposit_voucher_images': const.IMAGES #订金凭证图片图片集
        }
        self.APIconnection( self.USER2_TOKEN, "PUT", "/v1/orders/%s/sign" % self.order_id, order_params )

    def confirm_contract(self):
        order_params = {
            'selling_price': random.randint(0, 999999), #合同应收款总额
            'body_price': random.randint(0, 999999), #车身售价
            'selling_deposit_amount': random.randint(0, 999999), #客户订金收取
            'contract_number': 'ABCD201706'+ str(random.randint(10,30)) + 'X' #订单编号
        }
        self.APIconnection( self.CITY_MANAGER_TOKEN, "PUT", "/v1/orders/%s/confirm_contract" % self.order_id, order_params )

    def confirm_resource(self):
        order_params = {
            'buying_price': random.randint(0, 999999), #车身进价
            'buying_deposit_amount': random.randint(0, 999999), #资源订金支付
            'expected_time_of_pick_up': time.strftime('%Y-%m-%dT', time.localtime(time.time()+ random.randint(0, 9999999))), #预计提车时间
            'resource_contract_images': const.IMAGES, #资源合同图片集
        }
        self.APIconnection( self.RESOURCE_MANAGER_TOKEN, "PUT", "/v1/orders/%s/confirm_resource" % self.order_id, order_params )

    def confirm_capital(self):
        order_params = { 'advance': random.randint(0, 999999) } #预估垫资金额
        self.APIconnection( self.CAPITAL_MANAGER_TOKEN, "PUT", "/v1/orders/%s/confirm_capital" % self.order_id, order_params )

    def order_car(self):
        order_params = {
            'freight': random.randint(0, 9999), #大板运费
            'from_city_id': random.randint(0, 337), #发车城市
            'to_city_id': random.randint(0, 337), #到达城市
            'vehicle_examination_images': const.IMAGES
        }
        self.APIconnection( self.RESOURCE_MANAGER_TOKEN, "PUT", "/v1/orders/%s/order_car" % self.order_id, order_params )

    def fill_capital(self):
        order_params = {
            'actual_advance': random.randint(0, 999999),
            'actual_time_of_pick_up': time.strftime('%Y-%m-%dT', time.localtime(time.time()+ random.randint(0, 9999999))) #实际提车时间
        }
        self.APIconnection( self.CAPITAL_MANAGER_TOKEN, "PUT", "/v1/orders/%s/fill_capital" % self.order_id, order_params )

    def receive(self):
        order_params = {
            'actual_receive_at': time.strftime('%Y-%m-%dT', time.localtime(time.time()+ random.randint(0, 9999999))), #实际交车日期
            'plate_number': '闽D'+''.join(random.choice(string.ascii_letters.upper()) for x in range(5)), #车牌号
            'financial_service_fee': random.randint(0, 9999), #金融服务费
            'insurance_rebate': random.randint(0, 9999), #保险返点
            'plate_register_fee': random.randint(0, 9999), #报牌收取
            'accessory_profit': random.randint(0, 9999), #购买精品利润
            'other_income': random.randint(0, 9999), #其他收入合计
            'body_profit_modification': random.randint(0, 9999), #车身利润修正
            'extra_freight': random.randint(0, 9999), #小板运费
            'capital_cost': random.randint(0, 9999), #资金成本
            'plate_related_cost': random.randint(0, 9999), #上牌成本
            'accessory_gift_cost': random.randint(0, 9999), #赠送精品成本
            'other_cost': random.randint(0, 9999), #其他成本合计
            'store_sharing_profit': random.randint(0, 9999), #地面店分成
            'advisory_fees': random.randint(0, 9999), #顾问费
            'procedure_images': const.IMAGES, #车辆手续相关资料图片集
            'vehicles_delivery_images': const.IMAGES, #交车图片集
            'statement_images': const.IMAGES #客户应收款明细
        }
        self.APIconnection( self.CITY_MANAGER_TOKEN, "PUT", "/v1/orders/%s/receive" % self.order_id, order_params )

    def close(self):
        order_params = { 'payment_images': const.IMAGES }
        self.APIconnection( self.ACCOUNTANT_TOKEN, "PUT", "/v1/orders/%s/close" % self.order_id, order_params )

#订单Web端
class Order(OrderAPI):

    #订单执行命令初始化
    def __init__(self):
        OrderAPI.__init__(self)
        self.__APIcommands = {
            'create': self.create,
            'accept': self.accept,
            'sign': self.sign,
            'confirm_contract': self.confirm_contract,
            'confirm_resource': self.confirm_resource,
            'confirm_capital': self.confirm_capital,
            'order_car': self.order_car,
            'fill_capital': self.fill_capital,
            'receive': self.receive,
            'close': self.close
        }
        self.__cmds = ['create', 'accept', 'sign', 'confirm_contract', 'confirm_resource', 'confirm_capital', 'order_car', 'fill_capital', 'receive', 'close']

    #订单执行命令，传入步骤名称可顺序执行到该步骤
    def execute(self, command):
        for cmd in self.__cmds:
            self.__APIcommands[cmd]()
            if cmd == command: break;
        self.order_data = self.get_order()

    #进入订单详情页
    def get_order_detail(self, driver):
        time.sleep(const.WAIT_TIME)
        pending_list = WebDriverWait(driver, 20, 0.5).until(lambda driver: driver.find_element_by_xpath('//*[@id="react-app"]/div/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div[1]/div[2]/div[3]'))
        pending_list.click()
        time.sleep(const.WAIT_TIME)
        order_detail_button = WebDriverWait(driver, 20, 0.5).until(lambda driver: driver.find_element_by_xpath('//*[@id="react-app"]/div/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[2]/div/div/div/div[1]/div/div[1]/div[1]/div[4]'))
        order_detail_button.click()

    #点击确认订单按钮
    def check(self, driver, step):
        driver.find_element_by_xpath(const.CONFIRM_BUTTON[step]).click()
        time.sleep(const.WAIT_TIME)
        self.order_data = self.get_order()

    #输入订单数据，订单步骤：确认合同
    def confirm_contract_send_value(self, driver, values):
        for key in ['selling_price', 'body_price', 'selling_deposit_amount', 'contract_number']:
            driver.find_element_by_xpath(const.CONFIRM_CONTRACT_SEND_ELEMENT[key]).send_keys(values[key])
        driver.find_element_by_xpath(const.CONFIRM_CONTRACT_SEND_ELEMENT['send_button']).click()
        time.sleep(const.WAIT_TIME)

    #获取订单详情，订单步骤：确认合同
    def confirm_contract_get_value(self, driver):
        values = {}
        for key in ['selling_price', 'body_price', 'selling_deposit_amount']:
            values[key] = float(driver.find_element_by_xpath(const.ORDER_DETAIL_ELEMENT[key]).get_attribute('innerHTML').replace(',', ''))
        values['contract_number'] = driver.find_element_by_xpath(const.ORDER_DETAIL_ELEMENT['contract_number']).get_attribute('innerHTML')
        return values

    def confirm_resource_send_value(self, driver, values):
        for key in ['expected_time_of_pick_up_choose', 'expected_time_of_pick_up_day', 'expected_time_of_pick_up_confirm', 'confirm_resource_images', 'resource_contract_images_choose']:
            driver.find_element_by_xpath(const.CONFIRM_RESOURCE_SEND_ELEMENT[key]).click()
            time.sleep(const.WAIT_TIME)
        for key in ['buying_price', 'buying_deposit_amount', 'resource_contract_images']:
            driver.find_element_by_xpath(const.CONFIRM_RESOURCE_SEND_ELEMENT[key]).send_keys(values[key])
        time.sleep(const.WAIT_TIME)
        driver.find_element_by_xpath(const.CONFIRM_RESOURCE_SEND_ELEMENT['resource_contract_images_confirm']).click()
        time.sleep(const.WAIT_TIME)
        driver.find_element_by_xpath(const.CONFIRM_RESOURCE_SEND_ELEMENT['send_button']).click()
        time.sleep(const.WAIT_TIME)

    def confirm_resource_get_value(self, driver):
        values = {}
        for key in ['buying_price', 'buying_deposit_amount']:
            values[key] = float(driver.find_element_by_xpath(const.ORDER_DETAIL_ELEMENT[key]).get_attribute('innerHTML').replace(',', ''))
        values['expected_time_of_pick_up'] = driver.find_element_by_xpath(const.ORDER_DETAIL_ELEMENT['expected_time_of_pick_up']).get_attribute('innerHTML')
        return values

    def confirm_capital_send_value(self, driver, values):
         driver.find_element_by_xpath(const.CONFIRM_CAPITAL_SEND_ELEMENT['advance']).send_keys(values['advance'])
         driver.find_element_by_xpath(const.CONFIRM_CAPITAL_SEND_ELEMENT['send_button']).click()
         time.sleep(const.WAIT_TIME)

    def confirm_capital_get_value(self, driver):
         values = {}
         values['advance'] = float(driver.find_element_by_xpath(const.ORDER_DETAIL_ELEMENT['advance']).get_attribute('innerHTML').replace(',', ''))
         return values

    def order_car_send_value(self, driver, values):
        for key in ['from_city_id_1', 'from_city_id_2', 'from_city_id_3', 'to_city_id_1', 'to_city_id_2', 'to_city_id_3', 'order_car_images', 'vehicle_examination_images_choose' ]:
            driver.find_element_by_xpath(const.ORDER_CAR_SEND_ELEMENT[key]).click()
            time.sleep(const.WAIT_TIME)
        for key in ['freight', 'vehicle_examination_images']:
            driver.find_element_by_xpath(const.ORDER_CAR_SEND_ELEMENT[key]).send_keys(values[key])
        time.sleep(const.WAIT_TIME)
        driver.find_element_by_xpath(const.ORDER_CAR_SEND_ELEMENT['vehicle_examination_images_confirm']).click()
        driver.find_element_by_xpath(const.ORDER_CAR_SEND_ELEMENT['send_button']).click()
        time.sleep(const.WAIT_TIME)

    def order_car_get_value(self, driver):
        values = {}
        values['freight'] = float(driver.find_element_by_xpath(const.ORDER_DETAIL_ELEMENT['freight']).get_attribute('innerHTML').replace(',', ''))
        for key in ['from_city_id', 'to_city_id']:
            values[key] = driver.find_element_by_xpath(const.ORDER_DETAIL_ELEMENT[key]).get_attribute('innerHTML')
        return values

    def fill_capital_send_value(self, driver, values):
        driver.find_element_by_xpath(const.FILL_CAPITAL_SEND_ELEMENT['actual_advance']).send_keys(values['actual_advance'])
        for key in ['actual_time_of_pick_up_choose', 'actual_time_of_pick_up_day', 'actual_time_of_pick_up_confirm']:
            driver.find_element_by_xpath(const.FILL_CAPITAL_SEND_ELEMENT[key]).click()
            time.sleep(const.WAIT_TIME)
        driver.find_element_by_xpath(const.FILL_CAPITAL_SEND_ELEMENT['send_button']).click()
        time.sleep(const.WAIT_TIME)

    def fill_capital_get_value(self, driver):
        values = {}
        values['actual_advance'] = float(driver.find_element_by_xpath(const.ORDER_DETAIL_ELEMENT['actual_advance']).get_attribute('innerHTML').replace(',', ''))
        values['actual_time_of_pick_up'] = driver.find_element_by_xpath(const.ORDER_DETAIL_ELEMENT['actual_time_of_pick_up']).get_attribute('innerHTML')
        return values

    def receive_send_value(self, driver, values):
        driver.find_element_by_xpath(const.RECEIVE_SEND_ELEMENT['plate_number']).send_keys(values['plate_number'])
        for key in ['actual_receive_at_choose',
                    'actual_receive_at_day',
                    'actual_receive_at_confirm',
                    'receive_images']:
            driver.find_element_by_xpath(const.RECEIVE_SEND_ELEMENT[key]).click()
            time.sleep(const.WAIT_TIME)
        for key in [ 'procedure_images', 'vehicles_delivery_images', 'statement_images']:
            driver.find_element_by_xpath(const.RECEIVE_SEND_ELEMENT[key+'_choose']).click()
            driver.find_element_by_xpath(const.RECEIVE_SEND_ELEMENT[key]).send_keys(values[key])
            time.sleep(const.WAIT_TIME)
            driver.find_element_by_xpath(const.RECEIVE_SEND_ELEMENT[key+'_confirm']).click()
            time.sleep(const.WAIT_TIME)
        driver.find_element_by_xpath(const.RECEIVE_SEND_ELEMENT['send_button']).click()
        time.sleep(const.WAIT_TIME)

    def receive_get_value(self, driver):
        values = {}
        for key in ['actual_receive_at', 'plate_number']:
            values[key] = driver.find_element_by_xpath(const.ORDER_DETAIL_ELEMENT[key]).get_attribute('innerHTML')
        return values

    def close_send_value(self, driver, values):
        driver.find_element_by_xpath(const.CLOSE_ELEMENT['close_images']).click()
        time.sleep(const.WAIT_TIME)
        driver.find_element_by_xpath(const.CLOSE_ELEMENT['payment_images_choose']).click()
        driver.find_element_by_xpath(const.CLOSE_ELEMENT['payment_images']).send_keys(values['payment_images'])
        time.sleep(const.WAIT_TIME)
        driver.find_element_by_xpath(const.CLOSE_ELEMENT['payment_images_confirm']).click()
        time.sleep(const.WAIT_TIME)
        driver.find_element_by_xpath(const.CLOSE_ELEMENT['send_button']).click()
        time.sleep(const.WAIT_TIME)
