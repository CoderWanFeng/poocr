# -*- coding: UTF-8 -*-
'''
@学习网站      ：https://www.python-office.com
@读者群     ：http://www.python4office.cn/wechat-group/
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：CoderWanFeng
@代码日期    ：2024/11/30 14:17 
@本段代码的视频说明     ：
'''
import json
import os

import pandas as pd

SecretId = os.getenv("SecretId", None)
SecretKey = os.getenv("SecretKey", None)

# res=poocr.ocr.BankSlipOCR(img_path=r'test_files/2.png', id=SecretId, key=SecretKey)
# print(res)


# 读取JSON文件内容作为字符串
with open(r'test_files/res-2.json', 'r', encoding='utf-8') as file:
    res_json = json.load(file)

    print(res_json)
    # 从字典中提取需要的数据
    bank_slip_infos = res_json['BankSlipInfos']

    # 创建一个DataFrame
    df = pd.DataFrame(bank_slip_infos)

    # 将DataFrame保存为Excel文件
    df.to_excel('bank_slips.xlsx', index=False)
# 现在res_json包含了文件的完整内容，但它是作为字符串处理的
# print(res_json)
