# /usr/bin/env python
# _*_coding:UTF-8 _*_
import calendar
print(calendar.isleap(2022)) #判断闰年

cal = calendar.month(2021,9) #直观，但是不便于统计，类型string
print(cal)

cal = calendar.monthcalendar(2021,9)
print(cal)

cal = calendar.weekday(2021,9,27)
print(cal)

