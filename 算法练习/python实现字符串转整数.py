#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: python实现字符串转整数.py
@time: 2023/3/14  15:25
"""
'''
读入字符串并丢弃无用的前导空格
检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。
读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。如果没有读入数字，则整数为 0 。必要时更改符号（从步骤 2 开始）。
如果整数数超过 32 位有符号整数范围 [−231,  231 − 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −231 的整数应该被固定为 −231 ，大于 231 − 1 的整数应该被固定为 231 − 1 。
返回整数作为最终结果。
'''

class Solution:
    def myAtoi(self, s: str) -> int:
        # 去除前导空格
        s = s.lstrip()
        if not s:
            return 0
        s_list = list(s)
        res = ""
        if s_list[0] == "-":
            # 如果第一个是负号 那结果是负的
            res = "-"
        if (s_list[0] == "+") or (s_list[0] == "-"):
            # 如果第一个是正号 那结果是负的
            s_list.pop(0)
        for tmp in s_list:
            if tmp.isnumeric():
                res += tmp
            else:
                break
        if (res == "") or (res == "-"):
            return 0
        if int(res) > 2**31-1:
            return 2**31-1
        if int(res) < -2**31:
            return -2**31
        return int(res)
s='123222asd'
print(Solution.myAtoi(1,s))