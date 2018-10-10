# coding=utf-8

import unittest,time
from selenium import webdriver
from shadon.log import logger
from shadon.global_control import Global_control
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class Login(unittest.TestCase):
    '''衣联网登录'''
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(executable_path='C:\python36\Scripts\chromedriver.exe',options=chrome_options)
#       self.driver = webdriver.Chrome(options=chrome_options)  ## 创建chrome无界面对象
        self.base_url = "https://www.eelly.com/"
        self.driver.implicitly_wait(10)
        self.judge = False   #用来判断脚本是否执行到断言，没有执行则直接把测试结果置为False,然后系统会给相关人员发送邮件
        self.Ins = Global_control()  #实例化导入的类，模块中的方法才能调用该类中的方法
    def login(self):
        '''衣联网登录'''
        logger.info('开始调用login方法')
        self.driver.get(self.base_url)
#        self.driver.implicitly_wait(2)
        self.driver.fullscreen_window()
        logger.info(self.driver.title)
#        driver.find_element_by_xpath(".//*[@id='js_login_info']/div[2]/a[1]").click()
        self.driver.find_element_by_xpath(".//*[@class='login-link-wrap']/a[1]").click()
        self.driver.find_element_by_name("account_login").send_keys("yl_7d912872")
        self.driver.find_element_by_name("password").send_keys("1Q2W3e4rzz.")
        self.driver.find_element_by_name("submit_login").submit()
        logger.info("login......")
        WebDriverWait(self.driver,30,1).until(EC.visibility_of_element_located((By.XPATH,".//*[@id='sitenav']/div/div[2]/a")))
#        time.sleep(3)
        try:
            self.judge = True
            if self.driver.title !='衣联网,服装批发市场新的领航者,广州十三行,杭州四季青2018新款品牌男装女装批发':
                logger.info(self.driver.title)
            self.assertEqual(u"衣联网,服装批发市场新的领航者,广州十三行,杭州四季青2018新款品牌男装女装批发", self.driver.title)
            logger.info('pc 登陆成功')
        except BaseException:
            logger.info("断言失败")
            Global_control.Run_result = False
            self.Ins.screen_shot()   #进行判断，看截图文件夹是否创建，创建则跳过，否则创建文件夹
            self.driver.get_screenshot_as_file(Global_control.Screen_path + "/" + "衣联网登录断言失败"+ ".png")
            raise "测试出现错误，需要发送邮件"
    def tearDown(self):
        '''关闭浏览器'''
        if self.judge != True:
            logger.info("login test is False")
            Global_control.Run_result = False   #增加一步判断，避免出现脚本未执行到断言，而系统没有抛出异常
            self.Ins.screen_shot()  # 进行判断，看截图文件夹是否创建，创建则跳过，否则创建文件夹
            self.driver.get_screenshot_as_file(Global_control.Screen_path + "/" + "衣联网登录失败"+ ".png")
        self.driver.quit()

    def test_demo(self):
        # 整个接口需要调用的方法，都通过该方法进行调用，按顺序调用方法
        '''login》登录衣联网成功'''
        Login.login(self)
    def test_wap(self):
        logger.info('开始wap 站点的login方法')
        self.driver.get("https://m.eelly.com/member/login.html?returnUrl=%252Fmember%252Fview.html")
        logger.info(self.driver.title)
        self.driver.find_element_by_name("LoginForm[username]").send_keys("yl_7d912872")
        self.driver.find_element_by_name("LoginForm[password]").send_keys("1Q2W3e4rzz.")
        self.driver.find_element_by_id("J_submit").click()
        time.sleep(2)
        logger.info(self.driver.title)
        try:
            self.driver.find_element_by_id("J_elyMobilePage").is_displayed()
            logger.info("wap 登陆成功:")
            self.judge = True
        except BaseException:
            logger.info("wap 登陆失败")
if __name__ == "__main__":
   suite = unittest.TestLoader().loadTestsFromTestCase(Login.test_demo)
   unittest.TextTestRunner(verbosity=2).run(suite)