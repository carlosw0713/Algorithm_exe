#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 练习题.py
@time: 2023/2/8  10:13
"""
import random

from numpy import sort

'''1.给定两个字符串s和t判断t是否是s重新排列后组成的单词'''
def Judge_words(s,t):
    '''

    :param s:字符串
    :param t: 字符串
    :return: ture or false
    '''

    s=list(s)
    t=list(t)


    if len(s)==len(t):
        dict_s=sitf1(s)
        dict_t=sitf1(t)

    #     for key,value in dict_s.items():
    #         if key not in dict_t.keys():
    #             return False
    #
    #         else:
    #             if dict_t[key]!=value:
    #                 return False
    #
    #     return True
    #
    # else:
    #     return False

    # 第一种方法不需要循环，因为字典是键值对没有前后索引区分
    return dict_s==dict_t

    # 第二种直接用自带的排序写法
    return  sorted(s)==sorted(t)


def sitf1(list):

    list1=[]
    dict1={}

    '''
    字典计数可以用dict.get(key,default=None)
    key -- 字典中要查找的键。
    default -- 如果指定键的值不存在时，返回该默认值。
    
    for item in line:
    dict[item]=dict.get(item,0)+1
    '''

    for i in list:

        if i in list1:
            dict1[i] += 1
        else:
            dict1[i] = 1
            list1.append(i)

    return dict1

s=''.join(random.choice('ab') for _ in range(3))
t=''.join(random.choice('ab') for _ in range(3))
# s='qwer'
# t='rewq'

# print(f's:{s},t:{t}')
# print(Judge_words(s,t))




'''2.在一个二维数组中，每一行元素从左到右递增，从上到下递增，现输入一个整数，判断数组中是否存在该整数，要求时间复杂度为O(n)'''
def Find_existing(li,s):

    i=0
    while i<=len(li)-1:
        if li[i][0]<=s and s<=li[i][-1]:
            for j in li[i]:
                if j==s:
                    return True
            return False
        else:
            i+=1
    else:
        return False
# 创建排序好的桶（2维列表）
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
    # print(f'二维列表{buckets}')
    return buckets
list = [random.randint(0, 101) for i in range(50)]
tow_array=bucket_sort(list,10,100)
s=random.randint(0,100)

# print(f'排序好的二维数组:{tow_array}',f'\n随机值:{s}')
# print(Find_existing(tow_array,s))


'''3.给定一个列表和一个整数，设计算法找到两个数的下标
使得两个数的和为给定的整数，保证肯定仅有一个结果。'''
def list_lookup(li,s):
    '''

    :param li: 列表
    :param s: 给定整数
    :return:元素在列表中下标
    '''

    for ind,val in enumerate(li):
        x=ind+1#第二个值
        while x<=len(li)-1:

            if val+li[x]==s:
                return (ind,x)
            else:
                x+=1


list=list=random.sample(range(0, 10), 10)
s=random.randint(0,10)

# list=[5, 7, 2, 0, 4, 8, 6, 1, 9, 11]
# s=20
print(f'列表值：{list},整数：{s}')
print(list_lookup(list,s))
