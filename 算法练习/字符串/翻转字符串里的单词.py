#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 翻转字符串里的单词.py
@time: 2023/4/4  10:51
"""

'''
输入：s = "the sky is blue"
输出："blue is sky the"
输入：s = "a good   example"
输出："example good a"
解释：如果两个单词间有多余的空格，反转后的字符串需要将单词间的空格减少到仅有一个。
'''

class Solution:
    def reverseWords(self, s):

        # list=s.split(' ')
        # str=''
        # print(list.remove(''))
        # for i in range(len(list)-1,-1,-1):
        #     if list[i]!='':
        #         str+=list[i]+' '
        # return str.strip()
        list= (s.split(' ')[::-1])
        list.remove('')
        return  ' '.join(list).strip()





s = "the sky is  blue"

print(Solution.reverseWords(1,s))