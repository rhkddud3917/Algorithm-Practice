# -*- coding: utf-8 -*-
# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.
# 1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
# 2. X가 2로 나누어 떨어지면, 2로 나눈다.
# 3. 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

a = int(input())

# 초기값들 설정
sol_dic = {}
sol_dic[1] = 0
sol_dic[2] = 1
sol_dic[3] = 1

# 3보다 크면 자신의 수보다 작은 수들을 이용해 최솟값에 접근할 수 있다.
if a > 3:
    for i in range(4,a+1):
        candidate = []
        candidate.append(sol_dic[i-1])
        if i%2 == 0:
            candidate.append(sol_dic[i//2])
        if i%3 == 0:
            candidate.append(sol_dic[i//3])
        sol_dic[i] = min(candidate)+1


print(sol_dic[a])

