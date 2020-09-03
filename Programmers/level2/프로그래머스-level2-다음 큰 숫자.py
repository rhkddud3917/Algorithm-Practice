# -*- coding: utf-8 -*-
# 조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
# 조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
# 조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.
# 조건을 만족하는 다음 큰 숫자를 반환

# 이진법으로 바꾸는 함수
# 바꾸면서 1의 개수를 센다.
def make2th(n):
    answer = ''
    count = 0
    while n != 0:
        if n%2 == 1: count += 1
        answer = str(n%2) + answer
        n = n//2
    return [answer,count]

# 십진법으로 바꾼느 함수
def make10th(s):
    res = 0
    t = 0
    for i in range(len(s)-1,-1,-1):
        res += int(s[i]) * (2**t)
        t += 1
    return res

# 1씩 더해가면서 이진법으로 바꿨을때 1의 개수가 같다면 반환한다.
def solution(n):
    num = make2th(n)[1]
    while True:
        n += 1
        s = make2th(n)[0]
        if make2th(n)[1] == num: return make10th(s)

n = 182
print(solution(n))