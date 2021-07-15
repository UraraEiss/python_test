# /usr/bin/env python
# _*_coding:UTF-8 _*_
number = input("输入数字：")
if number.isdigit (): #判断输入的字符是否是数字
    f_n = int(number) #定义字符类型
    if f_n == 10:
        print("相等")
    elif f_n < 10 :
        print("小于")
    else:
        print("大于")
else:
    print("请输入数字")

