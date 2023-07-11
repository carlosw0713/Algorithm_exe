#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 四数之和.py
@time: 2023/3/23  17:47
"""

class Solution:
    def fourSum(self, nums, target):



        # 排序
        nums.sort()
        # 获取长度值
        lenght=len(nums)

        res=[]
        tmp=[]

        for i1 in range(lenght-3):

            if nums[i1] > 0 and nums[i1] > target:
                break

            for i2 in range(i1+1,lenght-2):
                if nums[i2] + nums[i1] > 0 and nums[i2] + nums[i1] > target:
                    break

                i3=i2+1
                i4=lenght-1

                while i4>i3:



                    tmp=[nums[i1],nums[i2],nums[i3],nums[i4]]
                    tmpsum=sum(tmp)



                    # 满足等于且 避免重复
                    if tmpsum==target and tmp not in res:
                    # if tmpsum==target:
                        res.append([nums[i1],nums[i2],nums[i3],nums[i4]])
                        i3+=1
                        i4-=1


                    # 根据大小判断是否包含
                    elif tmpsum<target:
                        i3+=1

                    else:
                        i4-=1


        # 直接返回值去重
        return res




if __name__=='__main__':

    nums=[1,0,-1,0,0,0,0,-2,2]
    target=0

    print(Solution.fourSum(1,nums,target))