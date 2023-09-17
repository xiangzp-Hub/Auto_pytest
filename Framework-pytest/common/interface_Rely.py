"""
时间： 2023-09-08 : 17:37
功能：处理接口依赖
思路：
    1、通过传参，使用正则表达式，提取依赖关键字段
    2、判断参数数据定义好的字段 rely 和 caseid，
      --> 该条case是否有依赖，并且依赖的接口是哪个
      --> 调用依赖的接口，获取实际依赖的数据
    3、替换需要依赖数据接口的依赖字段
"""
import re
from jsonpath import jsonpath
from common.sendHttp import SendHttp

class Interface_Rely:
    def __init__(self, testData):
        """
        :param testData: 获取所有的测试数据[{},{}]
        """
        self.testdata = testData

    # 处理依赖的方法
    def rely_run(self, dic):
        """
        处理依赖方法
        :param dic: 单条“case”数据
        :return:1-需要处理依赖：返回替换后结果 2-不需要处理依赖，直接返回原数据
        """
        # 获取测试数据中关键字段
        header = dic['header']
        body = dic['value']
        caseid = dic['caseid']
        rely = dic['rely']
        # print(f"获取到数据：header：{header}，body：{body}，caseid：{caseid},rely：{rely}")
        # 判断rely和caseid，是否需要处理依赖
        if rely.lower() == 'y' and caseid is not None:
            # 调用提取依赖字段key的函数
            goal_header = self._get_rely_key(header)
            goal_body = self._get_rely_key(body)
            # 调用，依据依赖key从响应中提取值的方法
            h, b = self.__get_value(caseid, goal_header, goal_body)
            # 判断提取的结果h是否为空，则替换掉测试数据中依赖字段的key
            if h is not None:
                header = header.replace("${" + goal_header + "}", h)
            if b is not None:
                body = body.replace("${" + goal_body + "}",b)
            # 返回替换后的数据
            return header, body
        # 不满足，则直接返回原数据
        else:
            return header, body

    # 提取需要依赖数据接口中的字段字段key
    def _get_rely_key(self, data):
        """
        :param data: 有需要处理依赖的字段：header/body
        :return:返回提取的依赖字段的key值
        """
        # 使用正则表达式提取依赖字段中依赖数据key
        res_data = re.findall(r"\${(.*?)}", data)
        if len(res_data) != 0:
            res_data = res_data[0]
            return res_data
        else:
            return None

    # 根据提取到依赖信息字段的key值，从响应中提取实际的值
    def __get_value(self, caseid, goal_header=None, goal_body=None):
        """
        :param caseid: 依赖数据接口的id-->int
        :param goal_header: header中依赖的字段key
        :param goal_body: body中依赖的字段key
        :return:返回提取到的依赖字段值
        """
        # 获取依赖接口的数据
        data = self.testdata[int(caseid) - 1]
        # 调用发送接口的实例-->得到接口返回的数据信息
        res_data = SendHttp(data).run_request()
        # 判断goal_header和goal_body是否为空；是否进行提取
        if goal_header is not None:
            # 根据“goal_header”去，接口中找实际的值
            goal_header = res_data.headers[goal_header]
        if goal_body is not None:
            # 根据“goal_body”去，接口中找实际的值
            goal_body = jsonpath(res_data.json(), "$.." + goal_body)[0]

        # 返回提取到的依赖字段值
        return goal_header, goal_body


if __name__ == '__main__':
    from common.readData import ReadData
    datacase = ReadData('data.xls').read_excel(1)
    dic = datacase[4]
    # print(dic)

    # 实例化依赖对象
    rely = Interface_Rely(datacase)
    aa = rely.rely_run(dic)
    print(aa)








