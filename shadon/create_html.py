#!/usr/bin/evn python
# -*- coding:utf-8 -*-
import time
import unittest
import os
from shadon.HTMLTestRunner import HTMLTestRunner

def create_html():
    # 生成测试报告
    global filename,now
    filename = 'null'
    # 用例路径
    case_path = os.path.join(os.getcwd(), "src")
    # 报告路径
    temp_path = os.path.dirname(__file__) + "/../"
    report_path = os.path.join(temp_path,"report")
    if not os.path.exists(report_path):
        os.mkdir(report_path)
    # 运行case路径下所有以test结尾的案例
    discover = unittest.defaultTestLoader.discover(case_path, pattern="*test.py", top_level_dir=None)
    now = time.strftime("%Y%m%d%H%M%S")
    # 报告名称
    filename = report_path + '/' + now + '_result.html'
    # print(filename)
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='衣联网系统UI测试报告:', description='测试用例如下:')
    runner.run(discover)
    fp.close()
