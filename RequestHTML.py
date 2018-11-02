#coding:utf-8
from bs4 import BeautifulSoup
import requests,ssl,urllib


# proxy = {
# "http":"",
# "http":"",
# "http":"",
# "http":"",
# "http":"",
# "http":"",
#          }

class LJNetWorker(object):

    #初始化
    def __init__(self):
        self.header = self.header = {
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language' : 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding' : 'gzip, deflate',
    }
        ssl._create_default_https_context = ssl._create_unverified_context

    #请求网站
    def HTMLRequester(self,url):

        r = requests.get(url,headers=self.header)

        if r.status_code == 200 and r.text:
            return {"isSuccess":True , "value":r.text}
        elif r.status_code == 200 and not r.text:
            return {"isSuccess":False , "value":""}
        else:
            return {"isSuccess": False, "value": ""}

    #下载器
    def DownLoader(self,url,path):

        downer = urllib.request.urlretrieve(url,path)

        print(path+"下载完毕")
