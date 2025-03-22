""" 读取文件 """
from aip import AipOcr  # pip install baidu-aip
APP_ID = '45968606'
API_KEY = ''
SECRET_KEY = ''
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

path='C:\\myProject\\test1\\工作使用\\oa验证码.png'
def get_file_content(path):
    with open(path, "rb") as fp:
        return fp.read()


image = get_file_content(path)
# url = "https://www.x.com/sample.jpg"
# pdf_file = get_file_content('文件路径')

# 调用通用文字识别（标准版）
# res_image = client.basicGeneral(image) #普通精度
res_image = client.basicAccurate(image) #高精度
# res_url = client.basicGeneralUrl(url)
# res_pdf = client.basicGeneralPdf(pdf_file)
print(res_image)
# print(res_url)
# print(res_pdf)

# 如果有可选参数
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"
# res_image = client.basicGeneral(image, options) #普通
res_image = client.basicAccurate(image, options) #高精度
# res_url = client.basicGeneralUrl(url, options)
# res_pdf = client.basicGeneralPdf(pdf_file, options)
print(res_image)
# print(res_url)
# print(res_pdf)

