#!/usr/bin/evn python
# -*- coding:utf-8 -*-

# Author: xietian
# Created Time: 20171223
import unittest
from selenium import webdriver
from shadon.log import logger
from shadon.global_control import Global_control
from selenium.webdriver.chrome.options import Options

class Check_goods_url(unittest.TestCase):
    '''检查线上服务器是否能正常打开系统地址'''
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(executable_path='C:\python36\Scripts\chromedriver.exe', options=chrome_options)
        self.url ='https://m.eelly.com/goods/6550142.html'
        self.judge = False   #用来判断脚本是否执行到断言，没有执行则直接把测试结果置为False,然后系统会给相关人员发送邮件
#       self.driver = webdriver.Chrome(options=chrome_options)  ## 创建chrome无界面对象
    def Check_goods_url(self):
        '''检查线上服务器是否能正常打开系统地址'''
        logger.info('开始调用Check_goods_url方法')
        self.driver.get(self.url)  # 发送请求
        try:
            goodsName = self.driver.find_element_by_xpath("//span[@class='title-l']").text
            logger.info(goodsName)
            self.assertEqual('河南郑州品牌库存女装批发推荐广州明浩',goodsName)
            self.judge = True
        except AssertionError:
            logger.info("获取 api 时间异常")
            raise "测试出现错误，需要发送邮件"
    def tearDown(self):
        if self.judge != True:
            logger.info("goods info test is False")
            Global_control.Run_result = False   #增加一步判断，避免出现脚本未执行到断言，而系统没有抛出异常
        self.driver.quit()
    def test_demo(self):
        #整个接口需要调用的方法，都通过该方法进行调用，按顺序调用方法
        '''Check_goods_url》检查线上服务器是否能正常打开系统地址'''
        Check_goods_url.Check_goods_url(self)


if __name__ == "__main__":
   suite = unittest.TestLoader().loadTestsFromTestCase(Check_goods_url.test_demo)
   unittest.TextTestRunner(verbosity=2).run(suite)