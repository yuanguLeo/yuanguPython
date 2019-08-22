#!/usr/bin/env python
# -*- coding: utf-8 -*-
__mtime__ = '2019/8/22'

import io

# format()基本用法
a = "名字是{0}，年龄是：{1}"
b = a.format("元古",33)
print(b)

c = "名字是{name}，年龄是：{age}"
d = c.format(name = "元古", age = 33)
print(d)


# 填充和对齐 ^居中，>右对齐 <左对齐
e = "我是：{0}, 我喜欢：{1:*>10}"
print(e.format("元古", 33))


# 数字的格式化
a1 = "我的存款有：{:.2f}"
a2 = a1.format(2222.2222)
print(a2)


# 可变字符串 is.StringIO
s = "hello sxt"
sio = io.StringIO(s)
print(sio)
print(sio.getvalue())
print(sio.seek(7))
print(sio.write("z"))
print(sio.getvalue())
