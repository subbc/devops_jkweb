# coding=utf-8

import unittest, time
from selenium import webdriver
from shadon.log import logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from shadon.global_control import Global_control
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

class Buy_goods(unittest.TestCase):
    '''买家购买商品'''
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(executable_path='C:\python36\Scripts\chromedriver.exe', options=chrome_options)
#       self.driver = webdriver.Chrome(options=chrome_options)  ## 创建chrome无界面对象
        self.base_url = "https://www.eelly.com/goods/6991253.html"  #线上地址
        self.base_url1='https://www.eelly.com/index.php?app=paycenter&act=account_info'
        self.driver.set_window_size(1920, 1080)  # 窗口大小变化
        self.judge = False   #用来判断脚本是否执行到断言，没有执行则直接把测试结果置为False,然后系统会给相关人员发送邮件
        self.Ins = Global_control()  # 实例化导入的类，模块中的方法才能调用该类中的方法
    def login(self):
        '''衣联网登录'''
        logger.info('开始调用login方法')
        self.driver.get(self.base_url)
        self.driver.set_window_size(1920, 1080)  # 窗口大小变化
        WebDriverWait(self.driver,30,1).until(EC.visibility_of_element_located((By.LINK_TEXT,'登录')))
        self.driver.find_element_by_link_text("登录").click()
        time.sleep(3)
        WebDriverWait(self.driver,30,1).until(EC.visibility_of_element_located((By.NAME,'account_login')))
        self.driver.refresh()  # 刷新方法 refresh
        self.driver.maximize_window()  ## 浏览器全屏显示
        self.driver.find_element_by_name("account_login").clear()
        self.driver.find_element_by_name("account_login").send_keys("yl_7d912872")
        # tab的定位相相于清除了密码框的默认提示信息，等同上面的clear()
#        self.driver.find_element_by_name("account_login").send_keys(Keys.TAB)
#        time.sleep(3)
        self.driver.find_element_by_name("password").send_keys("1Q2W3e4rzz.")
        # 通过定位密码框，enter（回车）来代替登陆按钮
        self.driver.find_element_by_name("submit_login").send_keys(Keys.ENTER)
#        self.driver.find_element_by_name("submit_login").submit()
#        self.driver.find_element_by_name("submit_login").click()
        logger.info("登录成功")
         #self.assertEqual(self.driver.title, "【新手体验演示店】 2017新款 打底衫 大码装_打底衫批发_衣联网")  #断言，判断页面是否加载正确
    def checkout(self):
        '''立即下单'''
        #self.Cumulative_number = self.driver.find_element_by_xpath(".//*[@id='store_name']/ul/li[1]/p[1]").text
        #print("累计成交数="+str(self.Cumulative_number))
        self.driver.refresh()  # 刷新方法 refresh
#        WebDriverWait(self.driver,30,1).until(EC.visibility_of_element_located((By.ID, "J_checkMarsk")))
        WebDriverWait(self.driver,30,1).until(EC.visibility_of_element_located((By.CLASS_NAME, 'u-ipt-num-cur')))
        logger.info('开始调用checkout方法')
#        js = "var q=document.documentElement.scrollTop=1000"
#        self.driver.execute_script(js)  # 处理向下与右侧的滚动条
#        self.driver.find_element_by_xpath(".//*[@class='u-ipt-num-rbtn']").click()
#        self.driver.find_element_by_xpath(".//*[@class='u-ipt-num-cur'][1]").send_keys("1")
        self.driver.find_element_by_class_name("u-ipt-num-cur").send_keys("1")   #输入下单件数
        self.driver.find_element_by_id("J_takeOrder").click()   #立即下单
        WebDriverWait(self.driver,30,1).until(EC.visibility_of_element_located((By.ID,'J_cartSettlement')))
#        time.sleep(5)
        self.driver.find_element_by_id("J_cartSettlement").click()  #结算"
    #    time.sleep(5)
        WebDriverWait(self.driver,30,1).until(EC.visibility_of_element_located((By.ID,'J_isDaofu148086')))
        self.driver.find_element_by_id("J_isDaofu148086").click() #勾选运费到付
        self.driver.find_element_by_id("J_confBtn").click()   #提交订单
        logger.info("zhixingwancheng")
        #self.assertEqual(self.driver.title, "收银台 - 衣联网,中国服装批发市场新的领航者,广州十三行,虎门新款品牌男装女装批发") #断言，判断页面是否加载正确
    def payment(self):
        '''使用衣联账户付款'''
        logger.info('开始调用payment方法')
        WebDriverWait(self.driver, 30, 1).until(EC.visibility_of_element_located((By.XPATH, ".//*[@id='J_selectPayType']/div[1]/div/div/span[1]/b")))
    #    time.sleep(10)
        self.first_business_sum = self.driver.find_element_by_xpath(".//*[@id='J_selectPayType']/div[1]/div/div/span[1]/b").text
        logger.info("交易前余额="+str(self.first_business_sum))
        self.driver.find_element_by_id("yepay").click()  #选择衣联账户付款
        time.sleep(3)
        self.driver.find_element_by_id("password").send_keys("YLW134679")  #输入支付密码
        time.sleep(3)
        self.driver.find_element_by_id("J_payBtn").click() #点击立即付款
        time.sleep(3)
        for i in range(1,4):
            try:
                self.driver.find_element_by_xpath(".//*[@id='el-pay-tips']/span").is_displayed() # 判断提示密码不正确是否存在
            except:
                logger.info("密码输入正确")
                break #跳出总循环
            else:
                self.driver.find_element_by_id("J_payBtn").click()  #点击立即付款
            time.sleep(30)
        WebDriverWait(self.driver, 30, 1).until(EC.visibility_of_element_located((By.XPATH, ".//*[@id='J_pay_wrap']/div[2]/div/div[2]/div[1]/p[1]/a[1]")))
        #self.result = self.driver.find_element_by_xpath(".//*[@id='msg-box']/h3").text
        #self.assertEqual(self.result, "您已成功付款")  #断言是否成功
    def check_point(self):
        '''检查金额是否减少正确'''
        logger.info('开始调用check_point方法')
    #    time.sleep(20)
        self.result = self.driver.find_element_by_xpath(".//*[@id='sitenav']/div/ul/li[1]/a").click()
        self.driver.get(self.base_url1)
        logger.info(self.driver.title)
        self.last_business_sum = self.driver.find_element_by_xpath("//span[@class='clr-e94700 bold']").text
        logger.info(self.last_business_sum)
        logger.info("交易后余额=" + str(self.last_business_sum))
        self.last_business_sum = float(self.last_business_sum)+0.01
        logger.info("交易后余额+0.01=" + str(self.last_business_sum))
        logger.info("留两位小数="+'%.2f'%self.last_business_sum)
        try:
            self.judge = True
            self.assertEqual(self.first_business_sum, '%.2f'%self.last_business_sum)  #断言，判断交易后减少的金额是否正确
        except AssertionError:
            Global_control.Run_result = False
            logger.info("断言异常")
            self.Ins.screen_shot()  #进行判断，看截图文件夹是否创建，创建则跳过，否则创建文件夹
            self.driver.get_screenshot_as_file(Global_control.Screen_path + "/" + "衣联网购买商品金额断言失败" + ".png")
            raise "测试出现错误，需要发送邮件"

    def tearDown(self):
        '''关闭浏览器'''
        if self.judge != True:
            logger.info("buy goods test is False")
            Global_control.Run_result = False   #增加一步判断，避免出现脚本未执行到断言，而系统没有抛出异常
            self.Ins.screen_shot()  # 进行判断，看截图文件夹是否创建，创建则跳过，否则创建文件夹
            self.driver.get_screenshot_as_file(Global_control.Screen_path + "/" + "衣联网购买商品失败，未成功购买"+ ".png")
        self.driver.quit()
    def test_demo(self):
        # 整个接口需要调用的方法，都通过该方法进行调用，按顺序调用方法
        '''login》登录衣联网成功、 checkout立即下单、 payment使用衣联账户付款、 check_point检查金额是否减少正确'''
        Buy_goods.login(self)
        Buy_goods.checkout(self)
        Buy_goods.payment(self)
        Buy_goods.check_point(self)

if __name__ == "__main__":
   suite = unittest.TestLoader().loadTestsFromTestCase(Buy_goods.test_demo)
   unittest.TextTestRunner(verbosity=2).run(suite)