#!/usr/bin/env python
#_*_coding:utf-8_*_


import  os

'''
os:包含了普通的操作系统的功能


'''
#获取操作系统类型  nt-windows  posix-Linux
print(os.name)

#获取操作系统中的环境变量
print(os.environ)

#获取指定的环境变量
print(os.environ.get("ALLUSERSPROFILE"))

#获取当前目录
print(os.curdir)

#获取当前工作目录，即当前python脚本所在的目录
print(os.getcwd())

#以列表的形式返回指定目录下的所有的文件
print(os.listdir(r"D:\Python\QFEDU\Day08"))

#在当前目录下创建新目录
#os.mkdir(r"D:\Python\QFEDU\Day08\DI")
#os.mkdir("dige")

#删除目录
#os.rmdir("dige")

#获取文件属性
#print(os.stat("DI"))

#重命名
#os.rename("DI","DiGe")

#删除普通文件
#os.remove("func1.txt")

#运行shell命令
#os.system("notepad") #记事本
#os.system("write")  #画图
#os.system("mspaint")
#os.system("mscongif")
#os.system("shutdown -s -t 500")   #关机
#os.system("shutdown -a")  #注销被取消
#os.system("taskkill /f /im notepad.exe")  #关闭记事本

#有些方法在os模块里，还有些存在os.path里
#查看当前的绝对路径

print(os.path.abspath("."))


#路径的拼接
p1 = r"D:\Python\QFEDU\Day08"
p2 = "DiGe"
#注意：参数2中开始不要有斜杠
print(os.path.join(p1,p2))

#拆分路径
path2 = r"D:\Python\QFEDU\Day08"
print(os.path.split(path2))

#获取扩展名
print(os.path.splitext(path2))

#判断是否是目录
print(os.path.isabs(path2))

#判断文件是否存在
path3 = r"D:\Python\QFEDU\Day08\DiGe\DiGe.txt"
print(os.path.isfile(path3))

#判断目录是否存在
path4 = r"D:\Python\QFEDU\Day08\DiGe\DiGe.txt"
print(os.path.exists(path4))

#获取文件大小（字节）
print(os.path.getsize(path4))

#文件的目录
print(os.path.dirname(path3))
print(os.path.basename(path3))
