# 博客园登录
import time
import os
from selenium import webdriver
#环境配置
browser = webdriver.Chrome('/Users/kaka/Downloads/chromedriver')
#打开登录页面
browser.get("https://cloud.kingdee.com/passport/#/auth/oauth2/third_login?state=583116043385479168&display=web&scope=basic&response_type=code&force_login=1&client_id=206059&redirect_uri=https%3A%2F%2Fdev.kingdee.com%2Fkd%2Fecos%2Fuser%2FloginCheck")
time.sleep(1)
username = "xxx"
password = "xxx"

# id/name/class/tag/link/partial_link/xpath/绝对路径定位
acc_input = browser.find_element_by_xpath("//*[@id='tellName']")
acc_input.send_keys(username)
acc_input = browser.find_element_by_xpath("//*[@id='cloudInput']/div[2]/input")
acc_input.send_keys(username)
# 勾选我同意
browser.find_element_by_xpath("//*[@id='app']/div/div[1]/div[1]/div/div/div[1]/div/div[3]/div/i").click()
time.sleep(1)
# login btn
browser.find_element_by_xpath("//*[@id='app']/div/div[1]/div[1]/div/div/div[1]/div/div[5]/button/span").click()
time.sleep(2)
# 接受cookie

browser.find_element_by_xpath("//*[@id='app']/div/div[1]/div[1]/div/div/div[3]/div/div[3]/button/span").click()