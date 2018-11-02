#coding:utf-8
import urllib
import ssl
import os

import AnalyzeHTML,RequestHTML

# url = "http://movietrailers.apple.com/movies/independent/what-they-had/what-they-had-clip-4_i320.m4v#t=10.730365"


url = "http://movietrailers.apple.com/movies/fox/spies-in-disguise/spies-in-disguise-trailer-1_i320.m4v"

#苹果电影网站
# url = "https://trailers.apple.com/"

netWorker = RequestHTML.LJNetWorker()

if __name__ == "__main__":

    # response = netWorker.HTMLRequester(url)

    # print(response)

    netWorker.DownLoader(url=url,path="2.mp4")
