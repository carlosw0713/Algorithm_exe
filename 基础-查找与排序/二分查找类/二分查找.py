#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 二分查找.py
@time: 2023/5/22  15:11
"""

class Solution:
    def search(self , nums, target: int) -> int:


        left=0
        right=len(nums)
        mid=(left+right)//2

        if right==0:
            return []

        while right-left!=1:
            print(mid, left, right)
            if nums[mid]>target:
                right=mid
            else:
                left=mid
            mid = (left + right) // 2

        # print(mid)
        return mid

if __name__=="__main__":

    nums=[-1,0,3,4,6,10,13,14]
    target=13

    Solution.search(1,nums,target)
