#!/usr/bin/env python
# *_* coding:utf-8 *_*
# python learning, keep on!

#函数内部的变量的作用域为这个函数，如果在函数的内部想改全局变量，就需要在函数内部声明.但是不推荐这么用。
#单数如果全局变量是列表，字典，集合是可以改的。
school='oldboy'
names=['lisi','wangwu']
def test():
    global school
    school='mage'
    names[0]='zhangsan'
    print(names)
test()
print(names)

test()
print(school)

#递归函数,在函数内部可以调用其它函数，但是如果它调用的是自己，就是递归函数。
#1、 必须有一个明确的结束条件
#2、

def calc(n):
    print(n)
    return calc(int(n/2))
    if n==1:
        return 0

calc(10)
