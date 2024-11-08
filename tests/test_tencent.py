import unittest

from poocr.api.ocr2excel import *


class TestTencent(unittest.TestCase):

    def setUp(self):
        self.SecretId = 'AKIDztbwHThnrtr7IHUm3Pugeq0vpfbeq4GY'
        self.SecretKey = 'Hi3KgI0b1FNes7Qlx5JnGg3jIm7HMZ2W'

    def test_vin_ocr(self):
        r = VatInvoiceOCR(img_path=r'C:\Users\Lenovo\Desktop\temp\增值税发票-test.jpg')
        print(r)

    def test_idcard_ocr(self):
        res = IDCardOCR(
            img_path=r'C:\Users\Lenovo\Desktop\temp\正面.jpg')
        print(res)

    def test_VatInvoiceOCR2Excel(self):
        VatInvoiceOCR2Excel(intput_path=r'C:\Users\Lenovo\Desktop\temp\Snipaste_2023-04-09_22-23-48.png',
                            output_excel=r'./VatInvoiceOCR2Excel.xlsx',
                            configPath=r'./poocr-config.toml')

    def test_TrainTicketOCR2Excel(self):
        TrainTicketOCR2Excel(input_path='', output_excel='', configPath='fdasf')

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
