#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 哈希表.py
@time: 2023/2/14  13:57
"""

class LinkList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    class LinkListIterable:
        def __init__(self, node):
            self.node = node

        def __next__(self):
            if self.node:
                data = self.node.data
                self.node = self.node.next
                return data
            else:
                raise StopIteration

        def __iter__(self):
            return self

    def __init__(self, iterator=None):
        self.head = None
        self.tail = None
        if iterator:
            self.extend(iterator)

    def __iter__(self):
        return self.LinkListIterable(self.head)

    def __repr__(self):
        return '<<'+",".join(map(str, self))+'>>'

    def append(self, data):
        n = self.Node(data)
        if self.head:
            self.tail.next = n
            self.tail = n
        else:
            self.head = n
            self.tail = n

    def extend(self, iterator):
        for i in iterator:
            self.append(i)

    def exist(self, n):
        for i in self:
            if n == i:
                return True
            else:
                return False


class HashTable:
    def __init__(self, size=50):
        self.size = size
        self.T = [LinkList() for i in range(size)]

    def __repr__(self):
        return ','.join((map(str, self.T)))

    def exist(self, data):
        pst = self.h(data)
        return self.T[pst].exist(data)

    def h(self, data):
        return data % self.size

    def insert(self, data):
        pst = self.h(data)
        if self.exist(data):
            return 'Insert Duplicated'
        else:
            self.T[pst].append(data)


ht=HashTable()

ht.insert(0)
ht.insert(1)
ht.insert(100)
ht.insert(203)
print(','.join(map(str,ht.T)))