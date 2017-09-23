

import requests
import re

#东莞理工学院登陆窗口模拟登陆


if __name__=='__main__':
    user=input("请输入学号：")
    password=input("请输入密码：")
    data={
        'DDDDD':user,
        'upass':password,
        '0MKKey':'(unable to decode value)'
    }
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3141.7 Safari/537.36',
        'Referer':'http://192.168.252.254/0.htm'

    }
    req=requests.post('http://192.168.252.254/0.htm',data=data,headers=headers)
    #print(req.text)`
    re=re.findall(r'<title>(.*)</title>',req.text)
    print(re)


