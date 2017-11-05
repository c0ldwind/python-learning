#!/usr/bin/env python
# *_* coding:utf-8 *_*
# python learning, keep on!

# import json#json只能序列化简单的数据类型，json是不同程序之间进行数据交换。如果要进行函数，类等复杂数据类型的序列化用pickle
# info={
#     'age':22,
#     'name':'alex'
# }
#
# file=open('test.txt','w')
# file.write(json.dumps(info))

import pickle
def printname(name):
    print('my name is ',name)

dict={
    'name':'alex',
    'age':22,
    'info':printname
}


f=open('test.txt','wb')
f.write(pickle.dumps(dict)) #等同于pickle.dump(dict,f)