import poocr
from pdf_invoice_utils import process_pdf_invoice

# 设置腾讯云API密钥
SecretId = ''
SecretKey = ''

# PDF发票识别多页并保存到Exce
process_pdf_invoice(
    pdf_path=r'C:\Users\Lenovo\Desktop\temp\增值税发票-test.pdf',
    output_excel='./晚枫.xlsx',
    id=SecretId,
    key=SecretKey
)



