#!/usr/bin/env python
# *_* coding:utf-8 *_*
# python learning, keep on!

set1 = set([1,3,5,6,7])
set2 = set([2,5,6,8,9])

#求交集
print(set1.intersection(set2))
print(set1 & set2)

#求并集
print(set1.union(set2))
print(set1 | set2)

#求差集
print(set1.difference(set2))
print(set1 - set2)

#子集，父集
print(set1.issubset(set2))
print(set1.issuperset(set2))
print(set1 <= set2)
print(set1 >= set2)

#求对称差集，去掉交集的其他部分
print(set1.symmetric_difference(set2))
print(set1 ^ set2)

#增加
set1.add(10)
print(set1)

set1.update([11,23])
print(set1)

#删除
set1.remove(23)
print(set1)
set1.pop()
print(set1)
set1.discard(10)
print(set1)

#求长度
print(len(set1))

#测试是否是成员
print(3 in set1)
print(3 not in set1)