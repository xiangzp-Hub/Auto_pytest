"""
功能：发送接口请求；依据传参来判断发送get、post请求方法
"""
# 导包
import requests


class SendHttp:
    def __init__(self, dic):
        """
        :param dic: 接口/用例-数据-->dict
        """
        self.data = dic
        self.interfaceUrl = dic["interfaceUrl"]
        self.header = dic["header"]
        self.value = dic["value"]

    # 发送接口请求
    def run_request(self):
        # 获取测试数据method字段，请求方式
        method = self.data["method"]
        # 判断 method 的请求方式，调用接口
        if method.lower() == 'get':
            return self.__get()
        # 发送post请求
        elif method.lower() == 'post':
            return self.__post()

    def __get(self):
        return requests.get(url=self.interfaceUrl,
                            headers=eval(self.header),
                            params=eval(self.value))

    def __post(self):
        return requests.post(url=self.interfaceUrl,
                             headers=eval(self.header),
                             data=eval(self.value))


if __name__ == '__main__':
    # 获取测试数据
    from common.readData import ReadData
    dic = ReadData('data.xls').read_excel(0)[1]
    print(dic)

    # 实例化接口类
    ht = SendHttp(dic)
    # 调用接口发送方法
    sd = ht.run_request()
    print(sd.status_code)
