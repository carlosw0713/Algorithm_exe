#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 删除链表中的N个节点.py
@time: 2023/3/24  10:42
"""

class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

def create_linklist(li):
    head=Node(li[0])
    for element in li[1:]:
        node =Node(element)
        node.next=head
        head=node
    return head


#打印链表
def PrintList(head,res,n):
    while head:
        # print(head.val,end=',')
        res.append(head.val)
        head = head.next

    res.pop(-n)
    return res

if __name__ == '__main__':

    head=create_linklist([1,3,6,9])
    n=2

    res=[]
    tmp=PrintList(head,res,n)

    print(tmp)