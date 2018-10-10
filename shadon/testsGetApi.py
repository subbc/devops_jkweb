#!/usr/bin/evn python
# -*- coding:utf-8 -*-

import json
import codecs
import os
from bs4 import BeautifulSoup
from shadon.tsetsHttp import testsHttp

class testGetApi():
    def __init__(self):
        self.path = os.path.dirname(__file__) + "/../src/"
        self.myhttp = testsHttp()
    #找模块
    def getApiMoudle(self):
        self.myhttp.set_url('/')
        a = self.myhttp.get()
        soup = BeautifulSoup(a.text,'lxml')
        apiMoudles=[]
        for list in soup.find_all(class_='list-group-item'):
            apiMoudles.append(str(list.a.string))
        return apiMoudles

    #找指定模块的类
    def getClassName(self,apiMoudle):
        #确保首字母小写
        lowerapiMoudle = apiMoudle.lower()
        self.myhttp.set_url('/'+ lowerapiMoudle)
        abrr = self.myhttp.get()
        soup = BeautifulSoup(abrr.text, 'lxml')
        apiClass = []
        apiClassName = []
        #取出是有 a 连接
        for list in soup.find_all("a"):
            apiClass.append(list.get('href'))
        #切割，获取需要的 class
        for list in apiClass:
            thislist =list.split("/"+lowerapiMoudle+'/')
            if len(thislist) == 2 :
                apiClassName.append(thislist[1])
        return apiClassName

    #找指定类下面的 api 接口
    def getFunction(self,apiMoudle,apiClass):
        lowerapiMoudle = apiMoudle.lower()
        self.myhttp.set_url('/' + lowerapiMoudle+'/'+apiClass)
        abrr = self.myhttp.get()
        soup = BeautifulSoup(abrr.text, 'lxml')
        # 定位右侧
        apilists=[]
        for list in soup.find_all(class_='markdown-body'):
            for i in list.find_all('a'):
                apilists.append(i.string)
        return apilists

    #找 api 的请求参数和返回参数
    def getApiInfo(self,apiMoudle,apiClass,functions):
        lowerapiMoudle = apiMoudle.lower()
        self.myhttp.set_url('/' + lowerapiMoudle + '/' + apiClass+'/'+functions)
        abrr = self.myhttp.get()
        soup = BeautifulSoup(abrr.text, 'lxml')
        req = ['language-json']
        rets = ''
        reqs = ''
        for list in soup.find_all("code"):
            if list.get('class') == req:
                reqs=list.string
            if list.get('class') ==None :
                rets=list.string
        if reqs == '':
            reqs = 'null'
        if rets == '':
            rets = 'null'
        return {"reqs":json.loads(reqs),"rets":json.loads(rets)}

    def setApiFile(self,apiMoudle,apiClass,functions):
        #基础目录
        controllerPath = self.path + apiMoudle +'/Controller/'
        modelPath = self.path + apiMoudle + '/Model/'
        if os.path.exists(controllerPath) != True:
            os.makedirs(controllerPath)
        if os.path.exists(modelPath) != True:
            os.makedirs(modelPath)
        initFile = self.path + apiMoudle +'/__init__.py'
        initApiCode = controllerPath + '/__init__.py'
        if os.path.exists(initFile) != True:
            file= open(initFile, 'w')
            file.write(str(' '))
        if os.path.exists(initApiCode) != True:
            file= open(initApiCode, 'w')
            file.write(str(' '))
        #文件相关，编译模板，写测试代码
        apiCode = controllerPath +apiClass.capitalize()+'_'+functions.capitalize()+'_'+'test'+'.py'
        apiCase = modelPath + apiClass.capitalize()+'_'+functions.capitalize()+'.json'
        if os.path.exists(apiCode) != True:
            templatePath =os.path.dirname(__file__) + "/testTemplate.txt"
            url = '/'+apiMoudle.lower()+'/'+apiClass+'/'+functions
            config ={"class_name":apiClass.capitalize()+functions.capitalize(),"url":url,"moudle":apiMoudle,"apiclass":apiClass,"apifunction":functions.capitalize()}
            self.codeFile(config,templatePath,apiCode)
        apiInfo =self.getApiInfo(apiMoudle,apiClass,functions)
        #写测试用例
        if os.path.exists(apiCase) != True:
            file = open(apiCase, 'w')
            case=[{'request':apiInfo['reqs'],"ecpect":apiInfo['rets']}]
            file.write(json.dumps(case,indent=4))

    def codeFile(self,config,template,outPutFile):
        with codecs.open(template, "rb", "UTF-8") as f:
            s = f.read()
        if not s:
            return
        s = s % config
        with codecs.open(outPutFile, "wb", "UTF-8") as f:
            f.write(s)
            f.flush()

if __name__== "__main__":
    a= testGetApi()
    a.getApiMoudle()
    a.getClassName('Activity')
    a.getFunction('Activity','activity')
    a.getApiInfo('Activity','activity','addActivity')
    a.setApiFile('Activity','activity','addActivity')