#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 树-创建目录.py
@time: 2023/2/14  15:11
"""

class Node:
    def __init__(self,name,type='dir'):
        self.name=name
        self.type=type
        self.children=[]
        self.parent=None
    def __repr__(self): #repr可以覆盖这种默认行为，并指定解释器对于对象的字符串表示
        return self.name

class FileSystemTree:
    def __init__(self):
        self.root =Node('/')
        self.now=self.root

    def mkdir(self,name):
        if name[-1] !='/':
            name+='/'
        node=Node(name)
        self.now.children.append(node)
        node.parent=self.now

    def ls(self):
        return  self.now.children

    def cd(self,name):
        if name[-1]!='/':
            name+='/'
        if name == "../":
            self.now=self.now.parent
            return
        for child in self.now.children:
            if child.name==name:
                self.now=child
                return
        raise ValueError(' invalid dir ')


tree=FileSystemTree()
tree.mkdir('var/')
tree.mkdir('bin/')
tree.mkdir('usr/')
print(tree.root.children)
tree.cd('bin/')
tree.mkdir('python/')
print(tree.ls())
tree.cd('../')
print(tree.now.children)