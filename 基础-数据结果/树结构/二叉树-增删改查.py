#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 二叉树-增删改查.py
@time: 2023/2/14  18:23
"""
import random


class BiTreeNode:
    def __init__(self,data):
        self.data=data
        self.lchild=None #左孩子
        self.rchild=None #右孩子
        self.parent=None #父亲

class BST:
    def __init__(self,li=None):
        self.root=None
        if li :
            for val in li:
                # print(f"插入:{val}")
                self.insert_no_rec(val)

    # 递归插入
    def insert(self,node,val):
        if not node:#如果不为0
            node=BiTreeNode(val)
        elif val < node.data:
            node.lchild=self.insert(node.lchild,val)
            node.lchild.parent = node
        elif val >node.data:
            node.rchild =self.insert(node.rchild,val)
            node.rchild.parent =node
        return  node
    # 非递归插入
    def insert_no_rec(self,val):
        p=self.root
        if not p:#空树
            self.root=BiTreeNode(val)
            return
        while True:

            if val<p.data:

                if p.lchild:
                    p=p.lchild

                else:#左孩子不存在
                    p.lchild=BiTreeNode(val)
                    p.lchild.parent = p

                    return
            elif val>p.data:

                if p.rchild:
                    p=p.rchild
                else:
                    p.rchild=BiTreeNode(val)
                    p.rchild.parent =p

                    return
            else:
                return

    #递归查找
    def query(self,node,val):
        if not node:#没有找到 返回None
            return '没有找到'
        if node.data<val:# 找右孩子
            return self.query(node.rchild,val)
        elif node.data>val:# 找左孩子
            return  self.query(node.lchild,val)
        else:# 如果一样返回node
            return node

    #非递归查找
    def query_no_rec(self,val):
        p=self.root
        while p:# 还有值一直循环
            if p.data<val:
                p=p.rchild
            elif p.data>val:
                p=p.lchild
            else:
                return p
        else:
            return '没有找到'

    '''
    删除三种场景：
    1.删除的时候，自己没有孩子，直接删除
    2.删除节点有一个孩子(左孩子、右孩子)，将孩子与父亲连接
    3.删除节点有两个孩子，将右子树的最小节点替换当前节点
    '''
    def remove_node_1(self,node):
        if not node.parent:
            self.root=None
        if node==node.parent.lchild:
            node.parent.lchild=None
        else:
            node.parent.rchild=None
    def remove_node_21(self,node):
        if not node.parent:#根节点
            self.root=node.lchild
            node.lchild.parent=None
        elif node==node.parent.lchild:
            node.parent.lchild=node.lchild
            node.lchild.parent=node.parent
        else:
            node.parent.rchild=node.lchild
            node.lchild.parent=node.parent

    def remove_node_22(self, node):
        if not node.parent:  # 根节点
            self.root = node.rchild

        elif node == node.parent.lchild:
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent
        else:
            node.parent.rchild = node.rchild
            node.lchild.parent = node.parent

    def delete(self,val):
        if self.root: # 不是空树
            node=self.query_no_rec(val)
            if not node:#不存在
                return False

            if not node.lchild and not node.rchild:# 如果没有孩子
                self.remove_node_1(node)
            elif not node.rchild: # 如果只有一个左孩子
                self.remove_node_21(node)
            elif not node.lchild:# 如果只有一个右孩子
                self.remove_node_22(node)
            else:
                min_node=node.rchild
                while min_node.lchild:
                    min_node=min_node.lchild
                node.data=min_node.data
                if min_node.rchild: #删除min_node
                    self.remove_node_22(min_node)
                else:
                    self.remove_node_1(min_node)

        return self.root.data


    #前序遍历 先左边所有，在左边
    def Pre_Order(self,root):

        '''

        :param root:根姐节点
        :return: 遍历后数据
        '''
        if root:
            print(root.data,end=',')
            self.Pre_Order(root.lchild)#左孩子
            self.Pre_Order(root.rchild)#右孩子

    # 中序遍历
    def  in_order(self,root):

        if root:
            self.in_order(root.lchild)
            print(root.data,end=',')
            self.in_order(root.rchild)

    # 后序遍历
    def post_order(self,root):
        if root:
            self.post_order(root.lchild)  # 左孩子
            self.post_order(root.rchild)  # 右孩子
            print(root.data,end=',')

    # 层序遍历
    def leverl_order(self,root):
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
    '''
    该二叉树满足，左边为最小的，靠右依次变大 满足，lchild<rchild
    '''
    # list=random.sample(range(1,20),10)
    list=[17, 16, 12, 8, 18, 7, 2, 10, 14, 4]
    print(f'起始二叉树表--{list}')
    tree=BST(list)

    # 遍历
    # tree.Pre_Order(tree.root)
    # print('前序排列')
    tree.in_order(tree.root)
    print('中序排列')
    # tree.post_order(tree.root)
    # print('后续排列')
    tree.leverl_order(tree.root)
    print('层级排列')

    # 查找
    print(tree.query(tree.root,41),'查找')
    print(tree.query_no_rec(4),'查找')

    # 删除
    tree.delete(4)
    tree.in_order(tree.root)
    print('中序排列')

