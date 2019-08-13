#!/usr/bin/env python
#_*_coding:utf-8_*_

'''
编写函数，实现功能，给函数两个数，返回这两个数的和
'''


def mySum(num1,num2):
    sum = num1 + num2
    return sum

res = mySum(1,9)
print(res)

'''
值传递：传递的不可变类型
string、tuple、number是不可变的
'''
def funcl(num):
    num = 100

number = 20
funcl(number)
print(number)

'''
引用传递：传递的可变类型
list、dict、set是可变的
'''

def funcl1(li):
    li[0] = 100

list = [1,2,3,4,5,6]
funcl1(list)
print(list)

'''
关键字参数
概念：允许函数调用时参数的顺序与定义时不一致


'''

def myPrint(str,age):
    print(str,age)

myPrint(age=17,str="leo is a good man!")


'''
默认参数
概念：调用函数时，如果没有传递参数，则使用默认参数

'''

def myPrint1(str="leo is a good man!",age=17):
    print(str,age)

myPrint1()
myPrint1("leo is a nice man!",18)

'''
不定长参数
概念：能处理比定义时更多的参数

'''
#加了星号（*）的变量存放所有未命名的变量参数，如果在函数调用时么有指定参数，它就是一个空元组

def func(name,*args):
    print(type((args)))
    print(name)
    for i in args:
        print(i)

func("leo","is","a","good","man")



#**代表键值对参数字典，和*所代表的意义类似
def func2(**kwargs):
    print(type((kwargs)))
    print(kwargs)

func2(x=1,y=2,z=3)

'''
匿名参数
概念：不适用def这样的语句定义函数，适用lambda来创建匿名函数

特点：
1、lambda只是一个表达式，函数体比def简单
2、lambda的主体是一个表达式，而不是代码块，仅仅只能在lambda表达式中封装简单的逻辑
3、lambda函数有自己的命名空间，且不能访问自由参数列表之外的或全局命名空间的参数
4、虽然lambda是一个表达式且看起来只能写一行，与C和C++内联函数不同

格式：
    lambda参数1,参数2，.....参数N：expression

'''

sum = lambda num1,num2:num1+num2
print(sum(1,2))



