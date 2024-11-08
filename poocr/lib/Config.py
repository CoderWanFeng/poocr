# -*- coding: UTF-8 -*-
'''
@Author  ：程序员晚枫，B站/抖音/微博/小红书/公众号
@WeChat     ：CoderWanFeng
@Blog      ：www.python-office.com
@Date    ：2023/1/22 18:45 
@Description     ：加载配置信息，core中类的父类
'''
import toml
from loguru import logger

from poocr.lib.Const import DEFAULT_CONFIG_PATH_NAME, DEFAULT_CONFIG_NAME, TUTORIA_VIDEO


class poocrConfig():
    def __init__(self):
        self.config_info = None

    def get_config(self, configPath):
        """
        解析配置文件
        :param toml_path: 存放配置文件的位置和名称，在py文件的同级路径下
        :return: 加载后的信息
        """
        try:
            if configPath == None:
                self.config_info = toml.load(DEFAULT_CONFIG_PATH_NAME)
            else:
                self.config_info = toml.load(configPath)
            logger.info(f'配置文件【{DEFAULT_CONFIG_NAME}】读取成功')
            return self.config_info
        except:
            logger.info(f'配置文件【{DEFAULT_CONFIG_NAME}】读取失败，请查看视频，进行配置：{TUTORIA_VIDEO}')
