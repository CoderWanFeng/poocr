import poocr
from pdf_invoice_utils import process_pdf_invoice

# 设置腾讯云API密钥
SecretId = ''
SecretKey = ''

# PDF发票识别多页并保存到Exce
process_pdf_invoice(
    pdf_path=r'F:\\python\\poocr\\merged(1).pdf',
    output_excel='F:\\python\\poocr\\发票识别结果.xlsx',
    id=SecretId,
    key=SecretKey
)

# import poocr
# from PyPDF2 import PdfReader, PdfWriter
# import pandas as pd
# import os
#
# # SecretId = ''
# # SecretKey = ''
# # input_path = r'C:\Users\CHENBOCHEN\PycharmProjects\pythonProject6\merged.pdf'
# # output_excel = r'C:\Users\CHENBOCHEN\PycharmProjects\pythonProject6\发票1.xlsx'
# #
# # pdf = PdfReader(input_path)
# # temp_excels = []
# # for i in range(len(pdf.pages)):
# #     writer = PdfWriter()
# #     writer.add_page(pdf.pages[i])
# #     temp_pdf = f'C:\\Users\\CHENBOCHEN\\PycharmProjects\\pythonProject6\\temp_{i}.pdf'
# #     temp_excel = f'C:\\Users\\CHENBOCHEN\\PycharmProjects\\pythonProject6\\temp_{i}.xlsx'
# #     with open(temp_pdf, 'wb') as f:
# #         writer.write(f)
# #     poocr.ocr2excel.VatInvoiceOCR2Excel(input_path=temp_pdf, output_excel=temp_excel, id=SecretId, key=SecretKey)
# #     temp_excels.append(temp_excel)
# #
# # # 合并所有临时Excel到一个文件
# # dfs = [pd.read_excel(f) for f in temp_excels]
# # pd.concat(dfs, ignore_index=True).to_excel(output_excel, index=False)
# #
# # # 清理临时文件
# # for f in temp_excels + [f.replace('.xlsx', '.pdf') for f in temp_excels]:
# #     os.remove(f)
#
# #
# # # 你的密钥信息
# # SecretId = ''
# # SecretKey = ''
# #
# # # 文件路径
# # input_path = r'C:\Users\CHENBOCHEN\PycharmProjects\pythonProject6\merged.pdf'
# # output_excel = r'C:\Users\CHENBOCHEN\PycharmProjects\pythonProject6\发票.xlsx'
# #
# # # 导入我们的多页处理函数
# # from process_invoices import process_multiple_invoices
# #
# # # 处理所有发票
# # process_multiple_invoices(input_path, output_excel, SecretId, SecretKey)

