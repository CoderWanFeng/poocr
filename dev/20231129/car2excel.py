# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：CoderWanFeng
@读者群     ：http://www.python4office.cn/wechat-group/
@学习网站      ：https://www.python-office.com
@代码日期    ：2023/11/29 0:17 
@本段代码的视频说明     ：
'''
import json
import os

import pandas as pd

import poocr

SecretId = os.getenv("SecretId")
SecretKey = os.getenv("SecretKey")
# SecretKey = os.getenv("TEMP")
# print(SecretId, SecretKey)

# 读取所有环境变量
# all_env_vars = os.environ
# print(all_env_vars)
# test_json = poocr.ocr.LicensePlateOCR(img_path=r'./files/car_test.png', id=SecretId, key=SecretKey)
# #
# # # {"CardNo": "6225768888888888", "BankInfo": "招商银行(03080000)", "ValidDate": "07/2023", "CardType": "贷记卡", "CardName": "招商银行信用卡", "BorderCutImage": null, "CardNoImage": null, "WarningCode": null, "QualityValue": null, "RequestId": "dfa4eb5c-e84a-4204-a23f-d71d92bff551"}
# df = pd.DataFrame(json.loads(str(test_json)), index=[0])
#
# df.to_excel('car.xlsx', index=False)

poocr.ocr2excel.LicensePlateOCR2Excel(input_path=r'./files/car_test.png', id=SecretId, key=SecretKey)
