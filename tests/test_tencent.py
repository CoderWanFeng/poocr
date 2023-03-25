import unittest

from poocr.api.ocr import *


class TestTencent(unittest.TestCase):

    def test_vin_ocr(self):
        r = VatInvoiceOCR(img_path=r'C:\Users\Lenovo\Desktop\temp\增值税发票-test.jpg')
        print(r)

    def test_idcard_ocr(self):
        res = IDCardOCR(
            img_path=r'C:\Users\Lenovo\Desktop\temp\正面.jpg')
        print(res)
