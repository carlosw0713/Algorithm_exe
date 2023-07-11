#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 括号的生成.py
@time: 2023/3/24  14:43
"""
class Solution:
    def isValid(self, n):

        '''当前左右括号都有大于1个可以使用的时候，才产生分支；
            产生左分支的时候，只看当前是否还有左括号可以使用；
            产生右分支的时候，还受到左分支的限制，右边剩余可以使用的括号数量一定得在严格大于左边剩余的数量的时候，才可以产生分支；
            在左边和右边剩余的括号数都等于的时候结算。
        '''

        res = []
        tmp = ''
        def dsf(res,left,right,tmp):
            print(tmp)
            if left==0 and right==0:
                res.append(tmp)

            if  left>right:
                return
            if left>0:
                dsf(res,left-1,right,tmp+'(')
            if right>0:
                dsf(res,left,right-1,tmp+')')


        dsf(res,n,n,tmp)

        return res


if __name__=='__main__':
    s=3
    # s="[()]"

    print(Solution.isValid(1,s))