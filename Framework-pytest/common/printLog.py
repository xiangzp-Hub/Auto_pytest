"""
时间： 2023-09-08 : 15:13
功能：重新定义log生成器，输出日志到“控制台和“文件testLog”中
思路：
    1、创建一个日志收集器，并起一个名称
       -->设置日志收集结级别
    2、
    3、
"""
import logging, os, time
from logging.handlers import TimedRotatingFileHandler


def report_dir():
    """日志路径处理"""
    time_now = time.strftime("%Y-%m-%d %H_%M_%S")
    # 设置文件名
    name = "log_" + time_now + ".txt"
    # 设置日志文件存放路径
    Report_dir = os.path.dirname(os.path.dirname(__file__)) + r"/testLog/" + name
    return Report_dir


def log():
    # 创建一个日志收集器 ‘Test’
    logger = logging.getLogger("Test")
    # 设置收集日志等级
    logger.setLevel("INFO")
    # 定义一个日志输出格式
    format1 = logging.Formatter("%(asctime)s - %(pathname)s-[line:%(lineno)d] - [%(levelname)s]-->: %(message)s")
    format2 = logging.Formatter(
        "%(asctime)s - [module: %(module)s.py]-[line:%(lineno)d] - [%(levelname)s]-->: %(message)s")
    # 添加一个日志输出渠道 --> 控制台
    sh = logging.StreamHandler()
    # 设置日志输出等级
    sh.setLevel('DEBUG')
    # 设置日志输出格式 format1
    sh.setFormatter(format2)
    # 将此渠道添加到日志收集器中
    logger.addHandler(sh)
    # 添加一个日志输出渠道 --> 文件
    # fh = TimedRotatingFileHandler(filename=report_dir(), when="D", backupCount=3, encoding="utf-8")
    fh = logging.FileHandler(filename=report_dir(), encoding="utf-8")
    fh.setFormatter(format2)
    logger.addHandler(fh)
    return logger


# 创建日志记录器(单例模式)
logger = log()

if __name__ == '__main__':
    loger = log()

    loger.info('我是---info---------')
    loger.debug('我是---debug-------')
    loger.error('我是---error-------')
    loger.critical('我是---critical-')
