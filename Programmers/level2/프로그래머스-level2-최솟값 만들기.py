# -*- coding: utf-8 -*-
# 길이가 같은 배열 A, B 두개가 있습니다. 각 배열은 자연수로 이루어져 있습니다.
# 배열 A, B에서 각각 한 개의 숫자를 뽑아 두 수를 곱합니다.
# 이러한 과정을 배열의 길이만큼 반복하며, 두 수를 곱한 값을 누적하여 더합니다.
# 이때 최종적으로 누적된 값이 최소가 되도록 만드는 것이 목표

def solution(A,B):
    answer = 0

    # 하나는 오름차순, 하나는 내림차순 정렬하여 각 배열의 최소와 최대를 곱하게 한다.
    A.sort()
    B.sort(reverse = True)

    for i in range(0,len(A)):
        answer += A[i]*B[i]

    return answer

