#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 数组拆分.py
@time: 2023/4/4  18:08
"""

class Solution:
    def arrayPairSum(self, nums):

        nums.sort()
        lenght=len(nums)
        n=0
        sum=0
        while n<lenght:
            sum+=nums[n]
            n+=2
        return sum


if __name__=='__main__':
    nums=[6,2,6,5,1,2]
    print(Solution.arrayPairSum(1,nums))


