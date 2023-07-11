#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 有效的括号.py
@time: 2023/3/24  13:36
"""


class Solution:
    def isValid(self, s):

        hashmap={'(':')','[':']','{':'}'}

        stak=[]

        # 依次循环获取数字
        for i in s:
            # 如果满足 存在 哈希表.value 和stak 不为空(怕stak为空情况)
            if i in hashmap.values() :
                # 如果满足栈的最后一个值，与其匹配，出栈
                if stak and i==hashmap[stak[-1]]:
                    stak.pop()
                else:
                    return  False
            # 进栈
            else:
                stak.append(i)

        # 如果最终 stak还有值，则返回False
        return not stak




if __name__=='__main__':
    s='()[]{}]'
    # s="[()]"

    print(Solution.isValid(1,s))

