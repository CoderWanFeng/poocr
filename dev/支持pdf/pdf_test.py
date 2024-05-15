# -*- coding: UTF-8 -*-
'''
@学习网站      ：www.python-office.com
@读者群     ：http://www.python4office.cn/wechat-group/
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：CoderWanFeng
@代码日期    ：2024/5/7 23:35 
@本段代码的视频说明     ：
'''
import base64


def pdf_to_base64(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_data = file.read()
        base64_encoded_pdf = base64.b64encode(pdf_data).decode('utf-8')
    return base64_encoded_pdf


# 使用函数
pdf_path = r'C:\Users\Lenovo\Desktop\temp\046002300111_58278670_20240428111616.pdf'
base64_string = pdf_to_base64(pdf_path)
print(base64_string)