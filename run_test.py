from selenium import webdriver
import unittest, time, sys
sys.path.append("./test_case")
sys.path.append("./test_case/modules")
sys.path.append("./test_case/data")
sys.path.append("./test_case/package")
sys.path.append("./test_case/page_obj")
from HTMLTestRunner import HTMLTestRunner
import order_flow_step1, order_flow_step2, order_flow_step3, order_flow_step4, order_flow_step5, order_flow_step6, order_flow_step7

if __name__ == '__main__':

    now = time.strftime('%Y-%m-%d %H:%M:%S')
    filename = './report/' + now +'_result.html'
    fp = open(filename, 'wb')

    order_flow_suite1 = unittest.TestLoader().loadTestsFromTestCase(order_flow_step1.ConfirmContractTest) #订单流程：1.确认合同
    order_flow_suite2 = unittest.TestLoader().loadTestsFromTestCase(order_flow_step2.ConfirmResourceTest) #订单流程：2.确认车源
    order_flow_suite3 = unittest.TestLoader().loadTestsFromTestCase(order_flow_step3.ConfirmCapitalTest) #订单流程：3.确认垫资
    order_flow_suite4 = unittest.TestLoader().loadTestsFromTestCase(order_flow_step4.OrderCarTest) #订单流程：4.完成订车
    order_flow_suite5 = unittest.TestLoader().loadTestsFromTestCase(order_flow_step5.FillCapitalTest) #订单流程：5.完成垫资
    order_flow_suite6 = unittest.TestLoader().loadTestsFromTestCase(order_flow_step6.ReceiveTest) #订单流程：6.确认交车
    order_flow_suite7 = unittest.TestLoader().loadTestsFromTestCase(order_flow_step7.CloseTest) #订单流程：6.完成结算

    order_flow_suite = unittest.TestSuite([order_flow_suite1, order_flow_suite2, order_flow_suite3, order_flow_suite4, order_flow_suite5, order_flow_suite6, order_flow_suite7])

    runner = HTMLTestRunner(stream=fp, title='订单流程测试报告', description='用例执行情况：', verbosity=2)
    runner.run(order_flow_suite)
    fp.close()
