# /usr/bin/env python
# _*_coding:UTF-8 _*_
import os


def get_py_file_lst (py_path,suffix):
    file_lst =[]
    for root,dits,files in os.walk(py_path):
        for file in files:
            file_name=os.path.join(root,file)
            if file_name.endswith(suffix):
                file_lst.append(file_name)
    return file_lst

def get_program_line_count (file_name):
    line_count =0
    with open(file_name, 'r',encoding='utf-8')as py_file:
        for line in py_file:
            line = line.strip()
            if not line:
                continue
            if line.startswith("#"):
                continue
            line_count += 1
    return line_count

def get_py_program_count(py_path):
    file_lst = get_py_file_lst(py_path,'.py')
    program_count=0
    for file_name in file_lst:
        program_count += get_program_line_count(file_name)
    return program_count

py_path='D:\python\\test1\\venv\Scripts\\'

print(get_py_program_count(py_path))