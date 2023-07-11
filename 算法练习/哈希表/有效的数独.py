#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:carlos
@file: 有效的数独.py
@time: 2023/5/22  15:43
"""
'''请你判断一个 9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。
数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图
'''

class Solution:
    def isValidSudoku(self, board) -> bool:
        dict={}

        row = [[0] * 9 for _ in range(9)]
        col = [[0] * 9 for _ in range(9)]
        block = [[0] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j]) - 1
                    print(num)
                    b = (i // 3) * 3 + j // 3
                    if row[i][num] or col[j][num] or block[b][num]:
                        return False
                    row[i][num] = col[j][num] = block[b][num] = 1
        return True




        '''根据坐标获取横轴和纵轴列表'''
        for i in range(9):  # 对每一行进行判断
            storage = []
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in storage:
                    return False
                else:
                    storage.append(board[i][j])
        for i in range(9):  # 对每一列进行判断
            storage = []
            for j in range(9):
                if board[j][i] == '.':
                    continue
                if board[j][i] in storage:
                    return False
                else:
                    storage.append(board[j][i])
        for i in range(0, 9, 3):  # 对九宫格是否重复进行判断
            for j in range(0, 9, 3):
                storage = []
                for x in range(0, 3):
                    for y in range(0, 3):
                        if board[i + x][j + y] == '.':
                            continue
                        if board[i + x][j + y] in storage:
                            return False
                        else:
                            storage.append(board[i + x][j + y])
        return True








if __name__ =='__main__':

    board=[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]




    print(Solution.isValidSudoku(1,board))

