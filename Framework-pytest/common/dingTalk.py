"""
思路分析:
定义一个类: DingTalk
1. 定义初始化方法
    1.1 创建一个请求头并绑定为实例属性
    1.2 将请求地址绑定为实例属性
2. 定义一个对外发送普通消息的方法:send_msg
    2.1 定义发送消息的所有参数:json格式
    2.2 携带着参数进行请求,发送消息
3. 定义一个对外发送链接消息的方法:send_link
    3.1 定义发送消息的所有参数:json格式
    3.2 携带着参数进行请求,发送消息
"""
import requests


# 定义一个类: DingTalk
class DingTalk:
    # 1. 定义初始化方法
    def __init__(self):
        # 1.1 创建一个请求头并绑定为实例属性
        self.headers = {'Content-Type': 'application/json;charset=utf-8'}
        # 1.2 将请求地址绑定为实例属性
        self.url = 'https://oapi.dingtalk.com/robot/send?access_token=ded597142fbee3889e19d9b1ecc06ad89b7b91c7bbc55fd30c38ba06f5f46818'

    # 2. 定义一个对外发送普通消息的方法:send_msg
    def send_msg(self, text):
        # 2.1 定义发送消息的所有参数:json格式
        dic = {
            "msgtype": "text",
            "text": {"content": text},
            "at": {
                "atMobiles": ["+86-13552828809", "+86-18601916518"],
                "isAtaLL": False}
        }
        # 2.2 携带着参数进行请求,发送消息
        requests.post(url=self.url, json=dic, headers=self.headers)

    # 3. 定义一个对外发送链接消息的方法:send_link
    def send_link(self, text, url):
        # 3.1 定义发送消息的所有参数:json格式
        dic = {
            "msgtype": "link",
            "link": {
                "text": text,
                "title": "橙好登录模块测试报告,请查收",
                "messageUrl": url
            }
        }
        # 3.2 携带着参数进行请求,发送消息
        requests.post(url=self.url, json=dic, headers=self.headers)


if __name__ == '__main__':
    dt = DingTalk()
    # dt.send_msg("测试:我是大聪明")
    dt.send_link("测试:天下武功,唯快不破", "http://127.0.0.1:8080/report/2023_02_04_18_52_21report.html")

