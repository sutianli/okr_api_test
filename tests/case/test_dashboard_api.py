import json
import logging
import  unittest

import requests

import config.config
from lib.case_log import log_case_info


class TestDashBoardAPI(unittest.TestCase):
    def test_GetCurrentSettingAndModel(self):
        url="http://test.quasar.oa.com:8082/okr/api/Setting/GetCurrentSettingAndModel"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json;charset=UTF-8",
            "Cookie": config.config.cookie
        }
        params={'StaffID':'33924'}
        res=requests.get(url=url,headers=headers,params=params)
        print(res.text)
        if res.status_code !=200:
            config.config.send_email_after_run = True
        result = res.json()['IsSuccess']  # 获取返回的某个字段值
        self.assertTrue(result)#不为true返回false
        self.assertEqual(res.status_code,200)
        log_case_info('test_GetCurrentSettingAndModel', url, '', res.text)
        if result==False:
            config.config.send_email_after_run=True



'''
    def test_UnReadNotificationCount(self):
        url="http://test.quasar.oa.com:8082/okr/api/Notification/UnReadNotificationCount"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json;charset=UTF-8",
            "Cookie": config.config.cookie
        }
        res=requests.post(url=url,headers=headers)
        print(res.text)
        result = res.json()['IsSuccess']  # 获取返回的某个字段值
        self.assertTrue(result)  # 不为true返回false
        self.assertEqual(res.status_code, 200)
        log_case_info('test_UnReadNotificationCount', url, '', res.text)

    def test_QueryNavigateList(self):
        url = "http://test.quasar.oa.com:8082/okr/api/BulletinBoard/QueryNavigateList"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json;charset=UTF-8",
            "Cookie": config.config.cookie
        }
        res = requests.get(url=url, headers=headers)
        print(res.text)
        result = res.json()['IsSuccess']  # 获取返回的某个字段值
        self.assertTrue(result)  # 不为true返回false
        self.assertEqual(res.status_code, 200)
        log_case_info('test_QueryNavigateList', url, '', res.text)

    def test_GetNewestNotifications(self):
        url = "http://test.quasar.oa.com:8082/okr/api/Notification/GetNewestNotifications"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json;charset=UTF-8",
            "Cookie": config.config.cookie
        }
        res = requests.get(url=url, headers=headers)
        print(res.text)
        result = res.json()['IsSuccess']  # 获取返回的某个字段值
        self.assertTrue(result)  # 不为true返回false
        self.assertEqual(res.status_code, 200)
        log_case_info('test_GetNewestNotifications', url, '', res.text)

    def test_QueryMyDashboard(self):
        url = "http://test.quasar.oa.com:8082/okr/api/BulletinBoard/QueryMyDashboard"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json;charset=UTF-8",
            "Cookie": config.config.cookie
        }
        res = requests.get(url=url, headers=headers)
        print(res.text)
        result = res.json()['IsSuccess']  # 获取返回的某个字段值
        self.assertTrue(result)  # 不为true返回false
        self.assertEqual(res.status_code, 200)
        log_case_info('test_QueryMyDashboard', url, '', res.text)

    def test_UnReadNotificationCountStatistics(self):
        url = "http://test.quasar.oa.com:8082/okr/api/Notification/UnReadNotificationCountStatistics"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json;charset=UTF-8",
            "Cookie": config.config.cookie
        }
        #字符串格式
        # data='{"ModelID":"5f9654dac34f814c108deb05"}'
        # res = requests.post(url=url, headers=headers,data=data)
        #字典格式
        data={
            "ModelID": "5f9654dac34f814c108deb05"
        }
        # res=requests.post(url=url, headers=headers,data=data)  data支持字典或字符串
        # res=requests.post(url=url, headers=headers,data=json.dumps(data))#使用json.dumps()转换为合法的json字符串格式
        res = requests.post(url=url, headers=headers, json=data)#直接将data数据赋值给post方法的json参数
        print(res.text)
        result = res.json()['IsSuccess']  # 获取返回的某个字段值
        self.assertTrue(result)  # 不为true返回false
        self.assertEqual(res.status_code, 200)
        log_case_info('test_UnReadNotificationCountStatistics', url, data, res.text)

    def test_GetCurrentNotifications(self):
        url = "http://test.quasar.oa.com:8082/okr/api/Notification/GetCurrentNotifications"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json;charset=UTF-8",
            "Cookie": config.config.cookie
        }
        data = '{"Query":{"Basic.ActionID":{"$in":["10","50","90","130","140","150","160"]},"Basic.ReadStatusID":"0"},"Skip":0,"Limit":20}'
        res = requests.post(url=url, headers=headers, data=data)  # 直接将data数据赋值给post方法的json参数
        print(res.text)
        result = res.json()['IsSuccess']  # 获取返回的某个字段值
        self.assertTrue(result)  # 不为true返回false
        self.assertEqual(res.status_code, 200)
        log_case_info('test_GetCurrentNotifications', url, data, res.text)

    def test_ReportList(self):
        url = "http://test.quasar.oa.com:8082/okr/api/Report/List"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json;charset=UTF-8",
            "Cookie": config.config.cookie
        }
        data = '{"Skip":0,"Limit":10,"StaffID":"33924"}'
        res = requests.post(url=url, headers=headers, data=data)  # 直接将data数据赋值给post方法的json参数
        print(res.text)
        result = res.json()['IsSuccess']  # 获取返回的某个字段值
        self.assertTrue(result)  # 不为true返回false
        self.assertEqual(res.status_code, 200)
        log_case_info('test_ReportList', url, data, res.text)

    def test_ReportHtml(self):
        url = "http://test.quasar.oa.com:8082/okr/api/Report/Html"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json;charset=UTF-8",
            "Cookie": config.config.cookie
        }
        params={"StaffID": "33924","ReportID": "6059d9194bdd863f62ed3014"}
        res = requests.post(url=url, headers=headers, params=params)

        result = res.json()['IsSuccess']  # 获取返回的某个字段值
        self.assertTrue(result)  # 不为true返回false
        self.assertEqual(res.status_code, 200)
        log_case_info('test_ReportHtml', url, '', res.text)
'''
# if __name__ == '__main__':   # 非必要，用于测试我们的代码
#     unittest.main(verbosity=2)







