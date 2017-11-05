#!/usr/bin/env python
# *_* coding:utf-8 *_*
# python learning, keep on!

#可以直接作用于for循环的对象称为可迭代对象，Iterable。可以用isinstance()来判断是否是可迭代的。
#可以用next()函数调用并不断返回下一个值的对象叫做迭代器：Iterator

from collections import Iterable
from collections import Iterator
print(isinstance([],Iterable))
print(isinstance((x for x in range(10)),Iterator))

#可以通过iter()的方法把列表，字典等可迭代对象编程迭代器
a=iter([1,2,3,4])
print(a.__next__())
print(a.__next__())

for x in [1,2,3,4,5]:
    print(x)
#上面这个for完全等价于：
it= iter([1,2,3,5])
while True:
    try:
        print(it.__next__())
    except StopIteration:
        break

