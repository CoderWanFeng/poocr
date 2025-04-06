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

    def test_VatInvoiceOCR2Excel(self):
        v_path = r'D:\test\py310\pdf_work\merge.pdf'
        VatInvoiceOCR2Excel(input_path=v_path,
                            id=self.SecretId,
                            key=self.SecretKey)
