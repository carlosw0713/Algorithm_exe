#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 输入有序数组.py
@time: 2023/4/4  18:34
"""

class Solution:
    def twoSum(self, numbers, target):

        sum=numbers[0]+numbers[1]
        lenght=len(numbers)
        if target<sum:
            return ''

        left=0
        right=lenght-1


        while right>left:

            if numbers[left]+numbers[right]>target:
                right-=1

            elif numbers[right]+numbers[left]<target:
                left+=1

            else:
                break

        print(left,right)
        return [left+1,right+1]



if __name__=='__main__':
    numbers = [2, 7, 11, 15]
    # numbers=[2,3,4]
    numbers=[3,24,50,79,88,150,345]
    target = 200
    print(Solution.twoSum(1,numbers,target))