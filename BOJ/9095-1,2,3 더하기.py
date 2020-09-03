# -*- coding: utf-8 -*-
# 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.
# 각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.

num = int(input())

numList = []
answer = []

for i in range(0,num):
    numList.append(int(input()))

sol_dict = {}
sol_dict[0] = 1
sol_dict[1] = 1
sol_dict[2] = 2
sol_dict[3] = 4

# F(n) = F(n-1) + F(n-2) + F(n-3)
# 딕셔너리에 이미 있는 정보를 최대한 이용해서 시간을 단축시켰다.
def solution(x):
    try:
        return sol_dict[x]
    except:
        try:
            sol_dict[x] = sol_dict[x-1] + sol_dict[x-2] + sol_dict[x-3]
        except:
            sol_dict[x] = solution(x-1)+solution(x-2)+solution(x-3)

    return sol_dict[x]

for el in numList:
    answer.append(solution(el))

for el in answer:
    print(el)