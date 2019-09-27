#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/8/21 22:41

a = '''
我叫元古，今年33了，我在北京工作，我想学编程，但是编程太难了，我到现在还没有学会编程，
在学不会，我就要被行业淘汰了，我可能逼着自己努力看尚学堂高琪老师讲的python视频学习
'''

# 长度
print(len(a))

# 以指定字符串开头
print(a.startswith("我叫"))

# 以指定字符串结尾
print(a.endswith("视频学习"))

# 第一次出现指定字符串的位置
print(a.find("北京"))

# 最后一次出现指定字符串的位置
print(a.rfind("编程"))

# 指定字符串出现了几次
print(a.count("编程"))

# 所有字符串全是字母或数字
print(a.isalnum())


# strip()去除字符串首尾指定信息
print("  s x t  ".strip())
print("*s*x*t*".strip("*"))
print("*s*x*t*".lstrip("*"))
print("*s*x*t*".rstrip("*"))


# 大小写转换
b = "yuanguLoe is a good MAN"

# 首字母大写
print(b.capitalize())

# 每个单词都首字母大写
print(b.title())

# 所有字符全转成大写
print(b.upper())

# 所有字符全转成小写
print(b.lower())

# 所有字母大小写转换
print(b.swapcase())


#排版格式 居中：center() 左对齐：ljust()  右对齐：rjust()
c = "SXT"
print(c.center(10))
print(c.center(10,"*"))
print(c.ljust(10,"*"))
print(c.rjust(10,"*"))


# 其他方法
print("其他方法")

# 1、是否为字母或数字
print("sxt100".isalnum())

# 2、检测字符串是否由字母数字组成（含汉字）
print("sxt高老师".isalpha())

# 3、检测字符串是否只由数字组成
print("123456".isdigit())

# 4、检测是否为空白符
print("".isspace())

# 5、是否为大写字母
print("sxtSXT".isupper())

# 6、是否为小写字母
print("sxtSXT".islower())