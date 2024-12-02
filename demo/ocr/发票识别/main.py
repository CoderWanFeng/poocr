# -*- coding: UTF-8 -*-
'''
@作者 ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信 ：CoderWanFeng : https://mp.weixin.qq.com/s/8x7c9qiAneTsDJq9JnWLgA
@个人网站 ：www.python-office.com
@Date    ：2023/5/13 23:14 
@Description     ：
'''

# 批量识别发票
# pip install poocr
import poocr

poocr.ocr2excel.VatInvoiceOCR2Excel(input_path=r"E:\Python\程序员晚枫的文件夹\POCR\发票",
                                    output_path="识别结果.xlsx")
