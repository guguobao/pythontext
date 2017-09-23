import requests
import xlwt
import time
import urllib.parse
import sys
#写入execl
from datetime import datetime


def getJoblist(page):
    #data的数据是网页XHM的fomt表单post上去
    data={
        'first': 'true',
        'pn': page,
        'kd': 'python' }
    #%E5%8C%97%E4%BA%AC是北京的URLEncode（偏码），用URLdecode（解码）
    res=requests.post(
            'https://www.lagou.com/jobs/positionAjax.j'
            'son?city={0}&needAddtiona'
            'lResult=false&isSchoolJob=0'.format(utf,0),data=data,headers=headers)
   # print(res.text)
    print('*'*20)
    #res是一个对象
    print(dir(res))#dir显示对象类的方法
    print('*'*20)
    result=res.json()#result变成字典，json格式输出json(key:value)
    print(result)
    print('*'*20)
    #键值中还有键值
    jobs=result['content']['positionResult']['result']#取对应键值
    return jobs

#Workbook在当前目录下建立一个xls文档和对象（path）path文件创建路径
wb = xlwt.Workbook()
#有了wb对象就可以添加表单（sheet）ws是操作sheet的对象
ws = wb.add_sheet('ATestSheet',cell_overwrite_ok=True)
#创建一个表，表的名字，是否覆盖
#sheet.write(job)


if __name__=="__main__":
    word=input("请输入拉勾网职业：")
    city=input("请输入城市")
    utf=urllib.parse.quote(city)
    print(utf)

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/61.0.3141.7 Safari/537.36',
        #代表电脑和浏览器一些信息
        'Referer':'https://www.lagou.com/jobs/list_{0}?labelWords=&fromSearch=true&suginput='.format(word,0),
        #Referer是代表请求是从那一个页面点击进入当前页面
        'Cookie':'JSESSIONID=ABAAABAAADEAAFID589F81DDA4B135EA73D59382D94193B; _gat=1; user_trace_token=20170918201032-5e70e65e-9c6a-11e7-9196-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGUID=20170918201032-5e70e916-9c6a-11e7-9196-5254005c3644; index_location_city=%E5%8C%97%E4%BA%AC; TG-TRACK-CODE=index_search; _gid=GA1.2.1042499452.1505736518; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1505736518; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1505736559; _ga=GA1.2.2038003268.1505736518; LGSID=20170918201032-5e70e7a7-9c6a-11e7-9196-5254005c3644; LGRID=20170918201112-76a14753-9c6a-11e7-9196-5254005c3644; SEARCH_ID=23d97ca16048467a93241983f07b9f32'
    }
    n=1
    for page in range(1,10):
      #  print(page)
        jobs=getJoblist(page)
      #拿到字典就写进xls中
        for job in jobs:
            print(job['companyFullName'])
            ws.write(n,0,job['companyShortName'])
            ws.write(n,1,job['createTime'])
            ws.write(n,2,job['positionAdvantage'])
            ws.write(n,3,job['salary'])
            ws.write(n,4,job['workYear'])
            ws.write(n,5,job['education'])
            ws.write(n,6,job['city'])
            ws.write(n,7,job['companyLogo'])
            ws.write(n,8,job['industryField'])
            ws.write(n,9,job['companySize'])
            ws.write(n,10,job['positionLables'])

            n+=1
        time.sleep(1)
#保存用文件对象
wb.save('ATestSheet.xls')