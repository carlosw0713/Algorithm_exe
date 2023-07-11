#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 堆排序.py
@time: 2023/2/1  18:29
"""
import random


def sitf(li,low,high):
    '''

    :param li: 列表
    :param low: 根节点的位置
    :param high: 堆最后一数的位置
    :return: 父节点比子节点的数都要大
    '''

    i= low #起始根节点的位置
    j= i*2 +1 #左孩子的位置

    tmp=li[low] #根节点的值

    while high>=j: #只有孩子还在循环才会进行

        if high>=j+1 and li[j+1]<li[j]: #判断是否存在右孩子，且比较两个孩子的大小（选出最大的孩子）。
            j=j+1

        if li[j] < tmp: #如果孩子比父亲大,调换位置，继续找下一层

            '''找下一层'''
            li[i]=li[j] #替换值
            i=j
            j=2*i +1

            # print(li)
        else: #tmp更大，把tmp放在i位置
            li[i]=tmp
            break

    else:# 当while中有break的时候不会走else,反之会走else.
        li[i]=tmp

    # print(li)


def heap(li):

    n=len(li)
    for i in range(((n-1)-1)//2,-1,-1):
        # i表示一个父节点 表示建立堆时依次调整根的下标

        sitf(li,i,n-1)
        print(li,'建立堆')

    for i in range(n-1,-1,-1):
        # i 指向当前堆的最后一个
        li[0],li[i]=li[i],li[0]
        sitf(li,0,i-1)#i-1 表示high
        print(li,'堆排序')
# 堆的内置模块
def imp_heaqp():
    # 堆的内置模块 heapq q->queue 优先队列
    import heapq
    heapq.heapify(list)  # 建立堆
    n = len(list)
    for i in range(n):
        print(heapq.heappop(list))

'''topk排序'''
def topk(li,k):
    li_topk=li[0:k]
    # 建立堆
    for i in range(((k-1)-1)//2,-1,-1):
        sitf(li_topk,i,k-1)
        print(li_topk,'建立堆')

    # 遍历
    for i in range(k-1,-1,-1):
        li_topk[0],li_topk[i]=li_topk[i],li_topk[0]
        sitf(li_topk,0,i-1)
        print(li_topk,'堆排序')




if __name__=='__main__':
    # 生成随机列表
    # list = [random.randint(0, 11) for i in range(10)]
    list=random.sample(range(0, 100), 7)
    print(f'起始列表{list}')

    # 自己编写堆排序
    # heap(list)

    # 堆的内置模块
    # imp_heaqp()

    # topk堆排序方法
    topk(list,5)



