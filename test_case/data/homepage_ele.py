USER_HOMEPAGE_TITLE = '//div[text()="欢迎来到宜买车"]/following-sibling::div[1]'
COUNT = {
    'pending_count': '//div[text()="件待处理"]/../div[1]',
    'onging_count': '//div[text()="件进行中"]/../div[1]',
    'closed_count': '//div[text()="件已完成"]/../div[1]',
    'terminated_count': '//div[text()="件已取消"]/../div[1]',
    'employed_count': '//div[text()="销售"]/../div[1]',
    'store_manager_count': '//div[text()="店铺经理"]/../div[1]'
}
NEW_ORDERS = {
          'model': '//div[text()="最新"]/../following-sibling::div[1]/div/div[%s]/div/div/div[2]/div[1]',
           'name': '//div[text()="最新"]/../following-sibling::div[1]/div/div[%s]/div/div/div[2]/div[2]',
    'aasm_state1': '//div[text()="最新"]/../following-sibling::div[1]/div/div[%s]/div/div[2]/div[3]',
    'aasm_state2': '//div[text()="最新"]/../following-sibling::div[1]/div/div[%s]/div/div[2]/div[4]',
     'updated_at': '//div[text()="最新"]/../following-sibling::div[1]/div/div[%s]/div/div[3]/div'
}
