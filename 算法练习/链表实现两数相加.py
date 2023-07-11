#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 链表实现两数相加.py
@time: 2023/2/24  14:56
"""



class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self,l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        sum1 = count_link(l1)
        sum2 = count_link(l2)
        sum = sum1 + sum2
        print(sum1,sum2,sum)

        list_link = []
        # 将数字转为链表
        # 将数字转为链表
        head = Node(int(list(str(sum))[0]))
        for i in list(str(sum))[1:]:
            node = Node(int(i))
            node.next = head
            head = node

        return head

# 将链表的值转换为数字
def count_link(lk):
    sum = 0
    place = 0
    while lk:
        sum += int(lk.val) * (10 ** place)
        print(lk.val)
        lk = lk.next
        place += 1

    return sum

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
        print(lk.val,end=',')
        lk=lk.next


l1=create_linklist([3,5,6])
l2=create_linklist([1,4,5])
a=Solution.addTwoNumbers(1,l1,l2)
PrintList(a)
