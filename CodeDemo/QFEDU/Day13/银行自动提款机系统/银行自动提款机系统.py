#!/usr/bin/env python
# -*- coding: utf-8 -*-

from admin import Admin
from atm import ATM
import time
import os
import pickle

def main():

    #管理员界面对象
    admin = Admin()

    #管理员登录界面
    admin.printAdminView()
    if admin.adminOption():
        return -1

    #提款机
    filepath = os.path.join(os.getcwd(),"alluser.txt")
    f = open(filepath,"rb")
    allUsers = pickle.load(f)
    print (allUsers)
    atm = ATM(allUsers)

    #功能界面
    while True:
        admin.printSysView()
        option = input("请输入您的操作：")
        if option == "1":
            print("开户")
            atm.createUser()
            time.sleep(1)

        elif option == "2":
            print("查询")
            atm.searchUserInfo()
            time.sleep(1)

        elif option == "3":
            print("取款")
            atm.getMoney()
            time.sleep(1)

        elif option == "4":
            print("存款")
            atm.saveMoney()
            time.sleep(1)

        elif option == "5":
            print("转账")
            atm.transferMoney()
            time.sleep(1)

        elif option == "6":
            print("改密")

        elif option == "7":
            print("锁卡")
            atm.lockUser()
            time.sleep(1)

        elif option == "8":
            print("解锁")
            atm.unlockUser()
            time.sleep(1)

        elif option == "9":
            print("补卡")

        elif option == "0":
            print("销户")

        elif option == "q":
            if not admin.adminOption():
                f = open(filepath , "wb")
                pickle.dump(atm.allUsers , f)
                f.close
                return -1

    time.sleep(2)

if __name__ == '__main__':
    main()














