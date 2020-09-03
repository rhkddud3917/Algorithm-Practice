# -*- coding: utf-8 -*-
# 땅따먹기 게임을 하려고 합니다. 땅따먹기 게임의 땅(land)은 총 N행 4열로 이루어져 있고, 모든 칸에는 점수가 쓰여 있습니다.
# 1행부터 땅을 밟으며 한 행씩 내려올 때, 각 행의 4칸 중 한 칸만 밟으면서 내려와야 합니다.
# 단, 땅따먹기 게임에는 한 행씩 내려올 때, 같은 열을 연속해서 밟을 수 없는 특수 규칙이 있습니다.
# 최고점 반환

import copy
from collections import deque

def solution(land):
    answer = 0

    # 다이나믹 프로그래밍으로 풀면 되는데 그 전단계까지의 결과들을 계속 저장을 한다.
    # 각 층에서의 최대값을 기억하고 그 결과를 다음 층에서 이용한다.
    res = copy.deepcopy(land)
    for i in range(1,len(land)):
       for j in range(0,4):
           temp = [res[i-1][(j+1)%4],res[i-1][(j+2)%4],res[i-1][(j+3)%4]]
           res[i][j] += max(temp)

    answer = 0
    for el in res[-1]:
        if el > answer: answer = el

    return answer

land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))