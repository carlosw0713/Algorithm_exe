#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 复原IP地址.py
@time: 2023/3/23  14:57
"""

class Solution:
    def restoreIpAddresses(self, s):

        '''
        思路：1.依次循环s，获取当前的值满足num[0]不等于0且小于255，
             2.记录当前个数，回溯改值，回溯完记录已经算了几个数 idx+1
             3.当idx 满足等于4时，输出该值，返回结果
        :param digits:
        :return:
        '''

        #特殊情况 小于4和大于12 就不能计算ip值
        if len(s)<4 or len(s)>12:
            return ['']

        # 记录当前计算到第几个值了
        idx=0
        # 记录所有的结果
        res=[]
        # 记录当前路径
        path=''



        def dfs(s,idx,path,res):
            # print(idx)

            # 如果idx大于4，那么说明字符串s已经被分割的次数大于4，此时直接返回
            if idx > 4:
                return
            '''如果idx等于4，那么还要继续判断递归传入的s是否已经为空，如果s为空则说明字符串已经被
            完全分割为IP地址的形式，此时将该分割方法（路径）存储到结果列表res中，然后返回'''

            if idx==4 and not s:
                #这里符合条件的path的形式应该是"xxx.xxx.xxx.xxx."，因此path[:-1]是为了舍弃最后的'.'字符
                res.append(path[:-1])
                return


            for i in range(len(s)):


                # 判断如果s只有一位为且为0，或者 大于一位时 第一位为0 或者大于255
                if s[:i+1]=='0' or (s[0]!='0' and int(s[:i+1])<256):
                    dfs(s[i+1:], idx+1, path+s[:i+1]+'.', res)

        dfs(s, idx, path, res)

        return res



if __name__=='__main__':

    digits = "24525511135"

    print(Solution.restoreIpAddresses(1,digits))
    print(digits[0:3])