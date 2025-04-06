import os
import unittest

from poocr.api.ocr2excel import *


class Ocr2Excel(unittest.TestCase):
    """
    test for ocr2excel.py
    """

    def setUp(self):
        # 腾讯
        # self.SecretId = os.getenv("SecretId", None)
        # self.SecretKey = os.getenv("SecretKey", None)
        self.SecretId = os.getenv("SecretId", None)
        self.SecretKey = os.getenv("SecretKey", None)

    def test_RecognizeGeneralInvoiceOCR2Excel(self):
        RecognizeGeneralInvoiceOCR2Excel(input_path='../test_files/RecognizeGeneralInvoiceOCR/样例.png',
                                         output_path='../test_files/RecognizeGeneralInvoiceOCR',
                                         id=self.SecretId,
                                         key=self.SecretKey, sub_type=2)
        self.assertTrue(
            os.path.exists("../test_files/RecognizeGeneralInvoiceOCR/RecognizeGeneralInvoiceOCR2Excel.xlsx"))
        os.remove('../test_files/RecognizeGeneralInvoiceOCR/RecognizeGeneralInvoiceOCR2Excel.xlsx')

    def test_VatInvoiceOCR2Excel(self):
        VatInvoiceOCR2Excel(input_path='../test_files/VatInvoiceOCR',
                            output_path=r'../test_files/VatInvoiceOCR',
                            id=self.SecretId,
                            key=self.SecretKey)
        self.assertTrue(
            os.path.exists("../test_files/VatInvoiceOCR/VatInvoiceOCR2Excel.xlsx"))
        os.remove('../test_files/VatInvoiceOCR/VatInvoiceOCR2Excel.xlsx')

    def test_BankCardOCR2Excel(self):
        BankCardOCR2Excel(input_path='../test_files/BankCard/bankcard.png',
                          output_path=r'../test_files/BankCard',
                          id=self.SecretId,
                          key=self.SecretKey)
        self.assertTrue(
            os.path.exists("../test_files/BankCard/BankCardOCR2Excel.xlsx"))
        os.remove('../test_files/BankCard/BankCardOCR2Excel.xlsx')

    def test_BankSlipOCR2Excel(self):
        BankSlipOCR2Excel(input_path='../test_files/BankSlip/bankslip.png',
                          output_path=r'../test_files/BankSlip',
                          id=self.SecretId,
                          key=self.SecretKey)
        self.assertTrue(
            os.path.exists("../test_files/BankSlip/BankSlipOCR2Excel.xlsx"))
        os.remove('../test_files/BankSlip/BankSlipOCR2Excel.xlsx')

    def test_IDCardOCRFront2Excel(self):
        IDCardOCR2Excel(input_path='../test_files/IDCard/idcard_front.png',
                        output_path=r'../test_files/IDCard',
                        id=self.SecretId,
                        key=self.SecretKey)
        self.assertTrue(
            os.path.exists("../test_files/IDCard/IDCardOCR2Excel.xlsx"))
        os.remove('../test_files/IDCard/IDCardOCR2Excel.xlsx')

    def test_IDCardOCRBack2Excel(self):
        IDCardOCR2Excel(input_path='../test_files/IDCard/idcard_bak.png',
                        output_path=r'../test_files/IDCard',
                        id=self.SecretId,
                        key=self.SecretKey)
        self.assertTrue(
            os.path.exists("../test_files/IDCard/IDCardOCR2Excel.xlsx"))
        os.remove('../test_files/IDCard/IDCardOCR2Excel.xlsx')

    def test_TrainTicketOCR2Excel(self):
        TrainTicketOCR2Excel(input_path=r'../test_files/TrainTicket/img.png',
                             output_excel=r'../test_files/TrainTicket/ticket.xlsx',
                             configPath=r'../test_files/poocr-config.toml',
                             id=self.SecretId,
                             key=self.SecretKey)
        self.assertTrue(
            os.path.exists("../test_files/TrainTicket/ticket.xlsx"))
        os.remove('../test_files/TrainTicket/ticket.xlsx')

    def test_LicensePlateOCR2Excel(self):
        LicensePlateOCR2Excel(input_path=r'../test_files/LicensePlate/img.png',
                              output_excel=r'../test_files/LicensePlate/LicensePlate.xlsx',
                              configPath=r'../test_files/poocr-config.toml',
                              id=self.SecretId,
                              key=self.SecretKey)
        self.assertTrue(
            os.path.exists("../test_files/LicensePlate/LicensePlate.xlsx"))
        os.remove('../test_files/LicensePlate/LicensePlate.xlsx')

    def test_BizLicenseOCR2Excel(self):
        BizLicenseOCR2Excel(input_path=r'../test_files/BizLicense/img.png',
                            output_excel=r'../test_files/BizLicense/BizLicense.xlsx',
                            configPath=r'../test_files/poocr-config.toml',
                            id=self.SecretId,
                            key=self.SecretKey)
        self.assertTrue(
            os.path.exists("../test_files/BizLicense/BizLicense.xlsx"))
        os.remove('../test_files/BizLicense/BizLicense.xlsx')

    def test_household2excel(self):
        household2excel(ak=self.SecretId, sk=self.SecretKey, img_path=['../test_files/Household'],
                        output_excel=r'../test_files/Household/household2excel.xlsx')
        # household2excel(ak=r'HPUAKZ48UYAHP4HZ7NAS', sk=r'0hLDibc6ezOIOohNSnuLDbBO3Ue1U6NS4PIkmyur',img_path=['../test_files/Household'],
        #                      output_excel=r'../test_files/Household/household2excel.xlsx')
        self.assertTrue(
            os.path.exists("../test_files/Household/household2excel.xlsx"))
        os.remove('../test_files/Household/household2excel.xlsx')

    def test_household2excel2(self):
        household2excel2(ak=self.SecretId, sk=self.SecretKey, img_path=['../test_files/Household'],
                         output_excel=r'../test_files/Household/household2excel.xlsx')
        self.assertTrue(
            os.path.exists("../test_files/Household/household2excel.xlsx"))
        os.remove('../test_files/Household/household2excel.xlsx')
