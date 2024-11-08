# -*- coding: UTF-8 -*-
'''
@学习网站      ：https://www.python-office.com
@读者群     ：http://www.python4office.cn/wechat-group/
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：CoderWanFeng
@代码日期    ：2024/5/6 21:31 
@本段代码的视频说明     ：
'''
import base64
import json

import requests


class BaiduOCR():

    def __init__(self, id, key):

        self.API_Key = id
        self.Secret_Key = key

    def get_baidu_token(self):
        url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={self.API_Key}&client_secret={self.Secret_Key}"

        payload = ""
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)

        res = json.loads(response.text)
        return res['access_token']

    '''
    社保卡识别
    '''

    def social_security_card(self, img_path):
        request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/social_security_card"
        # 二进制方式打开图片文件
        f = open(img_path, 'rb')
        img = base64.b64encode(f.read())

        params = {"image": img}
        access_token = self.get_baidu_token()
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            return response.json()
        else:
            logger.info('no response,help:http://www.python4office.cn/wechat-group/')
            return None
