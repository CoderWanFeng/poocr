import os
import unittest

from poocr.api.ocr2excel import *


class TestTencent(unittest.TestCase):

    def setUp(self):
        self.SecretId = os.getenv("SecretId", None)
        self.SecretKey = os.getenv("SecretKey", None)

        self.ak = os.getenv('ak', None)
        self.sk = os.getenv('sk', None)

    def test_id_key(self):
        if not (self.SecretId and self.SecretKey):
            raise Exception("请配置腾讯云的SecretId和SecretKey")
        if not (self.ak and self.sk):
            raise Exception("请配置华为云的ak和sk")
        logger.info(f'腾讯云 {self.SecretId} {self.SecretKey}')
        logger.info(f'华为云 {self.ak} {self.sk}')

    def test_version(self):
        logger.info(f"poocr version:{poocr.__version__}")

    def test_doc(self):
        logger.info(f"poocr doc:{poocr.__doc__}")
