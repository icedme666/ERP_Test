import random, string, time

def random_create_params():
    order_params = {
        'name': ''.join(random.choice(string.ascii_letters) for x in range(4)),
        'telephone': "1825906135" + str(random.randint(0,9)),
        'model_id': random.randint(2, 25)
    }
    return order_params

def random_sign_params():
    order_params = {
        'order_contract_images': ["http://www.sznews.com/szsbcar/images/0016ece1797b0841b20c22.jpg","http://www.sznews.com/szsbcar/images/0016ece1797b0841b20c22.jpg"], #委托订购合同图片集
        'customer_info_images': ["http://www.sznews.com/szsbcar/images/0016ece1797b0841b20c22.jpg","http://www.sznews.com/szsbcar/images/0016ece1797b0841b20c22.jpg"], #客户信息图片图片集
        'deposit_voucher_images': ["http://www.sznews.com/szsbcar/images/0016ece1797b0841b20c22.jpg","http://www.sznews.com/szsbcar/images/0016ece1797b0841b20c22.jpg"] #订金凭证图片图片集
    }
    return order_params

def random_confirm_contract_params():
    order_params = {
        'selling_price': random.randint(0, 999999), #合同应收款总额
        'body_price': random.randint(0, 999999), #车身售价
        'selling_deposit_amount': random.randint(0, 999999), #客户订金收取
        'contract_number': 'ABCD201706'+ str(random.randint(10,30)) + 'X' #订单编号
    }
    return order_params

def random_confirm_resource_params( purpose='api' ):
    api_order_params = {
        'buying_price': random.randint(0, 999999), #车身进价
        'buying_deposit_amount': random.randint(0, 999999), #资源订金支付
        'expected_time_of_pick_up': time.strftime('%Y-%m-%dT', time.localtime(time.time()+ random.randint(0, 9999999))), #预计提车时间
        'resource_contract_images': ["http://www.sznews.com/szsbcar/images/0016ece1797b0841b20c22.jpg","http://www.sznews.com/szsbcar/images/0016ece1797b0841b20c22.jpg"], #资源合同图片集
    }
    page_order_params = {
        'buying_price': random.randint(0, 999999), #车身进价
        'buying_deposit_amount': random.randint(0, 999999), #资源订金支付
    }
    if purpose == 'api': return api_order_params
    if purpose == 'page': return page_order_params


def random_confirm_capital_params():
    order_params = { 'advance': random.randint(0, 999999) } #预估垫资金额
    return order_params

def random_order_car_params( purpose='api' ):
    api_order_params = {
        'freight': random.randint(0, 9999), #大板运费
        'from_city_id': random.randint(0, 337), #发车城市
        'to_city_id': random.randint(0, 337), #到达城市
        'vehicle_examination_images': ["http://www.sznews.com/szsbcar/images/0016ece1797b0841b20c22.jpg","http://www.sznews.com/szsbcar/images/0016ece1797b0841b20c22.jpg"]
    }
    page_order_params = { 'freight': random.randint(0, 9999) }
    if purpose == 'api': return api_order_params
    if purpose == 'page': return page_order_params

def random_fill_capital_params( purpose='api' ):
    api_order_params = {
        'actual_advance': random.randint(0, 999999),
        'actual_time_of_pick_up': time.strftime('%Y-%m-%dT', time.localtime(time.time()+ random.randint(0, 9999999))) #实际提车时间
    }
    page_order_params = { 'actual_advance': random.randint(0, 999999) }
    if purpose == 'api': return api_order_params
    if purpose == 'page': return page_order_params

def random_receive_params( purpose='api' ):
    api_order_params = {
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
        'procedure_images': ["http://www.sznews.com/szsbcar/images/0016ece1797b0841b20c22.jpg","http://www.sznews.com/szsbcar/images/0016ece1797b0841b20c22.jpg"], #车辆手续相关资料图片集
        'vehicles_delivery_images': ["http://www.sznews.com/szsbcar/images/0016ece1797b0841b20c22.jpg","http://www.sznews.com/szsbcar/images/0016ece1797b0841b20c22.jpg"], #交车图片集
        'statement_images': ["http://www.sznews.com/szsbcar/images/0016ece1797b0841b20c22.jpg","http://www.sznews.com/szsbcar/images/0016ece1797b0841b20c22.jpg"] #客户应收款明细
    }
    page_order_params = {
        'plate_number': '闽D'+''.join(random.choice(string.ascii_letters.upper()) for x in range(5))
    }
    if purpose == 'api': return api_order_params
    if purpose == 'page': return page_order_params

def random_close_params():
    order_params = { 'payment_images': ["http://www.sznews.com/szsbcar/images/0016ece1797b0841b20c22.jpg","http://www.sznews.com/szsbcar/images/0016ece1797b0841b20c22.jpg"] }
    return order_params
