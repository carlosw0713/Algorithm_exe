#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: lowb排序.py
@time: 2023/1/29  15:26
"""
import random

'''
冒泡排序
'''
def maopao_sort(li):

    for j in range(len(li)-1):

            for i in range(len(li)-j-1):

                if li[i] < li[i + 1]:
                    # x=li[i-1]
                    # li[i - 1] = li[i]
                    # li[i]=x

                    li[i], li[i + 1] = li[i + 1], li[i]
            print(f'冒泡排序：{li}')



'''选择排序'''
def select_sort(li):
    for i in range(len(li)):
        min_val=i
        print(li[min_val])

        exchange=False
        for j in range(i+1,len(li)):

            '''判断是否存在比li[min_val]小的值'''
            if li[j]<li[min_val]:
                min_val=j

        '''最小值与li[i]替换'''
        li[i],li[min_val]=li[min_val],li[i]
        print(f'选择排序{li}')



'''插入排序'''
def insert_sort(li):

    for i in range(1,len(li)): # i 表示摸到牌的下标
        j=i-1

        tmp=li[i] # 指最开始手里牌的下标

        while j >=0 and tmp<li[j]: # j到了最右边或者一直小于tmp就往右边一直移动。

            li[j+1]= li[j]

            j -= 1

        li[j+1]=tmp

        print(li)



if __name__=='__main__':
    # 生成随机列表
    list = [random.randint(0, 10) for i in range(10)]
    # list = [11, 6, 61, 35, 26]

    print(f'起始的列表{list}')

    # maopao_sort(list)

    # select_sort(list)

    insert_sort(list)


