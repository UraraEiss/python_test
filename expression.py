# /usr/bin/env python
# _*_coding:UTF-8 _*_
'''
inp = input("请输入三角形的三条边，用“,”隔开：")
inp = inp.split(',')
inp1, inp2, inp3 = int(inp[0]), int(inp[1]), int(inp[2])
if(inp1+inp2) > inp3 and \
    (inp2+inp3) > inp1 and \
    (inp3+inp1) > inp2:
    print("输入的边长{a},{b},{c}能构成三角形".format(a=inp1, b=inp2, c=inp3))
else:
    print("输入的边长{a},{b},{c}不能构成三角形".format(a=inp1, b=inp2, c=inp3))
'''

'''
month=int(input("请输入月份："))
day=int(input("请输入日期："))
print(f"您输入的日期是：{month}月{day}日".format(month=month,day=day))
if month >0 and month <=12:
  if month in (1,3,5,7,8,10,12):
      if day >0 and day <=31 :
        print("日期合法")
      else:
        print("日期不合法")
  elif month == 2 :
      if day >0 and day <=29 :
        print("日期合法")
  else:
      if day >0 and day <=30:
          print("日期合法")
      else:
          print("日期不合法")
else:
    print("日期不合法")
'''

'''
list = [1,5,6,2,4]
for i in range(len(list)) :
    print(list[-(i+1)])
'''

'''
lst = [4, 6, 1, 7, 2, 9, 3]
max_v=lst[0]  #设定第一位为最大值
for i in lst :
    if  i  > max_v:
        max_v = i
print(max_v)
'''

'''
lst = [3, 6, 1, 8, 10, 3, 20, 13]
max_lst = lst[0]
mix_lst = lst[0]
index = 0
while len(lst) :
    if lst[index] > max_lst:
        max_lst=lst[index]
    if lst[index] < mix_lst:
        mix_lst=lst[index]
    index += 1
    print(max_lst,mix_lst)
'''

word = input("请输入字符：")
changdu = len(str(word))
haed,end=0,-1
for i in range(changdu//2) :
    if word[haed]==word[end-i]:
        print("你输入的是回文")
        break
    else:
        print("你输入的不是回文")
        break