# -*- coding: utf-8 -*-
# 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
# 방법의 수를 10,007로 나눈 나머지를 출력

a = int(input())

sol_dict = {}
sol_dict[0] = 0
sol_dict[1] = 1
sol_dict[2] = 2

# n-1 일때와 n-2 일때로 표현할 수 있다.
if a > 2:
    for i in range(3,a+1):
        sol_dict[i] = sol_dict[i-1]+sol_dict[i-2]

print(sol_dict[a]%10007)
