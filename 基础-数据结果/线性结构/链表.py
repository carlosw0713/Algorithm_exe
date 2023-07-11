# -*- coding:utf-8 -*-
'''
用Python实现链表。
'''
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

#在第index处插入节点this_node
def insert(head, this_node):
    this_node.next = head.next
    head.next = this_node


#打印链表
def PrintList(lk):
    while lk:
        print(lk.itme,end=',')
        lk=lk.next

# 打印链表的元素大小 例：[2,4,3]，342
def Outprint(lk):
    sum=0
    place=0
    while lk:
            sum+=int(lk.itme)*(10**place)

            lk=lk.next
            place+=1
    return sum

if __name__ == '__main__':

    lk=create_linklist([1,3,6,9])

    a=PrintList(lk)

    # print(lk)

    # insert(lk,2)
    # PrintList(lk)
    # print(lk.itme)

    # print(Outprint(lk))


    # s.append(a)
    # s.append(b)
    # s.append(c)
    # s.PrintList()
    # s.insert(e,2)
    # print(s.head.data)
    # print(s.head.next.data)
    # print(s.head.next.next.data)
    # s.insert(d,0)
    # print(s.head.data)
    # print(s.head.next.data)
    # print(s.head.next.next.data)
    # s.delete(0)
    # print(s.head.data)
    # print(s.head.next.data)
    # print(s.head.next.next.data)
    # s.delete(2)
    # print(s.head.data)
    # print(s.head.next.data)
    # print(s.head.next.next.data)
    # s.update(0,1)
    # print(s.head.data)
    # print(s.head.next.data)
    # print(s.get_data(0))
    # print(s.get_data(1))
    # print(s.get_length())
    # s.PrintList()
