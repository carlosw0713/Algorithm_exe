#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 二叉树-实现与遍历.py
@time: 2023/2/14  16:09
"""



class BiTreeNode:
    def __init__(self,data):
        self.data=data
        self.lchild=None #左孩子
        self.rchild=None #右孩子

# 创建二叉树
def create_BiTree():

    print('''
    ；；；；E；；；；
    ；；A；；；G；；
    ；；；C；；；F；
    ；；B；D；；；；
    '''.replace('；','-'))


    a=BiTreeNode('A')
    b=BiTreeNode('B')
    c=BiTreeNode('C')
    d=BiTreeNode('D')
    e=BiTreeNode('E')
    f=BiTreeNode('F')
    g=BiTreeNode('G')

    e.lchild=a
    e.rchild=g
    a.rchild=c
    c.lchild=b
    c.rchild=d
    g.rchild=f

    return e # 返回根节点

#前序遍历 先左边所有，在左边
def Pre_Order(root):

    '''

    :param root:根姐节点
    :return: 遍历后数据
    '''
    if root:
        print(root.data,end=',')
        Pre_Order(root.lchild)#左孩子
        Pre_Order(root.rchild)#右孩子

# 中序遍历
def  in_order(root):

    if root:
        in_order(root.lchild)
        print(root.data,end=',')
        in_order(root.rchild)

# 后序遍历
def post_order(root):
    if root:
        post_order(root.lchild)  # 左孩子
        post_order(root.rchild)  # 右孩子
        print(root.data,end=',')

# 层序遍历
def leverl_order(root):
    from collections import deque
    queue=deque()#调用队列
    queue.append(root)
    while len(queue)>0: #队列不为空
        node=queue.popleft()
        print(node.data,end=',')
        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)

if __name__ == '__main__':
    root=create_BiTree()
    # Pre_Order(root) #前序遍历
    # in_order(root) #中序遍历
    # post_order(root) #后序遍历
    leverl_order(root) #层级遍历


