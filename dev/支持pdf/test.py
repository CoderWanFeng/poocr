# -*- coding: UTF-8 -*-
'''
@学习网站      ：www.python-office.com
@读者群     ：http://www.python4office.cn/wechat-group/
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：CoderWanFeng
@代码日期    ：2024/5/8 22:03 
@本段代码的视频说明     ：
'''

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ocr.v20181119 import ocr_client, models

# 腾讯云的AppID、SecretID和SecretKey
cred = credential.Credential("你的SecretID", "你的SecretKey")
httpProfile = HttpProfile()
httpProfile.endpoint = "ocr.tencentcloudapi.com"
clientProfile = ClientProfile()
clientProfile.httpProfile = httpProfile

# 实例化要请求产品的client对象, clientProfile是可选的。
client = ocr_client.OcrClient(cred, "ap-guangzhou", clientProfile)

# 实例化一个请求对象, 传入对应接口的参数
req = models.IDCardOCRRequest()

# 这里填入PDF文件的Base64信息
req.ImageBase64 = '你的PDF文件Base64编码'

# 返回的resp是一个IDCardOCRResponse的实例，与之对应的接口返回的数据
resp = client.IDCardOCR(req)

# 输出返回的信息
print(resp.to_json_string())