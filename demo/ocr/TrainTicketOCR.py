# -*- coding: UTF-8 -*-
'''
@作者 ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信 ：CoderWanFeng : https://mp.weixin.qq.com/s/Nt8E8vC-ZsoN1McTOYbY2g
@个人网站 ：www.python-office.com
@Date    ：2023/4/16 17:25 
@Description     ：
'''

# pip install poocr
import poocr


poocr.ocr2excel.TrainTicketOCR2Excel(input_path=r'D:\workplace\code\github\poocr\demo\imgs\hong.jpg',
                                     output_excel=r'./ticket.xlsx',
                                     configPath=r'./poocr-config.toml')

"""
待优化:
    去重
    添加文件名：单独一列吗？
    列名转中文：转成什么？
"""