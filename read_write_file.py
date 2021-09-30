# /usr/bin/env python
# _*_coding:UTF-8 _*_
# file = open('D:\python\\test_file\\list_file.txt', 'r')
# lines = file.readlines()
# print(lines)

# line = file.readline()
# while line:
#     print(line)
#     line=file.readline()

# for line in file:
    # print(line)
# file.close()

def read_lines(file_name):
    file = open(file_name, 'r')
    line = file.readlines()
    ip_set  = set()
    for lines in line:
        ip_set.add(lines.strip())  #strip：移除首位指定字符
    return ip_set

def same_ip():
    data1_ip_file = read_lines('D:\python\\test_file\\data1_ip.txt')
    data2_ip_file = read_lines('D:\python\\test_file\\data2_ip.txt')
    same_ip_list = data1_ip_file.intersection(data2_ip_file)
    print(same_ip_list)

same_ip()

