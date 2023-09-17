# -*- coding: UTF-8 -*-
'''
@作者 ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信 ：CoderWanFeng : https://mp.weixin.qq.com/s/B1V6KeXc7IOEB8DgXLWv3g
@个人网站 ：www.python-office.com
@Date    ：2023/3/28 23:19 
@Description     ：
'''

import poocr

id = poocr.ocr.IDCardOCR(img_path=r'C:\Users',
                         configPath=r'D:\workplace\code\github\poocr\demo\poocr-config.toml')
print(id)
