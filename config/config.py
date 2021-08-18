import logging
import os
import time
from optparse import OptionParser


# 项目路径
today = time.strftime('%Y%m%d', time.localtime())
now = time.strftime('%Y%m%d_%H%M%S', time.localtime())

#登录login接口需要用到的请求头，cookie需要经常更换
cookie='Quasar_TOF_TICKET=TOF4~eyJ2IjoiNCIsInRpZCI6Ik1icmJYcWU3NzY4bWRUdUg4WGx1aXBOVmpuMm9QaHN5IiwiaXNzIjoiMS4xLjEuMSIsImhrIjoiIiwiaWF0IjoiMjAyMS0wOC0xOFQxNDo0ODo0MC44MTY4NzMyMzUrMDg6MDAiLCJhdWQiOiIxMC45Ny4yMzYuNDUiLCJoYXNoIjoiQTNDNDE1REUwQTdGNkYwNTFBQkNBQ0Y2OUM0RTYxMDIyN0FCMEJBQkI3QTU4MjQ4ODQyQzBCN0JBM0IwMkRDRSJ9; Auth_UserInfo_Quasar=%7B%22UserID%22%3A%2233924%22%2C%22UserName%22%3A%22williszuo%28%E5%B7%A6%E5%BF%A0%E8%B1%AA%29%22%2C%22UserEngName%22%3A%22williszuo%22%2C%22StaffPropertyID%22%3A%225%22%2C%22OrgID%22%3A%2214322%22%2C%22OrgName%22%3A%22%E8%96%AA%E9%85%AC%E7%A6%8F%E5%88%A9%E5%BC%80%E5%8F%91%E7%BB%84%22%2C%22Tenant%22%3A%22Tencent%22%2C%22LoginUserID%22%3A%2233924%22%2C%22LoginUserName%22%3A%22williszuo%28%E5%B7%A6%E5%BF%A0%E8%B1%AA%29%22%2C%22LoginUserEngName%22%3A%22williszuo%22%2C%22LoginTenant%22%3A%22Tencent%22%7D; Auth_Quasar=BYDHQQn_R6NdCjwkwwaU759Zkns7AwkGhhxft4uQ122-41VcNP98DagUVDd30QMEloQP6BYvrgd5%0D%0ASxtquPT8p39a7o1zNCl4E_J7nlKYPBNd6EOni1bxY6hLL7rFPwKhByeI-KLyaMbLgRfOhHyIGHyS%0D%0AFNuoT9yiV7CF4Ms6KBLUbnwqgoXxP4urR1HsMzkXDYxrby9n4vyvs1JF3Fa0Evh6Yow0mmS_TqQX%0D%0A0_8KYClnaZyNyGvb9hQyekp5MYbBOg9Ee2X_FM5Vk4iq83lpHXyxk90cZAuhKPHM9nRGu-ybljzT%0D%0AmEuRfy_RXJTiPK0dqsiZ5tdPpa3uA9tINTmIzKiuNeE7IZCLe5FNoaLSXxBySjKcakPKNIJQeYic%0D%0AeuDF%0D%0A%26%261629270148543'
setcookie='Auth_UserInfo_Quasar=%7B%22UserID%22%3A%2233924%22%2C%22UserName%22%3A%22williszuo%28%E5%B7%A6%E5%BF%A0%E8%B1%AA%29%22%2C%22UserEngName%22%3A%22williszuo%22%2C%22StaffPropertyID%22%3A%225%22%2C%22OrgID%22%3A%2214322%22%2C%22OrgName%22%3A%22%E8%96%AA%E9%85%AC%E7%A6%8F%E5%88%A9%E5%BC%80%E5%8F%91%E7%BB%84%22%2C%22Tenant%22%3A%22Tencent%22%2C%22LoginUserID%22%3A%2233924%22%2C%22LoginUserName%22%3A%22williszuo%28%E5%B7%A6%E5%BF%A0%E8%B1%AA%29%22%2C%22LoginUserEngName%22%3A%22williszuo%22%2C%22LoginTenant%22%3A%22Tencent%22%7D; Path=/'

prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 当前文件的上一级的上一级目录（增加一级）
#生成文件
report_file = os.path.join(prj_path, 'report/report.html'.format(now))  # 也可以每次生成新的报告
log_file = os.path.join(prj_path, 'log.txt'.format(today))  # 也可以每天生成新的日志文件
# report_file = os.path.join(prj_path, 'report','report.html')  # 更改路径到report目录下
# log_file = os.path.join(prj_path, 'log','log.txt')  # 更改路径到log目录下

#读取文件
data_file=os.path.join(prj_path,'data','test_okr_data.xlsx')
testlist_file=os.path.join(prj_path,'tests','textlist.txt')
last_fails_file=os.path.join(prj_path,'last_failapi.pickle')

#数据路径
data_path = os.path.join(prj_path, 'data')  # 数据目录
test_path = os.path.join(prj_path, 'tests')   # 用例目录
test_case_path=os.path.join(prj_path,'tests','case')
# data_path = prj_path  # 数据目录，暂时在项目目录下
# test_path = prj_path  # 用例目录，暂时在项目目录下


# 数据库配置
db_host = '127.0.0.1'   # 自己的服务器地址
db_port = 3306
db_user = 'root'
db_passwd = '123456'
db = 'yun_bc_credit'

# 邮件配置
smtp_server = 'smtp.163.com'
smtp_user = 'stl298458@163.com'
smtp_password = 'GYNECKOIRSAKBXLG'
sender = smtp_user  # 发件人
receiver = '495225829@qq.com'  # 收件人
subject = '接口测试报告'  # 邮件主题

send_email_after_run = False  #配置邮件开关

# log配置
logging.basicConfig(level=logging.INFO,  # log level,
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename=log_file,  # 日志输出文件
                    filemode='a')  # 追加模式

if __name__ == '__main__':
    logging.info("hello")


'''
Log Level:

CRITICAL: 用于输出严重错误信息
ERROR: 用于输出错误信息qa

qw

WARNING: 用于输出警示信息
INFO: 用于输出一些提升信息
DEBUG: 用于输出一些调试信息
优先级 CRITICAL > ERROR > WARNING > INFO > DEBUG
指定level = logging.DEBUG所有等级大于等于DEBUG的信息都会输出
若指定level = logging.ERROR WARNING,INFO,DEBUG小于设置级别的信息不会输出

日志格式:

%(levelno)s: 打印日志级别的数值
%(levelname)s: 打印日志级别名称
%(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
%(filename)s: 打印当前执行程序名
%(funcName)s: 打印日志的当前函数
%(lineno)d: 打印日志的当前行号
%(asctime)s: 打印日志的时间
%(thread)d: 打印线程ID
%(threadName)s: 打印线程名称
%(process)d: 打印进程ID
%(message)s: 打印日志信息
'''

# 命令行选项
parser = OptionParser()
parser.add_option('--collect-only', action='store_true', dest='collect_only', help='仅列出所有用例')
parser.add_option('--rerun-fails', action='store_true', dest='rerun_fails', help='运行上次失败的用例')
parser.add_option('--testlist', action='store_true', dest='testlist', help='运行test/testlist.txt列表指定用例')
parser.add_option('--testsuite', action='store', dest='testsuite', help='运行指定的TestSuite')
parser.add_option('--tag', action='store', dest='tag', help='运行指定tag的用例')
(options, args) = parser.parse_args()  # 应用选项（使生效）

data={
    "Basic": {
    "StaffID": "33924",
    "StaffName": "williszuo(左忠豪)",
    "PeriodID": "60b5083d39ab1a11c32ec9c5",
    "PeriodName": {
    "CN": "2021 7~8月",
    "EN": "Jul to Aug, 2021"
    }
    },
    "BizDataList": [
    {
    "Objective": {
    "TypeID": "Achievement",
    "TypeName": {
    "CN": "业务",
    "EN": "Business goal"
    },
    "Index": 1,
    "Content": "目标可以适当激进，实现与否要有明确可衡量的标准。",
    "ROP": 40,
    "Prop": 33,
    "ModifyProp": False,
    "ProgressID": "Risky",
    "ProgressName": {
    "CN": "有风险",
    "EN": "Alert"
    },
    "RelationShip": [
    {
    "OID": "6113951a9e2c000d83c9eb49",
    "OName": "tea士大夫士大夫三大",
    "OwnerID": "23416",
    "OwnerName": "johnsonyang(杨俊森)"
    }
    ],
    "At": [
    {
    "StaffID": "50497",
    "StaffName": "taylorchen(陈君)"
    }
    ],
    "Observers": []
    },
    "KeyResults": [
    {
    "ID": "gl2drp34",
    "Content": "目标可以适当激进，实现与否要有明确可衡量的标准。",
    "ROP": 40,
    "Prop": 100,
    "ModifyProp": True,
    "TypeID": "Number",
    "TypeName": {
    "CN": "数值类型",
    "EN": "by #"
    },
    "BaseScore": 0,
    "TargetScore": 100,
    "CurScore": 40,
    "At": []
    }
    ],
    "PublicScope": {
    "TypeID": "FreeForAll",
    "TypeName": {
    "CN": "公司全员公开",
    "EN": "All Tencent employees"
    },
    "Value": []
    },
    "ObjectID": "610bc8eabc5c467323271b14"
    },
    {
    "Objective": {
    "TypeID": "Achievement",
    "TypeName": {
    "CN": "业务",
    "EN": "Business goal"
    },
    "Index": 2,
    "Content": "在填写之前，请再次确认是否跟你的上级和团队达成共识，如果还没有",
    "ROP": 0,
    "Prop": 33,
    "ModifyProp": False,
    "ProgressID": "Good",
    "ProgressName": {
    "CN": "正常",
    "EN": "Normal"
    },
    "RelationShip": [],
    "At": [],
    "Observers": []
    },
    "KeyResults": [
    {
    "ID": "xxugrw7f",
    "Content": "在填写之前，请再次确认是否跟你的上级和团队达成共识，如果还没有，请先做这一步再来填写！",
    "ROP": 0,
    "Prop": 100,
    "ModifyProp": False,
    "TypeID": "Default",
    "TypeName": {
    "CN": "系统默认",
    "EN": "Default"
    },
    "BaseScore": 0,
    "TargetScore": 100,
    "CurScore": 0,
    "At": []
    }
    ],
    "PublicScope": {
    "TypeID": "FreeForAll",
    "TypeName": {
    "CN": "公司全员公开",
    "EN": "All Tencent employees"
    },
    "Value": []
    },
    "ObjectID": "610bc8eabc5c467323271b15"
    },
    {
    "Objective": {
    "TypeID": "Achievement",
    "TypeName": {
    "CN": "业务",
    "EN": "Business goal"
    },
    "Index": 3,
    "Content": "目标回答的是“我们想做什么”的问题，是定性的，是简洁直白的陈述。",
    "ROP": 0,
    "Prop": 34,
    "ModifyProp": False,
    "ProgressID": "Good",
    "ProgressName": {
    "CN": "正常",
    "EN": "Normal"
    },
    "RelationShip": [],
    "At": [],
    "Observers": []
    },
    "KeyResults": [
    {
    "ID": "qym0s1ur",
    "Content": "目标回答的是“我们想做什么”的问题，是定性的，是简洁直白的陈述，能鼓舞人心、能激发团队共鸣。",
    "ROP": 0,
    "Prop": 100,
    "ModifyProp": False,
    "TypeID": "Default",
    "TypeName": {
    "CN": "系统默认",
    "EN": "Default"
    },
    "BaseScore": 0,
    "TargetScore": 100,
    "CurScore": 0,
    "At": []
    }
    ],
    "PublicScope": {
    "TypeID": "FreeForAll",
    "TypeName": {
    "CN": "公司全员公开",
    "EN": "All Tencent employees"
    },
    "Value": []
    },
    "ObjectID": "610bc8eabc5c467323271b16"
    }
    ],
    "SettingID": "610b6728bc5c467323265b5b"
}