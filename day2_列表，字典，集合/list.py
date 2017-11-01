#!/usr/bin/env python
# *_* coding:utf-8 *_*
# python learning, keep on!

data=['0','1','2','3','4','5','6','7','8']
print(data)
print(data[1])
print(data[2:5])
print(data[1:7:2])
print(data[5:])
print(data[-1])
print(data[-2:])
print(data[:3])

data.append('9')
print(data)

data.insert(2,'1.5')#插入
print(data)

data[2]='2.8'
print(data)

del data[2]#删除
print(data)

data.remove('9')#删除
print(data)

data.pop()
print(data)#删除最后一个

data.pop(5)#删除指定下标的元素
print(data)

#找出一个值得位置
print(data.index('3'))

print(data.count('3'))#统计一个值由多少个。

data.reverse() #反转
print(data)

data.sort() #排序
print(data)

data2=['11','12']
data.extend(data2)
print(data)

data.clear()#清空
print(data)

del data2 #删除变量
print(data2)

data2=data.copy() #复制列表，浅复制，只复制第一层，如果列表里有列表，则复制的时候只复制里边列表的地址。
print(data2)

#如果要实现深copy，则要引入
import copy

name2=copy.deepcopy(name)

