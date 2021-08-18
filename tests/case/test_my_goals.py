import unittest
import config.config
import requests
from lib.case_log import log_case_info

class TestMyGoals(unittest.TestCase):
    def test_MyList(self):
        url="http://test.quasar.oa.com:8082/okr/api/Period/MyList"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json;charset=UTF-8",
            "Cookie": config.config.cookie
        }
        res=requests.post(url=url,headers=headers)
        print(res.text)
        result=res.json()['IsSuccess']#获取返回的某个字段值
        self.assertTrue(result)#不为true返回false
        self.assertEqual(res.status_code,200)
        log_case_info('test_MyList',url,'',res.text)


    def test_MyObjectListByPeriod(self):
        url="http://test.quasar.oa.com:8082/okr/api/Object/MyObjectListByPeriod"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json;charset=UTF-8",
            "Cookie": config.config.cookie
        }
        data='{"PeriodID":"60b5083d39ab1a11c32ec9c5","ProgressIDList":[]}'
        res=requests.post(url=url,headers=headers,data=data)
        print(res.text)
        result=res.json()['IsSuccess']#获取返回的某个字段值
        self.assertTrue(result)#不为true返回false
        self.assertEqual(res.status_code,200)
        log_case_info('test_MyObjectListByPeriod',url,data,res.text)

    def test_GetSpecifiedGroupTree(self):
        url="http://test.quasar.oa.com:8082/okr/api/Object/GetSpecifiedGroupTree"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json;charset=UTF-8",
            "Cookie": config.config.cookie
        }
        params = {"StaffID": "33924", "PeriodID":"60b5083d39ab1a11c32ec9c5"}
        res=requests.get(url=url,headers=headers,params=params)
        print(res.text)
        result=res.json()['IsSuccess']#获取返回的某个字段值
        self.assertTrue(result)#不为true返回false
        self.assertEqual(res.status_code,200)
        log_case_info('test_GetSpecifiedGroupTree', url, '', res.text)

    def test_SaveObjects(self):
        url="http://test.quasar.oa.com:8082/okr/api/Object/SaveObjects"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json;charset=UTF-8",
            "Cookie": config.config.cookie
        }
        data=config.config.data
        res=requests.post(url=url,headers=headers,json=data)
        print(res.text)
        result=res.json()['IsSuccess']#获取返回的某个字段值
        self.assertTrue(result)#不为true返回false
        self.assertEqual(res.status_code,200)
        log_case_info('test_SaveObjects', url, data, res.text)

# if __name__ == '__main__':   # 非必要，用于测试我们的代码
#     unittest.main(verbosity=2)
#
