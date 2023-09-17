"""
时间： 2023-09-09 : 15:39
功能：获取目录路径
"""
import os

# 项目根目录
Base_dir = os.path.dirname(os.path.dirname(__file__))
# 测试报告存放文件夹路径
testReport = os.path.join(Base_dir, "testReport")
temp_json = os.path.join(testReport, "temp_json")
report_path = os.path.join(testReport, "report")
# 日志存放路径
testLog = os.path.join(Base_dir, "testLog")
# 测试数据存放路径
testData = os.path.join(Base_dir, "testData")
