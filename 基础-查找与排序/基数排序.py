#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 基数排序.py
@time: 2023/2/7  16:42
"""
import random


def radix_sort(li):
    max_num=max(li)# 确定最大值

    # 确定最大位数
    max_post=0
    while 10**max_post<=max_num:
        buckets=[[] for _ in range(10)]# 桶思想，每个桶的值不会大于9
        for var in li:
            digit=(var//10**max_post)%10 # 取余数
            buckets[digit].append(var)

        print(f'{10**max_post}位数比较：',buckets)

        li.clear()

        # 分桶完成 每次分桶保证某一位排序好
        for buc in buckets:
            li.extend(buc)# 添加一个列表中所有元素

        max_post+=1 # 每次循环增1

        # print(li)

if __name__ == '__main__':
    # 生成随机列表
    list = [random.randint(0, 10000) for i in range(20)]
    # list = random.sample(range(0, 100), 7)
    print(f'起始列表{list}')

    radix_sort(list)