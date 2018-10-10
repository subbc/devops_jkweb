# coding=utf-8
import unittest,time,os
from selenium import webdriver
from shadon.log import logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from shadon.global_control import Global_control
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class Publish_goods(unittest.TestCase):
    '''卖家发布商品、下架、删除'''
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(executable_path='C:\python36\Scripts\chromedriver.exe', options=chrome_options)
#       chrome_options.set_headless()      # 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
#       self.driver = webdriver.Chrome(options=chrome_options)  ## 创建chrome无界面对象
        self.base_url = "https://www.eelly.com/index.php?app=goods&act=addGoodsIndex"  #线上地址
        logger.info("调用setup")
        self.driver.set_window_size(1920, 1080)  # 窗口大小变化
        self.judge = False  #用来判断脚本是否执行到断言，没有执行则直接把测试结果置为False,然后系统会给相关人员发送邮件
        self.Ins = Global_control()  #实例化导入的类，模块中的方法才能调用该类中的方法
    def login(self):
        '''登录衣联网成功'''
        logger.info('开始调用login方法')
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        WebDriverWait(self.driver,30,1).until(EC.visibility_of_element_located((By.ID,'account_login')))
        self.driver.find_element_by_id("account_login").send_keys("molimoq")
        self.driver.find_element_by_id("password").send_keys("ely@95zz")
        self.driver.find_element_by_id("submit_login").click()
        logger.info("登录成功YES")
    def publish_new_goods(self):
        '''发布新商品'''
        logger.info('开始调用publish_new_goods方法')
        WebDriverWait(self.driver, 30,1).until(EC.visibility_of_element_located((By.CLASS_NAME, 'a-wrap1')))
       # mouse = self.driver.find_element_by_xpath("html/body/div[3]/div/div/ul/li[3]/a")
       # action = ActionChains(self.driver)
       # action.move_to_element(mouse).perform()  # 移动到write，显示“Mouse moved”
       # time.sleep(2)
       # self.driver.find_element_by_class_name("J_newCommodity").click()  # 点击发布新商品按钮
       # handles = self.driver.window_handles      #获取当前所有窗口
       # self.driver.switch_to.window(handles[1])  #driver跳转到新打开的窗口
        try:
            #self.driver.find_element_by_xpath("html/body/div[4]/div/div/a[2]").is_displayed()  # 判断是否存在
            self.driver.find_element_by_xpath("//a[@class='anew']").click()  # 存在点击重新开始
        except:
            logger.info("页面不在该页面，不用点击重新开始")
        WebDriverWait(self.driver,30,1).until(EC.visibility_of_element_located((By.ID,'J_goods_content')))
        logger.info("开始输入商品数据：")
        #self.driver.find_element_by_xpath("//input[@id='J_goods_content']").send_keys("10086")  #输入货号
        self.driver.find_element_by_id("J_goods_content").send_keys("10086")  #输入货号
        self.driver.find_element_by_id("J_goods_name").send_keys("自动化测试")  # 输入标题
        self.driver.find_element_by_id("J_stock0").send_keys("999999") # 输入库存数量
        self.driver.find_element_by_id("J_inventory_num").click()      #勾选全部相同
        logger.info("开始上传图片")
        WebDriverWait(self.driver, 30, 1).until(EC.visibility_of_element_located((By.ID, 'upimg_0')))
        #self.driver.find_element_by_xpath("//*[starts-with(@id,'rt_rt_1c29')]").click()
        #self.driver.find_element_by_name("file").send_keys(r'D:\function_test\config\dev\publish_goods_test.png')  #绝对路径
        case_path = os.path.dirname(__file__) + "/../config/dev"   #获取图片相对路径
        case_path = os.path.abspath(case_path + "/publish_goods_test.png")
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@name='file']").is_displayed()
        logger.info(case_path)
        #self.driver.find_element_by_xpath("//input[@name='file']").send_keys(case_path)
        try:
            self.driver.find_element_by_name("file").send_keys(case_path)
        except:
            self.driver.find_element_by_name("file").send_keys(r'/data/web/function_test/config/dev/publish_goods_test.png')
        logger.info("upload image is ok")
        time.sleep(3)
        self.driver.find_element_by_xpath(".//*[@id='J_step6']/div/div[3]/div/div[1]/label[2]/input").click() #去掉店内推荐
     #   WebDriverWait(self.driver,30,2).until(EC.visibility_of_element_located((By.ID,'J_release')))
        self.driver.find_element_by_xpath("//div[@id='J_release']").click();
        self.driver.find_element_by_id("J_release").click()            #点击发布按钮
        logger.info('onclick')
        time.sleep(2)
        WebDriverWait(self.driver,30,2).until(EC.visibility_of_element_located((By.XPATH,'html/body/div[3]/div[1]/p[1]')))
#        self.result = self.driver.find_element_by_xpath("html/body/div[3]/div[1]/p[1]").text
        self.result = self.driver.find_element_by_xpath("//*[@class='text_succeed']").text
        logger.info(self.result)
        self.assertEqual(self.result, "发布成功")  #断言是否成功
    def sold_out(self):
        '''下架商品'''
        logger.info('开始调用sold_out方法')
        self.driver.find_element_by_class_name("go_manage").click()  #点击商品管理按钮
        WebDriverWait(self.driver,30,1).until(EC.visibility_of_element_located((By.XPATH,".//*[@id='Js_page_ul']/li[3]/a")))  #等待页面
        self.driver.find_element_by_id("foggy_search").send_keys("10086")  #输入搜索商品货号
        self.driver.find_element_by_id("foggy_search_button").click()      #点击搜索商品按钮
        WebDriverWait(self.driver,30,1).until(EC.visibility_of_element_located((By.XPATH,".//*[@id='goods_list']/tbody/tr[1]/td[2]/p"))) #等待搜索成功
        time.sleep(5)
        self.driver.find_element_by_id("J_AllSelector").click()  #勾选全选按钮
        self.driver.find_element_by_name("if_show").click()    #点击下架按钮
        logger.info("下架成功")
    def delete_goods(self):
        '''删除新增商品'''
        logger.info('开始调用delete_goods方法')
        self.base_url1 = "https://www.eelly.com/index.php?app=seller_member"  # 线上地址
        self.driver.get(self.base_url1)
#        WebDriverWait(self.driver,30,2).until(EC.visibility_of_element_located((By.XPATH,".//*[@id='goods_list']/tbody/tr/td")))
        WebDriverWait(self.driver, 30, 1).until(EC.visibility_of_element_located((By.XPATH, ".//*[@id='Js_set_ul']/li[5]/a")))
        time.sleep(3)
        self.driver.find_element_by_xpath(".//*[@id='Js_set_ul']/li[5]/a").click()  #点击已下架商品
        time.sleep(2)
        WebDriverWait(self.driver,30,1).until(EC.visibility_of_element_located((By.ID,'foggy_search')))
        self.driver.find_element_by_id("foggy_search").clear()
        self.driver.find_element_by_id("foggy_search").send_keys("10086")  #输入货号
        self.driver.find_element_by_id("foggy_search_button").click()      #点击搜索商品
        logger.info("搜索出了下架商品，准备删除......")
        time.sleep(3)
        self.driver.find_element_by_id("J_AllSelector").click()            #勾选全选框
        self.driver.execute_script("window.confirm = function(msg) { return true; }")      # 兼容phantomjs
        self.driver.find_element_by_xpath("html/body/div[4]/div[3]/div/div[3]/div[1]/div[1]/a[3]").click()  #点击删除按钮
        #由于phantomjs不支持弹窗，所以无法使用
        #alert = self.driver.switch_to_alert()   #切换到alert弹出框
        #alert.accept()  #点击确认按钮
        logger.info("删除成功")
        time.sleep(2)
        WebDriverWait(self.driver,30,1).until(EC.visibility_of_element_located((By.XPATH,".//*[@id='Js_set_ul']/li[5]/a")))
        try:
            self.judge = True
            WebDriverWait(self.driver, 30, 1).until(EC.visibility_of_element_located((By.XPATH, "html/body/div[4]/div[3]/div/div[2]/div/span/i")))
            self.result = self.driver.find_element_by_xpath("html/body/div[4]/div[3]/div/div[2]/div/span/i").text
            self.assertEqual(self.result, '0')  #断言是否成功,看商品是否为0款
        except AssertionError:
            Global_control.Run_result = False
            logger.info("断言异常")
            self.Ins.screen_shot()  # 进行判断，看截图文件夹是否创建，创建则跳过，否则创建文件夹
            self.driver.get_screenshot_as_file("u"+(Global_control.Screen_path + "/" + "衣联网删除商品失败"+ ".png"))
            raise "测试出现错误，需要发送邮件"
    def tearDown(self):
        '''关闭浏览器'''
        if self.judge != True:
            logger.info("add goods test is False")
            Global_control.Run_result = False   #增加一步判断，避免出现脚本未执行到断言，而系统没有抛出异常
            self.Ins.screen_shot()  # 进行判断，看截图文件夹是否创建，创建则跳过，否则创建文件夹
            self.driver.get_screenshot_as_file(Global_control.Screen_path + "/" + "衣联网发布新商品失败"+ ".png")
        self.driver.quit()
    def test_demo(self):
        # 整个接口需要调用的方法，都通过该方法进行调用，按顺序调用方法
        '''login》登录衣联网成功、 publish_new_goods发布新商品、 sold_out下架商品、 delete_goods删除新增商品'''
        Publish_goods.login(self)
        Publish_goods.publish_new_goods(self)
        Publish_goods.sold_out(self)
        Publish_goods.delete_goods(self)

if __name__ == "__main__":
   suite = unittest.TestLoader().loadTestsFromTestCase(Publish_goods.test_demo)
   unittest.TextTestRunner(verbosity=2).run(suite)