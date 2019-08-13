#!/usr/bin/env python
# -*- coding: utf-8 -*-

from user import User
from card import Card
import random

class ATM(object):

    def __init__(self , allUsers):
        self.allUsers = allUsers

    #开户
    def createUser(self):

        name = input("请输入姓名：")
        idCard = input("请输入身份证号：")
        phone = input("请输入电话号码：")

        prestoreMoney = int(input("请输入预存款金额："))
        if prestoreMoney < 0:
            print("您输入的预存款金额有误，开户失败......")
            return -1
        onePasswd = input("请设置密码：")
        #验证密码
        if not self.checkPasswd(onePasswd):
            print("密码输入错误，开户失败......")
            return -1

        #生成卡号
        cardStr = self.randomCardId()
        card = Card(cardStr,onePasswd,prestoreMoney)

        user = User(name,idCard,phone,card)
        #存到字典
        self.allUsers[cardStr] = user
        print("开户成功，请牢记卡号:(%s)" % (cardStr))


    #查询
    def searchUserInfo(self):
        cardNum = input("请输入您的卡号：")

        #验证卡号是否存在
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！查询失败......")
            return -1

        #验证卡状态
        if user.card.cardLock:
            print ("该卡已被锁定，请解锁后在进行操作......")
            return -1

        #验证密码
        if not self.checkPasswd(user.card.cardPassed):
            print("您输入是密码错误！该卡已被锁定，请解锁后在进行其他操作......")
            user.card.cardLock = True
            return -1

        #卡号密码验证通过后，打印卡号和余额
        print("您的账号为：%s，余额为：%d" %(user.card.cardId,user.card.cardMoney))


    #取款
    def getMoney(self):
        cardNum = input("请输入您的卡号：")

        #验证卡号是否存在
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！取款失败......")
            return -1

        #验证卡状态
        if user.card.cardLock:
            print ("该卡已被锁定，请解锁后在进行操作......")
            return -1

        #验证密码
        if not self.checkPasswd(user.card.cardPassed):
            print("您输入是密码错误！该卡已被锁定，请解锁后在进行其他操作......")
            user.card.cardLock = True
            return -1

        #取款操作
        withdrawals = int(input("请输入您的取款金额："))
        if withdrawals > user.card.cardMoney:
            print ("您输入的取款金额大于卡余额，取款失败......")
            return -1
        else:
            user.card.cardMoney -= withdrawals
            print ("取款成功,余额为：%d" % (user.card.cardMoney))


    #存款
    def saveMoney(self):
        cardNum = input("请输入您的卡号：")

        #验证卡号是否存在
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！存款失败......")
            return -1

        #验证卡状态
        if user.card.cardLock:
            print ("该卡已被锁定，请解锁后在进行操作......")
            return -1

        #验证密码
        if not self.checkPasswd(user.card.cardPassed):
            print("您输入是密码错误！该卡已被锁定，请解锁后在进行其他操作......")
            user.card.cardLock = True
            return -1

        #存款操作
        withdrawals = int(input("请输入您的存款金额："))
        user.card.cardMoney += withdrawals
        print ("存款成功,余额为：%d" % (user.card.cardMoney))

    #转账
    def transferMoney(self):

        transferCardNum = input("请输入您收款人的卡号：")
        #验证卡号是否存在
        user = self.allUsers.get(transferCardNum)
        if not user:
            print("该卡号不存在！转账失败......")
            return -1

        #验证卡状态
        if user.card.cardLock:
            print ("该卡已被锁定，请解锁后在进行操作......")
            return -1

        cardNum = input("请输入付款人卡号：")

        #验证卡号是否存在
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！转账失败......")
            return -1

        #验证卡状态
        if user.card.cardLock:
            print ("该卡已被锁定，请解锁后在进行操作......")
            return -1

        #验证密码
        if not self.checkPasswd(user.card.cardPassed):
            print("您输入是密码错误！该卡已被锁定，请解锁后在进行其他操作......")
            user.card.cardLock = True
            return -1

        #转账操作
        withdrawals = int(input("请输入您的转账金额："))
        if withdrawals > user.card.cardMoney:
            print ("您输入的转账金额大于卡余额，转账失败......")
            return -1
        else:
            user.card.cardMoney -= withdrawals
            print ("转账成功,余额为：%d" % (user.card.cardMoney))



    #锁定
    def lockUser(self):

        cardNum = input("请输入您的卡号：")
        #验证卡号是否存在
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！锁定失败......")
            return -1

        if user.card.cardLock:
            print ("该卡已被锁定，请解锁后在使用功能......")
            return -1

        #验证密码
        if not self.checkPasswd(user.card.cardPassed):
            print("您输入是密码错误！锁定失败......")
            return -1

        tempIdCard = input("请输入您的身份证号码：")
        if tempIdCard != user.idCard:
            print ("身份证输入错误，锁卡失败......")
            return -1

        #锁定卡
        user.card.cardLock = True
        print ("锁卡成功......")


    #解锁
    def unlockUser(self):

        cardNum = input("请输入您的卡号：")
        #验证卡号是否存在
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！解锁失败......")
            return -1

        if not user.card.cardLock:
            print ("该卡没有锁定，无需解锁......")
            return -1

        #验证密码
        if not self.checkPasswd(user.card.cardPassed):
            print("您输入是密码错误！解锁失败......")
            return -1

        tempIdCard = input("请输入您的身份证号码：")
        if tempIdCard != user.idCard:
            print ("身份证输入错误，解锁失败......")
            return -1

        #解锁卡
        user.card.cardLock = False
        print ("解锁成功......")

    #补卡
    def newCard(self):
        pass

    #销户
    def killUser(self):
        pass

    #验证密码
    def checkPasswd(self,realPasswd):
        for i in range(3):
            rempPasswd = input("请输入密码：")
            if rempPasswd == realPasswd:
                return True
        return False

    #随机生成6位数卡号
    def randomCardId(self):

        while True:
            str = ""
            for i in range(6):
                ch = chr(random.randrange(ord('0'),ord('9') + 1))
                str += ch
                #卡号去重
                if not self.allUsers.get(str):
                    return str






