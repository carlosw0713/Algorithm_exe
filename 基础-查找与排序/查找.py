#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 查找.py
@time: 2023/1/29  15:11
"""
'''
顺序查找
'''
def order_select(li, val):
    for ind,inx in enumerate(li):

        if inx == val:
            print(f'列表{li}的{val}下标为{ind}')
        else:
            print(f'列表{li}没有{val}')

'''
'''