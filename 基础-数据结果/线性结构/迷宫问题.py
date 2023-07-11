#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 迷宫问题.py
@time: 2023/2/9  10:50
"""
from collections import deque

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]



def maze_path(x1,y1,x2,y2):
    '''

    :param x1: 起始x坐标
    :param y1: 起始y坐标
    :param x2: 终点x坐标
    :param y2: 终点y左标
    :return: 打印一条起始通往终点的路线。
    '''

    stack=[] #初始化栈
    stack.append((x1, y1))  # 初始化起点位置
    while(len(stack)>0): #栈不能为emtpy，或者就是没有路

        curNode=stack[-1] #当前栈节点

        if curNode[0] == x2 and curNode[1]==y2:
            print('找到路拉')
            print(stack)
            print('路线图')
            for i in maze:
                print(i)
            return True

        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])  # curNode[0],curNode[1]分别代表x,y的坐标。
            # print(f'坐标：{nextNode},坐标值：{maze[nextNode[0]][nextNode[1]]}')
            if maze[nextNode[0]][nextNode[1]]==0: # 如果值为0则进栈
                stack.append(nextNode) #进栈
                maze[nextNode[0]][nextNode[1]]=6 #走过的路赋值为2，避免以后再走
                print(stack,'进栈')
                break #找到一个位置可以走的，退出循环，stack加一
        else:
            maze[nextNode[0]][nextNode[1]]=2
            stack.pop()
            print(stack, '出栈')

    else:
        print(f'起始位置({x1},{y1})到终点位置({x2},{y2})没有路')
        return False


def maze_path_queue(x1,y1,x2,y2):

    queue=deque() #系统内置队列模块 双端队列，就是两头都可操作即出队和进队的一种数据结构。个人理解，就是两个队列的操作作用于一个队列的结构。
    queue.append((x1,y1,-1)) #起点
    path=[]

    while len(queue) >0: #队列不为空

        curNode=queue.pop() #获取起始位置的坐标

        path.append(curNode) #每次将坐标存起来


        if curNode[0]==x2 and curNode[1]==y2:
            print('找到路拉')
            print(analysis_path(path))

            return True

        for dir in dirs:
            nextNode=dir(curNode[0],curNode[1])
            if maze[nextNode[0]][nextNode[1]]==0:#如果路为0 继续找。
                queue.append((nextNode[0],nextNode[1],len(path)-1))
                maze[nextNode[0]][nextNode[1]] = 2 #标记已经走过的路
        print('输出位置',nextNode)

    else:
        print('没有路')
        return False

def analysis_path(path):

    curNode=path[-1] #获取最后一位的下标
    realpath=[]# 初始化真实路径
    while curNode[2]!=-1:# 让他一直循环
        realpath.append(curNode[0:2]) #元组切片只需要前两位位置数
        curNode=path[curNode[2]] #path[curNode[2]] 就是对他是那个位置走过来的

    realpath.append(curNode[0:2]) # 起点
    realpath.reverse()# 反转列表

    return realpath



if __name__=='__main__':
    '''可以将lambda函数作为参数传递给其他函数比如说结合map、filter、sorted、reduce等一些Python内置函数使用'''
    dirs = [
        lambda x, y: (x + 1, y),
        lambda x, y: (x - 1, y),
        lambda x, y: (x, y + 1),
        lambda x, y: (x, y - 1)
    ]
    # 用栈来解决迷宫问题
    # maze_path(1,1,8,8)

    # 用队列来实现迷宫问题
    maze_path_queue(1, 1, 8, 8)