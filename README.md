# tests

## 安装 Python
- 建议Python版本3.6以上
- 项目用到的库：selenium，requests,beautifulsoup4，setuptools，urllib3
## 安装chrome浏览器
下载地址：http://chromedriver.chromium.org/downloads
- 谷歌无头浏览器，用于在 Linux 等系统使用来支持 UI 自动化测试使用
- 建议版本为2.4以上
- 开发过程中遇到chrome无头版本有 bug ,可以参考官方平台说明
- 用pip3 list 可以查看包是否安装好

## 部署
- 使用自动任务部署，crontab
- 部署最好先写一个 shell 在项目根目录，命名为 start.sh，然后自动任务直接执行这个脚本即可

```
cd 项目
Python3 run_all_case.py

```
