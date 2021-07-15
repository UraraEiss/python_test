# /usr/bin/env python
# _*_coding:UTF-8 _*_
#The index
# a = "I am learning python"
# print(a [2:10])

# Escape character
list =  ['cao','you','gai']
with open('testfile','w') as f:
    for name in list :
        f.write(name + '\n')