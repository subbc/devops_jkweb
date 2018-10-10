#!/usr/bin/evn python
# -*- coding:utf-8 -*-

# Author: xietian
# Created Time: 20171223
import unittest
from selenium import webdriver
from shadon.log import logger
from shadon.global_control import Global_control
from selenium.webdriver.chrome.options import Options

class Check_time(unittest.TestCase):
    '''检查线上服务器是否正确返回时间'''
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(executable_path='C:\python36\Scripts\chromedriver.exe', options=chrome_options)
        self.url = 'https://mall.eelly.com/api/time'
#       self.driver = webdriver.Chrome(options=chrome_options)  ## 创建chrome无界面对象
        self.judge = False  # 用来判断脚本是否执行到断言，没有执行则直接把测试结果置为False,然后系统会给相关人员发送邮件
    def tearDown(self):
        if self.judge != True:
            logger.info("api time test is False")
            Global_control.Run_result = False   #增加一步判断，避免出现脚本未执行到断言，而系统没有抛出异常
        self.driver.quit()
    def test_Check_time(self):
        '''检查线上服务器是否正确返回时间'''
        for num in range(1,4):
            logger.info('开始'+ str(num) +'次调用Check_time方法')
            self.driver.get(self.url)  # 发送请求
            times = self.driver.find_element_by_xpath("//body").text
            lenth = len(times)
            logger.info(times)
            if lenth == 10:
                self.judge = True
                logger.info('this is very good!!')
                break
        self.assertEqual(self.judge,True)

if __name__ == "__main__":
   suite = unittest.TestLoader().loadTestsFromTestCase(Check_time.test_Check_time)
   unittest.TextTestRunner(verbosity=2).run(suite)