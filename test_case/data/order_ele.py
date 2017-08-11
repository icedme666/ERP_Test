from selenium import webdriver
import random

#ERP待领取列表
PENDING_LIST_BUTTON = '//div[text()="待处理"]/..'    #待领取tab按钮
ORDER_DETAIL_BUTTON = '//div[text()="查看订单详细"]/..'    #查看订单详情第一个按钮

#ERP订单详情页
DETAIL_VALUE = '//div[text()="%s"]/../following-sibling::div[1]/div'    #订单右侧参数数值
INPUT_VALUE = '//div[text()="%s"]/../..//input'
CONFIRM_BUTTON = '//div[text()="%s"]/..'    #订单提交按钮
CHECK_BUTTON = '//div[text()="确认"]/..'    #订单确认按钮
CONFIRM_BUTTON_DESC = {
    'confirm_contract': '发起订车需求',
    'confirm_resource': '确认车源',
    'confirm_capital': '确认垫资',
    'fill_capital': '完成垫资',
    'order_car': '完成订车',
    'receive': '完成交车',
    'close': '结算奖励'
}
SEND_VALUES_ELEMENT = {
    'confirm_contract': {
                     'selling_price': '合同应收款总额(元)',
                        'body_price': '车身售价(元)',
            'selling_deposit_amount': '客户订金收取(元)',
                   'contract_number': '订单编号'
    },
    'confirm_resource': {
                      'buying_price': '车身进价(元)',
             'buying_deposit_amount': '资源订金支付(元)',
    },
    'confirm_capital': { 'advance': '预估垫资金额(元)' },
    'order_car': { 'freight': '大板运费(元)' },
    'fill_capital': { 'actual_advance': '实际垫资金额(元)' },
    'receive': { 'plate_number': '车牌号' }
}
#时间组件
TIME_ELEMENT = {
    'choose': '//div[text()="请选择时间"]/..',
    'day': '//div[text()="%s"]/../..' % str(random.randint(10, 28)),
    'confirm': '//div[text()="确认"]/..'
}
#城市组件
CITY_ELEMENT = {
    'choose': '//div[text()="%s"]/../../div[2]',
    'province': '//div[text()="%s"]/../..',
    'city': '//div[text()="%s"]/../..'
}
#上传图片
ATTACHMENT_BUTTON = '//div[text()="%s"]/../..'
ATTACHMENT_DESC = {
    'confirm_resource': '确认车源相关图片',
           'order_car': '完成订车相关图片',
             'receive': '完成交车相关图片',
               'close': '结算奖励相关图片'
}
IMAGE_CHOOSE_BUTTON = '//div[text()="%s"]/../../div[2]/div'
IMAGE_DESC = {
    'confirm_resource': [ '资源合同图片' ],
    'order_car': ['验车照片图片'],
    'receive': ['车辆手续相关资料图片', '交车图片', '客户应收款明细'],
    'close': ['付款凭证图片']
}
IMAGE_INPUT = '/html/body/input'
IMAGE_CONFIRM_BUTTON = '//div[text()="确认新增"]/..'
STATUS_MESSAGE = '//div[text()="购买车型"]/../../../../div[3]/div/div'
