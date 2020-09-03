# -*- coding: utf-8 -*-
# N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다.
# 이 수열의 i번째 수부터 j번째 수까지의 합 A[i]+A[i+1]+…+A[j-1]+A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성

s = input().split(' ')
n, m = int(s[0]), int(s[1])

num = input().split(' ')
for i in range(0,n):
    num[i] = int(num[i])

answer = 0

i , j = 0, 0
sum = 0
# 포인터를 두 개를 만들어서 범위의 처음과 끝을 트래킹하며 계산을 진행했다.
while True:
    if sum < m:
        j += 1
        if j > len(num): break
        sum += num[j-1]
    elif sum == m:
        answer += 1
        i += 1
        j += 1
        if j > len(num):
            if i >= len(num): break
            sum -= num[i-1]
        else:
            sum -= num[i-1]
            sum += num[j-1]
    elif sum > m:
        i += 1
        if i >= len(num): break
        sum -= num[i-1]

print(answer)