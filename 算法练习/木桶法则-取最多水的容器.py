#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 木桶法则-取最多水的容器.py
@time: 2023/3/14  16:44
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        right=len(height)-1
        max_sum=min(height[right],height[left])*(right-left)
        # print(max_sum)

        for left in range(len(height)-1):

            for right in range(len(height)-1,left,-1):

                print(left,right)



                sum=min(height[right],height[left])*(right-left)
                # print(sum)

                max_sum=max(max_sum,sum)

        return max_sum



list=[2,3,10,5,7,8,9]
print(Solution.maxArea(1,list))