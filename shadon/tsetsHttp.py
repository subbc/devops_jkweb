#!/usr/bin/evn python
# -*- coding:utf-8 -*-
import requests
from shadon.testsConfig import testsConfig
from requests.packages import urllib3
urllib3.disable_warnings()

class testsHttp ():
    def __init__(self):
        global host, port, timeout
        Config =testsConfig()
        Config.getConfig()
        host = Config.api_url
        port = Config.port
        timeout = Config.timeout
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}

    def set_url(self, url):
        self.url = host + url

    def set_headers(self, header):
        self.headers = header

    def set_params(self, param):
        self.params = param

    def set_data(self, data):
        self.data = data

    def set_files(self, file):
        self.files = file

    def get(self):
        try:
            requests.adapters.DEFAULT_RETRIES = 5  #增加重试连接次数
            s = requests.session()
            s.keep_alive = False   #关闭多余的连接
            response = requests.get(self.url, params=self.params, headers=self.headers,verify=False)
            return response
        except TimeoutError:
            print("Time out!")
            return None

    def post(self):
        try:
          #  requests.adapters.DEFAULT_RETRIES = 5  #增加重试连接次数
          #  s = requests.session()
          #  s.keep_alive = False    #关闭多余的连接
            response = requests.post(self.url, headers=self.headers, data=self.data,verify=False)
            return response
        except TimeoutError:
            print("Time out!")
            return None


if __name__ == "__main__":
    aa = testsHttp()
    aa.set_url('/oauth/authorizationServer/accessToken')
    print(aa.url)
    print(aa.post())