#!/usr/bin/env python
# *_* coding:utf-8 *_*
# python learning, keep on!

#字典是无序的，没有下标。不能通过下标来查找
dic={
    'xiaoming':50,
    'zhangsan':35,
    'lisi':38
}

print(dic['xiaoming'])

#删除
del dic['lisi']
print(dic)

dic.pop('zhangsan')
print(dic)

dic.popitem()
print(dic)
dic={
    'xiaoming':50,
    'zhangsan':35,
    'lisi':38
}
#安全的获取key，用get
print(dic.get('lisi'))
#判断是否有某个key
print('lisi' in dic)

print(dic.values())

print(dic.keys())

print(dic.items())

#能查到就不改，如果不存在key就增加
dic.setdefault('lisi',80)
print(dic)

#两个字典合并，有交叉就用最新的。
dic.update({'lisi':11,'nihao':55})

print(dic)

#创建一个新的字典，都赋值同一个值

c=dict.fromkeys([1,2,3,4],'asd')
print(c)

c[1]='hll'
print(c)

#字典的循环
#更高效
for i in c:
    print(i,c[i])

for i,v in c.items():
    print(i,v)


