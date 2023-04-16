# -*- coding: UTF-8 -*-
'''
@Author  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫
@WeChat     ：CoderWanFeng
@Blog      ：www.python-office.com
@Date    ：2023/3/25 18:53 
@Description     ：
'''
import json
from pathlib import Path

import pandas as pd
from pofile import get_files
from poprogress import simple_progress

import poocr
from poocr.api.ocr import VatInvoiceOCR


def VatInvoiceOCR2Excel(intput_path, output_excel=None, img_url=None, configPath=None):
    abs_intput_path = Path(intput_path).absolute()
    if output_excel.endswith('.xlsx') or output_excel.endswith('xls'):
        abs_output_excel = Path(output_excel).absolute()
    elif output_excel:  # 指定了，但不是xlsx或者xls结束
        print(f'输出结果名：output_excel参数，必须以xls或者xlsx结尾，您的输入:{output_excel}有误，请修改后重新运行')
        return
    else:
        abs_output_excel = Path(intput_path).absolute() / 'VatInvoiceOCR2Excel.xlsx'
    api_res = VatInvoiceOCR(img_path=str(abs_intput_path), img_url=img_url, configPath=configPath)
    # api_res = '{"VatInvoiceInfos": [{"Name": "销售方识别号", "Value": "911201103409033300", "Polygon": {"LeftTop": {"X": 374, "Y": 824}, "RightTop": {"X": 614, "Y": 824}, "RightBottom": {"X": 614, "Y": 847}, "LeftBottom": {"X": 374, "Y": 847}}}, {"Name": "销售方名称", "Value": "深圳腾讯游戏有限公司", "Polygon": {"LeftTop": {"X": 374, "Y": 788}, "RightTop": {"X": 618, "Y": 788}, "RightBottom": {"X": 618, "Y": 813}, "LeftBottom": {"X": 374, "Y": 813}}}, {"Name": "购买方识别号", "Value": "91440300MA55UJ6L44", "Polygon": {"LeftTop": {"X": 378, "Y": 268}, "RightTop": {"X": 653, "Y": 268}, "RightBottom": {"X": 653, "Y": 294}, "LeftBottom": {"X": 378, "Y": 294}}}, {"Name": "购买方名称", "Value": "腾讯优图有限公司", "Polygon": {"LeftTop": {"X": 375, "Y": 230}, "RightTop": {"X": 572, "Y": 230}, "RightBottom": {"X": 572, "Y": 256}, "LeftBottom": {"X": 375, "Y": 256}}}, {"Name": "发票名称", "Value": "天津增值税电子普通发票", "Polygon": {"LeftTop": {"X": 606, "Y": 59}, "RightTop": {"X": 1186, "Y": 59}, "RightBottom": {"X": 1186, "Y": 114}, "LeftBottom": {"X": 606, "Y": 114}}}, {"Name": "发票代码", "Value": "012001100311", "Polygon": {"LeftTop": {"X": 1342, "Y": 62}, "RightTop": {"X": 1502, "Y": 62}, "RightBottom": {"X": 1502, "Y": 85}, "LeftBottom": {"X": 1342, "Y": 85}}}, {"Name": "发票号码", "Value": "No63591128", "Polygon": {"LeftTop": {"X": 1342, "Y": 101}, "RightTop": {"X": 1453, "Y": 101}, "RightBottom": {"X": 1453, "Y": 124}, "LeftBottom": {"X": 1342, "Y": 124}}}, {"Name": "开票日期", "Value": "2019年06月16日", "Polygon": {"LeftTop": {"X": 1341, "Y": 135}, "RightTop": {"X": 1510, "Y": 135}, "RightBottom": {"X": 1510, "Y": 162}, "LeftBottom": {"X": 1341, "Y": 162}}}, {"Name": "机器编号", "Value": "499099606262", "Polygon": {"LeftTop": {"X": 269, "Y": 186}, "RightTop": {"X": 432, "Y": 186}, "RightBottom": {"X": 432, "Y": 210}, "LeftBottom": {"X": 269, "Y": 210}}}, {"Name": "校验码", "Value": "04656054380312409795", "Polygon": {"LeftTop": {"X": 1342, "Y": 177}, "RightTop": {"X": 1631, "Y": 177}, "RightBottom": {"X": 1631, "Y": 198}, "LeftBottom": {"X": 1342, "Y": 198}}}, {"Name": "密码区1", "Value": "033-<<>7>616<-4+*-+4/5230604", "Polygon": {"LeftTop": {"X": 1061, "Y": 233}, "RightTop": {"X": 1641, "Y": 233}, "RightBottom": {"X": 1641, "Y": 260}, "LeftBottom": {"X": 1061, "Y": 260}}}, {"Name": "密码区2", "Value": "*/78+740454724/0<34*9/>61856", "Polygon": {"LeftTop": {"X": 1062, "Y": 270}, "RightTop": {"X": 1641, "Y": 270}, "RightBottom": {"X": 1641, "Y": 297}, "LeftBottom": {"X": 1062, "Y": 297}}}, {"Name": "密码区3", "Value": "29/-0651-2*91440-47386<535<5", "Polygon": {"LeftTop": {"X": 1058, "Y": 307}, "RightTop": {"X": 1640, "Y": 307}, "RightBottom": {"X": 1640, "Y": 334}, "LeftBottom": {"X": 1058, "Y": 334}}}, {"Name": "密码区4", "Value": "92<<9-9+-601452319091>67>--7", "Polygon": {"LeftTop": {"X": 1062, "Y": 345}, "RightTop": {"X": 1642, "Y": 345}, "RightBottom": {"X": 1642, "Y": 372}, "LeftBottom": {"X": 1062, "Y": 372}}}, {"Name": "货物或应税劳务、服务名称", "Value": "客运服务费", "Polygon": {"LeftTop": {"X": 203, "Y": 439}, "RightTop": {"X": 324, "Y": 439}, "RightBottom": {"X": 324, "Y": 466}, "LeftBottom": {"X": 203, "Y": 466}}}, {"Name": "规格型号", "Value": "无", "Polygon": {"LeftTop": {"X": 619, "Y": 428}, "RightTop": {"X": 647, "Y": 428}, "RightBottom": {"X": 647, "Y": 454}, "LeftBottom": {"X": 619, "Y": 454}}}, {"Name": "单位", "Value": "次", "Polygon": {"LeftTop": {"X": 761, "Y": 426}, "RightTop": {"X": 790, "Y": 426}, "RightBottom": {"X": 790, "Y": 454}, "LeftBottom": {"X": 761, "Y": 454}}}, {"Name": "数量", "Value": "1", "Polygon": {"LeftTop": {"X": 886, "Y": 429}, "RightTop": {"X": 905, "Y": 429}, "RightBottom": {"X": 905, "Y": 452}, "LeftBottom": {"X": 886, "Y": 452}}}, {"Name": "单价", "Value": "87.28", "Polygon": {"LeftTop": {"X": 1019, "Y": 428}, "RightTop": {"X": 1082, "Y": 428}, "RightBottom": {"X": 1082, "Y": 452}, "LeftBottom": {"X": 1019, "Y": 452}}}, {"Name": "金额", "Value": "87.28", "Polygon": {"LeftTop": {"X": 1194, "Y": 428}, "RightTop": {"X": 1257, "Y": 428}, "RightBottom": {"X": 1257, "Y": 452}, "LeftBottom": {"X": 1194, "Y": 452}}}, {"Name": "税率", "Value": "3%", "Polygon": {"LeftTop": {"X": 1374, "Y": 427}, "RightTop": {"X": 1410, "Y": 427}, "RightBottom": {"X": 1410, "Y": 451}, "LeftBottom": {"X": 1374, "Y": 451}}}, {"Name": "税额", "Value": "2.62", "Polygon": {"LeftTop": {"X": 1509, "Y": 428}, "RightTop": {"X": 1560, "Y": 428}, "RightBottom": {"X": 1560, "Y": 451}, "LeftBottom": {"X": 1509, "Y": 451}}}, {"Name": "合计金额", "Value": "¥87.28", "Polygon": {"LeftTop": {"X": 1252, "Y": 686}, "RightTop": {"X": 1335, "Y": 686}, "RightBottom": {"X": 1335, "Y": 709}, "LeftBottom": {"X": 1252, "Y": 709}}}, {"Name": "合计税额", "Value": "2.62", "Polygon": {"LeftTop": {"X": 1581, "Y": 685}, "RightTop": {"X": 1650, "Y": 685}, "RightBottom": {"X": 1650, "Y": 709}, "LeftBottom": {"X": 1581, "Y": 709}}}, {"Name": "价税合计(大写)", "Value": "捌拾玖圆玖角整", "Polygon": {"LeftTop": {"X": 573, "Y": 731}, "RightTop": {"X": 744, "Y": 731}, "RightBottom": {"X": 744, "Y": 758}, "LeftBottom": {"X": 573, "Y": 758}}}, {"Name": "小写金额", "Value": "¥89.90", "Polygon": {"LeftTop": {"X": 1414, "Y": 734}, "RightTop": {"X": 1497, "Y": 734}, "RightBottom": {"X": 1497, "Y": 756}, "LeftBottom": {"X": 1414, "Y": 756}}}, {"Name": "销售方地址、电话", "Value": "天津经济技术开发区南港工业区综合服务区办公楼", "Polygon": {"LeftTop": {"X": 372, "Y": 862}, "RightTop": {"X": 722, "Y": 862}, "RightBottom": {"X": 722, "Y": 881}, "LeftBottom": {"X": 372, "Y": 881}}}, {"Name": "销售方开户行及账号", "Value": "招商银行股份有限公司天津自由贸易试验区分行122905939910401", "Polygon": {"LeftTop": {"X": 372, "Y": 894}, "RightTop": {"X": 977, "Y": 894}, "RightBottom": {"X": 977, "Y": 917}, "LeftBottom": {"X": 372, "Y": 917}}}, {"Name": "收款人", "Value": "张强", "Polygon": {"LeftTop": {"X": 299, "Y": 937}, "RightTop": {"X": 350, "Y": 937}, "RightBottom": {"X": 350, "Y": 963}, "LeftBottom": {"X": 299, "Y": 963}}}, {"Name": "复核", "Value": "静静", "Polygon": {"LeftTop": {"X": 699, "Y": 936}, "RightTop": {"X": 751, "Y": 936}, "RightBottom": {"X": 751, "Y": 962}, "LeftBottom": {"X": 699, "Y": 962}}}, {"Name": "开票人", "Value": "丽丽", "Polygon": {"LeftTop": {"X": 1082, "Y": 937}, "RightTop": {"X": 1132, "Y": 937}, "RightBottom": {"X": 1132, "Y": 962}, "LeftBottom": {"X": 1082, "Y": 962}}}, {"Name": "省", "Value": "天津市", "Polygon": null}, {"Name": "是否有公司印章", "Value": "0", "Polygon": null}, {"Name": "发票类型", "Value": "增值税电子普通发票", "Polygon": null}, {"Name": "发票消费类型", "Value": "服务", "Polygon": null}, {"Name": "成品油标志", "Value": "", "Polygon": null}, {"Name": "购买方地址、电话", "Value": "", "Polygon": null}, {"Name": "购买方开户行及账号", "Value": "", "Polygon": null}, {"Name": "打印发票代码", "Value": "", "Polygon": null}, {"Name": "打印发票号码", "Value": "", "Polygon": null}, {"Name": "备注", "Value": "", "Polygon": null}, {"Name": "联次", "Value": "", "Polygon": null}, {"Name": "是否代开", "Value": "", "Polygon": null}, {"Name": "市", "Value": "", "Polygon": null}, {"Name": "服务类型", "Value": "", "Polygon": null}, {"Name": "通行费标志", "Value": "", "Polygon": null}, {"Name": "车船税", "Value": "", "Polygon": null}, {"Name": "车牌号", "Value": "", "Polygon": null}, {"Name": "类型", "Value": "", "Polygon": null}, {"Name": "通行日期起", "Value": "", "Polygon": null}, {"Name": "通行日期止", "Value": "", "Polygon": null}], "Items": [{"LineNo": "1", "Name": "客运服务费", "Spec": "无", "Unit": "次", "Quantity": "1", "UnitPrice": "87.28", "AmountWithoutTax": "87.28", "TaxRate": "3%", "TaxAmount": "2.62", "TaxClassifyCode": null}], "PdfPageSize": 0, "Angle": 0.06033841148018837, "RequestId": "5c647af9-e441-4622-85c9-6cbbaf36e50d"}'
    api_res_json = json.loads(str(api_res))
    VatInvoiceInfos = api_res_json['VatInvoiceInfos']
    dict_pandas = {}
    for VatInvoiceInfo in simple_progress(VatInvoiceInfos):
        dict_pandas[VatInvoiceInfo['Name']] = VatInvoiceInfo['Value']
    Items = api_res_json['Items']
    res_df = []
    for Item in Items:
        dict_pandas.update(Item)
        res_df.append(pd.DataFrame(dict_pandas, index=[0]))
    res_excel = res_df[0]
    for index, line_df in enumerate(res_df):
        if index == 0:
            continue
        res_excel = res_excel._append(line_df)
    pd.DataFrame(res_excel).to_excel(str(abs_output_excel))


def TrainTicketOCR2Excel(input_path: str, output_excel: str = r'./TrainTicketOCR2Excel.xlsx', img_url: str = None,
                         configPath: str = None) -> None:
    ticket_list = []
    ticket_files = get_files(input_path)
    for ticket in simple_progress(ticket_files):
        ticket_info = poocr.ocr.TrainTicketOCR(img_path=ticket, img_url=img_url, configPath=configPath)
        ticket_list.append(ticket_info)
    ticket_df = pd.DataFrame(ticket_list)
    ticket_df.to_excel(output_excel, index=None)
