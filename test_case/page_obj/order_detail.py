from selenium import webdriver
import sys, random, string, json, time
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
        return self.find(order_ele.ORDER_DETAIL_ELEMENT[key]).get_attribute('innerHTML')

    def get_status_message(self):
        return self.find(order_ele.STATUS_MESSAGE).get_attribute('innerHTML')

    def send_values(self, step, values=None):
        if step != 'close':
            for key in order_ele.SEND_VALUES_ELEMENT[step].keys():
                self.find(order_ele.SEND_VALUES_ELEMENT[step][key]).send_keys(values[key])
        self.find(order_ele.CONFIRM_BUTTON[step]).click()
        time.sleep(10)

    #点击确认订单按钮
    def check(self, step):
        self.find(order_ele.CHECK_BUTTON[step], sleep=True).click()
        time.sleep(10)

    def choose_time(self, param):
        for key in ['click', 'day', 'confirm']:
            self.find(order_ele.TIME_ELEMENT[param][key], sleep=True).click()
        time.sleep(10)

    def choose_city(self):
        for key in order_ele.CITY_ELEMENT.keys():
            for i in range(3):
                self.find(order_ele.CITY_ELEMENT[key][i], sleep=True).click()
        time.sleep(10)

    def send_images(self, step):
        image_elements = {
            'confirm_resource': order_ele.CONFIRM_RESOURCE_IMAGES,
            'order_car': order_ele.ORDER_CAR_IMAGES,
            'receive': order_ele.RECEIVE_IMAGES,
            'close': order_ele.CLOSE_IMAGES
        }
        images_value = {
            'confirm_resource': '/Users/iced_me/Desktop/Work/images/01.jpg', #资源合同图片集
            'order_car': '/Users/iced_me/Desktop/Work/images/02.jpg',
            'receive': '/Users/iced_me/Desktop/Work/images/03.jpg',
            'close': '/Users/iced_me/Desktop/Work/images/04.jpg'
        }
        self.find(order_ele.ATTACHMENT[step], sleep=True).click()
        for key in image_elements[step].keys():
            self.find(image_elements[step][key]['choose'], sleep=True).click()
            self.find(image_elements[step][key]['input'], sleep=True).send_keys(images_value[step])
            self.find(image_elements[step][key]['confirm'], sleep=True).click()
