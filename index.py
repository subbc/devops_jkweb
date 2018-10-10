#!/usr/bin/evn python
# -*- coding:utf-8 -*-

from __future__ import  unicode_literals
from threading import  Timer
from wxpy import *
import  requests,urllib,urllib2,os,sys
from wechat_sender import Sender
import time

#bot = Bot()
#bot = Bot(console_qr=2,cache_path="botoo.pkl")
def login_weixin():
    global uuid
    url = "https://login.wx.qq.com/"
    values = {
        'appid':wx


    }



def get_news():
    url = "http://www.iciba.com/dsapi/"
    r = requests.get(url)
    contents = r.json()['contents']
    translation =r.json()['translation']
    return contens,translation
def send_news():
    try:
        my_friend = bot.friends().search(u'subbca')[0]
        my_friend.send(get_news()[0])
        my_friend.send(get_news()[1][5:])
        my_friend.send(u'来自广州')
 #       t = Timer(86400,send_news)
 #       t.start()subbca
    except:
        my_friend = bot.friends().search('subbca')
        my_friend.send(u'发送失败')

if __name__ == "__main__":
    send_news()