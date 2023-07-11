#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 杨辉三角.py
@time: 2023/4/7  11:10
"""

class Solution:
    def getRow(self, rowIndex: int):

        row_list = [1]
        for i in range(1, rowIndex + 1):
            row_list.append(0)
            for j in range(1, i + 1):
                row_list[-j] = row_list[-j] + row_list[-j - 1]
                print(row_list)
        return row_list

print(Solution.getRow(1,5))


