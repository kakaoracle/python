#实现的功能
# 多页抓取
#
#
#


# -*- coding:utf-8 -*-
import urllib.request as urllibReq #导入模块并重命名
from bs4 import BeautifulSoup #导入模块中的具体方法,多个方法用,分开

# 要抓取的网址

x = 0


# 获取源码
# 定义一个函数
def crawl():
    for i in range(1000):
        url = 'http://www.dbmeinv.com/?page={}'.format(i)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        req = urllibReq.Request(url, headers=headers)  # 为了反爬虫而写一个请求头
        page = urllibReq.urlopen(req, timeout=20)
        contents = page.read()  # 获取源码,readline方法是获取第一行
        # print(contents)

        soup = BeautifulSoup(contents, 'html.parser')#获取网页标签
        my_girl = soup.find_all("img")
        print("=====url:"+url)
        # 遍历标签中的子标签内容
        for girl in my_girl:
            link = girl.get('src')
            print(link)

            global x
            urllibReq.urlretrieve(link, 'C:/Users/kakao/Desktop/image/%s.jpg' % x)  # 自动下载图片链接
            x += 1
            print("正在下载第%s张" % x)


# 执行方法
crawl()
