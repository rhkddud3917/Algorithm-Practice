# -*- coding: utf-8 -*-
# 자연수 n 개로 이루어진 각 원소의 합이 S가 되는 수의 집합
# 위 조건을 만족하면서 각 원소의 곱 이 최대가 되는 집합
# 위를 만족하는 것이 최고의 집합이다.
# 최고의 집합은 오름차순으로 정렬된 1차원 배열(list, vector) 로 return 해주세요.
# 만약 최고의 집합이 존재하지 않는 경우에 크기가 1인 1차원 배열(list, vector) 에 -1 을 채워서 return 해주세요.

def solution(n, s):
    answer = []

    if n > s: return [-1]

    # 곱이 최대가 되려면 합을 이루는 원소가 최대한 같아야 한다.
    b = s % n
    for i in range(0,n-b):
        answer.append(s//n)
    for i in range(0,b):
        answer.append(s//n+1)

    return answer