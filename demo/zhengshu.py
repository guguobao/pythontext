#!oding:utf-8
# coding=utf-8
#网页有易到难
#直接在网页数据中拿数据
#异步请求获取数据
#json加密
import urllib,urllib2
from json import loads
import cookielib
c = cookielib.LWPCookieJar()
cookie = urllib2.HTTPCookieProcessor(c)
opener = urllib2.build_opener(cookie)
urllib2.install_opener(opener)

headers={
    'Referer':'http://cx.cnca.cn/rjwcx/web/cert/publicCert.do?progId=10&title=%E8%AE%A4%E8%AF%81%E7%BB%93%E6%9E%9C%0A%09%20%20%20%20%20%20%20%20',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3141.7 Safari/537.36',
   # 'Cookie':'Hm_lvt_1ab04bcaf4dd6e15edf78188f2d6a32c=1507162749; Hm_lpvt_1ab04bcaf4dd6e15edf78188f2d6a32c=1507163718; JSESSIONID=0000se6UVxO22pmLT_4zl_KIWbQ:-1'
}

def getList():
    url='http://cx.cnca.cn/rjwcx/web/cert/queryOrg.do?progId=10'
    req=urllib2.Request(url)
    req.headers=headers
    code=input(u"请输入验证码：")
    company='广东生益科技股份有限公司'#input(u"请输入公司名:")
    data={
    'certNumber':'',
    'orgName':company,
    'queryType':'public',
    'checkCode':code
}
    data = urllib.urlencode(data)#data原来是str类型的，用urlopen要装换格式
    html=opener.open(req,data=data).read()
    result = loads(html)
    #print(result['data'])
    return result['data'],code,company
#那验证码图片
def getCode():
    url2='http://cx.cnca.cn/rjwcx/checkCode/rand.do?d=1507178665850'
    with open(u'code.png','wb') as fd:
        fd.write(opener.open(url2,'code.png').read())
    # urllib.urlretrieve(url2,'code.png')
#获取证书的
def getPage(html):
    # print('+'*100)
    url4='http://cx.cnca.cn/rjwcx/web/cert/showZyxGy.do?rzjgId={}&certNo={}&checkC={}'.format(html['rzjgId'],html['certNumber'],html['checkC'])
    print(url4)
    req=urllib2.Request(url4)
    req.headers=headers
    result=opener.open(req).read()
    print(result)
def getCer(List,code,company):
    url3='http://cx.cnca.cn/rjwcx/web/cert/list.do?progId=10'
    count=len(List)
    print(u"总共有%d",count)
    for list in List:
        #print(list['orgName']+list['orgCode']+list['checkC']+list['randomCheckCode'])
        data={
            'orgName':list['orgName'].encode('utf-8'),
            'orgCode':list['orgCode'],
            'method':'queryCertByOrg',
            'needCheck':'false',
            'checkC':list['checkC'],
            'randomCheckCode':list['randomCheckCode'],
            'queryType':'public',
            'page':'1',
            'rows':'10',
            'checkCode':code
        }
        #print(data)
        data = urllib.urlencode(data)#data要是str类型的，而不是字典
        #print(type(data))#装换后为str
        headers={
            'Referer':'http://cx.cnca.cn/rjwcx/web/cert/index.do?url=web/cert/show.do%3FrzjgId=CNCA-RF-2003-27%26certNo=1235-1998-AE-RGC-RVA%26checkC=639033097',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3141.7 Safari/537.36Query String Parametersview sourceview URL encoded'
        }
        req=urllib2.Request(url3)
        req.headers=headers
        html1=opener.open(req,data=data).read()
        print(loads(html1)['rows'])
        print(u"分支有",len(loads(html1)['rows']))
        for html in loads(html1)['rows']:
            print('*'*100)
            print(u'%s %s %s'%(html['rzjgId'],html['certNumber'],html['checkC']))
            #第三层数据爬取
            getPage(html)

getCode()
result_list,code,company =getList()
getCer(result_list,code,company)