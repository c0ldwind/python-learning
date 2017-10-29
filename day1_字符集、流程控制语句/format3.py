#!/usr/bin/env python
# *_* coding:utf-8 *_*
# python learning, keep on!

name = input('name:')
age = input('age:')
job = input('job:')
salary = input('salary:')

info='''
----------info of {_name}--------
name:{_name}
age:{_age}
job:{_job}
salary:{_salary}
'''.format(_name=name,_age=age,_job=job,_salary=salary)
print(info)