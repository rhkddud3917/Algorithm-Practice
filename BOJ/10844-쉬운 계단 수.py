# -*- coding: utf-8 -*-
# 인접한 모든 자리수의 차이가 1이 난다면 이런 수를 계단 수라고 한다.
# N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구하는 프로그램을 작성
# 첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력

import copy

n = int(input())

sol_dict = {}
sol_dict[0] = 0
for i in range(1,10):
    sol_dict[i] = 1

# 맨 끝자리의 숫자만 트래킹 해서 개수를 세면 된다.
# 예를들어 숫자 0은 숫자 1이 앞에 있어야만 하고 1은 0,2 가 앞에 있어야만 한다.
if n>1:
    for i in range(2,n+1):
        tmp_dict = {}
        tmp_dict[0] = sol_dict[1]
        for i in range(1,9):
            tmp_dict[i] = sol_dict[i-1] + sol_dict[i+1]
        tmp_dict[9] = sol_dict[8]
        sol_dict = copy.deepcopy(tmp_dict)

answer = 0
for el in sol_dict.values():
    answer += el

print(answer%1000000000)