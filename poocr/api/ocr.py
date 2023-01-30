# -*- coding: UTF-8 -*-
'''
@Author  ：程序员晚枫，B站/抖音/微博/小红书/公众号
@WeChat     ：CoderWanFeng
@Blog      ：www.python-office.com
@Date    ：2023/1/22 15:23
@Description     ：
'''

from poocr.core.OCR import OCR
from poocr.lib.CommonUtils import img2base64
import sys


def get_ocr(configPath):
    ocr = OCR()
    ocr.set_config(configPath)
    return ocr


def do_api(OCR_NAME, img_path, img_url, configPath):
    """
    通过类的方法名，直接调用方法
    :return:
    """
    ocr = get_ocr(configPath)
    if img_url:
        ocr_res = ocr.DoOCR(OCR_NAME, ImageBase64=img_path, ImageUrl=img_url)
    else:
        ImageBase64 = img2base64(img_path)
        ocr_res = ocr.DoOCR(OCR_NAME, ImageBase64=ImageBase64, ImageUrl=img_url)
    return ocr_res


def AdvertiseOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def ArithmeticOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def BankCardOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def BankSlipOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def BizLicenseOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def BusInvoiceOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def BusinessCardOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def CarInvoiceOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def ClassifyDetectOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def DriverLicenseOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def DutyPaidProofOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def EduPaperOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def EnglishOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def EnterpriseLicenseOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def EstateCertOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def FinanBillOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def FinanBillSliceOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def FlightInvoiceOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def FormulaOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def GeneralAccurateOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def GeneralBasicOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def GeneralEfficientOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def GeneralFastOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def GeneralHandwritingOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def HKIDCardOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def HmtResidentPermitOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def IDCardOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def ImageEnhancement(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def InstitutionOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def InsuranceBillOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def InvoiceGeneralOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def LicensePlateOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def MLIDCardOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def MLIDPassportOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def MainlandPermitOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def MixedInvoiceDetect(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def MixedInvoiceOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def OrgCodeCertOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def PassportOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def PermitOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def PropOwnerCertOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def QrcodeOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def QueryBarCode(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def QuotaInvoiceOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def RecognizeContainerOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def RecognizeHealthCodeOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def RecognizeIndonesiaIDCardOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def RecognizeMedicalInvoiceOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def RecognizeOnlineTaxiItineraryOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def RecognizePhilippinesDrivingLicenseOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def RecognizePhilippinesVoteIDOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def RecognizeTableOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def RecognizeThaiIDCardOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def RecognizeTravelCardOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def ResidenceBookletOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def RideHailingDriverLicenseOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def RideHailingTransportLicenseOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def SealOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def ShipInvoiceOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def SmartStructuralOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def TableOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def TaxiInvoiceOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def TextDetect(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def TollInvoiceOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def TrainTicketOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def VatInvoiceOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def VatInvoiceVerify(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def VatInvoiceVerifyNew(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def VatRollInvoiceOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def VehicleLicenseOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def VehicleRegCertOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def VerifyBasicBizLicense(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def VerifyBizLicense(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def VerifyEnterpriseFourFactors(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def VerifyOfdVatInvoiceOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def VinOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)


def WaybillOCR(img_path=None, img_url=None, configPath=None):
    return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
                  img_path=img_path,
                  img_url=img_url,
                  configPath=configPath)

# def VatInvoiceOCR(img_path=None, img_url=None, configPath=None):
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