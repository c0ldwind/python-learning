#!/usr/bin/env python
# *_* coding:utf-8 *_*
# python learning, keep on!

product_list=[
    ('Iphone',5000),
    ('Mac pro',9000),
    ('Watch',2000),
    ('Coffee',50),
    ('Python',30)
]
shopping_list=[]
salary=input('Input your salary:')

if salary.isdigit():
    salary=int(salary)
    print()
    while True:
        for index,item in enumerate(product_list):
            print(index,item)
        print("--------你买的商品如下：--------")
        for item in shopping_list:
            print(item)
        print('你的余额为：%s' % salary)
        user_no = input('选择要买的商品号：')
        if user_no.isdigit():
            user_no=int(user_no)
            if user_no<len(product_list) and user_no>=0:
                p_item=product_list[user_no]
                if p_item[1]<salary:
                    print('%s add to your shopping cart'% (p_item[0]))
                    shopping_list.append(p_item)
                    salary=salary-p_item[1]
                else:
                    print('你只剩%s了，还买个毛线，要么买个便宜的，要么退出。'% salary)
            else:
                print('你输入的商品不存在')
        elif user_no=='q':

            exit()
        else:
            print('你的输入错误，请重新选择')
else:
    exit('your input salary is invalid')