#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 最长有效括号.py
@time: 2023/3/30  13:37
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        '''
        1.依次找过去先找到第一dui
        :param s:
        :return:
        '''

        lenght=len(s)
        stack=[]
        res=0
        stk=[]

        for i in range(lenght):
            '''
            那满足什么条件才会导致当前不可以构成括号呢？
            i. 当前栈为空。当前字符s[i]将会是栈中第一个字符，无法跟之前的字符构成一对括号
            ii. 当前字符s[i]是左括号'('。左括号无法跟栈顶元素构成一对括号
            iii. 栈顶元素是右括号')'。无论当前字符s[i]是什么，都无法和栈顶元素构成一对括号
            其实也就是栈顶元素必须为'('，当前字符s[i]必须为')'，这样才能构成一对括号
            '''
            if not stack or s[i]=='(' or s[stack[-1]]==')':
                stack.append(i)
                stk.append(s[i])
                print(s[i],'进栈',stk)
            else:
                '''
                当前有效括号的长度 = 当前索引i - 栈顶存储的索引stack[-1]
                最后要返回的最长有效括号长度即为res = max(res, i - stack[-1])
                因为此时栈可能为空，如果为空就是res = max(res, i - (-1))
                '''
                stack.pop()
                stk.pop()
                print(s[i], '出栈',stk)
                if stack:
                    res=max(res,i-stack[-1])
                else:
                    res=max(res,i-(-1))
        return res







if __name__=='__main__':

    s=")(()()))"
    print(Solution.longestValidParentheses(1,s))