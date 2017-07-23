from selenium import webdriver
#ERP待领取列表
PENDING_LIST_BUTTON = '//*[@id="react-app"]/div/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div[1]/div[2]/div[3]'
ORDER_DETAIL_BUTTON = '//*[@id="react-app"]/div/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[2]/div/div/div/div[1]/div/div[1]/div[1]/div[4]'

#ERP订单详情页xpath
detail_page = '//*[@id="react-app"]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[2]/div/' #详情页面的xpath
detail_left_path = detail_page + 'div[1]/div[1]/div[1]/div[3]/'    #订单详情的左侧元素xpath的共同部分
detail_right_path = detail_page + 'div[1]/div[1]/div[2]/div[2]/div/div/'    #订单详情的右侧元素xpath的共同部分
STATUS_MESSAGE = detail_left_path + 'div/div'
select_image = '//*[@id="react-app"]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/'
IMAGE_INPUT = '/html/body/input'

ORDER_DETAIL_ELEMENT = {
                       'name': detail_right_path + 'div[1]/div/div[2]/div',
                  'telephone': detail_right_path + 'div[3]/div/div[2]/div',
              'selling_price': detail_right_path + 'div[5]/div/div[2]/div',
                 'body_price': detail_right_path + 'div[7]/div/div[2]/div',
     'selling_deposit_amount': detail_right_path + 'div[6]/div/div[2]/div',
            'contract_number': detail_right_path + 'div[8]/div/div[2]/div',
               'buying_price': detail_right_path + 'div[9]/div/div[2]/div',
      'buying_deposit_amount': detail_right_path + 'div[10]/div/div[2]/div',
   'expected_time_of_pick_up': detail_right_path + 'div[11]/div/div[2]/div',
                    'advance': detail_right_path + 'div[12]/div/div[2]/div',
                    'freight': detail_right_path + 'div[13]/div/div[2]/div',
               'from_city_id': detail_right_path + 'div[14]/div/div[2]/div',
                 'to_city_id': detail_right_path + 'div[15]/div/div[2]/div',
             'actual_advance': detail_right_path + 'div[16]/div/div[2]/div',
     'actual_time_of_pick_up': detail_right_path + 'div[17]/div/div[2]/div',
          'actual_receive_at': detail_right_path + 'div[18]/div/div[2]/div',
               'plate_number': detail_right_path + 'div[19]/div/div[2]/div',
}

SEND_VALUES_ELEMENT = {
    'confirm_contract': {
                     'selling_price': detail_left_path + 'div[1]/div/div/div[1]/div/div[2]/div/input',
                        'body_price': detail_left_path + 'div[1]/div/div/div[3]/div/div[2]/div/input',
            'selling_deposit_amount': detail_left_path + 'div[1]/div/div/div[2]/div/div[2]/div/input',
                   'contract_number': detail_left_path + 'div[1]/div/div/div[4]/div/div[2]/div/input'
    },
    'confirm_resource': {
                      'buying_price': detail_left_path + 'div[1]/div/div/div[1]/div/div[2]/div/input' ,
             'buying_deposit_amount': detail_left_path + 'div[1]/div/div/div[2]/div/div[2]/div/input'
    },
    'confirm_capital': { 'advance': detail_left_path + 'div[1]/div/div/div/div/div[2]/div/input' },
    'order_car': { 'freight': detail_left_path + 'div[1]/div/div/div[3]/div/div[2]/div/input' },
    'fill_capital': { 'actual_advance': detail_left_path + 'div[1]/div/div/div[1]/div/div[2]/div/input' },
    'receive': { 'plate_number': detail_left_path + 'div[1]/div/div/div[2]/div/div[2]/div/input' },
    'close': {}
}

#填写时间
TIME_ELEMENT = {
    'expected_time_of_pick_up': {
           'click': detail_left_path + 'div[1]/div/div/div[3]/div/div[2]/div/div[1]',
             'day': detail_page + 'div[2]/div[2]/div[1]/div/div[3]/div/div[6]/div[2]/div/div',
         'confirm': detail_page + 'div[2]/div[2]/div[2]/div[2]',
    },
    'actual_time_of_pick_up': {
           'click': detail_left_path + 'div[1]/div/div/div[2]/div/div[2]/div/div[1]',
             'day': detail_page + 'div[2]/div[2]/div[1]/div/div[3]/div/div[6]/div[2]/div/div',
         'confirm': detail_page + 'div[2]/div[2]/div[2]/div[2]'
    },
    'actual_receive_at': {
           'click': detail_left_path + 'div[1]/div/div/div[1]/div/div[2]/div/div[1]',
             'day': detail_page + 'div[2]/div[2]/div[1]/div/div[3]/div/div[6]/div[2]/div/div',
         'confirm': detail_page + 'div[2]/div[2]/div[2]/div[2]'
    }
}

#选择城市
CITY_ELEMENT = {
    'from_city_id': [ detail_left_path + 'div[1]/div/div/div[1]/div/div[2]/div/div[1]',
                      '//*[@id="react-app"]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div',
                      '//*[@id="react-app"]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[3]/div/div/div/div[2]/div/div' ],
      'to_city_id': [ detail_left_path + 'div[1]/div/div/div[2]/div/div[2]/div/div[1]',
                      '//*[@id="react-app"]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/div/div/div[3]/div/div',
                      '//*[@id="react-app"]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[3]/div/div/div/div[2]/div/div' ]
}

#上传图片
ATTACHMENT = {
    'confirm_resource': detail_page + 'div[1]/div[2]/div[2]/div[2]/div[1]',
           'order_car': detail_page + 'div[1]/div[2]/div[2]/div[3]',
             'receive': detail_page + 'div[1]/div[2]/div[2]/div[5]',
               'close': detail_page + 'div[1]/div[2]/div[2]/div[6]'
}
CONFIRM_RESOURCE_IMAGES =  {
    'resource_contract_images': {
         'choose': '//*[@id="react-app"]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div',
         'input': '/html/body/input',
         'confirm': '//*[@id="react-app"]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[4]/div[2]/div[2]/div[2]'
    }
}
ORDER_CAR_IMAGES = {
    'vehicle_examination_images': {
        'choose': '//*[@id="react-app"]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div',
        'input': '/html/body/input',
        'confirm': '//*[@id="react-app"]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]'
    }
}
RECEIVE_IMAGES = {
    'procedure_images': {
         'choose': '//*[@id="react-app"]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div',
         'input': '/html/body/input',
         'confirm': '//*[@id="react-app"]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]'
    },
    'vehicles_delivery_images': {
         'choose': '//*[@id="react-app"]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div',
         'input': '/html/body/input',
         'confirm': '//*[@id="react-app"]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[4]/div[2]/div[2]/div[2]'
    },
    'statement_images': {
        'choose': '//*[@id="react-app"]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/div[3]/div[2]/div',
        'input': '/html/body/input',
        'confirm': '//*[@id="react-app"]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[5]/div[2]/div[2]/div[2]'
    }
}
CLOSE_IMAGES = {
    'payment_images': {
         'choose': '//*[@id="react-app"]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div',
         'input': '/html/body/input',
         'confirm': '//*[@id="react-app"]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]'
    }
}

#确认按钮xpath
CONFIRM_BUTTON = {
    'confirm_contract': detail_left_path + 'div[2]/div[2]',
    'confirm_resource': detail_left_path + 'div[2]/div[3]/div',
     'confirm_capital': detail_left_path + 'div[2]/div[2]',
           'order_car': detail_left_path + 'div[2]/div',
        'fill_capital': detail_left_path + 'div[2]/div[2]',
             'receive': detail_left_path + 'div[2]/div',
               'close': detail_left_path + 'div[2]/div[3]'
}
#提交按钮xpath
CHECK_BUTTON = {
    'confirm_contract': detail_page + 'div[3]/div[2]/div[2]/div[2]',
    'confirm_resource': detail_page + 'div[5]/div[2]/div[2]/div[2]',
     'confirm_capital': detail_page + 'div[3]/div[2]/div[2]/div[2]',
           'order_car': detail_page + 'div[2]/div[2]/div[2]/div[2]',
        'fill_capital': detail_page + 'div[4]/div[2]/div[2]/div[2]',
             'receive': detail_page + 'div[3]/div[2]/div[2]/div[2]',
               'close': detail_page + 'div[3]/div[2]/div[2]/div[2]'
}
