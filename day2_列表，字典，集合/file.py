#!/usr/bin/env python
# *_* coding:utf-8 *_*
# python learning, keep on!

file=open('file.txt','r',encoding='utf-8')

#读方法
#print(file.read())
#print(file.readlines())

#for line in file:
   #print(line.strip())

with open('file.txt','r',encoding='utf-8') as f:
    for line in f:
        print(line.strip())
import sys
print(sys.getdefaultencoding())

