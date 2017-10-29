#!/usr/bin/env python
# *_* coding:utf-8 *_*
# python learning, keep on!

name = input('name:')
age = input('age:')
job = input('job:')
salary = input('salary:')

info='''
----------info of {0}--------
name:{1}
age:{2}
job:{3}
salary:{4}
'''.format(name,name,age,job,salary)
print(info)