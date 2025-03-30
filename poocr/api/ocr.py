# -*- coding: UTF-8 -*-

import base64
from pathlib import Path

import potx
import pymupdf

from poocr.core.BaiduOCR import BaiduOCR
from poocr.core.OCR import OCR
from poocr.lib.CommonUtils import img2base64


def get_ocr(configPath, id, key):
    ocr = OCR()
    ocr.set_config(configPath, id, key)
    return ocr


def do_api(OCR_NAME, img_path, img_url, configPath, id, key, pdf_path=None):
    """
    通过类的方法名，直接调用方法
    :return:
    """
    ocr = get_ocr(configPath, id, key)
    is_pdf = False
    if Path(img_path).suffix == '.pdf':
        is_pdf = True
    if pdf_path:
        # 打开PDF文件
        pdf = pymupdf.open(pdf_path)

        # 存储所有页面的识别结果  1
        all_results = []

        # 遍历每一页  2
        for page_num in range(len(pdf)):
            pdf_bytes = pdf.convert_to_pdf(page_num, page_num + 1)
            # 将图片转换为Base64编码的字符串
            base64_encoded_pdf = base64.b64encode(pdf_bytes).decode('utf-8')

            # 识别当前页  3
            page_result = ocr.DoOCR(OCR_NAME, ImageBase64=base64_encoded_pdf, ImageUrl=img_url, IsPdf=True)

            # 将当前页结果添加到总结果中  4
            all_results.append(page_result)
        # 关闭PDF文档
        pdf.close()
        # ocr_res = ocr.DoOCR(OCR_NAME, ImageBase64=base64_encoded_pdf, ImageUrl=img_url, IsPdf=True)
        # 如果只有一页，直接返回结果 6
        if len(all_results) == 1:
            return all_results[0]
        # 否则返回所有页面的结果列表
        return all_results
        # pdf_data = file.read()
        # base64_encoded_pdf = base64.b64encode(pdf_data).decode('utf-8')
        # ocr_res = ocr.DoOCR(OCR_NAME, ImageBase64=base64_encoded_pdf, ImageUrl=img_url, IsPdf=True)
    elif img_url:
        ocr_res = ocr.DoOCR(OCR_NAME, ImageBase64=img_path, ImageUrl=img_url, IsPdf=is_pdf)
    else:
        ImageBase64 = img2base64(img_path)
        ocr_res = ocr.DoOCR(OCR_NAME, ImageBase64=ImageBase64, ImageUrl=img_url, IsPdf=is_pdf)
    return ocr_res


def AdvertiseOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.AdvertiseOCR(img_path, img_url, configPath, id, key)


def ArithmeticOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.ArithmeticOCR(img_path, img_url, configPath, id, key)


def BankCardOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.BankCardOCR(img_path, img_url, configPath, id, key)


def BizLicenseOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.BizLicenseOCR(img_path, img_url, configPath, id, key)


def BusInvoiceOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.BusInvoiceOCR(img_path, img_url, configPath, id, key)


def BusinessCardOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.BusinessCardOCR(img_path, img_url, configPath, id, key)


def CarInvoiceOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.CarInvoiceOCR(img_path, img_url, configPath, id, key)


def ClassifyDetectOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.ClassifyDetectOCR(img_path, img_url, configPath, id, key)


def DriverLicenseOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.DriverLicenseOCR(img_path, img_url, configPath, id, key)


def DutyPaidProofOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.DutyPaidProofOCR(img_path, img_url, configPath, id, key)


def EduPaperOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.EduPaperOCR(img_path, img_url, configPath, id, key)


def EnglishOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.EnglishOCR(img_path, img_url, configPath, id, key)


def EnterpriseLicenseOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.EnterpriseLicenseOCR(img_path, img_url, configPath, id, key)


def EstateCertOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.EstateCertOCR(img_path, img_url, configPath, id, key)


def FinanBillOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.FinanBillOCR(img_path, img_url, configPath, id, key)


def FinanBillSliceOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.FinanBillSliceOCR(img_path, img_url, configPath, id, key)


def FlightInvoiceOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.FlightInvoiceOCR(img_path, img_url, configPath, id, key)


def FormulaOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.FormulaOCR(img_path, img_url, configPath, id, key)


def GeneralAccurateOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.GeneralAccurateOCR(img_path, img_url, configPath, id, key)


def GeneralBasicOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.GeneralBasicOCR(img_path, img_url, configPath, id, key)


def GeneralEfficientOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.GeneralEfficientOCR(img_path, img_url, configPath, id, key)


def GeneralFastOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.GeneralFastOCR(img_path, img_url, configPath, id, key)


def GeneralHandwritingOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.GeneralHandwritingOCR(img_path, img_url, configPath, id, key)


def HKIDCardOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.HKIDCardOCR(img_path, img_url, configPath, id, key)


def HmtResidentPermitOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.HmtResidentPermitOCR(img_path, img_url, configPath, id, key)


def IDCardOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.IDCardOCR(img_path, img_url, configPath, id, key)


def ImageEnhancement(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.ImageEnhancement(img_path, img_url, configPath, id, key)


def InstitutionOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.InstitutionOCR(img_path, img_url, configPath, id, key)


def InsuranceBillOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.InsuranceBillOCR(img_path, img_url, configPath, id, key)


def InvoiceGeneralOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.InvoiceGeneralOCR(img_path, img_url, configPath, id, key)


def LicensePlateOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.LicensePlateOCR(img_path, img_url, configPath, id, key)


def MLIDCardOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.MLIDCardOCR(img_path, img_url, configPath, id, key)


def MLIDPassportOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.MLIDPassportOCR(img_path, img_url, configPath, id, key)


def MainlandPermitOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.MainlandPermitOCR(img_path, img_url, configPath, id, key)


def MixedInvoiceDetect(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.MixedInvoiceDetect(img_path, img_url, configPath, id, key)


def MixedInvoiceOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.MixedInvoiceOCR(img_path, img_url, configPath, id, key)


def OrgCodeCertOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.OrgCodeCertOCR(img_path, img_url, configPath, id, key)


def PassportOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.PassportOCR(img_path, img_url, configPath, id, key)


def PermitOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.PermitOCR(img_path, img_url, configPath, id, key)


def PropOwnerCertOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.PropOwnerCertOCR(img_path, img_url, configPath, id, key)


def QrcodeOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.QrcodeOCR(img_path, img_url, configPath, id, key)


def QueryBarCode(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.QueryBarCode(img_path, img_url, configPath, id, key)


def QuotaInvoiceOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.QuotaInvoiceOCR(img_path, img_url, configPath, id, key)


def RecognizeContainerOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.RecognizeContainerOCR(img_path, img_url, configPath, id, key)


def RecognizeHealthCodeOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.RecognizeHealthCodeOCR(img_path, img_url, configPath, id, key)


def RecognizeIndonesiaIDCardOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.RecognizeIndonesiaIDCardOCR(img_path, img_url, configPath, id, key)


def RecognizeMedicalInvoiceOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.RecognizeMedicalInvoiceOCR(img_path, img_url, configPath, id, key)


def RecognizeOnlineTaxiItineraryOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.RecognizeOnlineTaxiItineraryOCR(img_path, img_url, configPath, id, key)


def RecognizePhilippinesDrivingLicenseOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.RecognizePhilippinesDrivingLicenseOCR(img_path, img_url, configPath, id, key)


def RecognizePhilippinesVoteIDOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.RecognizePhilippinesVoteIDOCR(img_path, img_url, configPath, id, key)


def RecognizeTableOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.RecognizeTableOCR(img_path, img_url, configPath, id, key)


def RecognizeThaiIDCardOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.RecognizeThaiIDCardOCR(img_path, img_url, configPath, id, key)


def RecognizeTravelCardOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.RecognizeTravelCardOCR(img_path, img_url, configPath, id, key)


def ResidenceBookletOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.ResidenceBookletOCR(img_path, img_url, configPath, id, key)


def RideHailingDriverLicenseOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.RideHailingDriverLicenseOCR(img_path, img_url, configPath, id, key)


def RideHailingTransportLicenseOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.RideHailingTransportLicenseOCR(img_path, img_url, configPath, id, key)


def SealOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.SealOCR(img_path, img_url, configPath, id, key)


def ShipInvoiceOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.ShipInvoiceOCR(img_path, img_url, configPath, id, key)


def SmartStructuralOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.SmartStructuralOCR(img_path, img_url, configPath, id, key)


def TableOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.TableOCR(img_path, img_url, configPath, id, key)


def TaxiInvoiceOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.TaxiInvoiceOCR(img_path, img_url, configPath, id, key)


def TextDetect(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.TextDetect(img_path, img_url, configPath, id, key)


def TollInvoiceOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.TollInvoiceOCR(img_path, img_url, configPath, id, key)


def TrainTicketOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.TrainTicketOCR(img_path, img_url, configPath, id, key)


def VatInvoiceVerify(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.VatInvoiceVerify(img_path, img_url, configPath, id, key)


def VatInvoiceVerifyNew(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.VatInvoiceVerifyNew(img_path, img_url, configPath, id, key)


def VatRollInvoiceOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.VatRollInvoiceOCR(img_path, img_url, configPath, id, key)


def VehicleLicenseOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.VehicleLicenseOCR(img_path, img_url, configPath, id, key)


def VehicleRegCertOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.VehicleRegCertOCR(img_path, img_url, configPath, id, key)


def VerifyBasicBizLicense(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.VerifyBasicBizLicense(img_path, img_url, configPath, id, key)


def VerifyBizLicense(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.VerifyBizLicense(img_path, img_url, configPath, id, key)


def VerifyEnterpriseFourFactors(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.VerifyEnterpriseFourFactors(img_path, img_url, configPath, id, key)


def VinOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.VinOCR(img_path, img_url, configPath, id, key)


def WaybillOCR(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.WaybillOCR(img_path, img_url, configPath, id, key)


def RecognizeGeneralInvoice(img_path=None, img_url=None, configPath=None, id=None, key=None):
    return potx.ocr.RecognizeGeneralInvoice(img_path, img_url, configPath, id, key)


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

def VatInvoiceOCR(img_path=None, img_url=None, configPath=None, id=None, key=None, pdf_path=None):
    return potx.ocr.VatInvoiceOCR(img_path, img_url, configPath, id, key, pdf_path)

    # return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
    #               img_path=img_path,
    #               img_url=img_url,
    #               configPath=configPath,
    #               id=id, key=key, pdf_path=pdf_path)


def VerifyOfdVatInvoiceOCR(ofd_file_path=None, ofd_file_url=None, id=None, key=None):
    return potx.ocr.VerifyOfdVatInvoiceOCR(ofd_file_path, ofd_file_url, id, key)
    # ocr = OfdOCR()
    # ocr.set_config(id, key)
    # if ofd_file_path:
    #     with open(ofd_file_path, 'rb') as file:
    #         pdf_data = file.read()
    #         base64_encoded_pdf = base64.b64encode(pdf_data).decode('utf-8')
    #         ocr_res = ocr.DoOCR(OfdFileBase64=base64_encoded_pdf)
    # elif ofd_file_url:
    #     ocr_res = ocr.DoOCR(OfdFileUrl=ofd_file_url)
    #
    # return ocr_res


def BankSlipOCR(img_path=None, img_url=None, configPath=None, id=None, key=None, pdf_path=None):
    return potx.ocr.BankSlipOCR(img_path, img_url, configPath, id, key, pdf_path)
    # return do_api(OCR_NAME=str(sys._getframe().f_code.co_name),
    #               img_path=img_path,
    #               img_url=img_url,
    #               configPath=configPath,
    #               id=id, key=key, pdf_path=pdf_path)


######## 优化示例函数 ########
def SmartStructuralPro(id, key, img_path):
    """
    直接调用potx中的方法，实现该功能
    Args:
        id:
        key:
        img_path:

    Returns:

    """
    return potx.ocr.SmartStructuralPro(id, key, img_path)
