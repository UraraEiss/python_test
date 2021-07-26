# /usr/bin/env python
# _*_coding:UTF-8 _*_
# def hello_world():
#     print('hello world')

def diamond(number):
    for i in range(number):
        if i <= (number//2):
            print(" "*(number//2-i) + "*"*(2*i+1))
        else:
            print(" "*(i-number//2) + "*"*((number-i)*2-1))
diamond(11)