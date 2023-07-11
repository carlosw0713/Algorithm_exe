#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 汉诺塔算法.py
@time: 2023/1/29  14:46
"""

'''
汉诺塔问题
'''
def hannota (n,a,b,c):

    if n>0:
        hannota(n-1,a,c,b)
        print(f'moving form {a},{c}')
        hannota(n-1,b,a,c)

hannota(2,'A','B','C')
