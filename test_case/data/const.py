WAIT_TIME = 10

#各角色账号
CITY_MANAGER = { 'username': '18259000004', 'password': '123456' }
RESOURCE_MANAGER = { 'username': '18259000005', 'password': '123456' }
CAPITAL_MANAGER = { 'username': '18259000006', 'password': '123456' }
ACCOUNTANT = { 'username': '18259000008', 'password': '123456' }
SALES_DIRECTOR = { 'username': '18259000021', 'password': '123456' }
INTRODUCER = { 'username': '18600000060', 'password': '123456' }
CITY_INTRODUCER = { 'username': '18600000061', 'password': '123456' }
HEAD_INTRODUCER = { 'username': '18600000065', 'password': '123456' }

#接口上传图片地址
IMAGES = ["http://www.sznews.com/szsbcar/images/0016ece1797b0841b20c22.jpg","http://www.sznews.com/szsbcar/images/0016ece1797b0841b20c22.jpg"]

#ERP订单详情页xpath
detail_page = '//*[@id="react-app"]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[2]/div/' #详情页面的xpath
detail_left_path = detail_page + 'div[1]/div[1]/div[1]/div[3]/'    #订单详情的左侧元素xpath的共同部分
detail_right_path = detail_page + 'div[1]/div[1]/div[2]/div[2]/div/div/'    #订单详情的右侧元素xpath的共同部分
STATUS_MESSAGE = detail_left_path + 'div/div'
select_image = '//*[@id="react-app"]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/'
#IMAGE_INPUT = '/html/body/input'

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

CONFIRM_CONTRACT_SEND_ELEMENT = {
                 'selling_price': detail_left_path + 'div[1]/div/div/div[1]/div/div[2]/div/input',
                    'body_price': detail_left_path + 'div[1]/div/div/div[3]/div/div[2]/div/input',
        'selling_deposit_amount': detail_left_path + 'div[1]/div/div/div[2]/div/div[2]/div/input',
               'contract_number': detail_left_path + 'div[1]/div/div/div[4]/div/div[2]/div/input',
                   'send_button': detail_left_path + 'div[2]/div[2]'
}

CONFIRM_RESOURCE_SEND_ELEMENT = {
                        'buying_price': detail_left_path + 'div[1]/div/div/div[1]/div/div[2]/div/input' ,
               'buying_deposit_amount': detail_left_path + 'div[1]/div/div/div[2]/div/div[2]/div/input',
     'expected_time_of_pick_up_choose': detail_left_path + 'div[1]/div/div/div[3]/div/div[2]/div/div[1]',
        'expected_time_of_pick_up_day': detail_page + 'div[2]/div[2]/div[1]/div/div[3]/div/div[6]/div[2]/div/div/div',
    'expected_time_of_pick_up_confirm': detail_page + 'div[2]/div[2]/div[2]/div[2]',
             'confirm_resource_images': detail_page + 'div[1]/div[2]/div[2]/div[2]/div[1]',
     'resource_contract_images_choose': '//*[@id="react-app"]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div',
            'resource_contract_images': '/html/body/input',
    'resource_contract_images_confirm': '//*[@id="react-app"]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[4]/div[2]/div[2]/div[2]',
                         'send_button': detail_left_path + 'div[2]/div[3]/div'
}

CONFIRM_CAPITAL_SEND_ELEMENT = {
        'advance': detail_left_path + 'div[1]/div/div/div/div/div[2]/div/input',
    'send_button': detail_left_path + 'div[2]/div[2]'
}

ORDER_CAR_SEND_ELEMENT = {
                               'freight': detail_left_path + 'div[1]/div/div/div[3]/div/div[2]/div/input',
                        'from_city_id_1': detail_left_path + 'div[1]/div/div/div[1]/div/div[2]/div/div[1]',
                        'from_city_id_2': '//*[@id="react-app"]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/div/div/div[2]/div/div',
                        'from_city_id_3': '//*[@id="react-app"]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[3]/div/div/div/div[2]/div/div',
                          'to_city_id_1': detail_left_path + 'div[1]/div/div/div[2]/div/div[2]/div/div[1]',
                          'to_city_id_2': '//*[@id="react-app"]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/div/div/div[3]/div/div',
                          'to_city_id_3': '//*[@id="react-app"]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[3]/div/div/div/div[2]/div/div',
                      'order_car_images': detail_page + 'div[1]/div[2]/div[2]/div[3]',
     'vehicle_examination_images_choose': '//*[@id="react-app"]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div',
                                          #//*[@id="react-app"]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/
            'vehicle_examination_images': '/html/body/input',
    'vehicle_examination_images_confirm': '//*[@id="react-app"]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]',
                           'send_button': detail_left_path + 'div[2]/div'

}

FILL_CAPITAL_SEND_ELEMENT = {
                    'actual_advance': detail_left_path + 'div[1]/div/div/div[1]/div/div[2]/div/input',
     'actual_time_of_pick_up_choose': detail_left_path + 'div[1]/div/div/div[2]/div/div[2]/div/div[1]',
        'actual_time_of_pick_up_day': detail_page + 'div[2]/div[2]/div[1]/div/div[3]/div/div[6]/div[2]/div/div',
    'actual_time_of_pick_up_confirm': detail_page + 'div[2]/div[2]/div[2]/div[2]',
                       'send_button': detail_left_path + '/div[2]/div[2]'
}

RECEIVE_SEND_ELEMENT = {
                         'plate_number': detail_left_path + 'div[1]/div/div/div[2]/div/div[2]/div/input',
             'actual_receive_at_choose': detail_left_path + 'div[1]/div/div/div[1]/div/div[2]/div/div[1]',
                'actual_receive_at_day': detail_page + 'div[2]/div[2]/div[1]/div/div[3]/div/div[6]/div[2]/div/div',
            'actual_receive_at_confirm': detail_page + 'div[2]/div[2]/div[2]/div[2]',
                        'receive_images': detail_page + 'div[1]/div[2]/div[2]/div[5]',
              'procedure_images_choose': '//*[@id="react-app"]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/div[1]/div[2]/div',
                     'procedure_images': '/html/body/input',
             'procedure_images_confirm': '//*[@id="react-app"]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]',
      'vehicles_delivery_images_choose': '//*[@id="react-app"]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div',
             'vehicles_delivery_images': '/html/body/input',
     'vehicles_delivery_images_confirm': '//*[@id="react-app"]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[4]/div[2]/div[2]/div[2]',
              'statement_images_choose': '//*[@id="react-app"]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/div[3]/div[2]/div',
                     'statement_images': '/html/body/input',
             'statement_images_confirm': '//*[@id="react-app"]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[5]/div[2]/div[2]/div[2]',
                          'send_button': detail_left_path + 'div[2]/div',
}

CLOSE_ELEMENT = {
              'close_images': detail_page + 'div[1]/div[2]/div[2]/div[6]',
     'payment_images_choose': '//*[@id="react-app"]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div',
            'payment_images': '/html/body/input',
    'payment_images_confirm': '//*[@id="react-app"]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]',
               'send_button': detail_left_path + 'div[2]/div[3]'
}

#确认按钮xpath
CONFIRM_BUTTON = {
    'confirm_contract': detail_page + 'div[3]/div[2]/div[2]/div[2]',
    'confirm_resource': detail_page + 'div[5]/div[2]/div[2]/div[2]',
     'confirm_capital': detail_page + 'div[3]/div[2]/div[2]/div[2]',
           'order_car': detail_page + 'div[2]/div[2]/div[2]/div[2]',
        'fill_capital': detail_page + 'div[4]/div[2]/div[2]/div[2]',
             'receive': detail_page + 'div[3]/div[2]/div[2]/div[2]',
               'close': detail_page + 'div[3]/div[2]/div[2]/div[2]'
}
