# -*- coding: UTF-8 -*-

import toml
from loguru import logger

from poocr.lib.Const import DEFAULT_CONFIG_PATH_NAME, DEFAULT_CONFIG_NAME, TUTORIA_VIDEO


class poocrConfig():
    """
    通过配置文件来验证id和key，现在已经弃用。改为通过函数里传参：id，key
    """

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
