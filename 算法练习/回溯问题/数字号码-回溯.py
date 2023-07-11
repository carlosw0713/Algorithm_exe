#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 数字号码-回溯.py
@time: 2023/3/22  17:39
"""

class Solution:
    def letterCombinations(self, digits):

        '''
        思路：1.先数字为“”，循环取第一棵树值a，第二棵树d，e，f，
             2.取完之后回溯到第一个树 第一颗树循环到 b ，依次又取第二颗树，d，e，f
             3.最终输出值
        :param digits:
        :return:
        '''

        if not digits:
            return []

        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }



        def back_way(depth):


            # 当满足位置下标等于 digits个数时，说明tmp个数达标可以添加tmp值
            if depth ==lenght:
                tmps.append(''.join(tmp))

            else:
                digit=digits[depth]

                for letter in phoneMap[digit]:

                    # 取上颗树的值加上这棵树所有可能
                    tmp.append(letter)
                    # print(f"小集合{tmp}：执行深度{depth}、执行数字{digit}")
                    # 继续递归填写下一个数
                    back_way(depth+1)
                    # 撤销操作 清掉最后一个tmp
                    tmp.pop()

        # 存储所有可能
        tmps=[]
        tmp=[]
        depth=0
        lenght=len(digits)
        back_way(0)
        return tmps



if __name__=='__main__':

    digits = '234'

    print(Solution.letterCombinations(1,digits))