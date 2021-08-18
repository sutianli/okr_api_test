import json
import logging
import  unittest

import requests
from config import config
from lib.HTMLTestReportCN import HTMLTestRunner
from lib.send_email import send_email
from config.config import *

'''
def login():
 
    url = 'http://test.quasar.oa.com:8082/platform/api/apptenant/FakeUser'
    data = {"App": "okr", "Tenant": "Tencent", "StaffID": "33924", "Domain": ""}
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json;charset=UTF-8",
        "Cookie": config.cookie
    }
    res=requests.post(url,data=json.dumps(data),headers=headers)
    try:
        res = requests.post(url, data=json.dumps(data), headers=headers)
    except IOError:
        logging.ERROR("login接口访问失败")
        return
    else:
        #获取返回的cookie，可以通过res.cookies["cookie_name"]的方式获取
        COOKIE=res.cookies
        print(COOKIE)
    '''

logging.info("====================== 测试开始 =======================")
suite = unittest.defaultTestLoader.discover("./tests/case")#路径不对，找不到用例下面代码会报：ZeroDivisionError: float division by zero
with open("report.html", 'wb') as f:  # 改为with open 格式
    HTMLTestRunner(stream=f, title="OKR Api Test", description="简单的接口测试", tester="老男孩").run(suite)

if send_email_after_run:
    send_email('report.html')  # 发送邮件

logging.info("======================= 测试结束 =======================")






