#!/usr/bin/env python
#_*_coding:utf-8_*_

from child import Child

def main():
    c = Child(1111,100)
    c.play()
    c.eat()
    #注意：父类中方法名相同，默认调用的是在括号中排前面的父类中的方法
    c.func()

if __name__ == "__main__":
    main()














