#!/usr/bin/env python
#_*_coding:utf-8_*_

#系统客户端
import win32com.client

dehua = win32com.client.Dispatch("SAPI_SPVOICE")
dehua.Speak("leo is a good man")