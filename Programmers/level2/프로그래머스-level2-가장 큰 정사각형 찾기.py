# -*- coding: utf-8 -*-
# 1와 0로 채워진 표(board)가 있습니다. 표 1칸은 1 x 1 의 정사각형으로 이루어져 있습니다. 표에서 1로 이루어진 가장 큰 정사각형을 찾아 넓이를 return
# 단 x 축에 평행한 정사각형

def solution(board):
    answer = 0

    row = len(board)
    col = len(board[0])

    # 가능한 정사각형의 최대 넓이를 계속 업데이트 시키는 dp 알고리즘을 사용했다.
    for i in range(0,row):
        for j in range(0,col):
            if i == 0 or j == 0:
                continue
            if board[i][j] != 0:
                board[i][j] = min(board[i][j-1],board[i-1][j],board[i-1][j-1])+1

    answer = 0
    for i in range(0,row):
        for j in range(0,col):
            if board[i][j] > answer: answer = board[i][j]
    return answer**2


board = [[0,0,1,1],[1,1,1,1]]
print(solution(board))
