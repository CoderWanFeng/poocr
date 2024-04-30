import unittest

from poocr.api.ocr2excel import *


class TestTencent(unittest.TestCase):

    def setUp(self):
        self.SecretId = 'AKIDITXZTE65a7Ujy77EScqy9D7nESSEmKoC'
        self.SecretKey = 'V4eI2f6A8vYBiECEFU2NUP8uXxEHOafh'

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
        poocr.ocr.BizLicenseOCR(img_path=r'd://test//营业执照的照片.jpg')

    def test_IDCardOCR2Excel(self):
        poocr.ocr2excel.IDCardOCR2Excel(input_path=r'./test_files/', id=self.SecretId, key=self.SecretKey)
