# -*- coding: UTF-8 -*-
'''
@学习网站      ：https://www.python-office.com
@读者群     ：http://www.python4office.cn/wechat-group/
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：CoderWanFeng
@代码日期    ：2024/7/27 13:10 
@本段代码的视频说明     ：
'''

import unittest

from poocr.api.ocr2excel import *


class TestTencent(unittest.TestCase):

    def setUp(self):
        self.SecretId = ''
        self.SecretKey = ''

    def test_hukouben2(self):
        r = household2excel2(ak=self.SecretId, sk=self.SecretKey,
                             img_path=r'../test_files/户口本/7121976潘会江户口簿_01.png')
        r = household2excel2(ak=self.SecretId, sk=self.SecretKey,
                             img_path=r'../test_files/户口本/7220102张瑞良户口薄_00.png')
        print(r)
