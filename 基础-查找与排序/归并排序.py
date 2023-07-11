#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 归并排序.py
@time: 2023/2/7  10:14
"""
import random


def sift_sort(li,low,mid,high):
    '''

    :param li:一个切割两边有序的列表
    :param low: 起始值
    :param mid:中间值
    :param high:最大值
    :return:排序后的列表
    '''
    i=low
    j=mid+1
    itmes=[]
    while mid>=i and high>=j:#当两段有序区超出范围则结束循环，返回一段有序去
        if li[i]>li[j]:
            itmes.append(li[j])
            j+=1
        else:
            itmes.append(li[i])
            i+=1

    # 判断那段有序区存在，如果存在依次添加
    while i<=mid:
        itmes.append(li[i])
        i += 1
    while j<=high:
        itmes.append(li[j])
        j += 1

    # 将itmes的值赋值回去到li
    li[low:high+1]=itmes



def merge_sort(li,low,high):
    if low<high: # 至少有两个数
        mid=(low+high)//2

        # 相当于做了拆分，最终拆分成可以判断大小的两个数，创造两个有序区间后，依次排序
        merge_sort(li,low,mid)
        merge_sort(li,mid+1,high)

        sift_sort(li,low,mid,high)
        # print(li[low:high+1])
        print(li[low:high+1])


if __name__=='__main__':
    # 生成随机列表
    # list = [random.randint(0, 11) for i in range(10)]
    list=random.sample(range(0, 11), 11)
    print(f'起始列表{list}')

    # list1=[1,3,6,8,5,9,11]
    # sift_sort(list1,0,3,6)

    merge_sort(list,0,len(list)-1)
    print(list)




