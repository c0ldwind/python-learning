#!/usr/bin/env python
# *_* coding:utf-8 *_*
# python learning, keep on!

#所有的内置方法：
print(abs(-1))                  #取绝对值
print(all([0,1,3,-1]))          #判断可迭代对象里是否有0，如果有就返回false，否则返回真，空的话也返回真。有一个假就返回假。
print(any([0,1,3,-1]))          #判断可迭代对象里是否有一个是真就返回真，空的话为False。只要有一个为真返回真。
print([ascii([1,2,'你好'])])    #把一个对象变成一个可打印的字符串
print(bin(0xa))                  #转成二进制
print(bool(['a']))              #返回一个布尔值。
print(bytearray('asdf'.encode()))#是一个可修改的二进制类型。
print(bytes('asdf'.encode()))   #转成字节类型。
print(callable(abs))            #是否是可调用的，可以加()的就是可调用的，函数，类。
print(chr(98))                  #把数字返回字符
print(ord('a'))                 #把字符转为ascii码
print(dir({}))                  #查看对象的方法
print(divmod(5,1))              #除法，返回整数和余数。
print(eval('1+2'))              #数学运算
exec('for x in range(2):print(x)')#执行代码
#过滤出结果，安装第一个参数的条件，过滤第二个结果。
res=filter(lambda  n:n>5,range(10))
for i in res:
    print(i)
#把后一个参数的结果带入到第一个参数中处理。
res=map(lambda  n:n*2,range(10))
for i in res:
    print(i)

import functools
res= functools.reduce(lambda x,y:x+y,range(10))
print(res)

print(float(1))                 #返回浮点数

a=frozenset([1,2,34])           #变成不可变的集合
print(globals())                #返回整个程序的所有变量，值得键值对。
print(hex(12))                  #转成十六进制。
print(oct(8))                   #转成八进制
print(bin(8))                   #转成二进制
print(int(0xab))
print(pow(2,3))                 #返回多少次方
print(round(1.323,3))              #返回第二个参数指定的精度
print(sorted({6:2,5:8,13:25}.items()))      #按键值进行排序,返回一个列表。
for i in zip([1,2,3,4],['a','b','c','d']):
    print(i)
