# coding:utf-8

import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import shadon.create_html
from shadon.testsConfig import testsConfig

def sendmail():
    #发送邮件
    #----------1.跟发件相关的参数------
    time.sleep(2)#等待5秒
    r = testsConfig() #实例化
    smtpserver = r.getFile('EMAIL','smtpserver')#服务器地址
    port = r.getFile('EMAIL','port')  # 端口
    sender = r.getFile('EMAIL','sender')   # 账号
    psw = r.getFile('EMAIL','psw')  # 密码
    receiver = r.getFile('EMAIL','receiver')   # 接收人
    receiver = receiver.split(",")  #把字符串格式转换成列表格式
    #	----------2.编辑邮件的内容------

    #	读文件
    file_path = shadon.create_html.filename
  #  print("file_path="+file_path)
    with open(file_path, "rb") as fp:
        mail_body = fp.read()
    msg = MIMEMultipart()
    msg["from"] = sender  # 发件人
    msg["to"] = ";".join(receiver)  # 收件人
    msg["subject"] = r.getFile('EMAIL','subject')   # 主题

    # 正文
    body = MIMEText(mail_body, "html", "utf-8")
    msg.attach(body)

    # 附件
    att = MIMEText(mail_body, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="test_report.html"'
    msg.attach(att)

    # ----------3.发送邮件------
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)  # 连服务器
        smtp.login(sender, psw)
    except:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
        smtp.login(sender, psw)  # 登录
    smtp.sendmail(sender, receiver, msg.as_string())  # 发送
    smtp.quit()

