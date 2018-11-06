#coding:utf-8
import urllib
import ssl
import os
import requests
import ssl
from selenium import webdriver
from bs4 import BeautifulSoup
import AnalyzeHTML,RequestHTML

header = {
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language' : 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding' : 'gzip, deflate',
    }

option = webdriver.ChromeOptions()
option.add_argument("headless")

webdriver.PhantomJS(executable_path='')  # phantomjs的绝对路径
browser = webdriver.Chrome(chrome_options=option)

url = "https://trailers.apple.com/trailers/"

browser.get(url)

soup = BeautifulSoup(browser.page_source, 'html.parser')

e =  soup.select("#trailers .hd")

movieUrlList = []

for x in e:
    f = x.find_all("a")
    list =  []
    for y in f:
        str = "https://trailers.apple.com/"+y['href']
        list.append(str)
    listSet = set(list)

    for d in listSet:
        movieUrlList.append(d)

for url in movieUrlList:
    ssl._create_default_https_context = ssl._create_unverified_context

    print(url)
    # exit()
    r = requests.get(url,headers=header)
    print(r.text)
    exit()


    # print(url)
    # browser.get(url)
    # soup2 = BeautifulSoup(browser.page_source, 'html.parser')
    #
    # print(soup2)
    #
    # btn_more = browser.find_element_by_class_name('link-play')
    #
    # btn_more.click()  # 模拟点击,可以模拟点击加载更多
    #
    # exit()

    # e = soup2.find_all("source")

    print(e)



