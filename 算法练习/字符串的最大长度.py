#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 字符串的最大长度.py
@time: 2023/2/23  14:42
"""


# arr = ["un","iq","ue"]
# arr = ["cha","r","act","ers"]
# arr=['adadadadasdwq','aa']
arr=["a", "abc", "d", "de", "def"]


def maxLength(arr):
    result = 0
    temp = []

    # 检查是否满足字符唯一的条件
    def can_add(str, temp):
        concat_str = ''.join(temp)
        for c in str:
            if c in concat_str:
                return False
        return True

    # 检查字符串本身有没有重复的字符
    def is_distinct(str):
        return len(set(str)) == len(str)

    def backtrace(arr):

        for i in range( len(arr)):
            if can_add(arr[i],temp) and is_distinct(arr[i]):
                for j in range(1,len(arr)):
                    temp.append([arr[i]])
                
                
    backtrace(arr)
                
    return result


print(maxLength(arr))