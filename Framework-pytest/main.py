# 导包
import pytest, time,shutil
from common.getOS import *
from Tool.getTime import time_now
from Tool.numRestrict import *
from common.edit_Allure import Edit_Allure

if __name__ == '__main__':
    # 定义report文件路径
    report = os.path.join(testReport,"report_"+ time_now)
    # 生出测试报告
    pytest.main(['-vs', "--alluredir=" + temp_json, "--clean-alluredir"])
    os.system("allure generate " + temp_json + " -o " + report)

    # 调用自定义修改测试报告方法
    set_allure = Edit_Allure()
    # 修改报告title标题
    set_allure.set_window_title(report,"接口测试报告")
    # 修改标题名称
    set_allure.set_topic(report,"登录模块测试")
    # 手动创建一个查看报告的脚本
    with open(report + r"/请点我.bat", "w", encoding="utf-8") as f:
        f.write(r"allure open ./")
    # 将刚生成的报告打成zip压缩包
    zip_dir = shutil.make_archive(base_name="./testReport/测试报告", format="zip", root_dir=report)
    print(zip_dir)
    # 调用发送钉钉、邮件、飞书……

    # 调用清理报告、日志方法，控制数量
    clear_report(5)
    clear_log(3)
    # ---------------------------------------------------------------------------
    # ---------------------------------------------------------------------------





