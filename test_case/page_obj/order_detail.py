from selenium import webdriver
import sys, string, json, time
sys.path.append("./modules")
sys.path.append("./data")
sys.path.append("./page_obj")
import user_info, order_info, order_ele, page, login


#订单页面操作
class OrderDetail(page.Page):
    def __init__(self, driver, role):
        page.Page.__init__(self, driver)
        user_login = login.Login(self.driver)
        user_login.login(role)
        self.find(order_ele.PENDING_LIST_BUTTON, sleep=True).click()
        self.find(order_ele.ORDER_DETAIL_BUTTON, sleep=True).click()
        time.sleep(10)

    def get_detai_value(self, key):
        return self.find(order_ele.DETAIL_VALUE % key).get_attribute('innerHTML')

    def get_status_message(self):
        return self.find(order_ele.STATUS_MESSAGE).get_attribute('innerHTML')

    #填写订单数值并提交
    def send_values(self, step, values=None):
        if step != 'close':
            for key in order_ele.SEND_VALUES_ELEMENT[step].keys():
                input_value_xpath = order_ele.INPUT_VALUE % order_ele.SEND_VALUES_ELEMENT[step][key]
                self.find(input_value_xpath).send_keys(values[key])
        confirm_button_xpath = order_ele.CONFIRM_BUTTON % order_ele.CONFIRM_BUTTON_DESC[step]
        self.find(confirm_button_xpath).click()
        time.sleep(10)

    #点击确认订单按钮
    def check(self):
        self.find(order_ele.CHECK_BUTTON, sleep=True).click()
        time.sleep(10)

    #使用时间组件
    def choose_time(self):
        for key in ['choose', 'day', 'confirm']:
            self.find(order_ele.TIME_ELEMENT[key], sleep=True).click()
        time.sleep(10)
        return order_ele.TIME_ELEMENT['day']

    def choose_city(self, param, province, city):
        choose_xpath = order_ele.CITY_ELEMENT['choose'] % param
        province_xpath = order_ele.CITY_ELEMENT['province'] % province
        city_xpath = order_ele.CITY_ELEMENT['city'] % city
        for key in [choose_xpath, province_xpath, city_xpath]:
            self.find(key, sleep=True).click()
        time.sleep(10)

    def send_images(self, step):
        images_value = {
            'confirm_resource': '/Users/iced_me/Desktop/Work/images/01.jpg', #资源合同图片集
            'order_car': '/Users/iced_me/Desktop/Work/images/02.jpg',
            'receive': '/Users/iced_me/Desktop/Work/images/03.jpg',
            'close': '/Users/iced_me/Desktop/Work/images/04.jpg'
        }
        attachment_xpath = order_ele.ATTACHMENT_BUTTON % order_ele.ATTACHMENT_DESC[step]
        self.find(attachment_xpath, sleep=True).click()
        for key in order_ele.IMAGE_DESC[step]:
            image_choose_xpath = order_ele.IMAGE_CHOOSE_BUTTON % key
            self.find(image_choose_xpath, sleep=True).click()
            self.find(order_ele.IMAGE_INPUT, sleep=True).send_keys(images_value[step])
            self.find(order_ele.IMAGE_CONFIRM_BUTTON, sleep=True).click()
        time.sleep(10)
