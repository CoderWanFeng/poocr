import os
import unittest

from poocr.api.ocr2excel import RecognizeGeneralInvoiceOCR2Excel, VatInvoiceOCR2Excel


class Ocr2Excel(unittest.TestCase):

    def setUp(self):
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
        VatInvoiceOCR2Excel(input_path='../test_files/VatInvoiceOCR/img.png',
                            output_path=r'../test_files/VatInvoiceOCR',
                            id=self.SecretId,
                            key=self.SecretKey)
        self.assertTrue(
            os.path.exists("../test_files/VatInvoiceOCR/VatInvoiceOCR2Excel.xlsx"))
        os.remove('../test_files/VatInvoiceOCR/VatInvoiceOCR2Excel.xlsx')
