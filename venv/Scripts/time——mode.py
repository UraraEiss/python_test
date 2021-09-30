# /usr/bin/env python
# _*_coding:UTF-8 _*_
import time
curr_time = time.time()
local_time = time.localtime(time.time())
print(curr_time)

print("现在时间：",local_time)
print("年",local_time.tm_year)
print("月",local_time.tm_mon)
print("日",local_time.tm_mday)
print("时",local_time.tm_hour)
print("分",local_time.tm_min)
print("秒",local_time.tm_sec)

print("现在时间时是{year}年{mon}月{day}日{hor}时{mi}分{sec}秒" .format(
      year=local_time.tm_year,
      mon=local_time.tm_mon,
      day=local_time.tm_mday,
      hor=local_time.tm_hour,
      mi=local_time.tm_min,
      sec=local_time.tm_sec))

local_time = time.strftime("%Y-%m-%d---%H:%M:%S",local_time)
print(local_time)