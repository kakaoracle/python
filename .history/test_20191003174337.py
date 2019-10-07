# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
html = '<title>1234</title>'
soup = BeautifulSoup(html,'html.parser')
print(soup.title)


