# -*- coding: UTF-8 -*-
'''
@作者 ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信 ：CoderWanFeng : https://mp.weixin.qq.com/s/yFcocJbfS9Hs375NhE8Gbw
@个人网站 ：www.python-office.com
@Date    ：2023/3/25 18:13 
@Description     ：
'''

# pip install poocr
import poocr

poocr.ocr2excel.VatInvoiceOCR2Excel(intput_path=r'C:\Users\Lenovo\Desktop\temp\增值税发票-test.jpg',
                                    output_excel='./晚枫.xlsx',
                                    configPath='./poocr-config.toml')
