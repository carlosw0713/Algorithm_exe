#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 整数反转.py
@time: 2023/3/14  14:54
"""

'''给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。
'''


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        y = x

        if x > 0:

            x = str(x)[::-1]
            while int(x[0]) == 0:
                x = x[1:]

            return int(x) if -2147483648 < int(x) < 2147483647 else 0

        elif x == 0:
            return 0
        else:
            x = str(x)[1:]  # 消除负数
            x = str(x)[::-1]
            while int(x[0]) == 0:
                x = x[1:]
            return -int(x) if -2147483648 < int(x) < 2147483647 else 0
x=90110011111
print(Solution.reverse(1,x))