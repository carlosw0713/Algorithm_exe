#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 最长公共前缀.py
@time: 2023/4/4  9:59
"""

class Solution:
    def longestCommonPrefix(self, strs):



        ret=0
        for i in zip(*strs):
            if len(set(i))==1:
                ret+=1
            else:
                break

        if ret==0:
            return ''
        print(ret)
        return strs[0][:ret]






if __name__=='__main__':

    strs=["flower","flow","flight"]
    strs=["cir","car"]

    print(Solution.longestCommonPrefix(1,strs))