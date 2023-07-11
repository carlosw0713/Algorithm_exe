#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 长度最小的子数组.py
@time: 2023/4/6  14:03
"""
class Solution:
    def minSubArrayLen1(self, target: int, nums) -> int:
        n = len(nums)
        ans = n + 1  # 也可以写 inf # 假设初始长度
        s = left = 0
        for right, x in enumerate(nums):
            s += x
            # while s - nums[left] >= target:
            #     s -= nums[left]
            #     left += 1
            # if s >= target:
            #     ans = min(ans, right-left+1)
            while s >= target:  # 满足要求
                ans = min(ans, right - left + 1)# 取最短值

                # 左边缩进
                s -= nums[left]
                left += 1
        return ans if ans <= n else 0


    # # 自己编写
    # def minSubArrayLen(self, target: int, nums) -> int:
    #     # 如果小于最小，大于总数合则返回0
    #     if sum(nums) < target:
    #         return 0
    #     # 计算总值
    #     n = 1
    #     left, right = 0, 0
    #
    #     # 直接找出满足匹配的长度
    #     for i in range(len(nums)):
    #         if sum(nums[0:i + 1]) >= target:
    #             max_lenght = i
    #             break
    #     # 当满足right<len(nums)
    #     right = left + max_lenght
    #     while right <=len(nums):
    #         print(right,left,sum(nums[left:right+1]),nums[left:right+1])
    #
    #         while sum(nums[left:right+1]) > target:
    #             left += 1
    #             # print('left',left)
    #         right += 1
    #     max_lenght = right - left
    #     return max_lenght


target =11
nums = [1,2,3,4,5]




print(Solution.minSubArrayLen1(1,target,nums))

