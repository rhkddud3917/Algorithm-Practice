# -*- coding: utf-8 -*-
# 테두리 한 줄은 갈색, 가운데는 노란색
# 갈색 개수와 노란색 개수 주어질 때 카펫의 [가로, 세로] 길이 반환
# 가로는 세로보다 같거나 길다

def solution(brown, yellow):
    answer = []
    # 가로 x 세로 y
    # x * y = brown + yellow
    # (x-2) * (y-2) = yellow
    # x > y
    # 가로의 최대 길이 구하기 -> 가로의 범위 세로의 범위 나옴
    square = brown+yellow-3+1
    for i in range(0,square+1):
        for j in range(0,i+1):
            if i * j == brown + yellow and (i-2)*(j-2) == yellow:
                return [i,j]

brown = 24
yellow = 24
print(solution(brown,yellow))