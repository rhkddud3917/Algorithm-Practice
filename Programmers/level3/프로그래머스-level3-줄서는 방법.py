# -*- coding: utf-8 -*-
# 사람의 수 n과, 자연수 k가 주어질 때, 사람을 나열 하는 방법을 사전 순으로 나열 했을 때, k번째 방법을 return

def solution(n, k):
    answer = []

    # 코드의 인덱스는 0부터 시작이므로 이를 맞추기 위해 k에서 1을 뺀다.
    k -= 1

    # n개의 숫자 리스트를 만든다.
    n_list = []
    for i in range(1,n+1):
        n_list.append(i)

    # 1부터 n-1 까지의 팩토리얼 수를 dp를 이용해서 계산을 한다.
    factorial_dict = {}
    factorial_dict[0] = 1
    for i in range(1,n+1):
        factorial_dict[i] = factorial_dict[i-1] * i

    # n개를 세우는 방법은 n!이고 맨 앞자리를 제외한 줄세우기 방법은 (n-1)!인 것을 이용한다.
    # 처음 k에서 (n-1)! 로 나눈 몫이 첫 숫자의 인덱스이고
    # 나머지는 다음 자리를 계산하기 위한 k가 된다.
    # 이과정을 반복하면 k 번째 줄세우기 방법을 구할 수 있다.
    for i in range(n,0,-1):
        x = k // factorial_dict[i-1]
        y = k % factorial_dict[i-1]
        answer.append(n_list.pop(x))
        k = y

    return answer

n = 3
k = 5
print(solution(n,k))