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


def household2excel2(ak, sk, img_path: list, output_excel: str = r'./household2excel.xlsx'):
    sig = signer.Signer()
    # 认证用的ak和sk硬编码到代码中或者明文存储都有很大的安全风险，建议在配置文件或者环境变量中密文存放，使用时解密，确保安全；
    # 本示例以ak和sk保存在环境变量中为例，运行本示例前请先在本地环境中设置环境变量HUAWEICLOUD_SDK_AK和HUAWEICLOUD_SDK_SK。
    sig.Key = ak
    sig.Secret = sk
    img = img2base64(img_path)
    body = "base64=data:image/jpeg;base64," + quote(img)
    # print(img)
    r = signer.HttpRequest(method="POST",
                           url="https://jmhkbocr.apistore.huaweicloud.com/ocr/householdRegister",
                           headers={'Content-Type': 'application/x-www-form-urlencoded'},
                           body=body)
    sig.Sign(r)
    resp = requests.request(r.method, r.scheme + "://" + r.host + r.uri, headers=r.headers, data=r.body)
    # logger.info(resp.status_code, resp.reason, resp.content)
    content = resp.content
    print(json.loads(content))

    # print(content.decode('utf-8'))
    """
    {'data': {'birthAddress': '中国云南省富民县', 'name': '杨利琼', 'relationship': '妻', 'cardNo': '530124196710280543', 'sex': '女', 'nation': '汉', 'belief': '无宗教信仰', 'career': '粮农', 'maritalStatus': '已婚', 'registerDate': '', 'birthday': '1967年10月28日', 'education': '初中', 'hometown': '中国云南省富民县', 'whenWhereToHere': '就地农转城派出所内移入20140520云南省富民县富民县公安局款庄派出所多宜甲村123号', 'whenWhereToCity': '年月日中国', 'householdNum': '', 'formerName': '', 'otherAddress': '', 'height': '159厘米', 'bloodType': '不明', 'veteranStatus': '未服兵役', 'workAddress': '多宜办事处多宜甲村'}, 'msg': '成功', 'success': True, 'code': 200, 'taskNo': '280995649212629441046596'}

    """


if __name__ == '__main__':
    pass
