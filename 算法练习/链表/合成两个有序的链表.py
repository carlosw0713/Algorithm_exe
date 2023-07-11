#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 合成两个有序的链表.py
@time: 2023/3/24  14:20
"""


class Node():
    def __init__(self, itme):
        self.itme = itme
        self.next = None

def create_linklist(li):
    head=Node(li[0])
    for element in li[1:]:
        node =Node(element)
        node.next=head
        head=node
    return head

#打印链表
def PrintList(lk):
    while lk:
        print(lk.itme,end=',')
        lk=lk.next
    print('\n')

def dsf(head,n):

    dummy = Node(0)
    dummy.next = head
    
    # step1: 获取链表长度
    cur, length = head, 0
    while cur:
        length += 1
        cur = cur.next
    
    # step2: 找到倒数第N个节点的前面一个节点
    cur = dummy
    for _ in range(length - n):
        cur = cur.next
    
    # step3: 删除节点，并重新连接
    cur.next = cur.next.next
    return dummy.next


if __name__=='__main__':

    list=[1,3,6,9]



    head=create_linklist(list)
    n=1
    PrintList(head)
    PrintList(dsf(head,2))