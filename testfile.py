# /usr/bin/env python
# _*_coding:UTF-8 _*_
'''
简单调用函数
name = str(input("输入名字：")) #直接定义该段输入的数据类型
age = int(input("输入年龄："))
word = "114514"
print("你的名字是：%s" %name)
print("你的年龄是：%i" %age))
print("名字是：%s 年龄是：%i ---%s " %(name,age,word))
'''

''' #
n=1
while n < 50:
    if n%3 == 0 :
        print(n)
    n+=1
'''

''' 1-2+3-4...+99的和
m=1
 n=m
 sum=0
 while m<100 :
    if m%2 != 0:
        n=m+1
        sum=sum+(m-n)
        m+=1
    else:
        m+=1
    print(sum)
'''

''' # 用户三次登陆
c = 3
name = "jack"
passwd = "jack123"
while c > 0:
    user_name = str(input("请输入用户名："))
    user_passwd = str(input("请输入密码："))
    if user_name != name or user_passwd != passwd:
        c -= 1
        print("密码或者用户名错误，您还剩%i次机会" % c)
        if c == 0:
            print("登陆失败")
        continue
    else:
        print("登陆成功")
    break
'''
print(__file__)



