# /usr/bin/env python
# _*_coding:UTF-8 _*_
from datetime import date

today = date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)

from datetime import time
now_time = time(11,1,22,321)
print(now_time.hour)
print(now_time.minute)
print(now_time.second)
print(now_time.microsecond)

from datetime import datetime
now = datetime.now()
print(now)
print(now.year)

now_sta = now.strftime("%Y-%m-%d")
print(type(now_sta),now_sta)

olympice_time = datetime.strptime("2020-09-27 14:23:33","%Y-%m-%d %H:%M:%S")
print(type(olympice_time),olympice_time)

a = datetime.fromtimestamp(1632819198.8495212)
print(a)

d1 = datetime(year=2021,month=3,day=31,hour=14,minute=22,second=32)
d2 = datetime(year=2021,month=9,day=28,hour=17,minute=3,second=24)
diff = d1 -d2
print(type(diff),diff)
print(diff.days,diff.seconds)

import datetime
today = datetime.datetime.now()
lastmouth_lastday = datetime.datetime(today.year,today.month,1) - datetime.timedelta(1)
lastmouth_firstday = datetime.datetime(lastmouth_lastday.year,lastmouth_lastday.month,1)
print(lastmouth_lastday)
print(lastmouth_firstday)