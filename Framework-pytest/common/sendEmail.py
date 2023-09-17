"""
时间： 2023-09-09 : 22:16
功能：
思路：
    1、
    2、
    3、
"""
# coding:utf-8

# 发送html附件的邮件
import smtplib, time, os
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from common.readConfig import ReadConfig

# 实例化
rc = ReadConfig()

class SendEmail:
    def __init__(self):
        '''''发送html内容邮件-非附件形式，即直接在邮件中显示html'''
        # 第一步：配置邮箱属性
        # 发送邮箱
        self.sender = rc.read_config("email", "sender")
        # 接收邮箱
        self.receiver = eval(rc.read_config("email", "receiver"))
        # 发送邮件主题
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.subject = '自动化测试结果_' + t
        # 发送邮箱服务器
        self.smtpserver = rc.read_config("email", "smtpserver")
        # 发送邮箱用户/授权码
        self.username = rc.read_config("email", "sender")
        self.password = rc.read_config("email", "password")

    def __config(self, file):
        # 读取html文件内容
        with open(file, 'rb') as f:
            mail_body = f.read()
            # 组装邮件内容和标题
            msg = MIMEMultipart()
            # 添加附件内容
            att = MIMEText(mail_body, 'plain', 'utf-8')
            att["Content-Type"] = 'application/octet-stream'
            att["Content-Disposition"] = 'attachment; filename=report.zip'
            msg.attach(att)
            # 添加邮件的文本内容
            content = '自动化测试报告详情，请查收附件'
            msg.attach(MIMEText(content, 'plain', 'utf-8'))
            msg['Subject'] = Header(self.subject, 'utf-8')
            msg['From'] = self.sender
            msg['To'] = ",".join(self.receiver)
        return msg

    def send(self, file):
        """
        :param file: 发送附件文件的路径
        """
        # 第二步：准备附件，增加附件，组装邮件内容和标题
        msg = self.__config(file)
        # 第三步：登录并发送邮件
        try:
            # 1--实例化smtp类
            smtp = smtplib.SMTP()
            # 2--连接stmp服务器
            smtp.connect(self.smtpserver)
            # 3--登录邮箱
            smtp.login(self.username, self.password)
            # 4--设置发件人，收件人，邮件内容
            smtp.sendmail(self.sender, self.receiver, msg.as_string())
        except Exception as msg:
            print("邮件发送失败！", msg)
        else:
            print("邮件发送成功！")
        finally:
            smtp.quit()


if __name__ == '__main__':
    se = SendEmail()
    se.send(r"F:\code\framework_vip28\common\dingTalk.py")

