# -*- coding: UTF-8 -*-
'''
@Author  ：程序员晚枫，B站/抖音/微博/小红书/公众号
@WeChat     ：CoderWanFeng
@Blog      ：www.python-office.com
@Date    ：2023/1/25 0:03
@Description     ：
'''

# pip install poocr
import poocr
import json
import os
from os.path import join
import pandas as pd

# Demo：识别银行卡
poocr.ocr.BankCardOCR(img_path=r'C://程序员晚枫的文件夹//银行卡照片（复印件）//1.jpg')
# GitHub：poocr
# 100多个功能，公众号：Python自动化办公社区，1.28文章链接：https://mp.weixin.qq.com/s/WxICBZZSgkm-OrvXB82hbg

# home_path = "你存放大量银行卡图片的位置"
home_path = r"C:\Users\Lenovo\Desktop\temp\test\card"
res_df = pd.DataFrame()
for (root, dirs, files) in os.walk(home_path):
    for file in files:
        single_res = poocr.ocr.BankCardOCR(img_path=join(root, file))
        single_res = json.loads(single_res.to_json_string())
        line_df = pd.DataFrame(single_res, index=[0])
        print(line_df)
        res_df = res_df.append(other=line_df)
print(res_df)
res_df.to_excel(r"./银行卡信息.xlsx")
