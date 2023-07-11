#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 下一个排序.py
@time: 2023/3/29  10:34
"""

class Solution:
    def nextPermutation(self,nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        1.从后到前依次提取元素。
        2.直到找到前一个元素大于后一个元素的
        3.如果没有输出列表最小排列
        '''

        n = len(nums)
        i = n - 2

        # 从右向左找到第一个升序对 (nums[i], nums[i + 1])
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 如果找到了升序对，从右向左找到第一个大于 nums[i] 的数并与 nums[i] 交换
        if i >= 0:
            j = n - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # 将i之后的部分排序成最小字典序列
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


        return nums





if __name__ == '__main__':

    nums=[3,5,6,2,1]
    nums=[1,4,3,5,2]
    # nums=[5,4,7,5,3,2]



    print(Solution.nextPermutation(1,nums))