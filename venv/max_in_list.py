# /usr/bin/env python
# _*_coding:UTF-8 _*_
def get_max(lst):
    """
    返回列表lst的最大值
    :param lst:
    :return:
    """
    pass
    max_list = lst[0]
    for count in lst:
        if count > max_list:
            max_list = count
    return max_list
lst = [4, 2, 1, 6, 7, 5]
max_value = get_max(lst)
print(max_value)