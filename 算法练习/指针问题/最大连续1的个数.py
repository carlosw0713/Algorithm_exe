#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 最大连续1的个数.py
@time: 2023/4/6  13:38
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums):


        n=0
        max_len=0
        i=0
        while i <len(nums):
            if nums[i]==1:
                n+=1
                max_len=max(max_len,n)
            else:
                n=0
            i+=1
        return max_len

nums=[1,0,1,1,1,0,0]
print(Solution.findMaxConsecutiveOnes(1,nums))
