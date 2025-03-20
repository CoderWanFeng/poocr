import os
import unittest

from poocr.api.ocr import DutyPaidProofOCR, VerifyOfdVatInvoiceOCR
from poocr.api.ocr2excel import *
from poocr.core.HuaweiOCR import BankReceipt2excel


class TestTencent(unittest.TestCase):

    def setUp(self):
        self.SecretId = os.getenv("SecretId", None)
        self.SecretKey = os.getenv("SecretKey", None)

        self.ak = os.getenv('ak', None)
        self.sk = os.getenv('sk', None)

    def test_vin_ocr(self):
        r = VatInvoiceOCR(img_path=r'C:\Users\Lenovo\Desktop\temp\增值税发票-test.jpg')
        print(r)

    def test_idcard_ocr(self):
        res = IDCardOCR(
            img_path=r'C:\Users\Lenovo\Desktop\temp\正面.jpg')
        print(res)

    def test_VatInvoiceOCR2Excel(self):
        VatInvoiceOCR2Excel(input_path=r'./test_files/火车票/1-铁路电子客票.pdf',
                            output_excel=r'./VatInvoiceOCR2Excel.xlsx',
                            id=self.SecretId, key=self.SecretKey
                            )

    def test_BankSlipOCR2Excel(self):
        BankSlipOCR2Excel(input_path=r'test_files/4-银行回单/huawei/002.pdf',
                          output_excel=r'./BankSlipOCR2Excel.xlsx',
                          output_path=r'./test_files/4-银行回单',
                          id=self.SecretId, key=self.SecretKey
                          )

    def test_TrainTicketOCR2Excel(self):
        TrainTicketOCR2Excel(input_path=r'./test_files/火车票/Snipaste_2025-01-18_14-51-10.jpg', id=self.SecretId,
                             key=self.SecretKey)

    def test_BizLicenseOCR(self):
        res = poocr.ocr.BizLicenseOCR(img_path=r'./test_files/biz_img/demo1.png', id=self.SecretId, key=self.SecretKey)
        print(res)

    def test_IDCardOCR2Excel(self):
        poocr.ocr2excel.IDCardOCR2Excel(input_path=r'./test_files/', id=self.SecretId, key=self.SecretKey)

    def test_BizLicenseOCR2Excel(self):
        poocr.ocr2excel.BizLicenseOCR2Excel(input_path=r'./test_files/biz_img/', id=self.SecretId, key=self.SecretKey)

    def test_RecognizeMedicalInvoiceOCR(self):
        res = poocr.ocr.RecognizeMedicalInvoiceOCR(
            img_path=r'./test_files/医疗发票/958b60388f12ce3889aa4696470483c.jpg', id=self.SecretId,
            key=self.SecretKey)
        print(res)

    def test_InsuranceBillOCR(self):
        res = poocr.ocr.InsuranceBillOCR(
            img_path=r'./test_files/医疗发票/958b60388f12ce3889aa4696470483c.jpg', id=self.SecretId,
            key=self.SecretKey)
        print(res)

    def test_bank_huawei(self):
        BankReceipt2excel(ak=self.ak, sk=self.sk, file_path=r"./test_files/4-银行回单/huawei/")

    def test_DutyPaidProofOCR(self):
        res = DutyPaidProofOCR(
            img_path=r'D:\workplace\code\github\poocr\dev\完税凭证\a91e72851b15cd76695e56ae70e09dc0326432.jpg.crdownload',
            id=self.SecretId, key=self.SecretKey)
        print(res)

    def test_VerifyOfdVatInvoiceOCR_Train(self):
        res = VerifyOfdVatInvoiceOCR(ofd_file_path=r'./test_files/火车票/08da5fd7-bac1-4757-a578-a7cb695351b7.ofd',
                                     id=self.SecretId, key=self.SecretKey)
        logger.info(res)

    def test_RET2excel(self):
        RET2excel(img_path=r'./test_files/train/imgs',
                  output_path=r'./test_files/train',
                  output_excel=r'./RET2excel.xlsx',
                  id=self.SecretId, key=self.SecretKey)
