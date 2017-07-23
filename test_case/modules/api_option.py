import http.client, json, order_info, user_info

class Api:
    def APIconnection(self, method, url, params=None, token=None):
        conn = http.client.HTTPConnection("staging.api.itsmycar.cn")
        if token == None: headers = { 'Content-Type': 'application/json' }
        else: headers = { 'Authorization': token,  'Content-Type': 'application/json' }
        conn.request(method, url, json.dumps(params), headers)
        APIres = conn.getresponse()
        response = {
            'status': APIres.status,
            'reason': APIres.reason,
            'data': json.loads(APIres.read())
        }
        conn.close()
        return response

#用户接口操作
class UserApi(Api):

    def __init__(self, user_params=user_info.REQUEST_SALER):
        response = self.APIconnection("POST", "/v1/sessions", params=user_params)
        self.user_data = response['data']
        self.message = { 'status': response['status'], 'reason': response['reason'] }

    def get_token(self):
        return 'Token token=' + self.user_data['token']

    def get_my_stats(self, token):
        self.response = self.APIconnection("GET", "/v1/users/my_stats ", token=token)
        return self.response['data']

#订单API操作
class OrderApi(Api):

    def create(self, order_params, token=UserApi().get_token()):
        self.response = self.APIconnection("POST", "/v1/orders", params=order_params, token=token)

    def accept(self, order_params=None, token=UserApi(user_info.RESPONSER_SALER).get_token()):
        self.response = self.APIconnection( "PUT", "/v1/orders/%s/accept" % self.response['data']['id'], token=token )

    def sign(self, order_params, token=UserApi(user_info.RESPONSER_SALER).get_token()):
        self.response = self.APIconnection( "PUT", "/v1/orders/%s/sign" % self.response['data']['id'], params=order_params, token=token )

    def confirm_contract(self, order_params, token=UserApi(user_info.STORE_MANAGER).get_token()):
        self.response = self.APIconnection( "PUT", "/v1/orders/%s/confirm_contract" % self.response['data']['id'], params=order_params, token=token )

    def confirm_resource(self, order_params, token=UserApi(user_info.RESOURCE_MANAGER).get_token()):
        self.response = self.APIconnection( "PUT", "/v1/orders/%s/confirm_resource" % self.response['data']['id'], params=order_params, token=token )

    def confirm_capital(self, order_params, token=UserApi(user_info.CAPITAL_MANAGER).get_token()):
        self.response = self.APIconnection( "PUT", "/v1/orders/%s/confirm_capital" % self.response['data']['id'], params=order_params, token=token )

    def order_car(self, order_params, token=UserApi(user_info.RESOURCE_MANAGER).get_token()):
        self.response = self.APIconnection( "PUT", "/v1/orders/%s/order_car" % self.response['data']['id'], params=order_params, token=token )

    def fill_capital(self, order_params, token=UserApi(user_info.CAPITAL_MANAGER).get_token()):
        self.response = self.APIconnection( "PUT", "/v1/orders/%s/fill_capital" % self.response['data']['id'], params=order_params, token=token )

    def receive(self, order_params, token=UserApi(user_info.STORE_MANAGER).get_token()):
        self.response = self.APIconnection( "PUT", "/v1/orders/%s/receive" % self.response['data']['id'], params=order_params, token=token )

    def close(self, order_params, token=UserApi(user_info.ADMIN).get_token()):
        self.response = self.APIconnection( "PUT", "/v1/orders/%s/close" % self.response['data']['id'], params=order_params, token=token )

    #订单执行命令，传入步骤名称可通过接口顺序执行到该步骤
    def execute(self, command):
        api_commands = {
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
        params = {
            'create': order_info.random_create_params(),
            'accept': '',
            'sign': order_info.random_sign_params(),
            'confirm_contract': order_info.random_confirm_contract_params(),
            'confirm_resource': order_info.random_confirm_resource_params(),
            'confirm_capital': order_info.random_confirm_capital_params(),
            'order_car': order_info.random_order_car_params(),
            'fill_capital': order_info.random_fill_capital_params(),
            'receive': order_info.random_receive_params(),
            'close': order_info.random_close_params()
        }
        cmds = ['create', 'accept', 'sign', 'confirm_contract', 'confirm_resource', 'confirm_capital', 'order_car', 'fill_capital', 'receive', 'close']
        for cmd in cmds:
            api_commands[cmd](params[cmd])
            if cmd == command: break;
        self.data = self.get_a_order()

    #返回所有订单
    @classmethod
    def get_orders(self, token=UserApi(user_info.ADMIN).get_token(), page=None, per_page=None, status=None, city_id=None, store_id=None, order='updated_at%20desc'):
        sub_url = {
            'page': '' if page==None else ('&page='+str(page)),
            'per_page': '' if per_page==None else ('&per_page='+str(per_page)),
            'status': '' if status==None else ('&aasm_state[]='+status),
            'city_id': '' if city_id==None else ('&city_id='+str(city_id)),
            'store_id': '' if store_id==None else ('&store_id='+str(store_id)),
            'order': 'updated_at%20desc' if order=='updated_at' else ('&order='+order)
        }
        url = "/v1/orders?" + sub_url['page'] + sub_url['per_page'] + sub_url['status'] + sub_url['city_id'] + sub_url['store_id'] + sub_url['order']
        return self.APIconnection( "GET", url, token=token )

    def get_a_order(self, token=UserApi(user_info.ADMIN).get_token()):
        self.response = self.APIconnection( "GET", "/v1/orders/%s" % self.response['data']['id'], token=token )
        self.data = self.response['data']
        return self.data
