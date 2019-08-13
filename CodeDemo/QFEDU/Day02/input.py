#!/usr/bin/env python
#_*_coding:utf-8_*_

import math #数学方法
import random #随机数
#测试input  作用：从外部获取变量的值


#age = input("请输入一个数字：")
#print("age =",age)

#返回数字的绝对值
a1 = -10
print(abs(a1))

#返回给定数值中的最大值
a1 = (1,2,3,4,5,6,7,8,9,0)
print("最大值为：",max(a1))
print("最小值为：",min(a1))

#求X的N次方
print("2的5次方等于：",pow(2,5))

#round(x[.n]) 返回浮点数x的四舍五入值，如果给出n值，则代表舍入到小数点后n位
print(round(3.4))
print(round(3.456,2))

#向上取整
print("向上取整数值为：",math.ceil(18.1))

#向下取整
print("向下取整数值为：",math.floor(18.9))

#返回整数部分与小数部分
print(math.modf(22.3))

#开方
print(math.sqrt(16))

#随机数  格式：random.choice([])
print(random.choice([1,23,4,56,79]))
print(random.choice(range(5)))
print(random.choice("sunck"))

#产生一个1-100之间个随机数
r1 = random.choice(range(100))+1
print(r1)

'''
从指定范围内，按指定的基数递增的集合中选取一个随机数
格式：random.randrange([start,],stop[,step])
start--指定范围的开始值，包含在范围内，默认是0
stop--指定范围的结束值，不包含在范围内
step--指定的递增基数，又称步长，默认是1
'''
print(random.randrange(1,100,2))

#生成[0-1)之间的随机数
print(random.random())


list = [1,2,3,4,5]
random.shuffle(list)  #将序列的所有元素随机排序
print(list)


#随机生成一个实数
print(random.uniform(3,9))

'''
表达式：由变量、常量和运算符组成的式子称为：表达式
阅读表达式：
    1、功能：
    2、值：

'''

'''
算术运算符和算术运算表达式
算术运算符
+   -   *   /    %     **    //
加  减  乘  除   取模   求幂  取整

'''