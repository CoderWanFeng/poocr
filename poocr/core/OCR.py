# -*- coding: UTF-8 -*-

import json

from loguru import logger
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.ocr.v20181119 import ocr_client, models

from poocr.lib.Config import poocrConfig
from poocr.lib.Const import NO_FILE_ERROR


class OCR(poocrConfig):
    def __init__(self):
        self.TENCENT_AI_CFG = None
        self.TENCENTCLOUD_SECRET_ID = None
        self.TENCENTCLOUD_SECRET_KEY = None
        self.CLIENT = None

    def set_config(self, configPath, id, key):
        """
        加载配置信息，生成client，获取配置信息：
        :param configPath: 可以自定义config文件的名称和位置，有默认值
        :return:
        """
        if id != None and key != None:
            self.TENCENTCLOUD_SECRET_ID = id
            self.TENCENTCLOUD_SECRET_KEY = key
        else:
            self.TENCENT_AI_CFG = self.get_config(configPath)
            if self.TENCENT_AI_CFG['tencent-ai']['TENCENTCLOUD_SECRET_ID'] and self.TENCENT_AI_CFG['tencent-ai'][
                'TENCENTCLOUD_SECRET_KEY']:
                self.TENCENTCLOUD_SECRET_ID = self.TENCENT_AI_CFG['tencent-ai']['TENCENTCLOUD_SECRET_ID']
                self.TENCENTCLOUD_SECRET_KEY = self.TENCENT_AI_CFG['tencent-ai']['TENCENTCLOUD_SECRET_KEY']
        cred = credential.Credential(self.TENCENTCLOUD_SECRET_ID, self.TENCENTCLOUD_SECRET_KEY)
        httpProfile = HttpProfile()
        httpProfile.endpoint = "ocr.tencentcloudapi.com"
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        self.client = ocr_client.OcrClient(cred, "ap-beijing", clientProfile)
        return self.client

    def get_params(self, ImageBase64, ImageUrl, is_pdf=False):
        """
        图片的ImageUrl、ImageBase64必须提供一个，如果都提供，只使用ImageUrl。
        如果 type 不为 None，则在参数中添加 type 字段。
        :param ImageBase64: 图片的 Base64 编码
        :param ImageUrl: 图片的 URL
        :param type: 类型列表，列表中的每个元素都是 int 类型
        :return: 包含图片信息和类型信息的 JSON 字符串或错误信息
        """
        if ImageUrl:
            params = {"ImageUrl": ImageUrl}
        elif ImageBase64:
            params = {"ImageBase64": ImageBase64}
        else:
            return json.dumps(NO_FILE_ERROR)

        if is_pdf:
            params['EnableMultiplePage'] = True
        return json.dumps(params)

    def DoOCR(self, OCR_NAME, ImageBase64, ImageUrl, IsPdf=False):

        try:
            ocr_req_func = getattr(models, f'{OCR_NAME}Request', None)
            req = ocr_req_func()
            req.from_json_string(self.get_params(ImageBase64, ImageUrl, (OCR_NAME == 'RecognizeGeneralInvoice' and IsPdf)))
            ocr_func = getattr(self.client, f'{OCR_NAME}', None)
            if OCR_NAME == 'VatInvoiceOCR' or OCR_NAME == 'BankSlipOCR':
                req.IsPdf = IsPdf
            resp = ocr_func(req)
            return resp

        except TencentCloudSDKException as err:
            logger.info(err)

    def VatInvoiceOCR(self, ImageBase64, ImageUrl):
        """
        本接口支持增值税专用发票、增值税普通发票、增值税电子发票全字段的内容检测和识别，
        包括发票代码、发票号码、打印发票代码、打印发票号码、开票日期、合计金额、校验码、税率、合计税额、价税合计、购买方识别号、复核、销售方识别号、开票人、密码区1、密码区2、密码区3、密码区4、发票名称、购买方名称、销售方名称、服务名称、备注、规格型号、数量、单价、金额、税额、收款人等字段。

        默认接口请求频率限制：10次/秒。
        图片的 ImageUrl、ImageBase64 必须提供一个，如果都提供，只使用 ImageUrl。
        :param ImageBase64:
        :param ImageUrl:
        :return:
        """
        try:
            req = models.VatInvoiceOCRRequest()
            req.from_json_string(self.get_params(ImageBase64, ImageUrl))
            resp = self.client.VatInvoiceOCR(req)
            return resp

        except TencentCloudSDKException as err:
            print(err)
