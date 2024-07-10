# -*- coding: UTF-8 -*-
'''
@学习网站      ：https://www.python-office.com
@读者群     ：http://www.python4office.cn/wechat-group/
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：CoderWanFeng
@代码日期    ：2024/7/10 0:27 
@本段代码的视频说明     ：
'''

import time
from pathlib import Path

import pandas as pd
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkocr.v1 import *
from huaweicloudsdkocr.v1.region.ocr_region import OcrRegion
from pofile import get_files
from poprogress import simple_progress

from poocr.lib.CommonUtils import img2base64


def household2excel(ak, sk, img_path: list, output_excel: str = r'./household2excel.xlsx'):
    credentials = BasicCredentials(ak, sk)

    client = OcrClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(OcrRegion.value_of("cn-north-4")) \
        .build()

    request = RecognizeHouseholdRegisterRequest()
    try:

        ticket_list = []
        img_list = get_files(img_path)
        for item in img_list:
            request.body = HouseholdRegisterRequestBody(
                image=img2base64(item)
            )
            response = client.recognize_household_register(request)
            time.sleep(3)
            # response.result
            print(response)
            for res_info in simple_progress(response.to_dict()["result"]):
                if res_info['type'] == "登记页":
                    one_content = res_info['content']
                    key_content = {}
                    key_content['文件名'] = Path(item).stem
                    key_content['姓名'] = one_content['name']
                    key_content['身份证号码'] = one_content['id_card_number']
                    if len(one_content['id_card_number']) < 18:
                        key_content['备注'] = '身份证号码小于18位'
                    key_content['与户主关系'] = one_content['householder_relationship']
                    ticket_list.append(key_content)
        ticket_df = pd.DataFrame(ticket_list)
        ticket_df.to_excel(output_excel, index=None)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


if __name__ == '__main__':
    pass
