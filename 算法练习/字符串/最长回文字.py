#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 最长回文字.py
@time: 2023/3/3  15:01
"""
s="babad"
s="cbbd"


class Solution:
    def longestPalindrome(self, s):

        lenght=len(s)
        max_str=''
        max_lenght=0

        for i in range(lenght):
            lenght=len(s)

            while lenght-i>max_lenght:
                # print(lenght-i,max_lenght)
                # print(s[i:lenght])
                if s[i:lenght]==s[i:lenght][::-1] :
                    max_str=s[i:lenght]
                    max_lenght=len(max_str)
                    break
                lenght-=1

        return max_str


print(Solution.longestPalindrome(1,s))



