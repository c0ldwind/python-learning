#!/usr/bin/env python
# *_* coding:utf-8 *_*
# python learning, keep on!

age_of_oldboy = 56
guess_age=int(input("input age:"))

if guess_age==age_of_oldboy:
    print('well,you get it ...')
elif guess_age>age_of_oldboy:
    print('think smaller...')
else :
    print('think bigger...')
