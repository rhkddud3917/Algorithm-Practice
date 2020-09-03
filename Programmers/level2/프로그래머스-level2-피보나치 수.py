# -*- coding: utf-8 -*-
# 2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성

def solution(n):

    sol_dict = {}
    sol_dict[1] = 1
    sol_dict[2] = 1

    # dp의 메모라이제이션을 이용하여 피보나치 수를 구했다.
    if n > 3:
        for i in range(3,n+1):
            sol_dict[i] = sol_dict[i-1] + sol_dict[i-2]

    return sol_dict[n]%1234567

n = 6
print(solution(n))