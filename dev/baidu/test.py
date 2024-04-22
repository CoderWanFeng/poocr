# -*- coding: UTF-8 -*-
'''
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：CoderWanFeng
@读者群     ：http://www.python4office.cn/wechat-group/
@学习网站      ：www.python-office.com
@代码日期    ：2023/12/10 2:57 
@本段代码的视频说明     ：
'''

import pandas as pd

res_df = []
api_res_json = {"Name": "刘洋", "Sex": "女", "Nation": "汉", "Birth": "1995/5/13",
                "Address": "广东省深圳市南山区腾讯大厦", "IdNum": "440305199505132561", "Authority": "",
                "ValidDate": "", "AdvancedInfo": "{}",
                "RequestId": "1794deb3-19c4-48fb-a729-9e1ec9846824"}

# api_res_json = json.loads(api_res)

api_df = pd.DataFrame(api_res_json, index=[0])
print(api_df)

res_df.append(pd.DataFrame(api_res_json, index=[0]))

if len(res_df) > 0:
    res_excel = res_df[0]
    for index, line_df in enumerate(res_df):
        if index == 0:
            continue
        res_excel = res_excel._append(line_df)
    abs_output_excel = "test_excel.xlsx"
    pd.DataFrame(res_excel).to_excel(str(abs_output_excel))  # 写入Excel