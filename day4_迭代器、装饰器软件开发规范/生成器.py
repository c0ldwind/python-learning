#!/usr/bin/env python
# *_* coding:utf-8 *_*
# python learning, keep on!

#列表生成式,
#[m for m in range(100)]
#print('1')
#生成器,好处是节省空间。用不到的元素不存到内存。
#把列表生成式的中括号改成小括号就是生成器
#只有一个方法next(g)或者g.__next__()
# g=(m for m in range(100))
# print(g.__next__())
# for i in g:#一般都用这个方法。
#     print(i)

# def fib(no):
#     n,a,b=0,0,1
#     while n<no:
#         print(b)
#         a,b=b,a+b
#         n+=1
# fib(10)

#只需要把上面的print改成yield就是一个生成器了。
#生成器可以在单线程下实现并发执行。

def fib(no):
    n,a,b=0,0,1
    while n<no:
        yield b
        a,b=b,a+b
        n+=1
    return '---done--'#生成其中，return的作用就是异常的时候返回的信息
f=fib(10)

while True:
    try:
        print(next(f))
    except StopIteration as e:
        print(e.value)
        break



#递归函数：
# def fib(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
#
# print(fib(5))








