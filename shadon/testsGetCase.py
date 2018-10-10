#!/usr/bin/evn python
# -*- coding:utf-8 -*-

import json
import os

class testsGetCase():

    def __init__(self,moude,apiclass,apifunction):
        self.fileName =  os.path.dirname(__file__) + "/../src/" + moude + "/Model/"+apiclass+'_'+apifunction.capitalize()+".json"
        print()
        self.fileInfo = open(self.fileName, "rb+")
        with open(self.fileName , encoding='utf-8') as json_file:
            data = json.load(json_file)
        self.result = data
        self.fileInfo.close()
        pass

    def getCase(self):
        return self.result

    # 按照索引获取指定期望数据
    def getEcpect(self, index):
        return self.result[index]['ecpect']

    # 按照索引获取指定请求数据
    def getRequest(self, index):
        return self.result[index]['request']


if __name__ == "__main__":
    sdk = testsGetCase('Oauth','authorizationServer','accessToken')
    print(sdk.getCase())
    result = sdk.getEcpect(1)
    print(result)