# -*- coding: utf-8 -*-
# 가로 길이가 2이고 세로의 길이가 1인 직사각형모양의 타일이 있습니다.
# 이 직사각형 타일을 이용하여 세로의 길이가 2이고 가로의 길이가 n인 바닥을 가득 채우려고 합니다.
# 채우는 방법의 수 반환

from collections import deque

def solution(n):

    sol_list = deque([])
    sol_list.append(0)
    sol_list.append(1)
    sol_list.append(2)

    # n-1 일때와 n-2 일때로 표현할 수 있다.
    if n > 2:
        for i in range(3, n + 1):
            sol_list.append((sol_list[-2] + sol_list[-1])%1000000007)

    return sol_list[-1]
n = 4
print(solution(n))