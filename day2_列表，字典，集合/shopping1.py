#!/usr/bin/env python
# *_* coding:utf-8 *_*
# python learning, keep on!

goods=[[1,'python',25],[2,'math',30],[3,'english',55],[4,'computer',37],[5,'music',78]]
salary=int(input('please input your salary:'))
shoppingcart=[]

print('our goods blow,please input no to add to your shopping cart')
for i in goods:
    print(i)

while True:
    inputs=input('goods no:')
    if inputs=='q':
        print('you have bought good blow:\n')
        print(shoppingcart)
        print('your salary is '+str(salary))
        break
    else:
        no=int(inputs)
    for i in goods:
        if i[0]==no:
            if i[2]<salary:
                shoppingcart.append(i)
                salary=salary-i[2]
                print(i, )
                print('has add to your shopping cart')
                print('now your shopping cart is:')
                print(shoppingcart)
                break
            else:
                print('your balance is not enough! please select other cheaper.')

