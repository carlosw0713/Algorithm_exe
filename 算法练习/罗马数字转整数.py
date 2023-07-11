#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 罗马数字转整数.py
@time: 2023/3/20  17:24
"""

s='MDCI'

dict={'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000,}


# pre_int=0

class Solution:

    def romanToInt(s):
        pre_int = 0
        sum = 0
        st = list(s)
        while len(st)>0:

            # 如果前一位
            if dict.get(st[-1]) < pre_int:
                sum-=dict.get(st[-1])

            else:
                sum += dict.get(st[-1])

            # 获取创建前的数据
            pre_int=dict.get(st[-1])

            # 每次运行列表减一
            st.pop()

        return sum

print(Solution.romanToInt(s))






