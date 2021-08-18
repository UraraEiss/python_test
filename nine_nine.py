# /usr/bin/env python
# _*_coding:UTF-8 _*_

def nine_nine (numbers):
    lst=[]
    for i in range(1,numbers+1):
        pro = "{line}*{number}={val}".format(line=i,number=numbers,val=i*numbers)
        lst.append(pro)
    print("  ".join(lst))
def nine_table ():
    for i in range(1,10):
        nine_nine(i)
nine_table()
'''
def print_line(line_number):
    lst = []
    for i in range(1, line_number+1):
        part = "{index}*{number} = {res}".format(index=i, number=line_number, res=i*line_number)
        lst.append(part)

    print("  ".join(lst))


def print_table():
    for i in range(1, 10):
        print_line(i)


print_table()
'''