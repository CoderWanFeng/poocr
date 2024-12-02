# -*- coding: UTF-8 -*-
'''
@Author  ：程序员晚枫，B站/抖音/微博/小红书/公众号
@WeChat     ：CoderWanFeng
@Blog      ：www.python-office.com
@Date    ：2023/1/22 18:45
@Description     ：通用的一些方法
'''

import fitz  # PyMuPDF


def get_error_info(error_info):
    """
    检查接口返回数据是否错误
    :param error_info: 调用接口的返回数据
    :return:
    """
    error_url = 'http://python4office.cn/pobaidu/pobaidu-error/'
    if error_info.get('error_code', False):
        return f"接口调用错误，错误信息是{error_info}，原因和解决方法请查看官方文档：{error_url}"
    return False


def img2base64(imgPath):
    with open(imgPath, "rb") as f:
        data = f.read()
        encodestr = base64.b64encode(data)  # 得到 byte 编码的数据
        picbase = str(encodestr, 'utf-8')
        return picbase


import base64


def pdf2base64(pdf_path):
    base64_encoded_pdf = []
    pdf = fitz.open(pdf_path)
    for i in range(len(pdf)):
        pdf_bytes = pdf.convert_to_pdf(i, i + 1)
        # 灏嗗浘鐗囪浆鎹负Base64缂栫爜鐨勫瓧绗︿覆
        base64_encoded_pdf.append(base64.b64encode(pdf_bytes).decode('utf-8'))
    # 鍏抽棴PDF鏂囨。
    pdf.close()
    return base64_encoded_pdf


if __name__ == '__main__':
    pdf2base64(pdf_path=r'D:\workplace\code\github\poocr\tests\test_files\4-银行回单\huawei\002.pdf')
