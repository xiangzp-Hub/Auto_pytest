# 导包
import pytest
from common.readData import ReadData
from common.sendHttp import SendHttp
from common.publicAssert import PublicAssert
from common.interface_Rely import Interface_Rely
from common.printLog import logger

# 实例化读取数据
test_data = ReadData('data.xls').read_excel(1)


class TestApi:

    @pytest.mark.parametrize("case", test_data)
    def test_01_demo(self, case):
        # 实例化接口依赖对象
        rely = Interface_Rely(test_data)
        case["header"], case["value"] = rely.rely_run(case)
        # 实例化发送接口对象
        http = SendHttp(case).run_request()
        # 实例化断言对象
        assert1 = PublicAssert(case, http)
        assert1.public_assert()


if __name__ == '__main__':
    pytest.main(['vs'])
