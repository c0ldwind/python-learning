#!/usr/bin/env python
# *_* coding:utf-8 *_*
# python learning, keep on!
count=0
while count <3:
    username = input('username:')
    password = input('password:')
    userlock=[]
    for i in open('lockuser.txt','r'):
        userlock.append(i.strip('\n'))
    if username in userlock:
        print('your username has locked! please contact administrator.')
        break
    else:
        user=[]
        for j in open('user.txt','r'):
            user.append(j.strip('\n'))
        up=username+':'+password
        if up in user:
            print('wellcome '+username+' login!!')
            break
        else:
            count+=1
            print('Invalid username or password, your try '+str(count)+' times')
else:
    print('too many time you try ,we locking your username.')
    usertolock=open('lockuser.txt','a')
    usertolock.write(username+'\n')
    usertolock.close()

