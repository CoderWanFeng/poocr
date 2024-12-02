import base64

from loguru import logger
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.ocr.v20181119 import ocr_client, models

from poocr.lib.Config import poocrConfig
from poocr.lib.Const import NO_FILE_ERROR


class OfdOCR(poocrConfig):
    def __init__(self):
        self.TENCENT_AI_CFG = None
        self.TENCENTCLOUD_SECRET_ID = None
        self.TENCENTCLOUD_SECRET_KEY = None
        self.CLIENT = None

    def set_config(self, id, key):
        """
        加载配置信息，生成client，获取配置信息：
        :param configPath: 可以自定义config文件的名称和位置，有默认值
        :return:
        """
        if id != None and key != None:
            self.TENCENTCLOUD_SECRET_ID = id
            self.TENCENTCLOUD_SECRET_KEY = key
        else:
            logger.error("请先设置腾讯云的SecretId和SecretKey")
        cred = credential.Credential(self.TENCENTCLOUD_SECRET_ID, self.TENCENTCLOUD_SECRET_KEY)
        httpProfile = HttpProfile()
        httpProfile.endpoint = "ocr.tencentcloudapi.com"
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        self.client = ocr_client.OcrClient(cred, "ap-beijing", clientProfile)
        return self.client

    def get_params(self, OfdFileBase64, OfdFileUrl):
        """
        图片的OfdFileUrl、OfdFileBase64必须提供一个，如果都提供，只使用OfdFileUrl。
        :param OfdFileBase64:
        :param OfdFileUrl:
        :return:
        """
        if OfdFileUrl:
            params = '{\"OfdFileUrl\":\"%s\"} ' % OfdFileUrl
        elif OfdFileBase64:
            params = '{\"OfdFileBase64\":\"%s\"} ' % OfdFileBase64
        else:
            return NO_FILE_ERROR
        return params

    def DoOCR(self, OfdFileBase64=None, OfdFileUrl=None):

        try:
            req = models.VerifyOfdVatInvoiceOCRRequest()
            req.from_json_string(self.get_params(OfdFileBase64, OfdFileUrl))
            resp = self.client.VerifyOfdVatInvoiceOCR(req)
            return resp

        except TencentCloudSDKException as err:
            logger.info(err)


def VerifyOfdVatInvoiceOCR(ofd_file_path=None, ofd_file_url=None, id=None, key=None):
    ocr = OfdOCR()
    ocr.set_config(id, key)
    if ofd_file_path:
        with open(ofd_file_path, 'rb') as file:
            pdf_data = file.read()
            base64_encoded_pdf = base64.b64encode(pdf_data).decode('utf-8')
            ocr_res = ocr.DoOCR(OfdFileBase64=base64_encoded_pdf)
    elif ofd_file_url:
        ocr_res = ocr.DoOCR(OfdFileUrl=ofd_file_url)

    return ocr_res


if __name__ == '__main__':
    SecretId = os.getenv("SecretId", None)
    SecretKey = 'xxx'
    ofd_file_path = r'./suzhou.ofd'
    res = VerifyOfdVatInvoiceOCR(ofd_file_path=ofd_file_path, id=SecretId, key=SecretKey)
    logger.error(res)
    ofd_file_url = 'https://test-1300615378.cos.ap-nanjing.myqcloud.com/suzhou.ofd'
    res = VerifyOfdVatInvoiceOCR(ofd_file_url=ofd_file_url, id=SecretId, key=SecretKey)
    logger.error(res)
