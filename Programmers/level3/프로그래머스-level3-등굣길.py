# -*- coding: utf-8 -*-
# 가장 왼쪽 위, 즉 집이 있는 곳의 좌표는 (1, 1)로 나타내고 가장 오른쪽 아래, 즉 학교가 있는 곳의 좌표는 (m, n)으로 나타냅니다.
# 격자의 크기 m, n과 물이 잠긴 지역의 좌표를 담은 2차원 배열 puddles이 매개변수로 주어집니다.
# 물웅덩이는 피해가야 한다.
# 집에서 학교까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈 나머지를 return

import copy

# 한 칸 한 칸 진행하면서 각 칸의 최단경로의 개수를 업데이트한다.
# 각 칸은 해당 칸의 왼쪽과 위쪽의 칸의 최단경로의 합이다.
def solution(m, n, puddles):

    # 좌표는 0,0 부터 시작하는 것으로 만든다.
    # 위쪽과 왼쪽 가장자리는 최단경로가 1이므로 1로 초기화를 하고 나머지는 0으로 초기화한다.
    root = []
    for i in range(0,n):
        temp = []
        for j in range(0,m):
            if i == 0 or j == 0:
                temp.append(1)
            else:
                temp.append(0)
        root.append(copy.deepcopy(temp))

    # 물웅덩이를 x 로 표시한다.
    for el in puddles:
        root[el[1]-1][el[0]-1] = 'x'

    # 위쪽과 왼쪽 가장자리에 중간에 물웅덩이가 있으면 그 뒤쪽은 최단경로의 개수가 0이된다.
    for i in range(0,n):
        if root[i][0] == 'x':
            for j in range(i+1,n):
                root[j][0] = 0
            break

    for i in range(0,m):
        if root[0][i] == 'x':
            for j in range(i+1,m):
                root[0][j] = 0
            break

    # 각 칸은 진행하면서 최단 경로를 업데이트 한다.
    for i in range(1,n):
        for j in range(1,m):
            if root[i][j] == 'x': continue
            elif root[i-1][j] == 'x' and root[i][j-1] == 'x': root[i][j] = 0
            elif root[i-1][j] == 'x': root[i][j] = root[i][j-1]
            elif root[i][j-1] == 'x': root[i][j] = root[i-1][j]
            else: root[i][j] = root[i][j-1] + root[i-1][j]

    return root[-1][-1] % 1000000007

m = 4
n = 1
puddles = [[2,1]]
print(solution(m,n,puddles))