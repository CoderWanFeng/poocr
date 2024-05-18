# -*- coding: UTF-8 -*-
'''
@作者 ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信 ：CoderWanFeng : https://mp.weixin.qq.com/s/8x7c9qiAneTsDJq9JnWLgA
@个人网站 ：www.python-office.com
@Date    ：2023/4/18 22:04 
@Description     ：
'''

import poocr

poocr.ocr2excel.VatInvoiceOCR2Excel(input_path=r'./测试发票',output_excel='456.xlsx',
                                    configPath=r'D:\workplace\code\github\poocr\tests\poocr-config.toml')
