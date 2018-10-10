#!/usr/bin/evn python
# -*- coding:utf-8 -*-

from shadon.create_build import create_build
from shadon.create_html import create_html
from shadon.send_mail import sendmail
from shadon.global_control import Global_control
from shadon.log import logger

def run_all_case():
    #生成报告
    create_html()
    #发送邮件
    logger.info(Global_control.Run_result)
    if Global_control.Run_result ==False:
        sendmail()
        logger.info("本轮测试执行有失败案例，需要给相应人员发送邮件")
    else:
        logger.info("本轮测试正确通过")
    #从接口地址拿数据生成测试文件
    #create_build()

if __name__ == "__main__":
    run_all_case()