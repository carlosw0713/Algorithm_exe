#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 格雷码.py
@time: 2023/2/23  13:52
"""
'''
运算符	描述	示例
&	按位与，都为1，结果为1，有一个0，就为0	a & b
|	按位或，都为0，结果为0，有一个1，就为1	a | b
^	按位异或，不同，结果为1，相同，就为0	a ^ b
~	按位取反，1变0，0变1	~a
<<	左移动，高位丢弃，低位补0	a << 2，左移2位
>>	右移动，丢弃右移位数，高位补0	a >> 3，右移3位
'''
# a = 0b0011 # 3的二进制
# b = 0b1010  # 10的二进制
# print(a&b,'=',bin(a&b),'    只有第二位都为1所以10')
# print(a|b,'=',bin(a|b),'    1、2、4位都含1所以为1011')
# print(a^b,'=',bin(a^b),'    2、3位相同，所以是1001')
# print(~a,'=',bin(~a),'  取反-100')
# print(a<<2,'=',bin(a<<2),'  左移动两位，低位补0，1100')
# print(b>>2,'=',bin(b>>2),'  右移动两位，高位补0，10')

'''
格雷编码的生成过程, G(i) = i ^ (i>>1);
'''
n=3
start=4
list=[]
list.append(bin(start))
for i in range(2**n):
    list.append(bin(i^(i>>1)^start))
    print(bin(i^(i>>1)^start))
print(list)
    # print(bin(i^(i>>1)),bin(i),bin(i>>1))