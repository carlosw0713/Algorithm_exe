#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 队列.py
@time: 2023/2/8  16:13
"""
'''
定义：队列是一种特殊的线性表，特殊之处在于它只允许在表的前端（front）进行删除操作，
而在表的后端（rear）进行插入操作，和栈一样，队列是一种操作受限制的线性表。进行插入操作的端称为队尾，进行删除操作的端称为队头
特点：先进先出
实现方式：环形队列，首未相连，这样就可以确保时间复杂度为o(1)
'''

class Queue:
    def __init__(self,size=100):
        self.queue=[ 0 for _ in range(size)] #初始化一个100长度的队列
        self.size=size
        self.near=0 #队尾指针
        self.front=0 #队首指针

    def push(self,element):
        if not self.is_filled():
            self.near=(self.near+1)%self.size
            self.queue[self.near]=element
        else:
            raise ImportError("Queue is filled")

    def pop(self):
        if not self.is_empty():
            self.front=(self.front+1)%self.size
            return self.queue[self.front]
        else:
            raise  ImportError("Queue is empty")

    # 判断队空
    def is_empty(self):
        return self.near==self.front

    #判断队满
    def is_filled(self):
        return (self.near+1)%self.size==self

