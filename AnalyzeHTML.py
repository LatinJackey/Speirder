#coding:utf-8
from bs4 import BeautifulSoup
import re

class AnalyzeHTML (object):
    def __init__(self):
        self.analyzeMathod = "lxml"

    def Analyze(self,html,selector):

        # print(html)

        soup = BeautifulSoup(html,self.analyzeMathod)

        return soup.find_all(src=re.compile(r"%s" %selector))

