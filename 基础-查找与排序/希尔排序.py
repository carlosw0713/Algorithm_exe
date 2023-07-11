#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 希尔排序.py
@time: 2023/2/7  14:15
"""
import random

from pythonProject.算法入门.基础.计时装饰器 import timer

'''希尔排序'''


def insert_sort(li, gap):  # 希尔排序相当于帮插入排序先分组进行插入排序，加入gap，直到分组为一时排序完成

    for i in range(gap, len(li)):  # i 表示摸到牌的下标
        j = i - gap

        tmp = li[i]  # 指最开始手里牌的下标

        while j >= 0 and tmp < li[j]:  # j到了最右边或者一直小于tmp就往右边一直移动。

            li[j + gap] = li[j]

            j -= gap

        li[j + gap] = tmp
        print('插入排序', li)


@timer
def shell_sort(li):
    d = len(li) // 2
    while d >= 1:
        insert_sort(li, d)
        d = d // 2

        print('希尔排序', li)


if __name__ == '__main__':
    # 生成随机列表
    list = [random.randint(0, 100) for i in range(10)]
    print(f'起始列表{list}')

    '''希尔'''
    shell_sort(list)
