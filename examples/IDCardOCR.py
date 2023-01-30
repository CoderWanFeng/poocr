# -*- coding: UTF-8 -*-
'''
@Author  ：程序员晚枫，B站/抖音/微博/小红书/公众号
@WeChat     ：CoderWanFeng
@Blog      ：www.python-office.com
@Date    ：2023/1/28 21:10 
@Description     ：
'''
# 全部100多个功能的合集链接：https://mp.weixin.qq.com/s/WxICBZZSgkm-OrvXB82hbg
# pip install poocr
# 清华大学下载地址：https://www.bilibili.com/video/BV1SM411y7vw/
import poocr

# img_url=''
res = poocr.ocr.IDCardOCR(
    img_path=r'C:\Users\Lenovo\Desktop\temp\正面.jpg',
    configPath=r'D:\test\py310\poocr-test\poocr-config.toml')

print(res)
