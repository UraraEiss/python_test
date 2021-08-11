# /usr/bin/env python
# _*_coding:UTF-8 _*_
#The index
# a = "I am learning python"
# print(a [2:10])

# Escape character
'''
list =  ['曹','犹','盖']
with open('testfile','w', encoding ='utf-8') as f:
    for name in list :
        f.write(name + '\n')
'''
#format
# string = "I like {color}".format(color='red')
# print(string)

# info = {'vehicle':'plane','place':'new york'}
# print(f"我要搭乘info['vehicle']去往info['place']")
'''
索引的插入与追加
list = [1,2,3,4,5]
list.insert(3,8)
print(list)

lst = ['a','b','c']
lst.insert(0,'r')
print(lst)

ls = ['a','b','c']
ls.append('d')
print(ls)
'''

'''
list = [0,1,2,3,2,1,3,4,1,4,5,0,0]
print(list.count(0))
print(list.count(4))
print(list.count(1))
'''

''''
list1 = [1,1,1]
list2 = [2,2,2]
print(id(list1))
print(id(list2))
list1.extend(list2)
print(list1)
print(id(list1))
list2.append(3)
print(list2)
print(id(list2))
'''

'''
study_dict = {
    'monday_dict' : {
      '校区': "东区",
      '楼号': 9,
      '教室': 9104
     },

    'tuesday_dict' : {
      '校区':'西区',
      '楼号': 2,
      '教室': 2204
     }
}
print(study_dict['tuesday_dict'])
'''
'''
stu_dict = {'数学',92,
            '语文',93
           }
stu2_dict = {'英语',78}
stu_dict.update(stu2_dict)
'''
'''
dict = {
    'python':6,
    'java':4,
    'c':1
}
dict ['php'] =3
dict ['javascript'] = 7
print(max(dict.values()))
'''
'''
set1 = set()
set2 = {'python','java','php','c'}

set1.add('java')
'''
'''
lst1 = [1, 2, 3, 5, 6, 3, 2]
lst2 = [2, 5, 7, 9]

set1 = set(lst1)
set2 = set(lst2)
print(set1.intersection(set2))
print(set1.difference((set2)))
print(set1.union(set2))
'''
'''
lst1 = [10, 3, 2, 6, 7, 5]
lst2 = [3, 2, 5, 6, 10, 7]

combine_set = set()

for item1 in lst1:
    for item2 in lst2:
        if item1 + item2 == 12:
            combine_set.add((min(item1, item2), max(item1, item2)))


print(combine_set)
'''