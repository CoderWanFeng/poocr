# -*- coding: UTF-8 -*-
'''
@Author  ：程序员晚枫，B站/抖音/微博/小红书/公众号
@WeChat     ：CoderWanFeng
@Blog      ：www.python-office.com
@Date    ：2023/1/22 18:45
@Description     ：通用的一些方法
'''
import base64


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


if __name__ == '__main__':
    res = img2base64(imgPath=r'C:\Us-01-25_00-18-41.jpg')
    print(res)
