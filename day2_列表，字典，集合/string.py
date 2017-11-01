#!/usr/bin/env python
# *_* coding:utf-8 *_*
# python learning, keep on!

name='my name is alex'
#第一个字母大写，只把字符串的第一个字母大写，如过时空格就不大写
print(name.capitalize())

#统计一个字符出现的个数
print(name.count('a'))

#居中，打印制定个字符
print(name.center(50,'-'))

#判断是否是以什么结尾,后面参数为范围
print(name.endswith('a',1,5))

#查找指定字符的位置，返回下标。
print(name.find('a'))
print(name.rfind('a'))

#判断是否为字符和数字
print('abc23'.isalnum())

#判断是否为字符
print('asdA'.isalpha())

#判断是否是十进制
print('1a'.isdecimal())

#判断是否是数字
print('1234.5'.isdigit())

#判断是否是合法的变量名
print('asd1_23'.isidentifier())

#判断是否是小写字符
print('asd1'.islower())

#判断是否是数字，和isdigit差不多
print('121'.isnumeric())

#判断是不是每个单词首字母大写
print('Asdf'.istitle())

#判断是否是可打印的
print('saad'.isprintable())

#判断是否是大写
print('nadSA'.isupper())

#吧前面字符串插入后面字符串里，或者列表里
print(','.join('s=we'))

#制定宽度，不够再左边填充制定字符
print(name.ljust(50,','))
print(name.rjust(50,','))

#默认过滤左右的空格或者换行
print(' 000alse  \n'.strip(' '))
print(' 000alse  \n'.lstrip())
print(' 000alse  \n'.rstrip())

#对应替换
p=str.maketrans('weasdfas','2321!@#3')
print('wella'.translate(p))

#替换
print('adwaf'.replace('a','A',1))

#从左往右，返回找到的最大下标。
print(name.rfind('a'))

#按指定字符把字符串分割成列表。默认是空格
print('asda asdf'.split('s'))

#按换行进行分割成列表
print('fwefa\nasdf\n2341'.splitlines())

#变换大小写
print('a@Eas'.swapcase())

#每个单词守字符大写
print('adf afe'.title())

#用0补位
print('asd'.zfill(50))





