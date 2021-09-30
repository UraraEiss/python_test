# /usr/bin/env python
# _*_coding:UTF-8 _*_

import os
path = 'D:/python/test1/venv/os/os_module.py'
print(os.path.abspath(path))
print(os.path.dirname(path))
print(os.path.getsize(path))
print(os.path.getatime(path))
print(os.path.getmtime(path))
print(os.path.getctime(path))