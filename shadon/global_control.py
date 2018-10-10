#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time,os
import shadon.create_html
from shadon.log import logger

class Global_control():
    '''定义全局变量，用来控制是否发送邮件等'''
    Run_result = True  # 设置全局变量，默认通过，当有案例失败，则会置为False，然后发邮件通知
    Screen_path = None   # 设置全局变量，默认为空，当有案例失败，则创建截图文件，赋值截图路径
    def setUp(self):
        pass
    def screen_shot(self):
        '''创建截图保存目录'''
        if Global_control.Screen_path == None:  # 进行判断，看截图保存是否创建，创建则跳过，否则创建文件夹
            #Path = os.path.join(os.getcwd(), "screenshot")
            Path = os.path.abspath(os.path.dirname(__file__) + "/../screenshot")
            if not os.path.isdir(Path):
                os.makedirs(Path)
#                logger.info(Path)
            try:
                now = shadon.create_html.now
             #   logger.info("判断now是否存在__"+now)
            except:
                now = time.strftime("%Y%m%d%H%M%S")
             #   logger.info("判断now不存在__" + now)
            Global_control.Screen_path = Path + "/" + now
            os.mkdir(Global_control.Screen_path)
#            logger.info(Global_control.Screen_path)

