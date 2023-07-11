#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 队列的内置模块.py
@time: 2023/2/9  15:59
"""

import time
from collections import deque

mydeque=deque(maxlen=10) # 可以指定 队列的长度
print(mydeque.maxlen)

# 默认从右边加入
mydeque.append(10)
mydeque.append(12)
print(mydeque)

# 左边加入
mydeque.appendleft('a')
mydeque.appendleft('b')
print(mydeque)

# 左边加入一个列表
mylist= range(5,8)
mydeque.extendleft(mylist)
print(mydeque)

# 出队列,返回出队列的元素
# 可以从左边也可以从右边 出队列
mydeque.pop()
mydeque.popleft()
print(mydeque)

print("查看长度",len(mydeque))
print("统计里面有多少个key",mydeque.count('a'))

mydeque.insert(2,'frank') #插入到第2个元素,后面的后移
print(mydeque)

mydeque.reverse() #队列翻转
print("翻转",mydeque)

mydeque.remove('a')  #删除某个元素
print("删除a后:",mydeque)

d4 = mydeque.copy()
print("拷贝过来的",d4)

mydeque.clear()#清空队列
print("清除后后:",mydeque)

#输出结果
'''
10
deque([10, 12], maxlen=10)
deque(['b', 'a', 10, 12], maxlen=10)
deque([7, 6, 5, 'b', 'a', 10, 12], maxlen=10)
deque([6, 5, 'b', 'a', 10], maxlen=10)
查看长度 5
统计里面有多少个key 1
deque([6, 5, 'frank', 'b', 'a', 10], maxlen=10)
翻转 deque([10, 'a', 'b', 'frank', 5, 6], maxlen=10)
删除a后: deque([10, 'b', 'frank', 5, 6], maxlen=10)
拷贝过来的 deque([10, 'b', 'frank', 5, 6], maxlen=10)
清除后后: deque([], maxlen=10)
'''

