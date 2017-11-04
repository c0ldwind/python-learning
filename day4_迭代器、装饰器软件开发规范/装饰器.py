#!/usr/bin/env python
# *_* coding:utf-8 *_*
# python learning, keep on!

import time
'''装饰器的定义：本质是函数、装饰其他函数的函数，就是为其他函数添加附加功能。
装饰器的原则：1、不改变原函数的源代码。2、不改变原函数的调用方式。


装饰器用到的知识：
1、函数即变量，函数名就是函数体在内存中的引用。
2、高阶函数（1、把函数名当作实参传给一个函数。2、返回值中包含函数名）
3、嵌套函数

高阶函数+嵌套函数就可以实现一个装饰器。
'''
#1、不带参数函数的装饰器
'''
def decorate(func):
    def cacu_time():
        start=time.time()
        func()
        stop=time.time()
        print('the function takes %s' % (start-stop))
    return cacu_time

@decorate
def son():
    time.sleep(1)
    print('I am in the son.')
@decorate

def dau():
    time.sleep(2)
    print('I am in the dau.')

son()
dau()


#2、带参数的装饰器

def decorate(func):
    def timerr(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)
        stop_time=time.time()
        print('the function takes %s time' % (stop_time-start_time))
    return timerr

@decorate
def son(age):
    time.sleep(1)
    print('I am a boy, and my age is %s' % age)

@decorate
def dau(age,merry):
    time.sleep(2)
    print('I am a girl, and my age is %s, and my merry situation is %s' %(age,merry))

son(25)
dau(23,'no')

#3、带返回值的装饰器

def decorate(func):
    def timmer(*args,**kwargs):
        start_time=time.time()
        res=func(*args,**kwargs)#要想有返回值就在这个就把这个结果在函数体的末尾返回。
        stop_time=time.time()
        print('the function takes %s time'% (stop_time-start_time))
        return res
    return timmer

@decorate
def son(age):
    time.sleep(1)
    print('I am a boy')
    return age

@decorate
def dau(age,job):
    time.sleep(2)
    print('I am a girl, my age is %s, and my job is %s'%(age,job))

print(son(25))
dau(23,'manager')
'''

#装饰器终极版，根据参数来判断装饰器的执行过程。
#给页面增加登陆认证的功能。
#需求home页面是本地认证，admin页面是ldap认证

def decorate(auth_type):
    def auth(func):
        def login(*args,**kwargs):
            if auth_type=='local':
                username=input('username:').strip()
                password=input('password:').strip()
                if username=='admin' and password=='local':
                    print('welcome %s login in'% username)
                    func(*args,**kwargs)
                else:
                    print('Invalid username or password')
                    exit()
            elif auth_type=='ldap':
                username = input('username:').strip()
                password = input('password:').strip()
                if username == 'admin' and password == 'ldap':
                    print('welcome %s login in' % username)
                    func(*args, **kwargs)
                else:
                    print('Invalid username or password')
                    exit()
        return login
    return auth

@decorate('local')
def home():
    print('in the home page')

@decorate('ldap')
def admin():
    print('in the admin page')

home()
admin()