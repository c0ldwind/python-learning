#!/usr/bin/env python
# *_* coding:utf-8 *_*
# python learning, keep on!
import sys
import os

print(sys.path) #打印python的环境变量
print(sys.argv) #打印命令行参数，第一个参数是脚本名字。
print(os.system('dir')) #执行命令不保存结果，返回0，表示命令成功。1表示命令执行错误
print(os.popen('dir').read())
os.mkdir('test')  #创建目录