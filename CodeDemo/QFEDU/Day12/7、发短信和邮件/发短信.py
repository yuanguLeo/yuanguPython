#!/usr/bin/env python
#_*_coding:utf-8_*_

import http.client
import urllib

host = "106.ihuyi.com"
sms_send_uri = "/webservice/sms.php?method=Submit"

#用户名是登录用户中心->验证码短信->产品总览->APIID
account = "C58023834"
#密码 查看密码请登录用户中心->验证码短信->产品总览->APIKEY
password = "32dc4c13668beeb673ba91202d61405d"

def send_sms(text,moblie):
    params = urllib.parse.urlencode(
        {'account':account,'password':password,'content':text,'mobile':mobile,'foemat':'json'}
    )
    headers = {"Content-type":"application/x-www-from-urlencoded","Accept":"text/plain"}
    conn = http.client.HTTPConnection(host,port=80,timeout=30)
    conn.request("POST",sms_send_uri,params,headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str

if __name__ == '__main__':
    mobile = '13810460796'
    text = "您的验证码是：121254。请不要把验证码泄露给其他人。"

    print(send_sms(text,mobile))









