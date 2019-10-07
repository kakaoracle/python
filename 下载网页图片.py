# -*- coding:utf-8 -*-
import urllib.request as urllibReq
from bs4 import BeautifulSoup

# 要抓取的网址
url = 'http://www.dbmeinv.com/?pager_offset=1'
x = 0


# 获取源码
# 定义一个函数
def crawl(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
    req = urllibReq.Request(url, headers=headers)  # 为了反爬虫而写一个请求头
    page = urllibReq.urlopen(req, timeout=20)
    contents = page.read()  # 获取源码,readline方法是获取第一行
    # print(contents)

    soup = BeautifulSoup(contents, 'html.parser')
    my_girl = soup.find_all("img")
    # 遍历标签中的子标签内容
    for girl in my_girl:
        link = girl.get('src')
        print(link)

        global x
        urllibReq.urlretrieve(link, 'C:/Users/kakao/Desktop/image/%s.jpg' % x)  # 自动下载图片链接
        x += 1
        print("正在下载第%s张" % x)


# 执行方法
crawl(url)
