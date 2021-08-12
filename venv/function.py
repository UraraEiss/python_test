# /usr/bin/env python
# _*_coding:UTF-8 _*_
# def hello_world():
#     print('hello world')
'''
def diamond(number):
    for i in range(number):
        if i <= (number//2):
            print(" "*(number//2-i) + "*"*(2*i+1))
        else:
            print(" "*(i-number//2) + "*"*((number-i)*2-1))
diamond(11)
'''
'''
def diamond(number):
    for i in range(number):
        if (number//2-1) <= i <= (number//2)  :  #取到中间值前一位的行，去除后就会从头开始
            print(" "*(number//2-i) + "*"*(2*i+1))

        if i> (number//2):
            print(" "*(i-number//2) + "*"*((number-i)*2-1))
diamond(11)
'''
'''
def my_print(content, count):
    for i in range(count):
        print(content)

my_print('ok', 2)
'''

import os
def select_file(file_path,suffix):
    file_list = os.listdir(file_path)
    file = []
    for file_name in file_list:
        if file_name.endswith(suffix):
            file.append(file_name)
    return file
# input("输入路径和文件后缀：",input_path,input_suffix)
input_path=str(input("输入路径："))
input_suffix=str(input("输入文件后缀："))
py_file=select_file(input_path,input_suffix)
print(py_file)