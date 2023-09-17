"""
时间： 2023-09-08 : 14:22
功能：公共断言方法
思路：
    1、传入参数1：测试用例数据-绑定实例属性 __init -->获取预期结果
    2、传入参数2：响应结果数据res -->获取res.json、res.status_code
    3、assert 断言实际结果 和 预期结果
"""
# 导包
from jsonpath import jsonpath
from common.printLog import logger


class PublicAssert:
    def __init__(self, dic_data, res_data):
        """
        获取测试用例数据 和 实际响应数据
        :param dic_data:测试用例数据 -->dict
        :param res_data:响应结果数据 -->object
        """
        self.testdata = dic_data
        self.res = res_data.json()
        # 获取响应状态码code
        self.status_code = res_data.status_code

    def public_assert(self):
        try:
            # 断言状态
            self.__assert_status_code()
            # 断言“实际结果”和“预期结果”值
            self.__assert_expect()
            # 打印日志
            logger.info("测试通过")
        except AssertionError as e:
            logger.error('失败',e)
            raise e


    def __assert_status_code(self):
        """断言响应状态码"""
        assert self.status_code in [200, 304], f"请求失败，响应状态码：{self.status_code}"

    def __assert_expect(self):
        """断言预期结果和实际结果值"""
        # 获取预期结果值 expect
        expect = eval(self.testdata['expect'])
        # 遍历expect字典数据，获取key，value
        for k, v in expect.items():
            # 根据k去响应数据中获取实际的值
            res_value = jsonpath(self.res, "$.." + k)[0]
            # 断言数据实际结果 和 预期结果
            assert str(res_value) == v, f"实际结果：[{res_value}] 与预期结果：[{v}] 不符"


if __name__ == '__main__':
    # 获取测试数据
    from common.readData import ReadData

    dic_data = ReadData("data.xls").read_excel(0)[2]

    # 发送结果请求，获取实际结果
    from common.sendHttp import SendHttp

    res_data = SendHttp(dic_data).run_request()

    # 实例化断言对象
    ps = PublicAssert(dic_data, res_data)
    # 调用断言实例方法
    ps.public_assert()
