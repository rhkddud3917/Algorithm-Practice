# -*- coding: utf-8 -*-
# 2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
# 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

a = int(input())

sol_dic = {}
sol_dic[0] = 0
sol_dic[1] = 1
sol_dic[2] = 3

# 점화식 F(n) = F(n-1) + 2F(n-2)
if a>=3:
    for i in range(3,a+1):
        sol_dic[i] = sol_dic[i-1] + 2*sol_dic[i-2]

print(sol_dic[a]%10007)