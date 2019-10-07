# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
html = ""
soup = BeautifulSoup(open('a.html'),'html.parser')
print(soup.prettify)

# html = '<title>1234</title>'
# soup = BeautifulSoup(html,'html.parser')
# print(soup.title)


