import unittest

from poocr.api.ocr import *
from poocr.api.ocr2excel import *


class TestTencent(unittest.TestCase):

    def test_vin_ocr(self):
        r = VatInvoiceOCR(img_path=r'C:\Users\Lenovo\Desktop\temp\增值税发票-test.jpg')
        print(r)

    def test_idcard_ocr(self):
        res = IDCardOCR(
            img_path=r'C:\Users\Lenovo\Desktop\temp\正面.jpg')
        print(res)

    def test_VatInvoiceOCR2Excel(self):
        VatInvoiceOCR2Excel(intput_path=r'C:\Users\Lenovo\Desktop\temp\v1-微信图片_20230409204718.png',
                            output_excel=r'./VatInvoiceOCR2Excel.xlsx',
                            configPath=r'./poocr-config.toml')
