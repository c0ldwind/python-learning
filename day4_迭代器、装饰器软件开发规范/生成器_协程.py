#!/usr/bin/env python
# *_* coding:utf-8 *_*
# python learning, keep on!


#生成器可以用来做单线程下的并发，叫做协程，ngix就是利用这个技术，使得单线程下的承载量比多线程还多好多倍。

import time
def consumer(name):
    print('%s 准备吃包子了' % name)

    while True:
        baozi=yield
        print('%s 被 %s 吃了'%(baozi,name))
        time.sleep(1)

def producer(name):
    a=consumer('A')
    b=consumer('B')
    a.__next__()
    b.__next__()
    print('%s开始生产包子了'%name)
    n=0

    while n<10:
        print('%s生产第%s个包子'%(name,n))
        time.sleep(1)
        a.send('肉馅')
        b.send('菜馅')
        n=n+1
producer('alex')
