# -*- coding: UTF-8 -*-
'''
@学习网站      ：www.python-office.com
@读者群     ：http://www.python4office.cn/wechat-group/
@作者  ：B站/抖音/微博/小红书/公众号，都叫：程序员晚枫，微信：CoderWanFeng
@代码日期    ：2024/5/6 20:42 
@本段代码的视频说明     ：
'''
from translate import Translator

translator = Translator(to_lang='zh', from_lang='en')
# typing the message
translation = translator.translate('LineNo')
print(translation)

# -*- coding:utf-8 -*-
import requests

string = str(input("请输入一段要翻译的文字："))
data = {
'doctype': 'json',
'type': 'AUTO',
'i':string
}
url = "http://fanyi.youdao.com/translate"
r = requests.get(url,params=data)
result = r.json()
print(result)
