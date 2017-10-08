#coding:utf-8
import re
import requests
import urllib2,urllib
from lxml import etree
from bs4 import BeautifulSoup
import os

headers={
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
def getser():
    #raw_input代表字符串输入，
    str=raw_input("输入你想查询的模块：")
    print(str)
    url='https://pypi.python.org/pypi?%3Aaction=search&term={}&submit=search'.format(str)
    print url
    req=urllib2.Request(url)
    req.headers=headers
    html=urllib2.urlopen(req).read()
    #用xpath
    html2=etree.HTML(html)
    #trs=[]
    trs=html2.xpath(".//*[@id='content']/div[3]/table/tbody/tr[3]")
    #用bs4

    soup = BeautifulSoup(html,'lxml',from_encoding='utf-8')
    html3=soup.find_all("table",class_="list")
    #html3还是soup对象
    trs=html3[0].select('a[href]')
    allstr=[]
    #print(html3)
    allhref=[]
    for (tr,i) in zip(trs,range(len(trs))):
        print i
        # s=str(i)
        # print(s)
        allstr.append(" : "+tr.string)
        href="https://pypi.python.org"+tr['href']
        allhref.append(href)
        print(allstr[i])
    for href in allhref:
        print(href)
    num=input("输入 你想下载的模块的序号：")
    return allhref[num],allstr[num]

def getdownload(href):
    res=urllib2.Request(href,headers=headers)
    html=urllib2.urlopen(res).read()
    #print(html)
    soup = BeautifulSoup(html,'lxml',from_encoding='utf-8')
    dhref= soup.find_all('a',class_="odd")
    #print(dhref)
    ddhref= dhref[0]['href']
    print(ddhref)
    return ddhref
def savefile(href,file):
    path='D:\安装包\python 模块'
    #用find函数
    a=href.find('/',len(href)-40,len(href))
    print(a)
    file=href[a+1:len(href)]
    #用正则从url中拿file名字
    # file=re.findall(r'/.*?tar.gz',href)
    # pattern=re.compile(r'/(.*)tar.gz')
    # file=re.match(pattern,href)
    dest_dir=os.path.join(path,file)
    try:
        urllib.urlretrieve(href,dest_dir)
    except:
        print '\tError retrieving the URL:', dest_dir
    # with open(u'1.tar.gz', "wb") as fd:
    #      fd.write(urllib.urlretrieve(href))
href,strname=getser()
dhref=getdownload(href)
savefile(dhref,strname)

