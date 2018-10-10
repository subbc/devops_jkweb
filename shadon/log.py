#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os,time
import logging
import threading
import configparser
from logging.handlers import RotatingFileHandler
from shadon.testsEnv import testsEnv

class LogSignleton(object):

    def __init__(self):
        global configDri,path,env  #定义全局变量
    def __new__(cls):
        mutex=threading.Lock()
        mutex.acquire() # 上锁，防止多线程下出问题
        env = testsEnv().getEnv()
        configDri = os.path.dirname(__file__) + "/../config/" + env + "/sdkConfig.conf"
        path = os.path.dirname(__file__) + "/../"
        if not hasattr(cls, 'instance'):
            cls.instance = super(LogSignleton, cls).__new__(cls)
          #  print("log_config="+log_config)
            config = configparser.ConfigParser()
            config.read(configDri, encoding='UTF-8')
          #  cls.instance.log_filename = config.get('LOGGING', 'log_file')
            resultpath = os.path.join(path,'logs')
            if not os.path.exists(resultpath):
                os.mkdir(resultpath)
            now = time.strftime("%Y%m%d%H")
            # 日志名称
            logPath = resultpath + '/' + now + '_log.txt'
           # print("logpath="+logPath)
            cls.instance.log_filename = logPath
            cls.instance.max_bytes_each = int(config.get('LOGGING', 'max_bytes_each'))
            cls.instance.backup_count = int(config.get('LOGGING', 'backup_count'))
            cls.instance.fmt = config.get('LOGGING', 'fmt')
            cls.instance.log_level_in_console = int(config.get('LOGGING', 'log_level_in_console'))
            cls.instance.log_level_in_logfile = int(config.get('LOGGING', 'log_level_in_logfile'))
            cls.instance.logger_name = config.get('LOGGING', 'logger_name')
            cls.instance.console_log_on = int(config.get('LOGGING', 'console_log_on'))
            cls.instance.logfile_log_on = int(config.get('LOGGING', 'logfile_log_on'))
            cls.instance.logger = logging.getLogger(cls.instance.logger_name)
            cls.instance.__config_logger()
        mutex.release()
        return cls.instance

    def get_logger(self):
        return  self.logger

    def __config_logger(self):
        # 设置日志格式
        fmt = self.fmt.replace('|','%')
        formatter = logging.Formatter(fmt)

        if self.console_log_on == 1: # 如果开启控制台日志
            console = logging.StreamHandler()
            console.setFormatter(formatter)
            self.logger.addHandler(console)
            self.logger.setLevel(self.log_level_in_console)

        if self.logfile_log_on == 1: # 如果开启文件日志
            rt_file_handler = RotatingFileHandler(self.log_filename, maxBytes=self.max_bytes_each, backupCount=self.backup_count)
            rt_file_handler.setFormatter(formatter)
            self.logger.addHandler(rt_file_handler)
            self.logger.setLevel(self.log_level_in_logfile)

logsignleton = LogSignleton()
logger = logsignleton.get_logger()


