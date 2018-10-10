#!/usr/bin/evn python
# -*- coding:utf-8 -*-

import os
import configparser
from shadon.testsEnv import testsEnv

class testsConfig():
    def __init__(self):
        self.env = testsEnv().getEnv()
        self.configDri = self.fileName = os.path.dirname(__file__) + "/../config/" + self.env + "/sdkConfig.conf"

    def getFile(self,section,option):
        conf = configparser.ConfigParser()
        conf.read(self.configDri, encoding='UTF-8')  # 文件路径
        value = conf.get(section, option)  # 获取指定section 的option值
        return value

    def getConfig(self):
        self.api_url = self.getFile(self.env,'api_url')
        self.port = self.getFile(self.env, 'port')
        self.timeout = self.getFile(self.env, 'timeout')
        self.grant_type = self.getFile(self.env, 'grant_type')
        self.client_id = self.getFile(self.env, 'client_id')
        self.client_secret = self.getFile(self.env, 'client_secret')

    def get_path(self):
        global log_path
        log_path = os.getcwd()
        return log_path

if __name__ == "__main__":
    test = testsConfig()
    print(test.getFile('dev','api_url'))
    test.getConfig()
    print(test.api_url)
