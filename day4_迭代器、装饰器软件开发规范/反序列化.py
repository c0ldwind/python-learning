#!/usr/bin/env python
# *_* coding:utf-8 *_*
# python learning, keep on!

# import json
# file=open('test.txt','r')
# data=json.loads(file.read())
#
# print(data['name'])

import pickle
def printname(name):
    print('nihao ',name)
f=open('test.txt','rb')
#data=pickle.loads(f.read())等同于下面一句话。
data=pickle.load(f)

data['info']('alex')