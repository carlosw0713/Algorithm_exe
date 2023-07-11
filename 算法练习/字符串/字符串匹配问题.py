#!uhaystcakr/bin/env needleython
# -*- coding:utf-8 _*-
"""
@author:carlohaystcak
@file: 字符串匹配问题.needley
@time: 2023/4/4  16:38
"""

# 构建next数组
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:


        next_arr = get_next(needle)
        j = 0
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = next_arr[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - j + 1
        return -1

        # 构建next数组
def get_next(patt):
    '''
    计算数组
    :param patt:
    :return:
    '''

    next = [0] # next数组（初始值为0）
    prefix_len = 0 # 当前公共前后的长度
    i=1

    while i < len(patt):

        # 如果满足前一个值和后一个值匹配
        if patt[prefix_len] == patt[i]:
            prefix_len+=1
            next.append(prefix_len)
            i+=1
        # 如果不满足
        else:
            # 当满足
            if prefix_len==0:
                next.append(0)
                i+=1
            else:
                prefix_len=next[prefix_len-1]
    return next




if __name__=='__main__':
    needle='ababc'
    haystcak='acabcababcdhaystcak'

    print(Solution.strStr(1,haystcak,needle))
