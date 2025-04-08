import os
import poocr
from PyPDF2 import PdfReader, PdfWriter
import pandas as pd

def process_pdf_invoice(pdf_path, output_excel, id=None, key=None):
    """
    将多页PDF发票拆分为单页，分别识别后合并到一个Excel文件
    :param pdf_path: PDF文件路径
    :param output_excel: 输出Excel文件路径
    :param id: 腾讯云API SecretId
    :param key: 腾讯云API SecretKey
    :return: None
    """
    try:
        # 创建临时目录
        temp_dir = os.path.join(os.path.dirname(pdf_path), "temp")
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)

        # 拆分
        pdf = PdfReader(pdf_path)
        temp_excels = []
        for i in range(len(pdf.pages)):
            writer = PdfWriter()
            writer.add_page(pdf.pages[i])
            temp_pdf = os.path.join(temp_dir, f"temp_{i}.pdf")
            temp_excel = os.path.join(temp_dir, f"temp_{i}.xlsx")
            temp_excels.append(temp_excel)

            with open(temp_pdf, 'wb') as f:
                writer.write(f)
            try:
                poocr.ocr2excel.VatInvoiceOCR2Excel(
                    input_path=temp_pdf,
                    output_excel=temp_excel,
                    id=id,
                    key=key
                )
                print(f"第 {i+1} 页处理完成")
            except Exception as e:
                print(f"第 {i+1} 页处理失败: {e}")

        # 合并所有Excel结果
        try:
            valid_excels = [excel for excel in temp_excels if os.path.exists(excel)]
            if valid_excels:
                result_df = pd.read_excel(valid_excels[0])
                for excel in valid_excels[1:]:
                    df = pd.read_excel(excel)
                    result_df = pd.concat([result_df, df], ignore_index=True)
                
                # 保存合并结果
                result_df.to_excel(output_excel, index=False)
            else:
                print("没有成功识别的发票页面，无法生成Excel")
        except Exception as e:
            print(f"合并结果失败: {e}")

        # 清理临时文件
        for file in os.listdir(temp_dir):
            try:
                os.remove(os.path.join(temp_dir, file))
            except:
                pass
            
    except Exception as e:
        print(f"处理失败: {e}") 