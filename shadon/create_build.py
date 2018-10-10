#!/usr/bin/evn python
# -*- coding:utf-8 -*-

from shadon.testsGetApi import testGetApi


def create_build():
    #生成测试文件
    getApiOb = testGetApi()
    modules = getApiOb.getApiMoudle()
    for list in modules:
        apiClass = getApiOb.getClassName(list)
        # print(apiClass)
        for list1 in apiClass:
            apiFunction = getApiOb.getFunction(list, list1)
            for list2 in apiFunction:
                print(list + '/' + list1 + '/' + list2)
                print('--------------')
                if list2 != 'accessToken':
                    getApiOb.setApiFile(list, list1, list2)
    pass