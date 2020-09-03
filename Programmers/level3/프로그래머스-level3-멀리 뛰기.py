# -*- coding: utf-8 -*-
# 한번에 1칸, 또는 2칸을 뛸 수 있습니다
# 멀리뛰기에 사용될 칸의 수 n이 주어질 때, 효진이가 끝에 도달하는 방법이 몇 가지인지 알아내, 여기에 1234567를 나눈 나머지를 리턴

def solution(n):

    # dp 를 이용해서 풀었다.
    # 점화식은 X[n] = X[n-1] + X[n-2] 이다.
    sol_dict = {}
    sol_dict[0] = 0
    sol_dict[1] = 1
    sol_dict[2] = 2

    if n > 2:
        for i in range(3,n+1):
            sol_dict[i] = sol_dict[i-1] + sol_dict[i-2]
    return sol_dict[n] % 1234567

n = 4
print(solution(n))