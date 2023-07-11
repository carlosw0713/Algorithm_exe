#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 桶排序.py
@time: 2023/2/7  15:14
"""
from pythonProject.算法入门.基础.计时装饰器 import timer

'''
计数排序延申的算法，因为计数排序开始需要创建一个巨长的列表[0~100]，耗费空间，
桶排序（Bucket_sort）在其基础上，将列表分割[0~10],[10~20]....[90~100]。
'''

# 已知在列表中数的范围都是在0~100之间，可以用计数排序，实现时间复杂度O(n)
import random

@timer
def bucket_sort(li,n,max_count):

    buckets=[[]for _ in range(n)]#创建桶，二维列表
    for var in li:
        i=min(var//(max_count//n),n-1)# 表示var放在那个桶里？
        buckets[i].append(var)#把var加到桶里面

        # 保持桶里的顺序，从小到大，所以从后面开始冒泡排序，
        for j in range (len(buckets[i])-1,0,-1):
            if buckets[i][j]<buckets[i][j-1]:
                buckets[i][j],buckets[i][j-1]=buckets[i][j-1],buckets[i][j]
            else:
                break
    print(buckets)
    sort_list=[]
    for buc in buckets:
        sort_list.extend(buc)
    # print(sort_list)

@timer
def count_sort(li,max_count):
    count_list=[0 for i in range(max_count+1)] # 因为是正整数，所以先创建个数种类长度的列表（max_count）
    # print(count_list)

    for val in li: #分别记录 不同值分别包含多少个
        count_list[val]+=1
    # print(count_list)

    li.clear() # 列表清空

    for ind,val in enumerate(count_list): #  count_list=[ind*vt_list=[ind*val]i in range(val):
            li.append(ind)
    # print(li)



if __name__ == '__main__':
    # 生成随机列表
    list = [random.randint(0, 101) for i in range(50)]
    # list = random.sample(range(0, 100), 7)
    print(f'起始列表{list}')

    # 桶排序
    bucket_sort(list,10,100)

    # 计数排序
    # count_sort(list,1000)