#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: python实现基本正则操作.py
@time: 2023/3/14  16:33
"""

'''
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
'''

def isMatch(s, p): # 如果都为空，则匹配 if not s and not p: return True




    # 任意一个为空，则不匹配
    if not s or not p:
        return False

    # 如果第一个字符相等，或者p的第一个字符为.
    if s[0] == p[0] or p[0] == '.':
        # 如果p的第二个字符为*
        if len(p) > 1 and p[1] == '*':
            # 分三种情况：1.s不变，p后移两位；2.s后移一位，p不变；3.s后移一位，p后移两位
            return isMatch(s, p[2:]) or isMatch(s[1:], p[2:]) or isMatch(s[1:], p)
        # 如果p的第二个字符不为*，则两个串都后移一位
        else:
            return isMatch(s[1:], p[1:])
    # 如果第一个字符不匹配，但是p的第二个字符为*
    elif len(p) > 1 and p[1] == '*':
        # 则p后移两位
        return isMatch(s, p[2:])
    # 其他情况均不匹配
    else:
        return False

s='qwerrrr'
p='qwer'
print(isMatch(s,p))

