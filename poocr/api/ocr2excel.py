# -*- coding: UTF-8 -*-
'''
@作者 ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@微信 ：CoderWanFeng : https://mp.weixin.qq.com/s/yFcocJbfS9Hs375NhE8Gbw
@个人网站 ：www.python-office.com
@Date    ：2023/3/25 18:53
@Description     ：
- id和key：
    - 开通和使用👉[免费教程](https://curl.qcloud.com/fuOGcm2R)

'''
import json
from pathlib import Path

import pandas as pd
from pofile import get_files, mkdir
from poprogress import simple_progress

import poocr
from poocr.api.ocr import VatInvoiceOCR, IDCardOCR


def VatInvoiceOCR2Excel(input_path, output_path=None, output_excel='VatInvoiceOCR2Excel.xlsx', img_url=None,
                        configPath=None, id=None, key=None, file_name=False, trans=False):
    """
    批量识别发票，并保存在Excel中
    :param input_path: 发票存放位置，可以填单个文件，也可以填一个目录
    :param output_path:
    :param output_excel:
    :param img_url:
    :param configPath:
    :return:
    """
    vat_img_files = get_files(input_path)
    if vat_img_files == None:
        raise BaseException(f'{input_path}这个路径下，没有存放任何发票，请确认后重新运行')
    abs_intput_path = Path(input_path).absolute()
    if output_path == None:
        output_path = './'
    mkdir(Path(output_path).absolute())  # 如果不存在，则创建输出目录
    if output_excel.endswith('.xlsx') or output_excel.endswith('xls'):  # 如果指定的输出excel结尾不正确，则报错退出
        abs_output_excel = Path(output_path).absolute() / output_excel
    else:  # 指定了，但不是xlsx或者xls结束
        raise BaseException(
            f'输出结果名：output_excel参数，必须以xls或者xlsx结尾，您的输入:{output_excel}有误，请修改后重新运行')
    res_df = []  # 装全部识别的结果
    for vat_img in simple_progress(vat_img_files):
        try:
            api_res = VatInvoiceOCR(img_path=str(vat_img), img_url=img_url, configPath=configPath, id=id, key=key)
            api_res_json = json.loads(str(api_res))
            VatInvoiceInfos = api_res_json['VatInvoiceInfos']
            dict_pandas = {}  # 存放一行数据
            # 读返回值的第一个key
            for VatInvoiceInfo in VatInvoiceInfos:
                if file_name:
                    dict_pandas['文件名'] = Path(vat_img).name  # 增加文件名作为一列

                dict_pandas[VatInvoiceInfo['Name']] = VatInvoiceInfo['Value']
            # 读返回值的第二个key
            key_trans_history = {}
            new_item_json = []
            Items = api_res_json['Items']
            if trans:
                import wftools

                for i in Items:
                    new_i = {}
                    for k, v in i.items():
                        if key_trans_history.get(k, None) == None:
                            key_trans_history[k] = wftools.transtools(k, to_lang='zh', from_lang='en')
                        new_i[key_trans_history.get(k)] = v
                    new_item_json.append(new_i)
            else:
                new_item_json = Items
            for Item in new_item_json:
                dict_pandas.update(Item)
                res_df.append(pd.DataFrame(dict_pandas, index=[0]))
        except Exception as e:
            print(e)
            continue
    # 整理全部识别结果
    if len(res_df) > 0:
        res_excel = res_df[0]
        for index, line_df in enumerate(res_df):
            if index == 0:
                continue
            res_excel = res_excel._append(line_df)
        pd.DataFrame(res_excel).to_excel(str(abs_output_excel))  # 写入Excel
    else:
        print(f'该文件夹下，没有任何符合条件的发票图片')


def IDCardOCR2Excel(input_path, output_path=None, output_excel='IDCardOCR2Excel.xlsx', img_url=None,
                    configPath=None, id=None, key=None):
    """
    批量识别身份证，并保存在Excel中
    :param input_path: 身份证存放位置，可以填单个文件，也可以填一个目录
    :param output_path:
    :param output_excel:
    :param img_url:
    :param configPath:
    :return:
    """
    id_img_files = get_files(input_path)
    if id_img_files == None:
        raise BaseException(f'{input_path}这个路径下，没有存放任何身份证，请确认后重新运行')
    abs_intput_path = Path(input_path).absolute()
    if output_path == None:
        output_path = './'
    mkdir(Path(output_path).absolute())  # 如果不存在，则创建输出目录
    if output_excel.endswith('.xlsx') or output_excel.endswith('xls'):  # 如果指定的输出excel结尾不正确，则报错退出
        abs_output_excel = Path(output_path).absolute() / output_excel
    else:  # 指定了，但不是xlsx或者xls结束
        raise BaseException(
            f'输出结果名：output_excel参数，必须以xls或者xlsx结尾，您的输入:{output_excel}有误，请修改后重新运行')
    res_df = []  # 装全部识别的结果
    for id_img in simple_progress(id_img_files):
        try:
            api_res = IDCardOCR(img_path=str(id_img), img_url=img_url, configPath=configPath, id=id, key=key)
            api_res_json = json.loads(str(api_res))
            del api_res_json['ReflectDetailInfos']

            res_df.append(pd.DataFrame(api_res_json, index=[0]))
        except:
            continue
    # 整理全部识别结果
    if len(res_df) > 0:
        res_excel = res_df[0]
        for index, line_df in enumerate(res_df):
            if index == 0:
                continue
            res_excel = res_excel._append(line_df)
        pd.DataFrame(res_excel).to_excel(str(abs_output_excel))  # 写入Excel
    else:
        print(f'该文件夹下，没有任何符合条件的身份证图片')


def TrainTicketOCR2Excel(input_path: str, output_excel: str = r'./TrainTicketOCR2Excel.xlsx', img_url: str = None,
                         configPath: str = None) -> None:
    ticket_list = []
    ticket_files = get_files(input_path)
    for ticket in simple_progress(ticket_files):
        ticket_info = poocr.ocr.TrainTicketOCR(img_path=ticket, img_url=img_url, configPath=configPath)
        ticket_list.append(ticket_info)
    ticket_df = pd.DataFrame(ticket_list)
    ticket_df.to_excel(output_excel, index=None)


def BankCardOCR2Excel(input_path, output_path=None, output_excel='BankCardOCR2Excel.xlsx', img_url=None,
                      configPath=None, id=None, key=None):
    """
    识别银行卡，自动保存为Excel文件
    :param input_path: 必填，银行卡图片的位置
    :param output_path: 选填，输出Excel的位置
    :param output_excel: 选填，输出Excel的名称
    :param img_url: 选填，可以是网络图片
    :param configPath: 已废弃
    :param id: 你的腾讯账号的密钥，获取方式：https://curl.qcloud.com/fuOGcm2R
    :param key: 你的腾讯账号的密钥，获取方式：https://curl.qcloud.com/fuOGcm2R
    :return:
    """
    test_json = poocr.ocr.BankCardOCR(img_path=input_path, img_url=img_url, configPath=configPath, id=id,
                                      key=key)
    df = pd.DataFrame(json.loads(str(test_json)), index=[0])
    if output_path == None:
        output_path = './'
    mkdir(Path(output_path).absolute())  # 如果不存在，则创建输出目录
    if output_excel.endswith('.xlsx') or output_excel.endswith('xls'):  # 如果指定的输出excel结尾不正确，则报错退出
        abs_output_excel = Path(output_path).absolute() / output_excel
    df.to_excel(str(abs_output_excel), index=False)


def LicensePlateOCR2Excel(input_path, output_path=None, output_excel='LicensePlateOCR2Excel.xlsx', img_url=None,
                          configPath=None, id=None, key=None):
    """
    识别银行卡，自动保存为Excel文件
    :param input_path: 必填，银行卡图片的位置
    :param output_path: 选填，输出Excel的位置
    :param output_excel: 选填，输出Excel的名称
    :param img_url: 选填，可以是网络图片
    :param configPath: 已废弃
    :param id: 你的腾讯账号的密钥，获取方式：https://curl.qcloud.com/fuOGcm2R
    :param key: 你的腾讯账号的密钥，获取方式：https://curl.qcloud.com/fuOGcm2R
    :return:
    """
    test_json = poocr.ocr.LicensePlateOCR(img_path=input_path, img_url=img_url, configPath=configPath, id=id,
                                          key=key)
    df = pd.DataFrame(json.loads(str(test_json)), index=[0])
    if output_path == None:
        output_path = './'
    mkdir(Path(output_path).absolute())  # 如果不存在，则创建输出目录
    if output_excel.endswith('.xlsx') or output_excel.endswith('xls'):  # 如果指定的输出excel结尾不正确，则报错退出
        abs_output_excel = Path(output_path).absolute() / output_excel
    df.to_excel(str(abs_output_excel), index=False)
