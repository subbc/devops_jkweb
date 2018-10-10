#!/usr/bin/evn python
# -*- coding:utf-8 -*-

from shadon.tsetsHttp import testsHttp
from shadon.testsConfig import testsConfig
import os

class testsToken():

    def __init__(self):
        self.url = '/oauth/authorizationServer/accessToken'
        self.mytestsConfig = testsConfig()
        self.mytestsConfig.getConfig()
        self.path = os.path.dirname(__file__) + "/../config/" + self.mytestsConfig.env + "/"
        self.grant='client_credentials'
        pass

    def setGrant(self,grant):
        global localgrant
        localgrant = grant
        if os.path.exists(self.path + 'token.txt') != True:
            os.remove(self.path + 'token.txt')
        pass

    def getToken(self):
        global apiToken
        if os.path.exists(self.path+ 'token.txt') != True:
            self.setToken(localgrant)
        file = open(self.path + 'token.txt', 'r')
        value = file.read()
        apiToken = eval(value)
        file.close()
        return apiToken

    def setToken(self,grant):
        myhttp = testsHttp()
        myhttp.set_url(self.url)
        self.data = {"grant_type": "client_credentials", "client_id": self.mytestsConfig.client_id,"client_secret": self.mytestsConfig.client_secret}
        if grant == 'password':
            self.mytestsConfig.grant_type = self.mytestsConfig.getFile('password', 'grant_type')
            self.mytestsConfig.username = self.mytestsConfig.getFile('password', 'username')
            self.mytestsConfig.password = self.mytestsConfig.getFile('password', 'password')
            self.data = {"grant_type": "password", "client_id": self.mytestsConfig.client_id,"client_secret": self.mytestsConfig.client_secret,"username":self.mytestsConfig.username,"password":self.mytestsConfig.password}
        myhttp.set_data(self.data)
        tokenInfo =myhttp.post().json()
        #如果目录不存在，建立目录
        if os.path.exists(self.path) != True:
            os.makedirs(self.path)
        #写入数据
        file = open(self.path+'token.txt','w')
        file.write(str(tokenInfo))
        file.close()

        pass



if __name__ == "__main__":
    shadon = testsToken()
    shadon.setToken('passwords')
    print(shadon.getToken())