#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 计时装饰器.py
@time: 2023/2/7  14:27
"""


from functools import wraps
import time

# time装饰器

from functools import wraps
import time


# time装饰器
def timer(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        begin_time = time.perf_counter()
        result = func(*args, **kwargs)
        start_time = time.perf_counter()
        # print('func:%r args:[%r, %r] took: %2.4f sec' % (func.__name__, args, kwargs, start_time - begin_time))
        print(f'该程序一共运行：{start_time-begin_time}秒')
        return result

    return wrap


@timer
def waste_some_time(num):
    my_list = []
    for i in range(num):
        my_list.append(i)
    return my_list


if __name__ == '__main__':
    arr = waste_some_time(1000)
    print(arr)



