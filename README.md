# ERP_Test
*语言：python
*框架：unittest + webdriver + selenium
*输出报告：HTMLTestRunner
*测试用例：订单流程回归测试
------------------------------------------------------------------------------------------------------------------------------
*范例报告如下：

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>订单流程测试报告</title>
    <meta name="generator" content="HTMLTestRunner 0.8.2"/>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    
<style type="text/css" media="screen">
body        { font-family: verdana, arial, helvetica, sans-serif; font-size: 80%; }
table       { font-size: 100%; }
pre         { }

/* -- heading ---------------------------------------------------------------------- */
h1 {
	font-size: 16pt;
	color: gray;
}
.heading {
    margin-top: 0ex;
    margin-bottom: 1ex;
}

.heading .attribute {
    margin-top: 1ex;
    margin-bottom: 0;
}

.heading .description {
    margin-top: 4ex;
    margin-bottom: 6ex;
}

/* -- css div popup ------------------------------------------------------------------------ */
a.popup_link {
}

a.popup_link:hover {
    color: red;
}

.popup_window {
    display: none;
    position: relative;
    left: 0px;
    top: 0px;
    /*border: solid #627173 1px; */
    padding: 10px;
    background-color: #E6E6D6;
    font-family: "Lucida Console", "Courier New", Courier, monospace;
    text-align: left;
    font-size: 8pt;
    width: 500px;
}

}
/* -- report ------------------------------------------------------------------------ */
#show_detail_line {
    margin-top: 3ex;
    margin-bottom: 1ex;
}
#result_table {
    width: 80%;
    border-collapse: collapse;
    border: 1px solid #777;
}
#header_row {
    font-weight: bold;
    color: white;
    background-color: #777;
}
#result_table td {
    border: 1px solid #777;
    padding: 2px;
}
#total_row  { font-weight: bold; }
.passClass  { background-color: #6c6; }
.failClass  { background-color: #c60; }
.errorClass { background-color: #c00; }
.passCase   { color: #6c6; }
.failCase   { color: #c60; font-weight: bold; }
.errorCase  { color: #c00; font-weight: bold; }
.hiddenRow  { display: none; }
.testcase   { margin-left: 2em; }


/* -- ending ---------------------------------------------------------------------- */
#ending {
}

</style>

</head>
<body>
<script language="javascript" type="text/javascript"><!--
output_list = Array();

/* level - 0:Summary; 1:Failed; 2:All */
function showCase(level) {
    trs = document.getElementsByTagName("tr");
    for (var i = 0; i < trs.length; i++) {
        tr = trs[i];
        id = tr.id;
        if (id.substr(0,2) == 'ft') {
            if (level < 1) {
                tr.className = 'hiddenRow';
            }
            else {
                tr.className = '';
            }
        }
        if (id.substr(0,2) == 'pt') {
            if (level > 1) {
                tr.className = '';
            }
            else {
                tr.className = 'hiddenRow';
            }
        }
    }
}


function showClassDetail(cid, count) {
    var id_list = Array(count);
    var toHide = 1;
    for (var i = 0; i < count; i++) {
        tid0 = 't' + cid.substr(1) + '.' + (i+1);
        tid = 'f' + tid0;
        tr = document.getElementById(tid);
        if (!tr) {
            tid = 'p' + tid0;
            tr = document.getElementById(tid);
        }
        id_list[i] = tid;
        if (tr.className) {
            toHide = 0;
        }
    }
    for (var i = 0; i < count; i++) {
        tid = id_list[i];
        if (toHide) {
            document.getElementById('div_'+tid).style.display = 'none'
            document.getElementById(tid).className = 'hiddenRow';
        }
        else {
            document.getElementById(tid).className = '';
        }
    }
}


function showTestDetail(div_id){
    var details_div = document.getElementById(div_id)
    var displayState = details_div.style.display
    // alert(displayState)
    if (displayState != 'block' ) {
        displayState = 'block'
        details_div.style.display = 'block'
    }
    else {
        details_div.style.display = 'none'
    }
}


function html_escape(s) {
    s = s.replace(/&/g,'&amp;');
    s = s.replace(/</g,'&lt;');
    s = s.replace(/>/g,'&gt;');
    return s;
}

/* obsoleted by detail in <div>
function showOutput(id, name) {
    var w = window.open("", //url
                    name,
                    "resizable,scrollbars,status,width=800,height=450");
    d = w.document;
    d.write("<pre>");
    d.write(html_escape(output_list[id]));
    d.write("\n");
    d.write("<a href='javascript:window.close()'>close</a>\n");
    d.write("</pre>\n");
    d.close();
}
*/
--></script>

<div class='heading'>
<h1>订单流程测试报告</h1>
<p class='attribute'><strong>Start Time:</strong> 2017-07-08 02:47:59</p>
<p class='attribute'><strong>Duration:</strong> 0:13:18.603780</p>
<p class='attribute'><strong>Status:</strong> Pass 88</p>

<p class='description'>用例执行情况：</p>
</div>



<p id='show_detail_line'>Show
<a href='javascript:showCase(0)'>Summary</a>
<a href='javascript:showCase(1)'>Failed</a>
<a href='javascript:showCase(2)'>All</a>
</p>
<table id='result_table'>
<colgroup>
<col align='left' />
<col align='right' />
<col align='right' />
<col align='right' />
<col align='right' />
<col align='right' />
</colgroup>
<tr id='header_row'>
    <td>Test Group/Test case</td>
    <td>Count</td>
    <td>Pass</td>
    <td>Fail</td>
    <td>Error</td>
    <td>View</td>
</tr>

<tr class='passClass'>
    <td>order_flow_step1.ConfirmContractTest:  订单流程：1.确认合同 </td>
    <td>7</td>
    <td>7</td>
    <td>0</td>
    <td>0</td>
    <td><a href="javascript:showClassDetail('c1',7)">Detail</a></td>
</tr>

<tr id='pt1.1' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_1_before_name: 操作前订单详情： 客户姓名</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt1.2' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_2_before_telephone: 操作前订单详情： 客户电话</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt1.3' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_3_check: 发送确认合同请求</div></td>
    <td colspan='5' align='center'>

    <!--css div popup start-->
    <a class="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_pt1.3')" >
        pass</a>

    <div id='div_pt1.3' class="popup_window">
        <div style='text-align: right; color:red;cursor:pointer'>
        <a onfocus='this.blur();' onclick="document.getElementById('div_pt1.3').style.display = 'none' " >
           [x]</a>
        </div>
        <pre>
        
pt1.3: 200 OK


        </pre>
    </div>
    <!--css div popup end-->

    </td>
</tr>

<tr id='pt1.4' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_4_after_selling_price: 操作后订单详情： 合同应收款总额</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt1.5' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_5_after_body_price: 操作后订单详情： 车身售价</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt1.6' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_6_after_selling_deposit_amount: 操作后订单详情： 客户订金收取</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt1.7' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_7_after_contract_number: 操作后订单详情： 订单编号</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr class='passClass'>
    <td>order_flow_step2.ConfirmResourceTest:  订单流程：2.确认车源 </td>
    <td>10</td>
    <td>10</td>
    <td>0</td>
    <td>0</td>
    <td><a href="javascript:showClassDetail('c2',10)">Detail</a></td>
</tr>

<tr id='pt2.1' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_1_before_name: 操作前订单详情： 客户姓名</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt2.2' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_2_before_telephone: 操作前订单详情： 客户电话</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt2.3' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_3_before_selling_price: 操作前订单详情： 合同应收款总额</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt2.4' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_4_before_body_price: 操作前订单详情： 车身售价</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt2.5' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_5_before_selling_deposit_amount: 操作前订单详情： 客户订金收取</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt2.6' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_6_before_contract_number: 操作前订单详情： 订单编号</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt2.7' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_7_check: 发送确认车源请求</div></td>
    <td colspan='5' align='center'>

    <!--css div popup start-->
    <a class="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_pt2.7')" >
        pass</a>

    <div id='div_pt2.7' class="popup_window">
        <div style='text-align: right; color:red;cursor:pointer'>
        <a onfocus='this.blur();' onclick="document.getElementById('div_pt2.7').style.display = 'none' " >
           [x]</a>
        </div>
        <pre>
        
pt2.7: 200 OK


        </pre>
    </div>
    <!--css div popup end-->

    </td>
</tr>

<tr id='pt2.8' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_8_after_buying_price: 操作后订单详情： 车身进价</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt2.9' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_9_after_buying_deposit_amount: 操作后订单详情： 资源订金支付</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt2.10' class='hiddenRow'>
    <td class='none'><div class='testcase'>test__10_after_expected_time_of_pick_up: 操作后订单详情： 预计提车时间</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr class='passClass'>
    <td>order_flow_step3.ConfirmCapitalTest:  订单流程：3.确认垫资 </td>
    <td>11</td>
    <td>11</td>
    <td>0</td>
    <td>0</td>
    <td><a href="javascript:showClassDetail('c3',11)">Detail</a></td>
</tr>

<tr id='pt3.1' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_1_before_name: 操作前订单详情：客户姓名</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt3.2' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_2_before_telephone: 操作前订单详情：客户电话</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt3.3' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_3_before_selling_price: 操作前订单详情：合同应收款总额</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt3.4' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_4_before_body_price: 操作前订单详情：车身售价</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt3.5' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_5_before_selling_deposit_amount: 操作前订单详情：客户订金收取</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt3.6' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_6_before_contract_number: 操作前订单详情：订单编号</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt3.7' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_7_before_buying_price: 操作前订单详情：车身进价</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt3.8' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_8_before_buying_deposit_amount: 操作前订单详情：资源订金支付</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt3.9' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_9_before_expected_time_of_pick_up: 操作前订单详情：预计提车时间</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt3.10' class='hiddenRow'>
    <td class='none'><div class='testcase'>test__10_check: 发送确认垫资请求</div></td>
    <td colspan='5' align='center'>

    <!--css div popup start-->
    <a class="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_pt3.10')" >
        pass</a>

    <div id='div_pt3.10' class="popup_window">
        <div style='text-align: right; color:red;cursor:pointer'>
        <a onfocus='this.blur();' onclick="document.getElementById('div_pt3.10').style.display = 'none' " >
           [x]</a>
        </div>
        <pre>
        
pt3.10: 200 OK


        </pre>
    </div>
    <!--css div popup end-->

    </td>
</tr>

<tr id='pt3.11' class='hiddenRow'>
    <td class='none'><div class='testcase'>test__11_after_advance: 操作后订单详情： 预估垫资金额</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr class='passClass'>
    <td>order_flow_step4.OrderCarTest:  订单流程：4.完成订车 </td>
    <td>14</td>
    <td>14</td>
    <td>0</td>
    <td>0</td>
    <td><a href="javascript:showClassDetail('c4',14)">Detail</a></td>
</tr>

<tr id='pt4.1' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_1_before_name: 操作前订单详情： 客户姓名</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt4.2' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_2_before_telephone: 操作前订单详情： 客户电话</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt4.3' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_3_before_selling_price: 操作前订单详情： 合同应收款总额</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt4.4' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_4_before_body_price: 操作前订单详情： 车身售价</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt4.5' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_5_before_selling_deposit_amount: 操作前订单详情： 客户订金收取</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt4.6' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_6_before_contract_number: 操作前订单详情： 订单编号</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt4.7' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_7_before_buying_price: 操作前订单详情： 车身进价</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt4.8' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_8_before_buying_deposit_amount: 操作前订单详情： 资源订金支付</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt4.9' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_9_before_expected_time_of_pick_up: 操作前订单详情： 预计提车时间</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt4.10' class='hiddenRow'>
    <td class='none'><div class='testcase'>test__10_before_buying_advance: 操作前订单详情： 预估垫资金额</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt4.11' class='hiddenRow'>
    <td class='none'><div class='testcase'>test__11_check: 发送完成订车请求</div></td>
    <td colspan='5' align='center'>

    <!--css div popup start-->
    <a class="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_pt4.11')" >
        pass</a>

    <div id='div_pt4.11' class="popup_window">
        <div style='text-align: right; color:red;cursor:pointer'>
        <a onfocus='this.blur();' onclick="document.getElementById('div_pt4.11').style.display = 'none' " >
           [x]</a>
        </div>
        <pre>
        
pt4.11: 200 OK


        </pre>
    </div>
    <!--css div popup end-->

    </td>
</tr>

<tr id='pt4.12' class='hiddenRow'>
    <td class='none'><div class='testcase'>test__12_after_freight: 操作后订单详情： 大板运费</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt4.13' class='hiddenRow'>
    <td class='none'><div class='testcase'>test__13_after_from_city_id: 操作后订单详情： 发车城市</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt4.14' class='hiddenRow'>
    <td class='none'><div class='testcase'>test__14_after_to_city_id: 操作后订单详情： 到达城市</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr class='passClass'>
    <td>order_flow_step5.FillCapitalTest:  订单流程：5.完成垫资 </td>
    <td>14</td>
    <td>14</td>
    <td>0</td>
    <td>0</td>
    <td><a href="javascript:showClassDetail('c5',14)">Detail</a></td>
</tr>

<tr id='pt5.1' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_1_before_name: 操作前订单详情： 客户姓名</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt5.2' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_2_before_telephone: 操作前订单详情： 客户电话</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt5.3' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_3_before_selling_price: 操作前订单详情： 合同应收款总额</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt5.4' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_4_before_body_price: 操作前订单详情： 车身售价</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt5.5' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_5_before_selling_deposit_amount: 操作前订单详情： 客户订金收取</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt5.6' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_6_before_contract_number: 操作前订单详情： 订单编号</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt5.7' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_7_before_buying_price: 操作前订单详情： 车身进价</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt5.8' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_8_before_buying_deposit_amount: 操作前订单详情： 资源订金支付</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt5.9' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_9_before_expected_time_of_pick_up: 操作前订单详情： 预计提车时间</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt5.10' class='hiddenRow'>
    <td class='none'><div class='testcase'>test__10_before_buying_advance: 操作前订单详情： 预估垫资金额</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt5.11' class='hiddenRow'>
    <td class='none'><div class='testcase'>test__11_before_freight: 操作前订单详情: 大板运费</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt5.12' class='hiddenRow'>
    <td class='none'><div class='testcase'>test__12_check: 发送完成垫资请求</div></td>
    <td colspan='5' align='center'>

    <!--css div popup start-->
    <a class="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_pt5.12')" >
        pass</a>

    <div id='div_pt5.12' class="popup_window">
        <div style='text-align: right; color:red;cursor:pointer'>
        <a onfocus='this.blur();' onclick="document.getElementById('div_pt5.12').style.display = 'none' " >
           [x]</a>
        </div>
        <pre>
        
pt5.12: 200 OK


        </pre>
    </div>
    <!--css div popup end-->

    </td>
</tr>

<tr id='pt5.13' class='hiddenRow'>
    <td class='none'><div class='testcase'>test__13_: 操作后订单详情： 实际垫资金额</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt5.14' class='hiddenRow'>
    <td class='none'><div class='testcase'>test__14_: 操作后订单详情： 实际提车时间</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr class='passClass'>
    <td>order_flow_step6.ReceiveTest:  订单流程：6.确认交车 </td>
    <td>16</td>
    <td>16</td>
    <td>0</td>
    <td>0</td>
    <td><a href="javascript:showClassDetail('c6',16)">Detail</a></td>
</tr>

<tr id='pt6.1' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_1_before_name: 操作前订单详情： 客户姓名</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt6.2' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_2_before_telephone: 操作前订单详情： 客户电话</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt6.3' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_3_before_selling_price: 操作前订单详情： 合同应收款总额</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt6.4' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_4_before_body_price: 操作前订单详情： 车身售价</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt6.5' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_5_before_selling_deposit_amount: 操作前订单详情： 客户订金收取</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt6.6' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_6_before_contract_number: 操作前订单详情： 订单编号</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt6.7' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_7_before_buying_price: 操作前订单详情： 车身进价</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt6.8' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_8_before_buying_deposit_amount: 操作前订单详情： 资源订金支付</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt6.9' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_9_before_expected_time_of_pick_up: 操作前订单详情： 预计提车时间</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt6.10' class='hiddenRow'>
    <td class='none'><div class='testcase'>test__10_before_buying_advance: 操作前订单详情： 预估垫资金额</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt6.11' class='hiddenRow'>
    <td class='none'><div class='testcase'>test__11_before_freight: 操作前订单详情: 大板运费</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt6.12' class='hiddenRow'>
    <td class='none'><div class='testcase'>test__12_before_actual_advance: 操作前订单详情: 实际垫资金额</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt6.13' class='hiddenRow'>
    <td class='none'><div class='testcase'>test__13_before_actual_time_of_pick_up: 操作前订单详情: 实际提车时间</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt6.14' class='hiddenRow'>
    <td class='none'><div class='testcase'>test__14_check: 发送完成交车请求</div></td>
    <td colspan='5' align='center'>

    <!--css div popup start-->
    <a class="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_pt6.14')" >
        pass</a>

    <div id='div_pt6.14' class="popup_window">
        <div style='text-align: right; color:red;cursor:pointer'>
        <a onfocus='this.blur();' onclick="document.getElementById('div_pt6.14').style.display = 'none' " >
           [x]</a>
        </div>
        <pre>
        
pt6.14: 200 OK


        </pre>
    </div>
    <!--css div popup end-->

    </td>
</tr>

<tr id='pt6.15' class='hiddenRow'>
    <td class='none'><div class='testcase'>test__15_after_actual_receive_at: 操作后订单详情：实际交车日期</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt6.16' class='hiddenRow'>
    <td class='none'><div class='testcase'>test__16_after_plate_number: 操作后订单详情：车牌号</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr class='passClass'>
    <td>order_flow_step7.CloseTest:  订单流程：7.完成结算 </td>
    <td>16</td>
    <td>16</td>
    <td>0</td>
    <td>0</td>
    <td><a href="javascript:showClassDetail('c7',16)">Detail</a></td>
</tr>

<tr id='pt7.1' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_1_before_name: 操作前订单详情： 客户姓名</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt7.2' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_2_before_telephone: 操作前订单详情： 客户电话</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt7.3' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_3_before_selling_price: 操作前订单详情： 合同应收款总额</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt7.4' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_4_before_body_price: 操作前订单详情： 车身售价</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt7.5' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_5_before_selling_deposit_amount: 操作前订单详情： 客户订金收取</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt7.6' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_6_before_contract_number: 操作前订单详情： 订单编号</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt7.7' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_7_before_buying_price: 操作前订单详情： 车身进价</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt7.8' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_8_before_buying_deposit_amount: 操作前订单详情： 资源订金支付</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt7.9' class='hiddenRow'>
    <td class='none'><div class='testcase'>test_9_before_expected_time_of_pick_up: 操作前订单详情： 预计提车时间</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt7.10' class='hiddenRow'>
    <td class='none'><div class='testcase'>test__10_before_buying_advance: 操作前订单详情： 预估垫资金额</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt7.11' class='hiddenRow'>
    <td class='none'><div class='testcase'>test__11_before_freight: 操作前订单详情: 大板运费</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt7.12' class='hiddenRow'>
    <td class='none'><div class='testcase'>test__12_before_freight: 操作前订单详情: 实际垫资金额</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt7.13' class='hiddenRow'>
    <td class='none'><div class='testcase'>test__13_before_actual_time_of_pick_up: 操作前订单详情: 实际提车时间</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt7.14' class='hiddenRow'>
    <td class='none'><div class='testcase'>test__14_before_actual_receive_at: 操作前订单详情：实际交车日期</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt7.15' class='hiddenRow'>
    <td class='none'><div class='testcase'>test__15_before_plate_number: 操作前订单详情：车牌号</div></td>
    <td colspan='5' align='center'>pass</td>
</tr>

<tr id='pt7.16' class='hiddenRow'>
    <td class='none'><div class='testcase'>test__16_check: 发送完成结算请求</div></td>
    <td colspan='5' align='center'>

    <!--css div popup start-->
    <a class="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_pt7.16')" >
        pass</a>

    <div id='div_pt7.16' class="popup_window">
        <div style='text-align: right; color:red;cursor:pointer'>
        <a onfocus='this.blur();' onclick="document.getElementById('div_pt7.16').style.display = 'none' " >
           [x]</a>
        </div>
        <pre>
        
pt7.16: 200 OK


        </pre>
    </div>
    <!--css div popup end-->

    </td>
</tr>

<tr id='total_row'>
    <td>Total</td>
    <td>88</td>
    <td>88</td>
    <td>0</td>
    <td>0</td>
    <td>&nbsp;</td>
</tr>
</table>

<div id='ending'>&nbsp;</div>

</body>
</html>
