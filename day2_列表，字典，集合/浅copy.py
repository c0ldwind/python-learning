#!/usr/bin/env python
# *_* coding:utf-8 *_*
# python learning, keep on!

import copy

person=['name',['saving',1000]]
#浅copy实现的四种方式,用于联合账号。。
p1=person[:]
p2=person.copy()
p3=copy.copy(person)
p4=list(person)

p1[0]='lisi'
p2[0]='wangwu'
p3[0]='laoda'
p4[0]='laoer'

p1[1][1]=950

print(p1)
print(p2)
print(p3)
print(p4)