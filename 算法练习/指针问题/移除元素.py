#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 移除元素.py
@time: 2023/4/6  11:01
"""

'''输入：nums = [3,2,2,3], val = 3
输出：2, nums = [2,2]
解释：函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。你不需要考虑数组中超出新长度后面的元素。
例如，函数返回的新长度为 2 ，而 nums = [2,2,3,3] 或 nums = [2,2,0,0]，也会被视作正确答案。'''

class Solution:
    def removeElement(self, nums, val: int):

        s, f = 0, 0
        while f < len(nums):
            if nums[f] != val:
                nums[s] = nums[f]
                s += 1
            f += 1
        return s



nums = [2,2,3]

val = 2
print(Solution.removeElement(1,nums,val))


