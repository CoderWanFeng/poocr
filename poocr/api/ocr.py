# -*- coding: UTF-8 -*-
'''
@Author  ：程序员晚枫，B站/抖音/微博/小红书/公众号
@WeChat     ：CoderWanFeng
@Blog      ：www.python-office.com
@Date    ：2023/1/22 15:23
@Description     ：
'''

import sys

from poocr.core.BaiduOCR import BaiduOCR
from poocr.core.OCR import OCR
from poocr.lib.CommonUtils import img2base64


def get_ocr(configPath, id, key):
    ocr = OCR()
    ocr.set_config(configPath, id, key)
    return ocr


def do_api(OCR_NAME, img_path, img_url, configPath, id, key):
    """
    通过类的方法名，直接调用方法
    :return:
    """
    ocr = get_ocr(configPath, id, key)
    if img_url:
        ocr_res = ocr.DoOCR(OCR_NAME, ImageBase64=img_path, ImageUrl=img_url)
    else:
        ImageBase64 = img2base64(img_path)
        ocr_res = ocr.DoOCR(OCR_NAME, ImageBase64=ImageBase64, ImageUrl=img_url)
    return ocr_res


def AdvertiseOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def ArithmeticOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def BankCardOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def BankSlipOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def BizLicenseOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def BusInvoiceOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def BusinessCardOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def CarInvoiceOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def ClassifyDetectOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def DriverLicenseOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def DutyPaidProofOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def EduPaperOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def EnglishOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def EnterpriseLicenseOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def EstateCertOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def FinanBillOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def FinanBillSliceOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def FlightInvoiceOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def FormulaOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def GeneralAccurateOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def GeneralBasicOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def GeneralEfficientOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def GeneralFastOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def GeneralHandwritingOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def HKIDCardOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def HmtResidentPermitOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def IDCardOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def ImageEnhancement(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def InstitutionOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def InsuranceBillOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def InvoiceGeneralOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def LicensePlateOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def MLIDCardOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def MLIDPassportOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def MainlandPermitOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def MixedInvoiceDetect(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def MixedInvoiceOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def OrgCodeCertOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def PassportOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def PermitOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def PropOwnerCertOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def QrcodeOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def QueryBarCode(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def QuotaInvoiceOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def RecognizeContainerOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def RecognizeHealthCodeOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def RecognizeIndonesiaIDCardOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def RecognizeMedicalInvoiceOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def RecognizeOnlineTaxiItineraryOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def RecognizePhilippinesDrivingLicenseOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def RecognizePhilippinesVoteIDOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def RecognizeTableOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def RecognizeThaiIDCardOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def RecognizeTravelCardOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def ResidenceBookletOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def RideHailingDriverLicenseOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def RideHailingTransportLicenseOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def SealOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def ShipInvoiceOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def SmartStructuralOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def TableOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def TaxiInvoiceOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def TextDetect(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def TollInvoiceOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def TrainTicketOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def VatInvoiceOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def VatInvoiceVerify(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def VatInvoiceVerifyNew(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def VatRollInvoiceOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def VehicleLicenseOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def VehicleRegCertOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def VerifyBasicBizLicense(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def VerifyBizLicense(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def VerifyEnterpriseFourFactors(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def VerifyOfdVatInvoiceOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def VinOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def WaybillOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath,
                  id=id, key=key)


def social_security_card(img_path, id, key):
    baidu_ocr = BaiduOCR(id, key)
    return baidu_ocr.social_security_card(img_path)
# def VatInvoiceOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
#     """
#     增值税发票的识别
#     :param img_path: 必填，发票的图片位置
#     :param configPath: 选填，配置文件的位置，有默认值
#     :return:
#     """
#
#     ocr = get_ocr(configPath)
#     if img_url:
#         ocr_res = ocr.VatInvoiceOCR(ImageBase64=img_path, ImageUrl=img_url)
#     else:
#         ImageBase64 = img2base64(img_path)
#         ocr_res = ocr.VatInvoiceOCR(ImageBase64=ImageBase64, ImageUrl=img_url)
#     return ocr_res
