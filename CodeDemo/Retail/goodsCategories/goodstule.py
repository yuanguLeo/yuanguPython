#!/usr/bin/env python
#_*_coding:utf-8_*_


import requests
import re
import unittest
from Retail.goodsCategories.login import Login

class GoodsTule(object):

	#进入添加售卖键界面，获取ruleNum值
	addurl = "http://retail.yinghezhong.com/goods/sellKey/add"
	ruleNum = None

	def goods_tule_add(self,addurl):
		tule = requests.get(addurl,cookies=Login.cookie)
		return tule.text
		print(type(tule.text))
		ruleNum = tule.text

	#ruleNum = re.findall(r"ruleNum=(.+?)&",ruleNum)

	print(ruleNum)

	data = {
        "channelType":2,
        "cinemaCode":7010,
        "cinemaNum":10000094,
        "counterPriceType":1,
        "goodsCounterPrice":15,
        "goodsId":74383,
        "goodsIsCardDiscount":1,
        "ruleDesc":"售卖键-01",
        "ruleName":"售卖键-01",
        "ruleNum":ruleNum,
        "sellGroupIds":"",
        "sellGroupIds2":1004,
        "sellTimeType":1,
        "userDefinedPriceFlag":0,
	}

	#保存售卖键信息
	saveSellKeyUrl = r"http://retail.yinghezhong.com/goods/sellKey/saveSellKey"
	def saveSellKey(self,saveSellKeyUrl,data):
		SellKey = requests.post(saveSellKeyUrl,data=data,cookies=Login.cookie)
		print(SellKey.text)



