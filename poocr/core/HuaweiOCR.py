# -*- coding: UTF-8 -*-
'''
@学习网站      ：https://www.python-office.com
@读者群     ：http://www.python4office.cn/wechat-group/
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：CoderWanFeng
@代码日期    ：2024/7/10 0:27 
@本段代码的视频说明     ：
'''
import json
import time
from pathlib import Path
from urllib.parse import quote

import pandas as pd
import requests
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkocr.v1 import *
from huaweicloudsdkocr.v1.region.ocr_region import OcrRegion
from loguru import logger
from pofile import get_files
from poprogress import simple_progress

from poocr.lib.CommonUtils import img2base64
from poocr.lib.apig_sdk import signer


def household2excel(ak, sk, img_path: list, output_excel: str = r'./household2excel.xlsx'):
    credentials = BasicCredentials(ak, sk)

    client = OcrClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(OcrRegion.value_of("cn-north-4")) \
        .build()

    request = RecognizeHouseholdRegisterRequest()

    ticket_list = []
    img_list = get_files(img_path)
    for item in img_list:
        request.body = HouseholdRegisterRequestBody(
            image=img2base64(item)
        )
        try:
            response = client.recognize_household_register(request)
            time.sleep(3)
            # response.result

            if response.status_code == 200:
                response_dict = response.to_dict()
                for res_info in simple_progress(response_dict["result"]):
                    if res_info['type'] == "登记页":
                        one_content = res_info['content']
                        one_content['文件名'] = Path(item).stem
                        if len(one_content['id_card_number']) < 18:
                            one_content['备注'] = '身份证号码小于18位'
                        ticket_list.append(one_content)
        except exceptions.ClientRequestException as e:
            logger.info(f'{Path(item).stem}识别失败，原因：{e.error_msg}')
    if len(ticket_list) > 0:
        ticket_df = pd.DataFrame(ticket_list)
        ticket_df.to_excel(output_excel, index=None)
    else:
        logger.info('没有识别到任何户口本图片')


def household2excel2(ak, sk, img_path: list, output_excel: str = r'./household2excel.xlsx'):
    sig = signer.Signer()
    # 认证用的ak和sk硬编码到代码中或者明文存储都有很大的安全风险，建议在配置文件或者环境变量中密文存放，使用时解密，确保安全；
    # 本示例以ak和sk保存在环境变量中为例，运行本示例前请先在本地环境中设置环境变量HUAWEICLOUD_SDK_AK和HUAWEICLOUD_SDK_SK。
    sig.Key = ak
    sig.Secret = sk
    res_list = []
    for one_img in simple_progress(get_files(img_path)):
        img = img2base64(one_img)
        body = "base64=data:image/jpeg;base64," + quote(img)
        r = signer.HttpRequest(method="POST",
                               url="https://jmhkbocr.apistore.huaweicloud.com/ocr/householdRegister",
                               headers={'Content-Type': 'application/x-www-form-urlencoded'},
                               body=body)
        sig.Sign(r)
        resp = requests.request(r.method, r.scheme + "://" + r.host + r.uri, headers=r.headers, data=r.body)
        content = resp.content
        api_res_json = json.loads(content.decode('utf-8'))
        if api_res_json['code'] == 200 and api_res_json['data'] != None:
            api_res_json['data']['文件名'] = Path(one_img).stem
            res_list.append(api_res_json['data'])
    res_df = pd.DataFrame(res_list)
    # res_df.append_(pd.DataFrame(, index=[0]))
    res_df.to_excel(output_excel, index=None)


if __name__ == '__main__':
    pass
