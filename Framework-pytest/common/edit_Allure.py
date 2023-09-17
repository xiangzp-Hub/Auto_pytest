"""
时间： 2023-09-09 : 21:19
功能：修改allure报告方法
思路：
    1、
    2、
    3、
"""

# 导包
import json
import os


class Edit_Allure:

    def set_window_title(self, file_path, new_title):
        """
        修改报告窗口标题:set_window_title
        :param file_path: HTML测试报告路径
        :param new_title: 新标题名
        """
        # 1.获取测试报告中 “index.html” 的路径
        index_path = os.path.join(file_path, "index.html")
        # 2.以读写的方式打开index.html文件,保存到对象f中
        with open(index_path, "r+", encoding="utf-8") as f:
            # 2.1 获取文件内所有内容
            all_the_lines = f.readlines()
            # 2.2 把指针挪动到开始位置
            f.seek(0, 0)
            # 2.3 截断(从当前指针位置之后的内容全部删除)
            f.truncate()
            # 2.4 循环遍历每一行内容,将Allure Report替换为新的标题
            for line in all_the_lines:
                f.write(line.replace("Allure Report", new_title))

    def set_topic(self, file_path, name):
        # 获取summary.json文件的数据内容
        file_path = file_path + r"/widgets/summary.json"
        # 以读的模式打开并保存到f内
        with open(file_path, "rb") as f:
            # 加载json文件内容到变量param内
            param = json.load(f)
            # 修改内容
            # 将修改后的内容保存在字典内
            param["reportName"] = name
        # 以写的方式再次打开文件,并写入修改后的数据
        with open(file_path, "w", encoding="utf-8") as w:
            # 将修改后的字典写入到文件内
            json.dump(param, w, ensure_ascii=False, indent=4)
