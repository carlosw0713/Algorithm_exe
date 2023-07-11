#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 快速排序.py
@time: 2023/1/30  13:55
"""
import random

'''快速排序'''

def way(li,left,right):

    tmp=li[left] # 取起始最左边值为排序下标

    print(tmp)
    while left < right:
        while left < right and li[right] >=tmp: # 从右面找比tmp小的数
            right-=1 # 往左边移动一步
        li[left] = li[right] # 把右边的值写到左边的空位上
        print(li,'right')

        while left< right and li[left] <=tmp:
            left +=1
        li[right] = li[left] #把左边的值写到右边的空位上取

        print(li,'left')

    li[left] =tmp # 把tmp复位

    print(f'排序后列表{li}--排序值{li[left]}')

    return left

def quick_sort(li,left,right):

    if right>left: # 如果满足调节就让他一直排序，直到相等或者只有一个值时
        mid=way(li,left,right)

        quick_sort(li,mid+1,right)

        quick_sort(li,left,mid-1)

    # print(li)


if __name__=='__main__':
    # 生成随机列表
    list = [random.randint(0, 100) for i in range(10)]
    print(f'起始列表{list}')

    '''快速排序'''
    quick_sort(list,0,len(list)-1)