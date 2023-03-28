# -*- coding: UTF-8 -*-
'''
@Author  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@WeChat     ：CoderWanFeng
@Blog      ：www.python-office.com
@Date    ：2023/3/28 23:34 
@Description     ：
'''
import os
from pathlib import Path

import poocr

input_path = r'd:/test'
for dirpath, dirnames, filenames in os.walk(input_path):
    for filename in filenames:
        id_info = poocr.ocr.IDCardOCR(img_path=os.path.join(dirpath, filename))
        print(id_info)
