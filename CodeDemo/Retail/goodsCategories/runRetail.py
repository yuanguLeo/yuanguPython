#!/usr/bin/env python
#_*_coding:utf-8_*_

from Retail.goodsCategories.login import Login
from Retail.goodsCategories.goodstule import GoodsTule
import time
import unittest


def main():

	#登录yhz
	loginYHZ = Login("27612800","yhz","leying")
	loginYHZ.loginAadmin()
	time.sleep(2)

	#跳转到卖品系统
	loginYHZ.retail()
	time.sleep(2)

	#添加售卖键
	GoodsTule.goods_tule_add()

if __name__ == '__main__':
	main()


