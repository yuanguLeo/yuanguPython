#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

class Admin(object):

    #设置用户名密码
    userAdmin = "1"
    password  = "1"

    #打印登录界面
    def printAdminView(self):
        print("***********************************************")
        print("************                   ****************")
        print("*********** 欢迎进入迪哥银行系统 ****************")
        print("************                   ****************")
        print("***********************************************")

    #打印功能界面
    def printSysView(self):
        print("***********************************************")
        print("                                               ")
        print("    开户（1）                     查询（2）     ")
        print("    取款（3）                     存款（4）     ")
        print("    转账（5）                     改密（6）     ")
        print("    锁定（7）                     解锁（8）     ")
        print("    补卡（9）                     销户（0）     ")
        print("                   退出（q）                    ")
        print("                                               ")
        print("***********************************************")

    #判断用户名密码
    def adminOption(self):
        admin = input("请输入用户名: ")
        if self.userAdmin != admin:
            print("您输入的用户名不正确！")
            return -1

        passwd = input("请输入密 码: ")
        if self.password != passwd:
            print("您输入的密码不正确！")
            return -1

        print("操作成功，请稍后。。。。")
        time.sleep(2)
        return 0
























