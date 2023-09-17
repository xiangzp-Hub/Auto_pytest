"""
时间处理
"""
import time


def getTime():
    """
       获取当前时间，以年-月-日  时_分_秒  形式显示
       :return:
    """
    time_now = time.strftime("%Y_%m_%d_%H_%M_%S")
    return time_now


# 调用时可直接使用(单例模式)
time_now = getTime()


def baseTime():
    """时间包的基本应用方法"""
    # 1. 获取时间戳:1970年1月1日早晨8点(东8区)到现在过了多少秒
    print(time.time())
    # 2. 获取当前时间对象,给他时间戳他会转化为时间对象
    print(time.localtime())
    print(time.localtime(0))
    # 3. 获取0时区的时间(格林威治)
    print(time.gmtime())
    print(time.gmtime(0))
    # 4 将时间对象转化为时间戳
    print(time.mktime(time.localtime()))
    # 5 睡眠
    # time.sleep(5)
    # print("下班")
    # 6. 将时间对象进行固定格式输出(老外常见的)
    print(time.asctime())
    print(time.asctime(time.localtime(0)))
    # 7. 将时间戳按照固定格式输出(老外常见的)
    print(time.ctime())
    print(time.ctime(0))
    # 8. 将时间对象转化为自定义的格式输出
    print(time.strftime("%Y_%m_%d_%H_%M_%S"))
    # 9. 将表示时间的字符串,反转化为时间对象
    print(time.strptime("2023_07_15_10_55_04", "%Y_%m_%d_%H_%M_%S"))


if __name__ == '__main__':
    print(time_now)
