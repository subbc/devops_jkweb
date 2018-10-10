# coding: utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#chrome_options = webdriver.ChromeOptions()
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
#chrome_options.setBinary("/usr/bin/chromedriver")
#chrome_options.set_headless()
#browser = Browser('chrome')
#chrome_options.binary_location = '/usr/bin/chromedriver'
#chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(executable_path='C:\python36\Scripts\chromedriver.exe',options=chrome_options)
# 如果没有把chromedriver加入到PATH中,就需要指明路径 executable_path='/home/chromedriver'

print("11111")
driver.get("https://www.aliyun.com/jiaocheng/124644.html")
content = driver.page_source
print(content)
driver.quit()