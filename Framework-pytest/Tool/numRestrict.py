"""
时间： 2023-09-09 : 16:10
功能：控制某个文件下文件夹或文件的数量

"""
# 导包
import shutil
from common.getOS import *


# 控制测试报告"testReport/report"文件夹的数量
def clear_report(n):
    # 获取路径:
    # path = os.path.dirname(os.path.dirname(__file__)) + r"/testReport/"
    path = testReport + "/"
    # os.listdir:获取目录下所有文件名得到一个列表
    file_list = os.listdir(path)
    # 根据创建时间对文件进行排序
    file_list.sort(key=lambda x: os.path.getctime(path + x))
    # 循环删除列表内每一个文件夹
    for i in file_list[:-n]:
        shutil.rmtree(path + i)


# 控制日志"testLog"下文件的数量
def clear_log(n):
    # 获取路径:
    path = testLog + "/"
    # os.listdir:获取目录下所有文件名得到一个列表
    file_list = os.listdir(path)
    # 根据创建时间对文件进行排序
    file_list.sort(key=lambda x: os.path.getctime(path + x))
    # 循环删除列表内每一个文件夹
    for i in file_list[:-n]:
        os.remove(path + i)



if __name__ == '__main__':
    # 报告
    # clear_report(2)
    # 日志
    clear_log(5)
