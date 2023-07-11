#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 计数排序.py
@time: 2023/2/7  14:45
"""

# 已知在列表中数的范围都是在0~100之间，可以用计数排序，实现时间复杂度O(n)
import random


def count_sort(li,max_count):
    count_list=[0 for i in range(max_count+1)] # 因为是正整数，所以先创建个数种类长度的列表（max_count）
    print(count_list)

    for val in li: #分别记录 不同值分别包含多少个
        count_list[val]+=1
    print(count_list)

    li.clear() # 列表清空

    for ind,val in enumerate(count_list): #  count_list=[ind*vt_list=[ind*val]i in range(val):
            li.append(ind)
    print(li)



if __name__ == '__main__':
    # 生成随机列表
    list = [random.randint(0, 21) for i in range(20)]
    # list = random.sample(range(0, 100), 7)
    print(f'起始列表{list}')

    count_sort(list,21)