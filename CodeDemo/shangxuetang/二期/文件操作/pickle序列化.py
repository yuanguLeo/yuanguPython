#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/14 8:49

'''
序列化：
'''

import pickle  # 引入序列化模块

#将对象序列化到文件中
with open(r"b.txt","wb") as f:
    a1 = "元古"
    a2 = 234
    a3 = [10,20,30]

    pickle.dump(a1,f)
    pickle.dump(a2,f)
    pickle.dump(a3,f)

#将获得的数据反序列化成对象
with open(r"b.txt","rb") as f:
    b1 = pickle.load(f)
    b2 = pickle.load(f)
    b3 = pickle.load(f)

    print("反序列化结果为：",b1)
    print("反序列化结果为：",b2)
    print("反序列化结果为：",b3)
