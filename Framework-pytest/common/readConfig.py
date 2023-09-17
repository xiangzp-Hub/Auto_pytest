"""
时间： 2023-09-09 : 16:53
功能：读取配置文件类方法
思路：
    创建一个类
1. 定义初始化方法:
    1.1 获取配置文件的路径
    1.2 实例化configpraser类
    1.3 使用“configpraser”：读取指定路径下面的配置文件
        -,reader(path，encoding)
2. 定义一个对外方法,获取某个section下面所有option的值:
    传一个参数；获取section下面所有option
    传二个参数：获取section下面所有option的值value
"""

# 导包
import os
from configparser import ConfigParser
from common.getOS import Base_dir


class ReadConfig:
    def __init__(self, fileName="config.ini"):
        """
        :param fileName: 配置文件名称;默认：config.ini
        """
        # 获取配置文件路径
        self.config_dir = os.path.join(Base_dir, fileName)
        # 实例化configparser类
        self.conf = ConfigParser()
        # 读取指定路径下的配置文件信息
        self.conf.read(self.config_dir, encoding='utf-8')

    # 获取配置文件信息（主函数）
    def read_config(self, *args):
        if len(args) == 1:
            # 获取配置文件中的 "option"
            # return self.conf.items(args[0])
            return self.conf.options(args[0])
        elif len(args) == 2:
            # 获取配置文件中的 "option"的值value
            return self.conf.get(args[0], args[1])
        else:
            return '参数传递错误！'


if __name__ == '__main__':
    path = os
    rc = ReadConfig('config.ini')
    print(rc.config_dir)
    res = rc.read_config("redis","host")
    print(res)
