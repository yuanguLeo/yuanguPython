#!/usr/bin/env python
#_*_coding:utf-8_*_

#发邮件的库
import smtplib

#邮件文本
from email.mime.text import MIMEText

#SMTP服务器
SMTPServer = "smtp.126.com"

#发邮件的地址
sender = "difree2008@126.com"

#发送者邮箱的密码
passwd = "0123456789a"

#设置发送的内容
message = "leo is a good man"

#转换成邮件文本
msg = MIMEText(message)

#标题
msg["Subject"] = "来自帅哥的问候"

#发送者
msg["From"] = sender

#创建SMTP服务器
mailServer = smtplib.SMTP(SMTPServer,25)

#登录邮箱
mailServer.login(sender,passwd)

#发送邮件
mailServer.sendmail(sender,["difree2008@126.com"],msg.as_string())

#退出邮箱
mailServer.quit()










