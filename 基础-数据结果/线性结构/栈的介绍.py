#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 栈的介绍.py
@time: 2023/2/8  15:48
"""

'''
定义：栈是一种只能在一端进行插入或删除的线性表。其中插入被称作进栈，删除被称作出栈。
允许进行插入或删除操作的一端被称为栈顶，另一段被称为栈底，栈底固定不变。其中，栈顶由一个称为栈顶指针的位置指示器来指示
特点：先进后出
基本操作：
进栈：push
出栈：pop
取栈顶：gettop
'''

'''列表实现栈'''


class Stack(object):
    # 初始化栈为空列表
    def __init__(self):
        self.items = []

    # 判断栈是否为空，返回布尔值
    def is_empty(self):
        return self.items == []

    # 返回栈顶元素
    def peek(self):
        return self.items[len(self.items) - 1]

    # 返回栈的大小
    def size(self):
        return len(self.items)

    # 压栈，入栈，进栈
    def push(self, item):
        self.items.append(item)

    # 出栈
    def pop(self):
        return self.items.pop()

if __name__ == '__main__':
    # 初始化一个栈对象
    my_stack = Stack()
    my_stack.push('h')
    my_stack.push('a')
    # 看一下栈的大小（有几个元素
    print(my_stack.size())
    # 打印栈顶元素
    print(my_stack.peek())
    print(my_stack.pop())
    print(my_stack.peek())
    print(my_stack.size())
    print(my_stack.pop())
    print(my_stack.size())
    print(my_stack.is_empty())

# 经常用来实现代码括号匹配问题，