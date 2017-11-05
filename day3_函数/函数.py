#!/usr/bin/env python
# *_* coding:utf-8 *_*
# python learning, keep on!

#1、函数的定义,没有return语句的话返回值为None
def test():
    print('fuction1')
    return 1,2,34,(2,3,4)#返回一个元组
print(test())

#2、参数分为，位置参数，关键字参数，默认参数，位置参数组，关键字参数组，其中，位置参数组转为元组，关键字参数转为字典

def test2(x,y,z):#形参
    print(x)
    print(y)
    print(z)
test2(1,z=2,y=3)#其中关键字参数只能写在位置参数后面，实参。

def test3(x,y=3):
    print(x)
    print(y)
test3(1)

#位置参数组,放在最后
def test4(x,y=3,*args):
    print('fuction4')
    print(x)
    print(y)
    print(args)
test4(1,5,6,7,8)

def test5(x,y=3,*args,**kwargs):
    print('fuction5')
    print(x)
    print(y)
    print(args)
    print(kwargs)
test5(1,2,3,4,5,name=3,age=5,sex='f')

#匿名函数：

calc = lambda n : print(n+2)
calc(5)

