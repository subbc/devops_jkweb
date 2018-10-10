#coding=utf-8
import logging,time,os
from logging.handlers import HTTPHandler,RotatingFileHandler
from  cloghandler import ConcurrentRotatingFileHandler
import platform
import config

import sys
reload(sys)
sys.setdefaultencoding('utf8')

format_dict = {
   1 : logging.Formatter('%(asctime)s - %(name)s - %(lineno)d - %(levelname)s -  %(message)s',"%Y-%m-%d %H:%M:%S"),
   2 : logging.Formatter('%(asctime)s - %(name)s - %(lineno)d - %(levelname)s -  %(message)s',"%Y-%m-%d %H:%M:%S"),
   3 : logging.Formatter('%(asctime)s - %(name)s - %(lineno)d - %(levelname)s -  %(message)s',"%Y-%m-%d %H:%M:%S"),
   4 : logging.Formatter('%(asctime)s - %(name)s - %(lineno)d - %(levelname)s -  %(message)s',"%Y-%m-%d %H:%M:%S"),
   5 : logging.Formatter('%(asctime)s - %(name)s - %(lineno)d - %(levelname)s -  %(message)s',"%Y-%m-%d %H:%M:%S"),
}

class LoggerUntil(object):

    """logger = LoggerUntil(name="aaa").getlog(logfilename='test.log', loglevel=2, add_StreamHandler=1)"""

    def __init__(self,name):
        self.logger = logging.getLogger(name)
        self.formatter = None

    def createlog(self):
        return self.logger

    def __set_logger_level(self,loglevel):
        if  loglevel == 1:
            lv=logging.DEBUG
        elif loglevel == 2:
            lv = logging.INFO
        elif loglevel == 3:
            lv = logging.WARNING
        elif loglevel == 4:
            lv = logging.ERROR
        elif loglevel == 5:
            lv = logging.CRITICAL
        self.logger.setLevel(lv)

    def __set_formatter(self,loglevel):
        self.formatter = format_dict[loglevel]

    def getlog(self, logfilename=None, loglevel=1,add_StreamHandler=1):
        self.__set_logger_level(loglevel)
        self.__set_formatter(loglevel)
        if add_StreamHandler == 1:
            self.__add_StreamHandler()
        if logfilename:
            self.__add_RotateHandler(logfilename)
        return self.logger


    def __add_StreamHandler(self):
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

    def __add_RotateHandler(self, logfilename):
        if platform.system() == 'Windows':
            log_path = config.LogConfig.log_path_windows
        else:
            log_path = config.LogConfig.log_path_linux

        if not os.path.exists(log_path):
            os.makedirs(log_path)

        '''进程安全的日志,多个进程写入同一个文件时不出错'''
        filename = log_path + logfilename
        rotate_handler = ConcurrentRotatingFileHandler(filename, mode = "a", maxBytes = 200*1024*1024, backupCount = 5,encoding="utf-8")
        rotate_handler.setLevel(logging.DEBUG)
        rotate_handler.setFormatter(self.formatter)
        self.logger.addHandler(rotate_handler)

if __name__=="__main__":
    logger = LoggerUntil(name="aaa").getlog(logfilename='test.log',loglevel=2,add_StreamHandler=1)
    while(1):
        logger.info('hello')
        time.sleep(20)