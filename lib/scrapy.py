#!/usr/bin/env python
# -*-coding:utf-8-*-
import  urllib.request
import logging
from lxml import etree
import os
pciturelist=[]
header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
            , "Connection": "keep-alive"
         }
set = {
    'site':{'home':'http://www.zngirls.com/rank/sum/','url':'http://www.zngirls.com/rank/sum/','xpath':'//div[@class="pagesYY"]/div/a/@href'},
    'lists':{'xpath':'//div[@class="rankli_imgdiv"]/a/@href'},
    'content':{'xpath':'//div[@class="rankli_imgdiv"]/a/@href'}
}
class Scrapy:
       def __init__(self, set , header):
           self.set=set
           self.header=header
           self.list = {}
       def Sites(self):
           request = urllib.request.Request(self.set['site']['url'])
           request.add_header('User-Agent',self.header['User-Agent'])
           request.add_header('Connection', self.header['Connection'])
           html = urllib.request.urlopen(request)
           data = html.read()
           path = etree.HTML(data)
           pages = path.xpath(self.set['site']['xpath'])
           total= len(self.list)
           for (p, v) in enumerate(pages):
               url = self.set['site']['home']+v
               self.list[total+p] = url
       def Lists(self,listUrl):
           request = urllib.request.Request(listUrl)
           request.add_header('User-Agent', self.header['User-Agent'])
           request.add_header('Connection', self.header['Connection'])
           html = urllib.request.urlopen(request)
           data = html.read()
           path = etree.HTML(data)
           pages = path.xpath(self.set['lists']['xpath'])
           total = len(self.list)
           for (p, v) in enumerate(pages):
               url = self.set['site']['home'] + v
               self.list[total + p] = url
       def Contents(self):
           print(333)

sc=Scrapy(set,header)
sc.Sites()
for k,v in sc.list.items():
     sc.Lists(v)


