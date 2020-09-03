# -*- coding: utf-8 -*-
# n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성

def gcd(a,b):
    while b != 0:
        a,b = b, a%b
    return a

def lcm(a,b):
    return a * b // gcd(a,b)

def solution(arr):

    # 순차적으로 처음 두개 최소공배수 구하고 그 최소공배수랑 그 다음 수의 최소공배수를 구하고
    # 이것을 반복한다.
    answer = lcm(arr[0],arr[1])
    for i in range(2,len(arr)):
        answer = lcm(answer,arr[i])
    return answer

arr = [2,6,8,14]
print(solution(arr))