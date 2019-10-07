# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
html = ""
soup = BeautifulSoup(open('a.html'),'html.parser')
print(soup.prettify)#打印本地文件的内容(格式化)

# html = '<title>1234</title>'
# soup = BeautifulSoup(html,'html.parser')#parser是python官方的一个html解析器
# print(soup.title)
#-------------------字符串格式化----------------------






