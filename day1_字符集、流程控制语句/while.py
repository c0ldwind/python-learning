#!/usr/bin/env python
# *_* coding:utf-8 *_*
# python learning, keep on!

age_of_oldboy = 56
count=3
while count>0:
    guess_age=int(input("input age:"))
    if guess_age==age_of_oldboy:
        print('well,you get it ...')
        break
    elif guess_age>age_of_oldboy:
        print('think smaller...')
    else :
        print('think bigger...')
    count-=1
    if count==0:
        anser=input('sorry you could not guess the age ,do you want go quit(q)?')
        if anser!='q':
            count=3
        else:
            print('sorry ,you could not guess the age')
            break